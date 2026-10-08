"""Testes de tools.dren.tubos (selecao indicativa de classe de tubo de concreto, NBR 8890).

Tolerancias: livro 1 %; acervo 5 %; formulas fechadas 1e-9. Fontes: ABTC (TUBOS = Projeto
estrutural de tubos, ESPEC = como especificar), USACE EM 1110-2-2902 (EM). Nao ha exemplo
numerico de Cap/aterro no TUBOS: essas funcoes sao testadas por consistencia (limites e continuidade).
"""
import json
import math
import os
import pathlib
import subprocess
import sys

import pytest

from tools.dren import tubos as t

RAIZ = str(pathlib.Path(__file__).resolve().parents[2])


def test_versao_010():
    assert t.VERSAO == "0.1.0"


# ============================ EM 1110-2-2902 (livro, 1 %) =====================
def test_em2902_vala_cd_e_we1():
    """EM Ap. B p. 66-68: k_mu' 0,15, H 2,44 m, Bd 1,52 m, g 18 850 N/m3 -> Cd 1,274; We1 55 483 N/m."""
    r = t.carga_solo_vala(2.44, 1.52, gamma=18.85, k_mu=0.15)
    assert r["Cv"] == pytest.approx(1.274, rel=0.001)
    assert r["q_kN_m"] == pytest.approx(55.483, rel=0.001)
    # We2 = g Bc H com Bc = 1,22 m = 56 113 N/m (p. 68, prisma sem atrito de parede)
    assert 18.85 * 1.22 * 2.44 == pytest.approx(56.113, rel=0.001)


def test_em2902_fator_de_berco_aterro_e_d_load():
    """EM p. 71-72: chi 0,811 (rho 0,7, berco de concreto), eta 0,505, theta = 1/3 -> Bf 6,098;
    D0,01 = Hf W_T/(Si Bf) = 57 N/m/mm com W_T = W_L 145 940 + W_E 175 130 N/m, Si 1200 mm.
    (O mapa G2 duvidava do exemplo por usar so W_E; com W_T = W_L + W_E o D0,01 de 57 fecha.)"""
    r = t.fator_berco_aterro("A", 0.7, hs=3.0, de=1.4, k=0.33, Cap=2.0, theta_fixo=1 / 3)
    assert r["chi"] == pytest.approx(0.811) and r["eta"] == pytest.approx(0.505)
    assert r["alfa_eq"] == pytest.approx(6.098, rel=0.001)
    d = t.d_load_em2902(145940 + 175130, 1200, 6.098)
    assert d == pytest.approx(57.0, rel=0.01)
    assert t.d_load_em2902(145940 + 175130, 1200, 6.098) < 65  # classe III (65) atende
    # se fosse so W_E (leitura do mapa), D0,01 = 31 e o exemplo nao fecharia
    assert t.d_load_em2902(175130, 1200, 6.098) == pytest.approx(31.1, rel=0.01)


def test_tabelas_em_e_abtc_coincidem_onde_ha_correspondencia():
    # EM Tab. 3-1 (1,5 / 1,9 / 2,5) x TUBOS Tab. 4.1: C e B iguais; A do EM dentro da faixa 2,25-3,4
    assert t.fator_berco_vala("C", fonte="em2902")["alfa_eq"] == t.fator_berco_vala("C")["alfa_eq"] == 1.5
    assert t.fator_berco_vala("B", fonte="em2902")["alfa_eq"] == t.fator_berco_vala("B")["alfa_eq"] == 1.9
    lo, hi = t.FATOR_BERCO_VALA["A"]
    assert lo <= t.fator_berco_vala("A", fonte="em2902")["alfa_eq"] <= hi
    with pytest.raises(ValueError):
        t.fator_berco_vala("D", fonte="em2902")  # inadmissivel no EM
    # eta (Tab. 4.2) e chi (Tab. 4.3) = EM Tab. 3-2
    assert t.ETA_BASE == {"A": 0.505, "B": 0.707, "C": 0.840, "D": 1.310}
    assert [c[1] for c in t.CHI_TAB_4_3] == [0.150, 0.743, 0.856, 0.811, 0.678, 0.638]
    assert [c[2] for c in t.CHI_TAB_4_3] == [0.0, 0.217, 0.423, 0.594, 0.655, 0.638]
    assert t.chi_aterro(0.4, "A") == pytest.approx((0.743 + 0.856) / 2)  # interpolacao linear


