"""Testes de tools.dren.drenos.

(a) livro/consistencia: exemplos do USBR Drainage Manual (1993) e propriedades de monotonia;
(b) gabaritos dos casos reais (casos/drenagem_dissipadores/*.md), tolerancia 5 % (D11) salvo o
indicado. Divergencia > 5 % => xfail(strict=True) e linha em tools/dren/DIVERGENCIAS.md.
"""
import json
import math
import os
import subprocess
import sys

import pytest

from tools.dren import drenos as D

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


# ---------------------------------------------------------------- (a) livro
def test_d_equivalente_usbr_exemplo_5_10():
    # USBR Drainage Manual 5-10 ex.1 (p. 168): d=6,1 m, L=91 m, r=0,18 m -> d' = 4,4 m (figura 5-5)
    assert D.d_equivalente_hooghoudt(6.1, 91.0, 0.18) == pytest.approx(4.4, rel=0.03)


def test_d_equivalente_limites():
    assert D.d_equivalente_hooghoudt(0.0, 50, 0.1) == 0.0
    # d pequeno frente a L: d_e ~ d
    assert D.d_equivalente_hooghoudt(0.2, 100.0, 0.1) <= 0.2
    # ramo d/L > 0,31: d_e = L / (2,55 (ln(L/r) - 1,15)) independe de d
    a = D.d_equivalente_hooghoudt(30.0, 40.0, 0.1)
    b = D.d_equivalente_hooghoudt(60.0, 40.0, 0.1)
    assert a == pytest.approx(b)
    assert a == pytest.approx(40.0 / (2.55 * (math.log(400.0) - 1.15)))
    # d_e nunca excede d
    assert D.d_equivalente_hooghoudt(0.05, 20.0, 0.1) <= 0.05


def test_donnan_usbr_exemplo_1():
    # K=3,05 m/d, a=6,7, b=7,92, q=0,025/14 m/d -> L = 347 m (manual p. 169)
    r = D.donnan_espacamento(3.05, 6.7, 7.92, 0.025 / 14.0)
    assert r["L"] == pytest.approx(347.0, rel=0.01)


def test_donnan_dreno_na_barreira_exemplo_2():
    # a=0, b=1,22 m, K=3,05, q=0,0018 -> metade na barreira -> L = 142 m (manual p. 170)
    r = D.donnan_espacamento(3.05, 0.0, 1.22, 0.025 / 14.0, dreno_na_barreira=True)
    assert r["L"] == pytest.approx(142.0, rel=0.02)


def test_hooghoudt_equacao_fechada():
    q, K, h, Dd, r = 0.002, 1.0, 0.6, 5.0, 0.1
    res = D.hooghoudt_espacamento(q, h, Dd, r, K=K)
    L, de = res["L"], res["d_e"]
    assert L ** 2 == pytest.approx((8 * K * de * h + 4 * K * h * h) / q, rel=1e-5)
    assert de == pytest.approx(D.d_equivalente_hooghoudt(Dd, L, r), rel=1e-4)
    assert 10 < L < 200


def test_hooghoudt_monotonia():
    base = dict(q=0.002, h=0.6, D=5.0, r=0.1)
    L0 = D.hooghoudt_espacamento(K=1.0, **base)["L"]
    assert D.hooghoudt_espacamento(K=2.0, **base)["L"] > L0                      # cresce com K
    assert D.hooghoudt_espacamento(K=1.0, **dict(base, h=0.9))["L"] > L0       # cresce com h
    assert D.hooghoudt_espacamento(K=1.0, **dict(base, q=0.004))["L"] < L0     # decresce com q
    assert D.hooghoudt_espacamento(K=1.0, **dict(base, D=10.0))["L"] > L0      # camada mais espessa


def test_hooghoudt_duas_camadas_e_barreira_no_dreno():
    # D = 0: L^2 = 4 K1 h^2/q (Donnan na barreira, sem convergencia)
    r = D.hooghoudt_espacamento(0.005, 0.8, 0.0, 0.1, K_acima=1.5, K_abaixo=0.2)
    assert r["L"] == pytest.approx(math.sqrt(4 * 1.5 * 0.64 / 0.005), rel=1e-9)
    # K_abaixo maior (camada profunda mais permeavel) aumenta L
    a = D.hooghoudt_espacamento(0.002, 0.6, 5.0, 0.1, K_acima=1.0, K_abaixo=1.0)["L"]
    b = D.hooghoudt_espacamento(0.002, 0.6, 5.0, 0.1, K_acima=1.0, K_abaixo=3.0)["L"]
    assert b > a


