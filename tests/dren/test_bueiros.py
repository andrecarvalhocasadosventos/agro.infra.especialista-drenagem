"""Testes de tools.dren.bueiros (HDS-5 e metodos legados do acervo).

Tolerancias: formulas fechadas 1e-6 relativo; gabaritos dos casos reais 5 %
(D11) salvo a tolerancia declarada no caso; cotas 0,01 m.
"""
import json
import math
import os
import pathlib
import subprocess
import sys

import pytest

from tools.dren import bueiros as b

RAIZ = str(pathlib.Path(__file__).resolve().parents[2])


# ============================ (a) livro / consistencia =====================
def test_ku_si_equivale_a_unidades_inglesas():
    # 36 in (3 ft), Q = 30 cfs, A=7,0686 ft2: Q/(A D^0.5) = 2,4504 (US, Ku=1)
    x_us = 30.0 / (math.pi * 9 / 4 * math.sqrt(3.0))
    Q = 30.0 * 0.0283168466
    D = 3.0 * 0.3048
    r = b.controle_de_entrada(Q, "circular", D, "circ_concreto_aresta_viva_muro", 0.0, detalhado=True)
    assert r["saidas"]["X"] == pytest.approx(x_us, rel=1e-3)


def test_entrada_submersa_formula_fechada():
    # retangular 2x2, 1 celula, alas 30-75: HW/D = 0,0347 X^2 + 0,81 - 0,5 S0
    Q, S0 = 20.0, 0.01
    X = 1.811 * Q / (4 * math.sqrt(2))
    esperado = (0.0347 * X ** 2 + 0.81 - 0.5 * S0) * 2
    assert b.controle_de_entrada(Q, "retangular", (2, 2), "ret_alas_30_75", S0) == pytest.approx(esperado, rel=1e-9)


def test_entrada_nao_submersa_forma1_usa_carga_critica():
    Q, S0 = 3.0, 0.005
    HW = b.controle_de_entrada(Q, "retangular", (2, 2), "ret_alas_30_75", S0)
    dc = (Q ** 2 / 9.81 / 4) ** (1 / 3)
    Hc = dc + (Q / (2 * dc)) ** 2 / (2 * 9.81)
    X = 1.811 * Q / (4 * math.sqrt(2))
    assert HW == pytest.approx((Hc / 2 + 0.026 * X ** 1.0 - 0.5 * S0) * 2, rel=1e-5)


def test_entrada_forma2():
    Q = 4.0
    X = 1.811 * Q / (4 * math.sqrt(2))
    HW = b.controle_de_entrada(Q, "retangular", (2, 2), "ret_muro_chanfro_3_4", 0.01)
    assert HW == pytest.approx(0.515 * X ** 0.667 * 2, rel=1e-9)


def test_hw_cresce_com_Q_e_transicao_continua():
    qs = [0.3 * k for k in range(1, 40)] + [12 * 1.1 ** k for k in range(0, 15)]
    for tipo, forma, dim in (("circ_concreto_aresta_viva_muro", "circular", 1.2),
                             ("circ_concreto_boca_sino_muro", "circular", 1.2),
                             ("ret_alas_30_75", "retangular", (2, 2)),
                             ("ret_alas_90_15", "retangular", (2, 2)),
                             ("arco_corrugado_muro", "arco", (2.0, 1.5))):
        hws = [b.controle_de_entrada(q, forma, dim, tipo, 0.01) for q in qs]
        assert all(h2 > h1 for h1, h2 in zip(hws, hws[1:])), tipo
        # sem saltos acima de Q = 3 m3/s (passo de 10 %): razao limitada
        assert max(h2 / h1 for q1, h1, h2 in zip(qs, hws, hws[1:]) if q1 >= 3) < 1.25, tipo


def test_transicao_liga_os_extremos():
    g = (2, 2)
    A, D = 4.0, 2.0
    q35 = 3.5 * A * math.sqrt(D) / 1.811
    q40 = 4.0 * A * math.sqrt(D) / 1.811
    h35 = b.controle_de_entrada(q35 * 0.9999, "retangular", g, "ret_alas_30_75", 0.01)
    h35b = b.controle_de_entrada(q35 * 1.0001, "retangular", g, "ret_alas_30_75", 0.01)
    h40 = b.controle_de_entrada(q40 * 1.0001, "retangular", g, "ret_alas_30_75", 0.01)
    assert h35b == pytest.approx(h35, rel=1e-3)
    meio = b.controle_de_entrada(0.5 * (q35 + q40), "retangular", g, "ret_alas_30_75", 0.01, detalhado=True)
    assert meio["saidas"]["regime"] == "transicao"
    assert h35 < meio["saidas"]["HW_m"] < h40


def test_correcao_declividade_mitrado_sinal():
    # regime submerso, X>4: S0 reduz HW (-0,5 S) exceto mitrado (+0,7 S)
    kw = dict(Q=6.0, forma="arco", dim=(1.8, 1.4), n_celulas=1)
    a0 = b.controle_de_entrada(tipo_de_entrada="arco_corrugado_mitrado", S0=0.0, **kw)
    a1 = b.controle_de_entrada(tipo_de_entrada="arco_corrugado_mitrado", S0=0.05, **kw)
    assert a1 > a0
    kw2 = dict(Q=6.0, forma="circular", dim=1.0, n_celulas=1)
    c0 = b.controle_de_entrada(tipo_de_entrada="circ_concreto_aresta_viva_muro", S0=0.0, **kw2)
    c1 = b.controle_de_entrada(tipo_de_entrada="circ_concreto_aresta_viva_muro", S0=0.05, **kw2)
    assert c1 < c0