# ============================ ABTC ESPEC p. 6 (selecao exata) =================
@pytest.mark.parametrize("DN,F,tipo,classe", [
    (1200, 65, "pluvial", "PA2"),   # Ex. 1: PA2 = 72 >= 65
    (800, 85, "esgoto", "EA4"),     # Ex. 2: EA4 = 96 >= 85 (EA3 = 72 < 85)
    (400, 37, "pluvial", "PA4"),    # Ex. 3: PA4 = 48 >= 37 (PA3 = 36 < 37)
])
def test_espec_exemplos_de_classe(DN, F, tipo, classe):
    r = t.classe_de_tubo(DN, F, tipo)
    assert r["classe"] == classe
    assert r["F_fissura_classe_kN_m"] >= F


def test_classe_de_tubo_limites_e_avisos():
    assert t.classe_de_tubo(400, 36, "pluvial")["classe"] == "PA3"      # igualdade atende
    assert t.classe_de_tubo(1000, 10, "pluvial")["classe"] == "PA1"
    r = t.classe_de_tubo(300, 40, "pluvial")                            # acima de PA4 (36)
    assert r["classe"] is None and any("NBR 15396" in a for a in r["avisos"])
    assert any("armado" in a for a in t.classe_de_tubo(1200, 65)["avisos"])  # DN > 600
    assert any("ponta e bolsa" in a for a in t.classe_de_tubo(400, 37)["avisos"])  # DN < 500
    with pytest.raises(ValueError):
        t.classe_de_tubo(1300, 50)   # DN 1300 nao consta da Tab. 2
    with pytest.raises(ValueError):
        t.classe_de_tubo(800, 50, "misto")
    with pytest.raises(ValueError):
        t.classe_de_tubo(800, 0)


def test_tabela_de_classes_consistente():
    for dn, cl in t.FORCAS_PLUVIAL.items():
        fis = [cl[c][0] for c in t.CLASSES["pluvial"]]
        assert fis == sorted(fis) and fis[1] == 1.5 * fis[0] and fis[3] == 3 * fis[0]  # PA1:PA2:PA3:PA4 = 1:1,5:2,25:3
        for c, (f, r) in cl.items():
            assert r == pytest.approx(1.5 * f, abs=1.0)   # ruptura = 1,5 x fissura (arredondada)
    # Qd (forca por unidade de DN): DN 1200 PA2 = 60 kN/m/m x 1,2 m = 72 kN/m
    assert t.FORCAS_PLUVIAL[1200]["PA2"][0] == pytest.approx(60 * 1.2)
    # esgoto EA2-EA4 = PA2-PA4
    for dn in t.FORCAS_ESGOTO:
        assert t.FORCAS_ESGOTO[dn]["EA2"] == t.FORCAS_PLUVIAL[dn]["PA2"]
        assert t.FORCAS_ESGOTO[dn]["EA4"] == t.FORCAS_PLUVIAL[dn]["PA4"]