def test_hooghoudt_entradas_invalidas():
    with pytest.raises(ValueError):
        D.hooghoudt_espacamento(0.002, 0.6, 5.0, 0.1)          # sem K
    with pytest.raises(ValueError):
        D.hooghoudt_espacamento(-0.002, 0.6, 5.0, 0.1, K=1.0)


def test_ernst_soma_das_resistencias():
    r = D.ernst_espacamento(q=0.002, h=0.7, Dv=0.4, Kv=0.8, KD_h=6.0, Dr=3.0, Kr=1.0, r=0.1)
    assert (r["h_vertical"] + r["h_horizontal"] + r["h_radial"]) == pytest.approx(0.7, rel=1e-6)
    assert r["L"] > 0
    # solo mais permeavel (KD maior) -> L maior
    r2 = D.ernst_espacamento(q=0.002, h=0.7, Dv=0.4, Kv=0.8, KD_h=12.0, Dr=3.0, Kr=1.0, r=0.1)
    assert r2["L"] > r["L"]
    with pytest.raises(ValueError):
        D.ernst_espacamento(q=0.002, h=0.3, Dv=100.0, Kv=0.5, KD_h=6.0, Dr=3.0, Kr=1.0, r=0.1)  # h_v > h


def test_ernst_coerente_com_hooghoudt_solo_homogeneo():
    # homogeneo K=1, D=5, sem resistencia vertical: Ernst (radial ln) ~ Hooghoudt (+-25 %)
    q, h, K, Dd, r = 0.002, 0.6, 1.0, 5.0, 0.1
    L_h = D.hooghoudt_espacamento(q, h, Dd, r, K=K)["L"]
    L_e = D.ernst_espacamento(q=q, h=h, Dv=0.0, Kv=K, KD_h=K * Dd, Dr=Dd, Kr=K, r=r)["L"]
    assert L_e == pytest.approx(L_h, rel=0.25)


def test_glover_dumm_usbr_exemplo_5_10():
    # K=0,305, d_e=4,4, h0=2,7, D'=d_e+h0/2, mu=0,07, L=91: rebaixar 1,5 m abaixo da superficie
    # (ht = 1,2 m) em ~31,8 d (manual p. 168)
    res = D.glover_dumm_tempo(2.7, 1.2, 0.305, 4.4 + 2.7 / 2.0, 0.07, 91.0)
    assert res["t"] == pytest.approx(31.8, rel=0.03)


def test_glover_dumm_ida_e_volta():
    t = D.glover_dumm_tempo(1.0, 0.4, 0.5, 4.0, 0.05, 60.0)["t"]
    assert D.glover_dumm_altura(t, 1.0, 0.5, 4.0, 0.05, 60.0) == pytest.approx(0.4, rel=1e-9)
    L = D.glover_dumm_espacamento(1.0, 0.4, t, 0.5, 4.0, 0.05)["L"]
    assert L == pytest.approx(60.0, rel=1e-9)


def test_tempo_de_drenagem_cresce_com_L_e_mu():
    a = D.tempo_de_drenagem(1.0, 0.4, 0.5, 5.0, 0.1, 0.05, 40.0)["t"]
    b = D.tempo_de_drenagem(1.0, 0.4, 0.5, 5.0, 0.1, 0.05, 80.0)["t"]
    c = D.tempo_de_drenagem(1.0, 0.4, 0.5, 5.0, 0.1, 0.10, 40.0)["t"]
    assert b > 3 * a and c == pytest.approx(2 * a, rel=1e-9)


def test_vazao_de_dreno():
    r = D.vazao_de_dreno(L=40.0, q=0.002, comprimento=300.0)
    assert r["Q_m3_dia"] == pytest.approx(24.0)
    assert r["Q"] == pytest.approx(24.0 / 86400.0)


def test_capacidade_manning_pleno_formula_fechada():
    Dd, S = 0.20, 0.002
    Q = D.capacidade_tubo_dreno(Dd, S, n=0.016)["Q"]
    A, R = math.pi * Dd ** 2 / 4, Dd / 4
    assert Q == pytest.approx(A * R ** (2 / 3) * math.sqrt(S) / 0.016, rel=1e-3)
    # liso (0,011) leva mais vazao que corrugado (0,016)
    assert D.capacidade_tubo_dreno(Dd, S, n=0.011)["Q"] > Q


def test_diametro_minimo_e_inverso_da_capacidade():
    Q = D.capacidade_tubo_dreno(0.20, 0.002, n=0.016)["Q"]
    r = D.diametro_minimo_dreno(Q, 0.002, n=0.016)
    assert r["D_minimo"] == pytest.approx(0.20, rel=1e-6)
    assert r["D_comercial"] == 0.20
    r2 = D.diametro_minimo_dreno(Q * 1.01, 0.002, n=0.016)
    assert r2["D_comercial"] == 0.25