def test_boca_de_sino_melhor_que_aresta_viva():
    for q in (1.0, 2.0, 4.0, 6.0):
        a = b.controle_de_entrada(q, "circular", 1.2, "circ_concreto_aresta_viva_muro", 0.005)
        s = b.controle_de_entrada(q, "circular", 1.2, "circ_concreto_boca_sino_muro", 0.005)
        assert s < a


def test_mais_celulas_reduz_hw():
    h1 = b.controle_de_entrada(10, "retangular", (2, 2), "ret_alas_30_75", 0.005, 1)
    h2 = b.controle_de_entrada(10, "retangular", (2, 2), "ret_alas_30_75", 0.005, 2)
    assert h2 < h1


def test_tipo_forma_incompativel_e_desconhecido():
    with pytest.raises(ValueError):
        b.controle_de_entrada(1, "circular", 1.0, "ret_alas_30_75", 0.01)
    with pytest.raises(ValueError):
        b.controle_de_entrada(1, "circular", 1.0, "inexistente", 0.01)


def test_profundidade_critica_e_normal():
    for forma, dim in (("circular", 1.2), ("retangular", (2.0, 1.5)), ("arco", (2.0, 1.5))):
        Q = 1.5
        dc = b.profundidade_critica(Q, forma, dim)
        g = b._geo(forma, dim)
        A, _, T = b._secao(g, dc)
        assert A ** 3 / T == pytest.approx(Q ** 2 / 9.81, rel=1e-4)
        yn = b.profundidade_normal(Q, forma, dim, 0.015, 0.004)
        assert b.manning_lamina(forma, dim, yn, 0.015, 0.004)["Q"] == pytest.approx(Q, rel=1e-4)
    # retangular: dc = (q^2/g)^(1/3)
    assert b.profundidade_critica(6.0, "retangular", (2.0, 2.0)) == pytest.approx((9 / 9.81) ** (1 / 3), rel=1e-6)


def test_saida_formula_fechada_afogado():
    # 2x2, 1 celula, Q=8: V=2; R=0,5; TW=2,5 >= D
    V = 2.0
    hv = V * V / (2 * 9.81)
    esperado = 2.5 + (1 + 0.5 + 19.63 * 0.015 ** 2 * 50 / 0.5 ** 1.33) * hv - 50 * 0.001
    r = b.controle_de_saida(8.0, "retangular", (2, 2), 0.015, 0.5, 50, 0.001, 2.5, detalhado=True)
    assert r["saidas"]["HW_m"] == pytest.approx(esperado, rel=1e-9)
    assert not any("saida livre" in a for a in r["avisos"])


def test_saida_livre_usa_dc_mais_D_sobre_2_e_avisa():
    r = b.controle_de_saida(8.0, "retangular", (2, 2), 0.015, 0.5, 50, 0.001, 0.0, detalhado=True)
    dc = (4.0 ** 2 / 9.81) ** (1 / 3)  # q = 4 m2/s
    assert r["saidas"]["ho_m"] == pytest.approx((dc + 2) / 2, rel=1e-6)
    assert any("saida livre" in a for a in r["avisos"])


def test_saida_domina_quando_L_grande_e_S0_pequena():
    kw = dict(Q=3.0, forma="circular", dim=1.2)
    hi = b.controle_de_entrada(tipo_de_entrada="circ_concreto_boca_sino_muro", S0=0.001, **kw)
    ho = b.controle_de_saida(n=0.015, Ke=0.2, L=120, S0=0.001, TW=1.2, **kw)
    assert ho > hi
    # e entrada domina com declividade forte, curto e sem remanso
    hi2 = b.controle_de_entrada(tipo_de_entrada="circ_concreto_aresta_viva_muro", S0=0.05, **kw)
    ho2 = b.controle_de_saida(n=0.015, Ke=0.5, L=10, S0=0.05, TW=0.0, **kw)
    assert hi2 > ho2


def test_dimensionar_ordena_por_area_e_respeita_HW_max():
    r = b.dimensionar_bueiro(Q=10.0, HW_max=3.0, TW=0.5, L=30, S0=0.005, forma="retangular",
                             tipo_de_entrada="ret_alas_30_75")
    alts = r["saidas"]["alternativas"]
    assert alts and all(a["HW_m"] <= 3.0 for a in alts)
    areas = [a["area_total_m2"] for a in alts]
    assert areas == sorted(areas)
    assert r["saidas"]["melhor"] == alts[0]
    for a in alts:
        assert a["HW_m"] == pytest.approx(max(a["HW_entrada_m"], a["HW_saida_m"]))
        assert a["controle"] in ("entrada", "saida")
    assert set(r) == {"entradas", "saidas", "metodo", "avisos", "versao"}


def test_dimensionar_candidatas_explicitas_e_aviso_celulas():
    cands = [{"forma": "circular", "dim": 1.5, "n_celulas": 3, "tipo_de_entrada": "circ_concreto_boca_sino_muro"}]
    r = b.dimensionar_bueiro(Q=6.0, HW_max=5.0, TW=0.0, L=20, S0=0.01, candidatas=cands)
    assert len(r["saidas"]["alternativas"]) == 1
    assert any("afastamento" in a for a in r["avisos"])
    r2 = b.dimensionar_bueiro(Q=60.0, HW_max=1.0, TW=0.0, L=20, S0=0.01, candidatas=cands)
    assert r2["saidas"]["alternativas"] == [] and r2["avisos"]