# ============================ Marston (consistencia) =========================
def test_vala_limites_e_alfa_linha_do_tabela_1_1():
    # alfa' = 2 k_mu' = 0,22 a 0,384 (Fig. 2.2 do TUBOS traz as curvas 0,22 / 0,26 / 0,30 / 0,33 / 0,38)
    assert sorted(round(2 * k, 2) for k, _ in t.SOLOS_TAB_1_1.values()) == [0.22, 0.26, 0.3, 0.33, 0.38]
    r = t.carga_solo_vala(1.0, 0.8, tipo_solo=2)
    a = 2 * 0.165
    assert r["Cv"] == pytest.approx((1 - math.exp(-a * 1.25)) / a, rel=1e-12)
    assert r["q_kN_m"] == pytest.approx(r["Cv"] * 17.6 * 0.64, rel=1e-12)
    # Cv < lambda (atrito alivia o prisma) e Cv -> 1/alfa' para hs/bv grande
    assert r["Cv"] < 1.25
    assert t.carga_solo_vala(50.0, 0.8, tipo_solo=2)["Cv"] == pytest.approx(1 / a, rel=1e-6)
    # q cresce com a largura da vala (TUBOS p. 18)
    assert t.carga_solo_vala(2.0, 1.2, tipo_solo=2)["q_kN_m"] > t.carga_solo_vala(2.0, 0.9, tipo_solo=2)["q_kN_m"]
    with pytest.raises(ValueError):
        t.carga_solo_vala(1.0, 0.8)
    with pytest.raises(ValueError):
        t.carga_solo_vala(0.0, 0.8, tipo_solo=2)
    with pytest.raises(ValueError):
        t.carga_solo_vala(1.0, 0.8, tipo_solo=9)
    assert any("0,6" in a for a in t.carga_solo_vala(0.4, 0.8, tipo_solo=2)["avisos"])


def test_aterro_positiva_casos_limite():
    de = 1.4
    # r_ap = 0: carga = peso do prisma (Cap = hs/de; plano de igual recalque no topo do tubo)
    r0 = t.carga_solo_aterro_positiva(3.0, de, 0.7, 0.0, gamma=18.0, k_mu=0.165)
    assert r0["Cap"] == pytest.approx(3.0 / de, rel=1e-9)
    assert r0["q_kN_m"] == pytest.approx(18.0 * 3.0 * de, rel=1e-9)
    # r_ap > 0: carga maior que o peso do prisma; cresce com r_ap e com rho
    r5 = t.carga_solo_aterro_positiva(3.0, de, 0.7, 0.5, gamma=18.0, k_mu=0.165)
    r10 = t.carga_solo_aterro_positiva(3.0, de, 0.7, 1.0, gamma=18.0, k_mu=0.165)
    assert r0["q_kN_m"] < r5["q_kN_m"] < r10["q_kN_m"]
    assert t.carga_solo_aterro_positiva(3.0, de, 0.3, 0.5, gamma=18.0, k_mu=0.165)["q_kN_m"] < r5["q_kN_m"]
    # equacao do plano de igual recalque (2.6) satisfeita
    a, le = r5["alfa"], r5["lambda_e"]
    assert math.exp(a * le) == pytest.approx(a * le + a * 0.7 * 0.5 + 1, rel=1e-9)


def test_aterro_positiva_continuidade_em_hs_igual_he():
    de, rho, r = 1.4, 0.7, 0.8
    he = t.carga_solo_aterro_positiva(10.0, de, rho, r, gamma=18.0, k_mu=0.165)["he_m"]
    abaixo = t.carga_solo_aterro_positiva(he * 0.99999, de, rho, r, gamma=18.0, k_mu=0.165)["Cap"]
    acima = t.carga_solo_aterro_positiva(he * 1.00001, de, rho, r, gamma=18.0, k_mu=0.165)["Cap"]
    assert abaixo == pytest.approx(acima, rel=1e-4)
    # hs << he: Cap = (e^(a lam)-1)/a (eq. 2.4); hs >> he: crescimento linear de inclinacao e^(a lam_e)
    r1 = t.carga_solo_aterro_positiva(0.2 * he, de, rho, r, gamma=18.0, k_mu=0.165)
    a = r1["alfa"]
    assert r1["Cap"] == pytest.approx((math.exp(a * 0.2 * he / de) - 1) / a, rel=1e-9)
    c2 = t.carga_solo_aterro_positiva(20.0, de, rho, r, gamma=18.0, k_mu=0.165)
    c3 = t.carga_solo_aterro_positiva(21.4, de, rho, r, gamma=18.0, k_mu=0.165)
    assert (c3["Cap"] - c2["Cap"]) / (1.4 / de) == pytest.approx(math.exp(a * c2["lambda_e"]), rel=1e-9)
    with pytest.raises(ValueError):
        t.carga_solo_aterro_positiva(3.0, de, 1.2, 0.5, tipo_solo=2)
    with pytest.raises(ValueError):
        t.carga_solo_aterro_positiva(3.0, de, 0.5, -0.3, tipo_solo=2)