def test_criterio_de_filtro_terzaghi():
    # solo: D15 = 0,02 mm, D85 = 0,30 mm ; filtro D15 = 1,0 mm: reten. 3,33 <= 4, perm. 50 >= 4 (>40: aviso)
    r = D.criterio_de_filtro_hidraulico(1.0, 0.30, 0.02)
    assert r["retencao_D15f_D85s"] == pytest.approx(1.0 / 0.30)
    assert r["atende_retencao"] and r["atende_permeabilidade"]
    assert any("40" in a for a in r["avisos"])
    # filtro grosseiro nao retem
    assert not D.criterio_de_filtro_hidraulico(2.0, 0.30, 0.02)["atende_retencao"]
    # filtro fino nao drena
    assert not D.criterio_de_filtro_hidraulico(0.05, 0.30, 0.02)["atende_permeabilidade"]
    # delegacao do geotextil
    assert any("DELEGAR" in a for a in r["avisos"])


def test_tabelas_indicativas_com_aviso():
    p = D.porosidade_drenavel("areia")
    assert p["mu_min"] < p["mu_medio"] < p["mu_max"]
    r = D.recomendacao_indicativa(1.0)
    assert any("INDICATIVO" in a for a in r["avisos"])
    with pytest.raises(ValueError):
        D.recomendacao_indicativa(50.0)
    with pytest.raises(ValueError):
        D.porosidade_drenavel("lava")


# ---------------------------------------------------------------- (b) casos reais
# --- Xingo Lote I (doc 1419:20-21)
def test_xingo_vazao_por_furo_H3():
    r = D.vazao_por_furo_geomembrana(0.008, 3.0)
    assert r["Q_furo"] == pytest.approx(2.44e-4, rel=0.01)


def test_xingo_tubo_D300_i1e4():
    Q = D.capacidade_tubo_dreno(0.300, 1e-4, formula="xingo")["Q"]
    assert Q == pytest.approx(0.0135, rel=0.01)


def test_xingo_vazao_por_metro_secao_hipotetica():
    r = D.vazao_infiltracao_geomembrana(0.008, 3.5, 16.6)
    assert r["Q_por_m"] == pytest.approx(1.8e-6, rel=0.05)
    # ~3 % da taxa do CSB (6e-5 m3/s/m)
    assert r["Q_por_m"] / 6e-5 == pytest.approx(0.03, rel=0.1)


def test_xingo_n_implicito_da_formula_legada():
    r = D.capacidade_tubo_dreno(0.300, 1e-4, formula="xingo")
    assert any("n pleno implicito" in a for a in r["avisos"])
    Q_man = D.capacidade_tubo_dreno(0.300, 1e-4, n=0.011)["Q"]
    assert 1.1 < r["Q"] / Q_man < 1.3   # legado ~ 18 % acima do Manning pleno liso


# --- CSB GEOHIDRO (doc 1341:74-77)
def test_csb_L800_2DN300():
    r = D.dreno_de_fundo_de_canal_revestido(6e-5, 800.0)
    assert r["Q_total"] == pytest.approx(0.048)
    assert r["Q_por_tubo"] == pytest.approx(0.024)
    assert r["tubo_csb"]["DN"] == 0.300 and not r["tubo_csb"]["no_limite"]


def test_csb_L1000_2DN300_no_limite():
    r = D.dreno_de_fundo_de_canal_revestido(6e-5, 1000.0)
    assert r["Q_por_tubo"] == pytest.approx(0.030)
    assert r["tubo_csb"]["DN"] == 0.300 and r["tubo_csb"]["no_limite"]


@pytest.mark.parametrize("L_acum,DN", [(2000.0, 0.400), (3200.0, 0.500)])
def test_csb_trechos_acumulados(L_acum, DN):
    r = D.dreno_de_fundo_de_canal_revestido(6e-5, L_acum)
    assert r["tubo_csb"]["DN"] == DN


@pytest.mark.xfail(strict=True, reason="DIVERGENCIAS.md: CSB 2DN150 ate 200 m: Q=0,012 -> 0,006 m3/s por tubo "
                   "> 0,005 (limite superior da faixa DN150 do proprio memorial)")
def test_csb_L200_2DN150():
    r = D.dreno_de_fundo_de_canal_revestido(6e-5, 200.0)
    assert r["tubo_csb"]["DN"] == 0.150


def test_csb_mvf_regra_interpretativa():
    # n_MVF = ceil(L*0,30/10)*2 (regra interpretativa do gabarito)
    assert D.dreno_de_fundo_de_canal_revestido(6e-5, 800.0)["n_MVF"] == 2 * math.ceil(24.0)