def test_velocidade_saida_e_dissipador():
    v = b.velocidade_de_saida(2.0, "retangular", (2, 2), 0.015, 0.02, TW=0.0)
    assert v["V_m_s"] > 2.0 and v["Fr"] > 1  # declividade forte: supercritico
    assert b.dissipador_necessario(v["V_m_s"], "argila_rija")["necessario"]
    assert not b.dissipador_necessario(v["V_m_s"], "concreto")["necessario"]
    cheio = b.velocidade_de_saida(8.0, "retangular", (2, 2), 0.015, 0.001, TW=2.5, controle="saida")
    assert cheio["V_m_s"] == pytest.approx(2.0)
    with pytest.raises(ValueError):
        b.dissipador_necessario(1.0, "rocha_inventada")


def test_orificio_ida_e_volta():
    h = b.verificacao_por_orificio(10.0, 5.0)
    assert h == pytest.approx((10 / (0.62 * 5)) ** 2 / 19.62)
    assert b.verificacao_por_orificio(None, 5.0, 0.62, h) == pytest.approx(10.0)


def test_manning_plena_circular():
    c = b.manning_cheia("circular", 1.0, 0.013, 0.01)
    assert c["Q"] == pytest.approx(math.pi / 4 * 0.25 ** (2 / 3) * 0.1 / 0.013, rel=1e-9)
    v = b.verificacao_manning_plena(c["Q"] * 1.1, "circular", 1.0, 0.013, 0.01)
    assert not v["atende"]


def test_cli_json():
    cmd = [sys.executable, "-m", "tools.dren.bueiros", "--json", json.dumps(
        {"funcao": "controle_de_entrada", "Q": 3.0, "forma": "circular", "dim": 1.2,
         "tipo_de_entrada": "circ_concreto_boca_sino_muro", "S0": 0.01})]
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    out = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", env=env, cwd=RAIZ,
                         stdin=subprocess.DEVNULL).stdout
    d = json.loads(out)
    assert d["saidas"]["HW_m"] > 0 and d["versao"] and "avisos" in d and "metodo" in d
    assert d["entradas"]["forma"] == "circular"


# ============================ (b) gabaritos dos casos ======================
# --- Baixio de Irece (casos/.../baixio_irece_bueiros_dimensionamento.md) ----
def test_baixio_manning_celular_2_5x2_5():
    m = b.manning_lamina("retangular", (2.5, 2.5), 2.4, 0.015, 0.005)
    assert m["V"] == pytest.approx(4.136, rel=0.005)
    assert m["Q"] == pytest.approx(24.82, rel=0.005)
    assert 2 * m["Q"] == pytest.approx(49.64, rel=0.005)


def test_baixio_manning_celular_2x2():
    m = b.manning_lamina("retangular", (2.0, 2.0), 1.9, 0.015, 0.005)
    assert m["V"] == pytest.approx(3.556, rel=0.005)
    assert m["Q"] * 2 == pytest.approx(27.03, rel=0.005)


def test_baixio_orificio_tr50():
    # Q50=61,98; 2 celulas 2,5x2,5 (A total 12,5), C=0,62 -> h=3,260 m; cota 407,846 (tol 0,01 m)
    h = b.verificacao_por_orificio(61.98, 12.5, 0.62)
    assert h == pytest.approx(3.260, abs=0.01)
    assert 403.335 + 1.25 + h == pytest.approx(407.846, abs=0.01)


@pytest.mark.xfail(reason="Baixio BU-CP0-15: caso diz folga 0,66 m com TN=408,31, mas 408,31-407,846=0,464 m "
                          "(inconsistencia aritmetica do gabarito; TN implicito seria 408,51). Ver DIVERGENCIAS.md",
                   strict=True)
def test_baixio_folga_ao_tn():
    h = b.verificacao_por_orificio(61.98, 12.5, 0.62)
    assert 408.31 - (403.335 + 1.25 + h) == pytest.approx(0.66, abs=0.01)


OBRAS_BAIXIO = {  # nome: (Q50, (B,H), n_celulas, i)
    "BU-CP0-13": (33.37, (2.0, 2.0), 2, 0.005),
    "BU-CP0-15": (61.98, (2.5, 2.5), 2, 0.005),
    "BU-CP0-18": (185.36, (3.0, 3.0), 4, 0.005),
    "BU-CP0-27": (9.34, (1.5, 1.5), 1, 0.0068),
    "BU-CS1-01": (73.13, (2.2, 2.2), 3, 0.005),
}


@pytest.mark.parametrize("obra", [
    pytest.param("BU-CP0-13", marks=pytest.mark.xfail(
        reason="legado (orificio) x HDS-5 alas 30-75: -8,0 % (>5 %); ver DIVERGENCIAS.md", strict=True)),
    pytest.param("BU-CP0-15", marks=pytest.mark.xfail(
        reason="legado (orificio) x HDS-5 alas 30-75: -6,4 % (>5 %); ver DIVERGENCIAS.md", strict=True)),
    pytest.param("BU-CP0-18", marks=pytest.mark.xfail(
        reason="legado (orificio) x HDS-5 alas 30-75: -7,8 % (>5 %); ver DIVERGENCIAS.md", strict=True)),
    "BU-CP0-27",
    "BU-CS1-01",
])
def test_baixio_legado_vs_hds5_5pct(obra):
    """Metodo legado (orificio) vs HDS-5 nos mesmos dados (hipotese: entrada com alas
    30-75, L=40 m, TW=0). O legado sempre subestima o HW; a diferenca cresce com
    entradas menos eficientes (0 e 90/15 graus: -12 a -18 %)."""
    Q, dim, k, i = OBRAS_BAIXIO[obra]
    r = b.comparar_legado_hds5(Q, "retangular", dim, "ret_alas_30_75", 0.015, 40, i, 0.0, k)
    assert abs(r["saidas"]["diferenca_relativa"]) <= 0.05