# ============================ fator de berco / sobrecarga / forca ============
def test_fator_berco_vala_classes_e_avisos():
    assert t.fator_berco_vala("C")["alfa_eq"] == 1.5
    assert t.fator_berco_vala("b")["alfa_eq"] == 1.9
    a = t.fator_berco_vala("A")
    assert a["alfa_eq"] == 2.25 and any("padrao provisorio" in x for x in a["avisos"])
    assert t.fator_berco_vala("A", alfa_A=3.0)["alfa_eq"] == 3.0
    assert any("condenavel" in x for x in t.fator_berco_vala("D")["avisos"])
    with pytest.raises(ValueError):
        t.fator_berco_vala("A", alfa_A=4.0)
    with pytest.raises(ValueError):
        t.fator_berco_vala("X")


def test_fator_berco_aterro_abtc_formula_fechada():
    # classe C, rho 0,5: chi 0,423; theta = (rho k/Cap)(hs/de + rho/2) limitado a 0,33
    hs, de, k, cap = 3.0, 1.4, 0.33, 2.2
    theta = 0.5 * k / cap * (hs / de + 0.25)
    r = t.fator_berco_aterro("C", 0.5, hs, de, k, cap)
    assert r["theta"] == pytest.approx(min(theta, 0.33), rel=1e-12)
    assert r["alfa_eq"] == pytest.approx(1.431 / (0.840 - r["theta"] * 0.423), rel=1e-12)
    # theta saturado em 0,33
    assert t.fator_berco_aterro("C", 0.5, 30.0, de, k, 1.0)["theta"] == pytest.approx(0.33)
    # berco melhor => maior fator (A > B > C > D) para o mesmo rho
    f = [t.fator_berco_aterro(c, 0.5, hs, de, k, cap)["alfa_eq"] for c in "ABCD"]
    assert f[0] > f[1] > f[2] > f[3]
    assert any("0,7" in a for a in t.fator_berco_aterro("B", 0.9, hs, de, k, cap)["avisos"])
    with pytest.raises(ValueError):
        t.fator_berco_aterro("E", 0.5, hs, de, k, cap)


def test_impacto_sobrecarga_e_forca():
    assert [t.coef_impacto(h) for h in (0.2, 0.3, 0.5, 0.6, 0.8, 0.9, 1.5)] == [1.3, 1.3, 1.2, 1.2, 1.1, 1.1, 1.0]
    assert t.sobrecarga_multidao(1.4) == pytest.approx(5.0 * 1.4)
    assert t.forca_de_ensaio(60, 20, 1.5, 1.0) == pytest.approx(80 / 1.5)
    assert t.forca_de_ensaio(60, 20, 1.5, 1.5) == pytest.approx(1.5 * 80 / 1.5)
    with pytest.raises(ValueError):
        t.forca_de_ensaio(60, 20, 0.0)
    with pytest.raises(ValueError):
        t.coef_impacto(0)