def test_csb_manning_i_dado_retorna_diametros():
    r = D.dreno_de_fundo_de_canal_revestido(6e-5, 800.0, i=1e-4)
    assert r["D_manning"] > 0.3 and r["D_xingo_legado"] > 0.3
    assert any("gradiente de pressao" in a for a in r["avisos"])


# --- Iuiu 2002 (diagnostico: so consistencia)
def test_iuiu_drenabilidade_sem_dreno_parcelar():
    for K in (0.44, 0.78, 1.98, 2.12):
        r = D.diagnostico_drenabilidade(K, 2.0)
        assert not r["drenagem_subterranea_necessaria"] or K > 2.1
    r = D.diagnostico_drenabilidade(0.05, 2.0)
    assert r["classe"] == "pobre/critica"


# ---------------------------------------------------------------- F5 / v0.2.0: livro (tolerancia 1 %)
# ILRI-DPA16 Tab. 8.1 (PDF 267): d de Hooghoudt para r0 = 0,1 m; forma de Moody reproduz a tabela a < 1 %
@pytest.mark.parametrize("Dd,L,d_tab", [(4.0, 50.0, 2.71), (5.0, 75.0, 3.49), (6.0, 150.0, 4.70),
                                        (10.0, 250.0, 7.53), (2.0, 50.0, 1.72), (3.0, 30.0, 1.97)])
def test_ilri16_tab_8_1_d_equivalente_moody(Dd, L, d_tab):
    assert D.d_equivalente_hooghoudt(Dd, L, 0.1) == pytest.approx(d_tab, rel=0.01)


def test_ilri16_exemplo_8_2_d_serie():
    # Ex. 8.2 (PDF 278): vala, r0 = 0,61 (u = 1,91 m), D = 4,8, L = 72 -> d = 4,16 m
    assert D.d_equivalente_serie(4.8, 72.0, 0.61) == pytest.approx(4.16, rel=0.01)


def test_d_serie_ramos_e_limites():
    # continuidade na troca de ramo (x = 0,5 -> D = L/(4 pi)) e d <= D
    L = 60.0
    D0 = 0.5 * L / (2 * math.pi)
    assert D.d_equivalente_serie(D0 * 0.999, L, 0.1) == pytest.approx(D.d_equivalente_serie(D0 * 1.001, L, 0.1), rel=0.01)
    assert D.d_equivalente_serie(0.05, 100.0, 0.1) <= 0.05
    assert D.d_equivalente_serie(0.0, 50.0, 0.1) == 0.0
    # serie fica abaixo da Tab. 8.1 em 2-3 % (documentado em DIVERGENCIAS)
    assert D.d_equivalente_serie(5.0, 75.0, 0.1) == pytest.approx(3.49, rel=0.04)


def test_ilri16_exemplo_8_1_hooghoudt_65_m():
    # q = 1 mm/d, h = 1,0, D = 4,8, r0 = 0,10, K = 0,14 -> 65 m (tabela; Moody 64,8) e 64 m pela serie
    r = D.hooghoudt_espacamento(0.001, 1.0, 4.8, 0.1, K=0.14)
    assert r["L"] == pytest.approx(65.0, rel=0.01)
    assert D.hooghoudt_espacamento(0.001, 1.0, 4.8, 0.1, K=0.14, metodo_de="serie")["L"] == pytest.approx(64.0, rel=0.01)
    with pytest.raises(ValueError):
        D.hooghoudt_espacamento(0.001, 1.0, 4.8, 0.1, K=0.14, metodo_de="x")


def test_ilri16_exemplo_8_2_hooghoudt_vala_72_m():
    r = D.hooghoudt_espacamento(0.001, 1.0, 4.8, 0.61, K=0.14, metodo_de="serie")
    assert r["L"] == pytest.approx(72.0, rel=0.01)


def test_ilri16_exemplo_8_3_duas_camadas_95_m():
    # Kt = 0,06 (acima do dreno), Kb = 0,30 (abaixo), interface no dreno -> 95 m (= WATERLOG-ENDRAIN Ex. 3, Ritzema)
    r = D.hooghoudt_espacamento(0.001, 1.0, 4.8, 0.1, K_acima=0.06, K_abaixo=0.30)
    assert r["L"] == pytest.approx(95.0, rel=0.01)


def test_hooghoudt_manicoba_dreno_na_barreira_16_96():
    # Embrapa Manicoba p. 3: K = 2,3, h = 1,60 - 1,10 = 0,50, q = 8,0 mm/d, d = 0 -> L = 16,96 m
    r = D.hooghoudt_espacamento(0.008, 0.5, 0.0, 0.05, K=2.3)
    assert r["L"] == pytest.approx(16.96, rel=0.01)