@pytest.mark.parametrize("obra", list(OBRAS_BAIXIO))
def test_baixio_legado_subestima_hds5(obra):
    """Treinamento: o orificio legado fica abaixo do HDS-5 (entre 3 e 20 %) para
    qualquer entrada retangular de concreto; o controle de entrada governa."""
    Q, dim, k, i = OBRAS_BAIXIO[obra]
    for te in ("ret_alas_30_75", "ret_alas_90_15", "ret_alas_0"):
        r = b.comparar_legado_hds5(Q, "retangular", dim, te, 0.015, 40, i, 0.0, k)["saidas"]
        assert -0.20 <= r["diferenca_relativa"] <= -0.03
        assert r["HW_entrada_m"] >= r["HW_saida_m"]


# --- Salitre RC500-800 (Tabela 10.9, doc 1357:197) -------------------------
@pytest.mark.parametrize("nome,B,y,i,V_doc,Qcam_doc", [
    ("BTCC1", 1.5, 1.3, 0.0101, 4.1, 8.1),
    ("BTCC2", 2.0, 1.4, 0.0076, 4.1, 11.5),
    ("BTCC7", 2.0, 1.9, 0.0107, 5.2, 20.2),
    ("BDCC5", 1.5, 1.3, 0.0120, 4.4, 8.4),
])
def test_salitre_manning_v(nome, B, y, i, V_doc, Qcam_doc):
    m = b.manning_lamina("retangular", (B, B), y, 0.015, i)
    assert m["V"] == pytest.approx(V_doc, rel=0.03)
    # Q/camara do doc = Q total/n_camaras, comparavel a capacidade de Manning (tol 5 %)
    assert m["Q"] == pytest.approx(Qcam_doc, rel=0.06)


# --- Jaiba Etapas 3-4 (sifao como bueiro afogado, doc 1182:57) -------------
def test_jaiba_controle_de_saida():
    r = b.controle_de_saida(2.54, "retangular", (1.5, 1.5), 0.015, 0.5, 90.0, 0.0, 1.2, 2, detalhado=True)
    s = r["saidas"]
    assert s["V_m_s"] == pytest.approx(0.564, rel=0.01)
    assert s["Hf_m"] == pytest.approx(0.024, abs=0.005)  # doc 0,02
    na_montante = 480.09 - 1.2 + s["HW_m"]
    assert na_montante == pytest.approx(480.13, abs=0.01)


def test_jaiba_vazao_2_44_tambem_dentro_da_tolerancia():
    r = b.controle_de_saida(2.44, "retangular", (1.5, 1.5), 0.015, 0.5, 90.0, 0.0, 1.2, 2, detalhado=True)
    assert 480.09 - 1.2 + r["saidas"]["HW_m"] == pytest.approx(480.13, abs=0.01)


# --- CSB: BTCC-No17 (doc 1341:205) -----------------------------------------
@pytest.mark.xfail(reason="CSB BTCC-N17: Manning n=0,015, y=1,5 m, i=0,0045 da 28,6 m3/s (3 cel. 2x2) "
                          "vs Q=39,18 do projeto (-27 %); V/Yo da Tab 4.7 nao reproduzem (doc 1341:205). "
                          "Ver DIVERGENCIAS.md", strict=True)
def test_csb_btcc17_capacidade_manning():
    m = b.manning_lamina("retangular", (2.0, 2.0), 1.5, 0.015, 0.0045)
    assert 3 * m["Q"] == pytest.approx(39.18, rel=0.05)


def test_csb_btcc17_hds5_hw_dentro_da_ordem_de_grandeza():
    # sem HW no doc; verificacao de consistencia: HDS-5 (entrada) com 3 cel 2x2, alas 30-75
    r = b.comparar_legado_hds5(39.18, "retangular", (2.0, 2.0), "ret_alas_30_75", 0.015, 40.0, 0.0045, 0.0, 3)
    assert 2.0 < r["saidas"]["HW_hds5_m"] < 3.5  # HW/D ~ 1,4
    assert r["saidas"]["diferenca_relativa"] < 0


# --- Xingo Lote I (doc 1419:154-155): lamina supercritica -------------------
def test_xingo_continuidade_bu01():
    # Q/celula / (B y) = V (doc: 4,48/(1,5*0,96) = 3,11 ~ 3,10)
    assert (8.96 / 2) / (1.5 * 0.96) == pytest.approx(3.10, rel=0.01)
    assert b.manning_cheia("retangular", (1.5, 1.5), 0.015, 0.01009, 2)["Q"] > 8.96  # cabe a seccao plena


@pytest.mark.parametrize("nome,B,i,Q,cel,y_doc,V_doc", [
    pytest.param("BU-01", 1.5, 0.01009, 8.96, 2, 0.96, 3.10, marks=pytest.mark.xfail(
        reason="Xingo BU-01: Manning normal da y=0,83 m V=3,6 vs doc 0,96 m/3,10 (energia/remanso; "
               "ver DIVERGENCIAS.md)", strict=True)),
    pytest.param("BU-06", 2.5, 0.0119, 39.30, 2, 1.76, 4.46, marks=pytest.mark.xfail(
        reason="Xingo BU-06: yn=1,42 vs 1,76 m doc (energia/remanso)", strict=True)),
    pytest.param("BU-24", 3.0, 0.00976, 48.8, 2, 1.87, 4.36, marks=pytest.mark.xfail(
        reason="Xingo BU-24: yn=1,50 vs 1,87 m doc (energia/remanso)", strict=True)),
])
def test_xingo_lamina_normal_vs_doc(nome, B, i, Q, cel, y_doc, V_doc):
    yn = b.profundidade_normal(Q / cel, "retangular", (B, B), 0.015, i)
    assert yn == pytest.approx(y_doc, rel=0.05)
    assert b.manning_lamina("retangular", (B, B), yn, 0.015, i)["V"] == pytest.approx(V_doc, rel=0.05)