# ============================ selecao completa ===============================
def test_selecionar_tubo_vala_e_monotonicidade():
    kw = dict(DN_mm=1000, hs=2.0, instalacao="vala", bv=1.8, tipo_solo=2, sobrecarga_kN_m=30.0)
    r = t.selecionar_tubo(base="C", **kw)
    # conferencia a mao: Cv gamma bv^2 + phi qm, / 1,5
    de = 1.0 + 2 * 0.080
    a = 2 * 0.165
    q = (1 - math.exp(-a * 2.0 / 1.8)) / a * 17.6 * 1.8 ** 2
    assert r["de_m"] == pytest.approx(de)
    assert r["q_solo_kN_m"] == pytest.approx(q, rel=1e-9)
    assert r["qm_kN_m"] == pytest.approx(30.0 * 1.0)   # hs 2,0 m: phi = 1,0
    assert r["F_fissura_kN_m"] == pytest.approx((q + 30.0) / 1.5, rel=1e-9)
    assert r["F_ruptura_kN_m"] == pytest.approx(1.5 * r["F_fissura_kN_m"], rel=1e-9)
    assert r["F_fissura_classe_kN_m"] >= r["F_fissura_kN_m"]
    assert any("indicativo" in x for x in r["avisos"]) and any("armado" in x for x in r["avisos"])
    # berco melhor nunca piora a classe
    ordem = {c: i for i, c in enumerate(("PA1", "PA2", "PA3", "PA4"))}
    cls = [t.selecionar_tubo(base=b, **kw)["classe"] for b in ("D", "C", "B", "A")]
    assert all(ordem[x] >= ordem[y] for x, y in zip(cls, cls[1:]))
    # mais cobrimento sobre a mesma vala aumenta F
    f2 = t.selecionar_tubo(base="C", **dict(kw, hs=4.0))["F_fissura_kN_m"]
    assert f2 > r["F_fissura_kN_m"]


def test_selecionar_tubo_aterro_impacto_e_avisos():
    r = t.selecionar_tubo(DN_mm=800, hs=0.5, instalacao="aterro", base="B", rho=0.5, r_ap=0.5,
                          sobrecarga_kN_m=40.0, de_m=1.0)
    assert r["phi_impacto"] == 1.2 and r["qm_kN_m"] == pytest.approx(48.0)
    assert any("0,6" in x for x in r["avisos"])   # hs < 0,6 m
    sem = t.selecionar_tubo(DN_mm=800, hs=2.0, instalacao="aterro", base="C", rho=0.5, de_m=1.0)
    assert any("sobrecarga nao informada" in x for x in sem["avisos"])
    com = t.selecionar_tubo(DN_mm=800, hs=2.0, instalacao="aterro", base="C", rho=0.5, de_m=1.0,
                            sobrecarga_kN_m=40.0, aplicar_impacto=False)
    assert com["qm_kN_m"] == 40.0 and com["F_fissura_kN_m"] > sem["F_fissura_kN_m"]
    with pytest.raises(ValueError):
        t.selecionar_tubo(DN_mm=800, hs=2.0, instalacao="vala", base="C")        # falta bv
    with pytest.raises(ValueError):
        t.selecionar_tubo(DN_mm=800, hs=2.0, instalacao="aterro", base="C")      # falta rho
    with pytest.raises(ValueError):
        t.selecionar_tubo(DN_mm=800, hs=2.0, instalacao="cravacao", base="C")
    # carga extrema: sem classe e aviso de aduela
    ext = t.selecionar_tubo(DN_mm=400, hs=12.0, instalacao="aterro", base="D", rho=1.0, r_ap=1.0, de_m=0.5)
    assert ext["classe"] is None and any("NBR 15396" in x for x in ext["avisos"])


# ============================ CLI ============================================
def _cli(d):
    r = subprocess.run([sys.executable, "-m", "tools.dren.tubos", "--json", json.dumps(d)], cwd=RAIZ,
                       capture_output=True, text=True, encoding="utf-8",
                       env={**os.environ, "PYTHONIOENCODING": "utf-8"}, stdin=subprocess.DEVNULL)
    return r.returncode, json.loads(r.stdout)


def test_cli_classe_e_selecao():
    rc, d = _cli({"funcao": "classe_de_tubo", "DN_mm": 1200, "F_kN_m": 65})
    assert rc == 0 and d["saidas"]["classe"] == "PA2" and d["versao"] == "0.1.0" and "avisos" in d and "metodo" in d
    rc, d = _cli({"funcao": "selecionar_tubo", "DN_mm": 1000, "hs": 2.0, "instalacao": "vala", "base": "C",
                  "bv": 1.8, "sobrecarga_kN_m": 30.0})
    assert rc == 0 and d["saidas"]["classe"] in ("PA1", "PA2", "PA3", "PA4")
    rc, d = _cli({"funcao": "classe_de_tubo", "DN_mm": 1300, "F_kN_m": 65})
    assert rc == 2 and "erro" in d