def test_ernst_ilri16_exemplo_8_4_38_m():
    # q = 0,007, h = 0,70, Kt = 0,5, Kb = 2,0, Do = 1,0, Db = 4,0, r0 = 0,05 (PDF 280-281): L = 38 m
    r = D.ernst_duas_camadas_dreno_no_topo(0.007, 0.70, 0.5, 2.0, 1.0, 4.0, 0.05)
    assert r["L"] == pytest.approx(38.0, rel=0.01)
    assert r["a"] == pytest.approx(3.9, rel=0.01)
    assert r["u"] == pytest.approx(0.157, rel=0.01)
    # perdas de carga do livro: 0,01, 0,15 e 0,54 m
    assert r["h_vertical"] == pytest.approx(0.01, abs=0.001)
    assert r["h_horizontal"] == pytest.approx(0.15, abs=0.01)
    assert r["h_radial"] == pytest.approx(0.54, abs=0.01)


def test_ernst_waterlog_endrain_exemplo_4_sem_fator_a():
    # WATERLOG-ENDRAIN p. 10 (Ritzema): 51,8 m reproduz-se com a = 1 (o fator a da Tab. 8.2 foi omitido na nota);
    # com a = 3,9 o ILRI-16 da 38 m (DIVERGENCIAS). Tolerancia 1,5 %: a quadratica impressa usa coeficientes arredondados.
    r = D.ernst_espacamento(q=0.007, h=0.70, Dv=0.70, Kv=0.5, KD_h=2.0 * 4.0 + 0.5 * 1.35, Dr=1.0, Kr=0.5,
                            r=0.05, a=1.0)
    assert r["L"] == pytest.approx(51.8, rel=0.015)


def test_ernst_u_padrao_semicirculo():
    # u = pi r (ILRI-16 Eq. 8.14); u explicito 2 pi r da L maior (resistencia radial menor)
    base = dict(q=0.002, h=0.7, Dv=0.4, Kv=0.8, KD_h=6.0, Dr=3.0, Kr=1.0, r=0.1)
    a = D.ernst_espacamento(**base)
    b = D.ernst_espacamento(**base, u=2 * math.pi * 0.1)
    assert a["u"] == pytest.approx(math.pi * 0.1)
    assert b["L"] > a["L"]
    with pytest.raises(ValueError):
        D.ernst_espacamento(**base, u=-1.0)


def test_fator_geometrico_ernst_tabela_8_2():
    assert D.fator_geometrico_ernst(2.0, 4.0)["a"] == pytest.approx(4.6)
    assert D.fator_geometrico_ernst(50.0, 32.0)["a"] == pytest.approx(4.6)
    assert D.fator_geometrico_ernst(4.0, 2.96)["a"] == pytest.approx(3.9, rel=0.01)   # exemplo 8.4
    assert D.fator_geometrico_ernst(0.05, 3.0)["a"] == 1.0
    assert D.fator_geometrico_ernst(80.0, 3.0)["a"] == 4.0
    assert D.fator_geometrico_ernst(0.5, 3.0)["avisos"]
    with pytest.raises(ValueError):
        D.fator_geometrico_ernst(-1.0, 3.0)


def test_elipse_neh624_exemplo_1():
    # NEH 624 cap. 4 Eq. 4-8 (PDF 63-66): K = 2 pol/h, q = 0,01 pol/h, a = 7 ft, m = 3 ft -> S = 202 ft
    assert D.elipse_espacamento(2.0, 3.0, 7.0, 0.01)["S"] == pytest.approx(202.0, rel=0.01)
    # equivale a Donnan com b = a + m
    assert D.elipse_espacamento(2.0, 3.0, 7.0, 0.01)["S"] == pytest.approx(
        D.donnan_espacamento(2.0, 7.0, 10.0, 0.01)["L"], rel=1e-9)
    with pytest.raises(ValueError):
        D.elipse_espacamento(2.0, 0.0, 7.0, 0.01)


def test_glover_dumm_manicoba_12_72_m():
    # Embrapa Manicoba p. 3: K = 2,3, mu = 0,15, h0 = 0,8, ht = 0,4, t = 3 d, D = D0 + (h0 + ht)/4 = 0,3 m
    Dm = D.d_medio_glover_dumm(0.0, 0.8, 0.4, "manicoba")
    assert Dm == pytest.approx(0.3)
    r = D.glover_dumm_espacamento(0.8, 0.4, 3.0, 2.3, Dm, 0.15)
    assert r["L"] == pytest.approx(12.72, rel=0.01)
    # media dos dois metodos: 14,84 m (p. 3)
    L_h = D.hooghoudt_espacamento(0.008, 0.5, 0.0, 0.05, K=2.3)["L"]
    assert 0.5 * (L_h + r["L"]) == pytest.approx(14.84, rel=0.01)