# ===================== v0.2.0: achados da skill bueiros-e-drenagem-superficial =====================
def test_versao_030():
    assert b.VERSAO == "0.3.0"


# --- HDS-5 DG 1 (tolerancia 2 %) -------------------------------------------------------------
@pytest.mark.parametrize("tipo,esperado", [("ret_alas_90_15", 2.94), ("ret_muro_bisel_45", 2.62)])
def test_hds5_p280_caixa_1524_q8495(tipo, esperado):
    # HDS-5 p. 279-281: caixa 5x5 ft, Q50 = 8,495 m3/s, S = 0,02 (HY-8 2,94 m; nomograma bisel 2,62 m)
    hw = b.controle_de_entrada(8.495, "retangular", (1.524, 1.524), tipo, 0.02)
    assert hw == pytest.approx(esperado, rel=0.02)


def test_hds5_p273_274_tubo_54pol_boca_sino_muro():
    # HDS-5 p. 273-274: DN 1,3716 m, Q25 = 5,663 m3/s, S = 0,01, TW = 1,067 m
    hw = b.controle_de_entrada(5.663, "circular", 1.3716, "circ_concreto_boca_sino_muro", 0.01)
    assert 2.41 * 0.98 <= hw <= 2.44 * 1.02  # HY-8 2,41 m; nomograma 2,44 m
    # controle de saida (n = 0,012, Ke = 0,2) fica abaixo: governa a entrada
    ho = b.controle_de_saida(5.663, "circular", 1.3716, 0.012, 0.2, 60.96, 0.01, 1.067)
    assert ho < hw
    # velocidade de saida pelo controle de saida: nomograma 15,3 ft/s = 4,66 m/s
    v = b.velocidade_de_saida(5.663, "circular", 1.3716, 0.012, 0.01, TW=1.067, controle="saida")
    assert v["V_m_s"] == pytest.approx(4.66, rel=0.02)


# --- HEC-22 p. 80, Exemplo 5.1 ----------------------------------------------------------------
def test_sarjeta_izzard_exemplo_5_1_hec22():
    r = b.sarjeta_triangular_izzard(Sx=0.02, SL=0.01, n=0.016, Q=0.051)
    assert r["saidas"]["T_m"] == pytest.approx(2.76, rel=0.02)
    r = b.sarjeta_triangular_izzard(Sx=0.02, SL=0.01, n=0.016, T=2.5)
    assert r["saidas"]["Q_m3s"] == pytest.approx(0.0395, rel=0.02)
    q = r["saidas"]["Q_m3s"]
    assert b.sarjeta_triangular_izzard(0.02, 0.01, 0.016, Q=q)["saidas"]["T_m"] == pytest.approx(2.5, rel=1e-9)
    with pytest.raises(ValueError):
        b.sarjeta_triangular_izzard(0.02, 0.01, 0.016)
    with pytest.raises(ValueError):
        b.sarjeta_triangular_izzard(0.02, 0.01, 0.016, Q=0.05, T=2.0)


def test_sarjeta_izzard_cli():
    r = subprocess.run([sys.executable, "-m", "tools.dren.bueiros", "--json",
                        json.dumps({"funcao": "sarjeta_triangular_izzard", "Sx": 0.02, "SL": 0.01,
                                    "n": 0.016, "Q": 0.051})],
                       cwd=RAIZ, capture_output=True, text=True, encoding="utf-8",
                       env={**os.environ, "PYTHONIOENCODING": "utf-8"}, stdin=subprocess.DEVNULL)
    assert r.returncode == 0 and json.loads(r.stdout)["saidas"]["T_m"] == pytest.approx(2.76, rel=0.02)


# --- Velocidades admissiveis (DNIT Tab. 31, p. 131) -------------------------------------------
def test_dissipador_usa_tabela31_dnit_por_padrao_e_cita_fonte():
    d = b.dissipador_necessario(1.0, "areia_fina")
    assert d["limite_m_s"] == pytest.approx(0.30) and d["necessario"]
    assert "Tabela 31" in d["metodo"] and "p. 131" in d["metodo"]
    assert b.dissipador_necessario(4.4, "concreto")["necessario"] is False
    assert b.dissipador_necessario(4.6, "concreto")["necessario"] is True  # legado (6,0) aceitaria
    assert b.dissipador_necessario(0.7, "areia_fina", fonte="legado")["necessario"] is False  # limite 0,75
    assert b.dissipador_necessario(0.7, "areia_fina")["necessario"] is True
    assert b.dissipador_necessario(1.0, "argila", criterio="max")["limite_m_s"] == pytest.approx(1.30)
    # chave antiga mapeada; sem equivalente no DNIT cai no legado com aviso
    assert b.dissipador_necessario(1.0, "argila_rija")["limite_m_s"] == pytest.approx(0.80)
    e = b.dissipador_necessario(2.0, "enrocamento")
    assert e["limite_m_s"] == pytest.approx(3.0) and e["avisos"]


def test_tabela31_transcricao_e_legado_preservado():
    assert b.LIMITE_VELOCIDADE_DNIT["concreto"] == (4.50, 4.50)
    assert b.LIMITE_VELOCIDADE_DNIT["revestimento_betuminoso"] == (3.00, 4.00)
    assert b.LIMITE_VELOCIDADE_DNIT["areia_fina"] == (0.30, 0.40)
    assert b.LIMITE_VELOCIDADE_MATERIAL_LEGADO["concreto"] == 6.0
    assert b.LIMITE_VELOCIDADE_MATERIAL is b.LIMITE_VELOCIDADE_MATERIAL_LEGADO
    with pytest.raises(ValueError):
        b.dissipador_necessario(1.0, "rocha_inventada")


