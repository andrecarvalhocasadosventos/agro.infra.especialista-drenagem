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