def test_glover_dumm_fator_116_ilri16():
    # ILRI-16 Eq. 8.31/8.32 (PDF 284): freatico inicial horizontal 4/pi = 1,27; parabola de 4o grau 1,16
    h116 = D.glover_dumm_altura(10.0, 1.0, 0.5, 4.0, 0.05, 60.0)
    h127 = D.glover_dumm_altura(10.0, 1.0, 0.5, 4.0, 0.05, 60.0, fator=4.0 / math.pi)
    assert h127 / h116 == pytest.approx((4.0 / math.pi) / 1.16, rel=1e-9)
    # h_t = 1,16 h0 e^{-alfa t}, alfa = pi^2 K d/(mu L^2)
    alfa = math.pi ** 2 * 0.5 * 4.0 / (0.05 * 60.0 ** 2)
    assert h116 == pytest.approx(1.16 * math.exp(-alfa * 10.0), rel=1e-9)
    # ida e volta com fator horizontal
    t = D.glover_dumm_tempo(1.0, 0.4, 0.5, 4.0, 0.05, 60.0, fator=4.0 / math.pi)["t"]
    assert D.glover_dumm_altura(t, 1.0, 0.5, 4.0, 0.05, 60.0, fator=4.0 / math.pi) == pytest.approx(0.4, rel=1e-9)


def test_d_medio_glover_dumm_criterios_divergem():
    # USBR (d_e + h0/2) x Manicoba (d_e + (h0+ht)/4): tempos do exemplo USBR 5-10 diferem > 5 % (DIVERGENCIAS)
    t_usbr = D.glover_dumm_tempo(2.7, 1.2, 0.305, D.d_medio_glover_dumm(4.4, 2.7, 1.2, "usbr"), 0.07, 91.0)["t"]
    t_man = D.glover_dumm_tempo(2.7, 1.2, 0.305, D.d_medio_glover_dumm(4.4, 2.7, 1.2, "manicoba"), 0.07, 91.0)["t"]
    assert t_usbr == pytest.approx(31.8, rel=0.03)
    assert abs(t_man - t_usbr) / t_usbr > 0.05
    assert D.d_medio_glover_dumm(4.4, 2.7, 1.2, "ilri") == 4.4
    with pytest.raises(ValueError):
        D.d_medio_glover_dumm(4.4, 2.7, 1.2, "x")


# ---------------------------------------------------------------- capacidade de tubo e dreno de fundo (Delmiro)
def test_tubo_parcial_meia_secao_e_geometria_exata():
    Dd, S, n = 0.30, 0.002, 0.016
    pleno = D.capacidade_tubo_dreno(Dd, S, n)["Q"]
    assert D.capacidade_tubo_parcial(Dd, S, n, 0.5)["Q"] == pytest.approx(0.5 * pleno, rel=1e-3)
    # y/D = 0,8: Q/Q_pleno = 0,977 (curva de Manning para secao circular, valor usual de tabelas)
    assert D.capacidade_tubo_parcial(Dd, S, n, 0.8)["Q"] / pleno == pytest.approx(0.977, rel=0.01)
    # cheio (y/D = 1) = pleno
    assert D.capacidade_tubo_parcial(Dd, S, n, 1.0)["Q"] == pytest.approx(pleno, rel=1e-3)
    with pytest.raises(ValueError):
        D.capacidade_tubo_parcial(Dd, S, n, 1.2)


def test_delmiro_tubo_recalculo_manning_acervo_sem_h():
    # acervo, sem checagem humana: caso Delmiro recalculo (D interno 0,149 e 0,200, n = 0,016, S = 3e-4, meia secao)
    assert D.capacidade_tubo_parcial(0.149, 3e-4, 0.016, 0.5)["Q"] == pytest.approx(1.05e-3, rel=0.05)
    assert D.capacidade_tubo_parcial(0.200, 3e-4, 0.016, 0.5)["Q"] == pytest.approx(2.31e-3, rel=0.05)


def test_delmiro_razao_entre_dn_segue_d_8_3():
    # Q ~ D^(8/3): (200/149)^(8/3) = 2,19; o memorial dá 4,929e-4/1,518e-4 = 3,25 (equivale a D^4)
    q1 = D.capacidade_tubo_parcial(0.149, 3e-4, 0.016)["Q"]
    q2 = D.capacidade_tubo_parcial(0.200, 3e-4, 0.016)["Q"]
    assert q2 / q1 == pytest.approx((200 / 149) ** (8 / 3), rel=0.01)
    assert 4.929e-4 / 1.518e-4 > 1.4 * (q2 / q1)