# --- Afastamento entre celulas: fontes do corpus -----------------------------------------------
def test_aviso_afastamento_cita_es023_es025():
    cands = [{"forma": "retangular", "dim": (2, 2), "n_celulas": 2, "tipo_de_entrada": "ret_alas_30_75"}]
    r = b.dimensionar_bueiro(Q=6.0, HW_max=5.0, TW=0.0, L=20, S0=0.01, candidatas=cands)
    av = " ".join(a for a in r["avisos"] if "afastamento" in a)
    assert "ES023 p. 4" in av and "ES025 p. 5" in av and "0,30" in av and "0,50" in av
    assert "HEC-14" not in av


# --- Ke de muros de ala paralelos: HDS-5 (0,7) x DNIT Tab. 30 (0,2) ----------------------------
def test_fonte_ke_hds5_padrao_e_dnit():
    assert b.ke_entrada("ret_alas_0") == 0.7
    assert b.ke_entrada("ret_alas_0", "dnit") == 0.2
    assert b.ke_entrada("ret_alas_90_15", "dnit") == b.ke_entrada("ret_alas_90_15", "hds5")
    with pytest.raises(ValueError):
        b.ke_entrada("ret_alas_0", "xyz")
    kw = dict(Q=10.0, HW_max=20.0, TW=1.0, L=60, S0=0.005, forma="retangular",
              tipo_de_entrada="ret_alas_0",
              candidatas=[{"forma": "retangular", "dim": (2, 2), "n_celulas": 1}])
    h = b.dimensionar_bueiro(**kw)["saidas"]["melhor"]["HW_saida_m"]
    d = b.dimensionar_bueiro(fonte_ke="dnit", **kw)["saidas"]["melhor"]["HW_saida_m"]
    V = 10.0 / 4.0
    assert h - d == pytest.approx((0.7 - 0.2) * V * V / (2 * 9.81), rel=1e-6)
    with pytest.raises(ValueError):
        b.dimensionar_bueiro(fonte_ke="xyz", **kw)
    c = b.comparar_legado_hds5(10.0, "retangular", (2, 2), "ret_alas_0", 0.015, 60, 0.005, 1.0)
    cd = b.comparar_legado_hds5(10.0, "retangular", (2, 2), "ret_alas_0", 0.015, 60, 0.005, 1.0, fonte_ke="dnit")
    assert cd["saidas"]["HW_saida_m"] < c["saidas"]["HW_saida_m"]


# --- Vazao critica LEGADO do DNIT (Tabelas 1 e 2, p. 55-56) ----------------------------------
@pytest.mark.parametrize("dim,esp", [((2.0, 2.0), 9.64), ((3.0, 3.0), 26.58)])
def test_legado_dnit_bscc_tabela2(dim, esp):
    # legado: Vc = 2,56 H^0,5 -> Q = 1,705 B H^1,5 (DNIT-DREN p. 56)
    assert b.vazao_critica_legado_dnit("retangular", dim) == pytest.approx(esp, rel=0.005)
    assert b.vazao_critica_exata("retangular", dim) == pytest.approx(esp, rel=0.005)


@pytest.mark.parametrize("D,esp", [(0.6, 0.43), (0.8, 0.88), (1.0, 1.53), (1.2, 2.42), (1.5, 4.22)])
def test_legado_dnit_bstc_tabela1_e_excesso_sobre_exata(D, esp):
    q = b.vazao_critica_legado_dnit("circular", D)
    assert q == pytest.approx(esp, rel=0.02)  # reproduz a Tabela 1 (p. 55)
    ex = b.vazao_critica_exata("circular", D)
    assert 0.06 < q / ex - 1 < 0.09  # ~7 % acima da exata: contra a seguranca
    assert b.vazao_critica_legado_dnit("circular", 1.0, n_celulas=2) == pytest.approx(2 * 1.536)
    r = b.vazao_critica_legado_dnit("circular", 1.0, detalhado=True)
    assert r["avisos"] and r["saidas"]["desvio_relativo"] > 0.06


# --- Constante Y (arco projetante): tabela A.2 (0,57) x exemplo A.3.1 (0,53) -----------------------
def test_arco_projetante_usa_Y_da_tabela_A2_nao_do_exemplo():
    c = b.ENTRADAS["arco_corrugado_projetante"]
    assert c["Y"] == 0.57 and c["c"] == 0.0496 and c["K"] == 0.0340 and c["M"] == 1.5  # HDS-5 p. 198
    Q, S0 = 20.0, 0.01
    A, D = math.pi * 2.0 * 1.5 / 4, 1.5
    X = 1.811 * Q / (A * math.sqrt(D))
    hw = b.controle_de_entrada(Q, "arco", (2.0, 1.5), "arco_corrugado_projetante", S0)
    assert X > 4
    assert hw == pytest.approx((0.0496 * X ** 2 + 0.57 - 0.5 * S0) * D, rel=1e-9)


# ===================== v0.3.0 (F5): V de saida HDS-5, tubo parcialmente cheio, IME =====================
FT, CFS = 0.3048, 0.0283168466