@pytest.mark.xfail(strict=True, reason="DIVERGENCIAS.md: Delmiro DN170: Q declarado 1,518e-4 m3/s x Manning meia "
                   "secao 1,05e-3 (6,9x)")
def test_delmiro_capacidade_dn170_declarada():
    assert D.capacidade_tubo_parcial(0.149, 3e-4, 0.016)["Q"] == pytest.approx(1.518e-4, rel=0.05)


@pytest.mark.xfail(strict=True, reason="DIVERGENCIAS.md: Delmiro DN230: Q declarado 4,929e-4 m3/s x Manning meia "
                   "secao 2,31e-3 (4,7x)")
def test_delmiro_capacidade_dn230_declarada():
    assert D.capacidade_tubo_parcial(0.200, 3e-4, 0.016)["Q"] == pytest.approx(4.929e-4, rel=0.05)


def test_delmiro_qd_darcy_e_lmax():
    # acervo (rastro B): K = 1e-6 m/s, H = 1,26, X = 4,06 -> qd = 3,91e-7; Lmax = Q/qd = 388 e 1260 m
    qd = D.vazao_unitaria_darcy_dreno_fundo(1e-6, 1.26, 4.06)["qd"]
    assert qd == pytest.approx(3.910e-7, rel=0.01)
    assert D.comprimento_maximo_dreno_fundo(1.518e-4, 3.910e-7)["L_max"] == pytest.approx(388.0, rel=0.01)
    r = D.comprimento_maximo_dreno_fundo(4.929e-4, 3.910e-7)
    assert r["L_max"] == pytest.approx(1260.0, rel=0.01)
    assert r["L_trecho"] == 250.0          # limite de manutencao governa
    assert D.vazao_unitaria_darcy_dreno_fundo(1e-6, 1.26, 4.06, lados=1)["qd"] == pytest.approx(qd / 2)
    with pytest.raises(ValueError):
        D.comprimento_maximo_dreno_fundo(0.0, 1e-7)


# ---------------------------------------------------------------- envoltorio (ILRI-56) e tabelas paginadas
def test_envoltorio_pontos_de_controle_ilri56():
    r = D.envoltorio_granular_pontos_controle(0.05, 0.20)
    assert r["D15c_max"] == pytest.approx(1.4)          # ponto 1: 7 d85f
    assert r["D50c"] == pytest.approx(7.0)              # ponto 2: 5 D15c
    assert r["D100c_max"] == 9.5                        # ponto 3
    assert r["D15f_4a"] == pytest.approx(0.20)          # ponto 4a: 4 d15c
    assert r["D15f_4b"] == pytest.approx(0.28)          # ponto 4b: D15c/5
    assert r["D15f"] == pytest.approx(0.28)             # 4b > 4a: usa 4b
    assert r["D5f_min"] == 0.074
    # conflito: d15c grande => 4a > ponto 1
    c = D.envoltorio_granular_pontos_controle(0.5, 0.20)
    assert any("4a" in a for a in c["avisos"])
    with pytest.raises(ValueError):
        D.envoltorio_granular_pontos_controle(0.05, 0.20, D15c_adotado=2.0)


def test_necessidade_envoltorio_hfg_ilri56():
    r = D.necessidade_envoltorio_ilri56(argila_pct=10, PI=5, Ks=0.5, q1max=0.0002, Ap=0.002)
    assert r["HFG"] == pytest.approx(math.exp(0.332 - 0.132 * 0.5 + 1.07 * math.log(5.0)))
    assert r["i_x"] == pytest.approx(0.0002 / (0.5 * 0.001))
    assert r["envoltorio_necessario_por_HFG"] is False
    # gradiente de saida alto (area perfurada minima): envoltorio necessario
    assert D.necessidade_envoltorio_ilri56(10, 5, 0.5, 0.01, 0.002)["envoltorio_necessario_por_HFG"] is True
    assert any("40" in a for a in D.necessidade_envoltorio_ilri56(45, 5, 0.5, 0.0002, 0.002)["indicadores"])
    with pytest.raises(ValueError):
        D.necessidade_envoltorio_ilri56(10, 0, 0.5, 0.0002, 0.002)


def test_tabelas_paginadas_ilri56():
    assert D.faixa_K_por_textura("areia_media")["K_min"] == 1.0
    assert D.faixa_K_por_textura("areia_media")["K_max"] == 5.0
    assert D.faixa_K_por_textura("cascalho_brita")["K_max"] == 3500.0
    assert D.coeficiente_drenagem_tipico("irrigado_arido")["q_mm_d"] == (1.0, 2.0)
    assert D.coeficiente_drenagem_tipico("umido")["q_m_d"] == (0.007, 0.014)
    with pytest.raises(ValueError):
        D.faixa_K_por_textura("lava")
    with pytest.raises(ValueError):
        D.coeficiente_drenagem_tipico("polar")