def test_hds5_p280_velocidade_de_saida_caixa_1524():
    """HDS-5 DG 1.4 Step 7 [p. 280 do PDF]: caixa 5x5 ft (1524 mm), Q50 = 300 cfs (8,495 m3/s),
    S = 0,02, TW = 1,219 m; Vo = 20,8 ft/s = 6,47 m/s (nomograma). O texto nao diz o n:
    adotado 0,012 (concreto liso, caixa RCB). Livro: tolerancia 1 % (obtido 6,45 m/s, -0,3 %).
    Sensivel a n: n = 0,013 daria 6,07 m/s (-6 %), ver DIVERGENCIAS."""
    v = b.velocidade_de_saida(8.495, "retangular", (1.524, 1.524), 0.012, 0.02, TW=1.219, controle="entrada")
    assert v["V_m_s"] == pytest.approx(6.47, rel=0.01)
    assert v["Fr"] > 1  # supercritico: lamina normal (yn < dc)
    assert 20.8 * FT == pytest.approx(6.34, rel=0.001)  # 20,8 ft/s impresso (6,34 m/s); 6,47 m/s do SI e o do texto
    # HY-8 do mesmo problema: 19,61 ft/s (nao atinge a profundidade normal no fim do bueiro), abaixo do nomograma
    assert 19.61 * FT < v["V_m_s"]


# --- tubo circular parcialmente cheio: HDS-3 Ex. 10-17 (livro; leitura de grafico) -------------
def test_hds3_ex10_circular_30in():
    r = b.tubo_parcialmente_cheio(25 * CFS, 2.5 * FT, 0.015, 0.005)["saidas"]
    assert r["y_m"] / FT == pytest.approx(2.05, rel=0.01)   # impresso 2,05 ft; recalculo 2,037
    assert r["V_m_s"] / FT == pytest.approx(5.8, rel=0.01)  # impresso 5,8 fps
    dc = b.profundidade_critica(25 * CFS, "circular", 2.5 * FT)
    assert dc / FT == pytest.approx(1.7, rel=0.01)           # impresso 1,7 ft


def test_hds3_ex12_14_capacidade():
    m = b.manning_lamina("circular", 6 * FT, 3.0 * FT, 0.030, 0.003)
    assert m["Q"] / CFS == pytest.approx(50.0, rel=0.01)       # Ex. 12: 50 cfs
    assert m["V"] / FT == pytest.approx(3.5, rel=0.05)         # leitura de grafico (+1,6 %)
    c = b.manning_cheia("circular", 4 * FT, 0.011, 0.005)["Q"] / CFS
    assert c == pytest.approx(120.0, rel=0.01)                 # Ex. 14: Qfull = 120
    q = b.manning_lamina("circular", 4 * FT, 3.0 * FT, 0.011, 0.005)["Q"] / CFS
    assert q == pytest.approx(109.0, rel=0.01)                 # Ex. 14: 109 cfs (Q/Qfull 0,91)


def test_hds3_ex15_16_17():
    r = b.tubo_parcialmente_cheio(315 * CFS, 10 * FT, 0.012, 0.0006)["saidas"]
    assert r["y_sobre_D"] == pytest.approx(0.63, rel=0.01) and r["y_m"] / FT == pytest.approx(6.3, rel=0.01)
    assert r["V_m_s"] / FT == pytest.approx(6.0, rel=0.05)     # impresso 6,0; exato 6,08 (leitura de grafico)
    # Ex. 16: Sf = 0,0058 para Q = 600 cfs, d = 7,5 ft, n = 0,025
    D = 10 * FT
    m = b.manning_lamina("circular", D, 7.5 * FT, 0.025, 1.0)
    assert (600 * CFS / m["Q"]) ** 2 == pytest.approx(0.0058, rel=0.01)
    # Ex. 17: dc = 5,9 ft; Sc = 0,0026; Hc = 8,4 ft (n = 0,012)
    dc = b.profundidade_critica(600 * CFS, "circular", D)
    assert dc / FT == pytest.approx(5.9, rel=0.01)
    mc = b.manning_lamina("circular", D, dc, 0.012, 1.0)
    assert (600 * CFS / mc["Q"]) ** 2 == pytest.approx(0.0026, rel=0.05)   # 0,00266 (grafico, +2,2 %)
    A, _, T = b._secao(b._geo("circular", D), dc)
    assert (dc + (600 * CFS / A) ** 2 / 19.62) / FT == pytest.approx(8.4, rel=0.05)  # 8,30 (grafico, -1,1 %)


# --- Delmiro Gouveia, BUC-2 a BUC-5 (acervo, sem ✓h: tolerancia 5 %) ---------------------------
@pytest.mark.parametrize("Q,D,S,y,V,Fr", [
    (0.499, 0.80, 0.005, 0.454, 1.70, 0.89),   # BUC-2 TR 20 (gabarito proposto: y 0,454, Fr 0,89)
    (1.716, 1.20, 0.005, 0.753, 2.30, 0.91),   # BUC-3 (2 linhas)
    (0.557, 0.80, 0.005, 0.487, 1.74, 0.87),   # BUC-4
    (0.777, 0.80, 0.007, 0.546, 2.12, 0.97),   # BUC-5
    (0.593, 0.80, 0.005, 0.508, 1.76, 0.85),   # BUC-2 TR 50
    (2.039, 1.20, 0.005, 0.853, 2.37, 0.85),   # BUC-3 TR 50
    (0.662, 0.80, 0.005, 0.550, 1.80, 0.81),   # BUC-4 TR 50
    (0.923, 0.80, 0.007, 0.630, 2.17, 0.86),   # BUC-5 TR 50 (y/D = 79 %)
])
def test_delmiro_tubo_parcialmente_cheio(Q, D, S, y, V, Fr):
    r = b.tubo_parcialmente_cheio(Q, D, 0.015, S)["saidas"]
    assert r["y_m"] == pytest.approx(y, rel=0.05)
    assert r["V_m_s"] == pytest.approx(V, rel=0.05)
    assert r["Fr"] == pytest.approx(Fr, rel=0.05)