def test_cli_ernst_duas_camadas():
    p = _cli(["--json", json.dumps({"funcao": "ernst_duas_camadas_dreno_no_topo", "q": 0.007, "h": 0.7,
                                    "Kt": 0.5, "Kb": 2.0, "Do": 1.0, "Db": 4.0, "r": 0.05})])
    assert p.returncode == 0, p.stdout + p.stderr
    out = json.loads(p.stdout)
    assert out["saidas"]["L"] == pytest.approx(38.0, rel=0.01)
    assert out["versao"] == "0.2.0"


# ---------------------------------------------------------------- CLI
def _cli(args):
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    return subprocess.run([sys.executable, "-m", "tools.dren.drenos"] + args, cwd=RAIZ, capture_output=True,
                          text=True, env=env, encoding="utf-8", stdin=subprocess.DEVNULL)


def test_cli_json_padrao():
    p = _cli(["--json", json.dumps({"funcao": "hooghoudt_espacamento", "q": 0.002, "K": 1.0, "h": 0.6,
                                    "D": 5.0, "r": 0.1})])
    assert p.returncode == 0, p.stdout + p.stderr
    out = json.loads(p.stdout)
    assert set(out) >= {"entradas", "saidas", "metodo", "avisos", "versao"}
    assert out["saidas"]["L"] > 0


def test_cli_argumentos_nomeados_e_erro():
    p = _cli(["--funcao", "criterio_de_filtro_hidraulico", "--D15_filtro", "1.0", "--D85_solo", "0.3",
              "--D15_solo", "0.02"])
    assert p.returncode == 0, p.stdout + p.stderr
    assert json.loads(p.stdout)["saidas"]["atende"] is True
    assert _cli(["--funcao", "nao_existe"]).returncode == 2


# ---------------------------------------------------------------- Wesseling (opcao; padrao segue Manning)
# Item 20 do PARA_O_ANDRE_F7. Q = 89 d^2,714 s^0,571 [FAO-IDP62 p. 214]; formula para tubo tecnicamente liso.
def test_wesseling_valor_de_mao():
    # 89 * 0,30^2,714 * 1e-3^0,571 = 6,57e-2 m3/s (tabela de tubo-dreno-e-coletores.md)
    assert D.capacidade_tubo_dreno(0.30, 1e-3, formula="wesseling")["Q"] == pytest.approx(6.57e-2, rel=0.01)
    assert D.capacidade_tubo_dreno(0.10, 1e-3, formula="wesseling")["Q"] == pytest.approx(3.33e-3, rel=0.01)


def test_wesseling_teste_de_livro_blasius_a040():
    # Livro: "quase os mesmos resultados das Eq. 6-9 com a = 40" (Blasius a = 0,40). Derivacao de Blasius com
    # inflow linear reproduz C = 89 a 1 % com nu = 1,3e-6 m2/s (10 C; nu nao e dado no trecho) e a 5 % com
    # nu = 1e-6 (o "aprox. 1e-6" do texto).
    assert D.wesseling_coeficiente(0.40, 1.3e-6) == pytest.approx(89.0, rel=0.01)
    assert D.wesseling_coeficiente(0.40, 1.0e-6) == pytest.approx(89.0, rel=0.05)


def test_wesseling_padrao_continua_manning_e_aviso_dominio():
    assert D.capacidade_tubo_dreno(0.30, 1e-4)["Q"] == pytest.approx(7.86e-3, rel=0.01)  # padrao n = 0,016
    r = D.capacidade_tubo_dreno(0.30, 1e-4, formula="wesseling")
    assert any("tecnicamente liso" in a for a in r["avisos"])
    assert D.diametro_minimo_dreno(r["Q"], 1e-4, formula="wesseling")["D_minimo"] == pytest.approx(0.30, rel=1e-3)


def test_wesseling_d86_dn300_efeito():
    # D-86: DN300, s = 1e-4. Manning n 0,016 -> 7,86e-3; n 0,011 -> 1,14e-2; Wesseling -> 1,76e-2 m3/s
    qm16 = D.capacidade_tubo_dreno(0.30, 1e-4, n=0.016)["Q"]
    qm11 = D.capacidade_tubo_dreno(0.30, 1e-4, n=0.011)["Q"]
    qw = D.capacidade_tubo_dreno(0.30, 1e-4, formula="wesseling")["Q"]
    assert qw == pytest.approx(1.76e-2, rel=0.01)
    assert qw / qm16 == pytest.approx(2.24, rel=0.02) and qw / qm11 == pytest.approx(1.54, rel=0.02)