def test_tubo_parcialmente_cheio_froude_com_profundidade_hidraulica_e_avisos():
    r = b.tubo_parcialmente_cheio(0.499, 0.80, 0.015, 0.005)
    s = r["saidas"]
    assert s["A_m2"] == pytest.approx(0.294, rel=0.005)
    assert s["Fr"] == pytest.approx(s["V_m_s"] / math.sqrt(9.81 * 0.294 / 0.79), rel=0.01)  # A/T, T = 0,79
    assert s["Fr"] != pytest.approx(s["V_m_s"] / math.sqrt(9.81 * s["y_m"]), rel=0.02)  # nao e Fr com y
    assert s["regime"] == "subcritico" and r["avisos"] == []
    # TR 50 de BUC-5: y/D = 79 % > 75 % (padrao provisorio) gera aviso; limite como argumento
    a = b.tubo_parcialmente_cheio(0.923, 0.80, 0.015, 0.007)
    assert any("padrao provisorio" in x for x in a["avisos"])
    assert not any("padrao provisorio" in x for x in
                   b.tubo_parcialmente_cheio(0.923, 0.80, 0.015, 0.007, limite_y_sobre_D=0.85)["avisos"])
    # Q acima da capacidade plena: aviso e y = D; entrada invalida: erro
    c = b.tubo_parcialmente_cheio(2.0, 0.80, 0.015, 0.005)
    assert c["saidas"]["y_sobre_D"] == 1.0 and any("cheio" in x for x in c["avisos"])
    with pytest.raises(ValueError):
        b.tubo_parcialmente_cheio(0.5, 0.8, 0.0, 0.005)
    # supercritico em declividade forte
    assert b.tubo_parcialmente_cheio(0.5, 0.8, 0.015, 0.05)["saidas"]["regime"] == "supercritico"


def test_tubo_parcialmente_cheio_cli():
    r = subprocess.run([sys.executable, "-m", "tools.dren.bueiros", "--json", json.dumps(
        {"funcao": "tubo_parcialmente_cheio", "Q": 0.499, "D": 0.8, "n": 0.015, "S0": 0.005})],
        cwd=RAIZ, capture_output=True, text=True, encoding="utf-8",
        env={**os.environ, "PYTHONIOENCODING": "utf-8"}, stdin=subprocess.DEVNULL)
    assert r.returncode == 0 and json.loads(r.stdout)["saidas"]["y_m"] == pytest.approx(0.454, rel=0.01)


# --- IME p. 151-152: regime critico do tubular (A_c = 0,601 D2) --------------------------------
def test_ime_regime_critico_tubular():
    r = b.regime_critico_tubular_ime(1.0, 0.015)["saidas"]
    th = r["theta_c_rad"]
    assert th == pytest.approx(math.radians(231 + 6 / 60 + 9 / 3600), rel=1e-4)   # 231 graus 06' 09"
    A, _, T = b._secao(b._geo("circular", 1.0), r["dc_m"])
    assert 1.5 * A / T == pytest.approx(1.0, rel=1e-3)           # Ec = (3/2) A/T = D
    assert r["dc_m"] == pytest.approx(0.716, rel=0.002)          # dc = 0,716 D (impresso)
    assert r["A_c_sobre_D2"] == pytest.approx(0.601, rel=0.002)  # A_c = 0,601 D2 (recalculo; mapa G1 12)
    assert r["Vc_m_s"] == pytest.approx(2.56, rel=0.002)         # Vc = 2,56 D^0,5 (impresso)
    assert r["Qc_m3s"] == pytest.approx(1.533, rel=0.005)        # Qc = 1,533 D^2,5 (impresso; 1,538 recalc.)
    assert r["Ic"] == pytest.approx(32.82 * 0.015 ** 2, rel=0.001)  # Ic = 32,82 n2 / D^(1/3)
    r2 = b.regime_critico_tubular_ime(2.0, 0.013)["saidas"]
    assert r2["Qc_m3s"] == pytest.approx(r["Qc_m3s"] * 2 ** 2.5, rel=1e-9)
    assert r2["Ic"] == pytest.approx(32.82 * 0.013 ** 2 / 2 ** (1 / 3), rel=0.001)
    # o 0,60 D2 do legado DNIT e o arredondamento do 0,601 do IME (0,2 %)
    assert b.A_CRIT_TUBO_SOBRE_D2 == pytest.approx(r["A_c_sobre_D2"], rel=0.003)
    # celular: Qc = 1,705 B H^1,5 (IME p. 152) = legado DNIT
    assert b.vazao_critica_legado_dnit("retangular", (1.0, 1.0)) == pytest.approx(1.705, rel=0.001)
    with pytest.raises(ValueError):
        b.regime_critico_tubular_ime(0.0)


# --- Xingo legado: 33,5 D^2,67 i^0,5 equivale a n = 0,0093 (caso negativo, mapa G2 pendencias) ---
def test_xingo_legado_equivale_a_n_0093_abaixo_do_n_de_projeto():
    D, i = 1.2, 0.01
    q_legado = 33.5 * D ** 2.67 * i ** 0.5
    n_eq = 0.3117 / 33.5   # Q plena = (pi/4 (1/4)^(2/3)/n) D^(8/3) i^0,5 = (0,3117/n) D^(8/3) i^0,5
    assert n_eq == pytest.approx(0.0093, rel=0.01)
    assert b.manning_cheia("circular", D, n_eq, i)["Q"] == pytest.approx(q_legado, rel=0.005)
    # com n de projeto da ABTC (0,012 drenagem; 0,013 esgoto) a capacidade cai ~22 a 28 %: o legado superestima
    for n_proj in (0.012, 0.013):
        queda = b.manning_cheia("circular", D, n_proj, i)["Q"] / q_legado - 1
        assert -0.30 < queda < -0.20
