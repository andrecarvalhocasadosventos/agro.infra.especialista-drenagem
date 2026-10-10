"""Testes de tools.dren.hidrologia.

Tolerancias: casos reais = 5 % (D11) salvo indicacao do gabarito do caso;
formulas fechadas = 1e-6 relativo.
"""
import json
import math
import os
import pathlib
import subprocess
import sys

import pytest

from tools.dren import hidrologia as h

RAIZ = str(pathlib.Path(__file__).resolve().parents[2])


# ---------------------------------------------------------------- (a) livro
def test_idf_potencial_csb_grupo1():
    # K=5590,88 a=0,241 b=40,11 c=1,091 (doc 1341:36); t=114,09 min TR=100
    i = h.idf_potencial(100, 114.09, 5590.88, 0.241, 40.11, 1.091)
    assert i == pytest.approx(69.54, rel=0.01)


def test_idf_potencial_aviso_faixa():
    r = h.idf_potencial(500, 5, 5590.88, 0.241, 40.11, 1.091,
                        faixa_TR=(2, 100), faixa_t=(10, 1440), detalhado=True)
    assert len(r["avisos"]) == 2
    assert set(r) == {"entradas", "saidas", "metodo", "avisos", "versao"}


def test_idf_tabela_interpola_log_e_avisa():
    pts = [(10, 100.0), (100, 10.0)]  # i = 1000/t exato em log-log
    assert h.idf_tabela(pts, 31.6227766) == pytest.approx(31.6227766, rel=1e-6)
    r = h.idf_tabela(pts, 500, detalhado=True)
    assert r["avisos"]


def test_idf_tabela_dois_TR():
    pts = {10: [(10, 100.0), (100, 10.0)], 100: [(10, 200.0), (100, 20.0)]}
    assert h.idf_tabela(pts, 10, TR=31.6227766) == pytest.approx(141.42136, rel=1e-5)


def test_kirpich_bacia_tipica():
    # L=1000 m, S=0,05: 0,0195*1000^0,77*0,05^-0,385 = 0,0195*204,17*3,168 = 12,6 min
    assert h.kirpich(1000, 0.05) == pytest.approx(12.61, rel=0.01)
    r = h.kirpich(1000, 0.05, detalhado=True)
    assert r["saidas"]["tc_min"] == pytest.approx(12.61, rel=0.01)


def test_kirpich_aviso_fora_de_faixa():
    r = h.kirpich(5000, 0.002, detalhado=True)
    assert any("3-10" in a for a in r["avisos"])


def test_california_culverts_e_giandotti_kerby_dooge():
    assert h.california_culverts(1.0, 10.0) == pytest.approx(57 * 0.1 ** 0.385, rel=1e-9)
    assert h.giandotti(100, 20, 300) == pytest.approx((40 + 30) / (0.8 * math.sqrt(300)), rel=1e-9)
    assert h.kerby(100, 0.4, 0.01) == pytest.approx(1.44 * (400) ** 0.467, rel=1e-9)
    assert h.dooge(10, 0.01) > 0
    assert h.dnos(3.234, 3.0, 0.2, 4.0) > 0


def test_racional_unidades():
    q_km2 = h.racional(0.3, 60, 1.0, "km2")
    q_ha = h.racional(0.3, 60, 100, "ha")
    assert q_km2 == pytest.approx(5.0, rel=1e-9)  # 0,3*60*1/3,6
    assert q_ha == pytest.approx(q_km2, rel=1e-9)


def test_racional_aviso_acima_de_2km2():
    r = h.racional(0.3, 60, 3.0, "km2", detalhado=True)
    assert r["avisos"]
    assert not h.racional(0.3, 60, 1.0, detalhado=True)["avisos"]
    # criterios do acervo: 350 ha (CSB) aceita sem aviso se limite = 3,5
    r2 = h.racional(0.25, 70, 211, "ha", limite_km2=h.LIMITES_RACIONAL_ACERVO_KM2["csb_geohidro_2016"],
                    detalhado=True)
    assert not r2["avisos"]


def test_mcmath_faixa():
    assert h.mcmath(0.3, 60, 100, 0.01, detalhado=True)["avisos"] == []
    assert h.mcmath(0.3, 60, 10, 0.01, detalhado=True)["avisos"]
    assert h.mcmath(0.3, 60, 100, 0.01) == pytest.approx(0.0091 * 0.3 * 60 * 100 ** 0.8 * 0.01 ** 0.2)


def test_scs_chuva_efetiva_neh():
    # CN=80 -> S=63,5 mm; P=100 -> Ia=12,7; Q=(87,3)^2/(87,3+63,5)=50,55 mm
    assert h.retencao_S(80) == pytest.approx(63.5, rel=1e-9)
    assert h.chuva_efetiva(100, 80) == pytest.approx(50.55, rel=1e-3)
    assert h.chuva_efetiva(10, 80) == 0.0
    # v0.2: sem conversao do CN so com ajustar_cn=False (comportamento legado)
    assert h.chuva_efetiva(100, 80, lam=0.05, ajustar_cn=False) > h.chuva_efetiva(100, 80, lam=0.2)


def test_hu_triangular_geometria():
    hu = h.hidrograma_unitario_triangular(10.0, 2.0, 0.5)
    assert hu["tlag_h"] == pytest.approx(1.2)
    assert hu["tp_h"] == pytest.approx(1.45)
    assert hu["tb_h"] == pytest.approx(2.67 * 1.45)
    assert hu["qp_m3s_por_mm"] == pytest.approx(0.208 * 10 / 1.45)


def test_convolucao_conserva_volume():
    hu = h.hidrograma_unitario_triangular(10.0, 2.0, 0.25)
    pe = [2.0, 5.0, 3.0, 1.0]
    r = h.convolucao_hu(pe, hu)
    dt3600 = hu["D_h"] * 3600
    vol_mm = sum(r["Q_m3s"]) * dt3600 / (10.0e6) * 1000.0
    assert vol_mm == pytest.approx(sum(pe), rel=0.08)  # amostragem pontual do HU
    assert r["Qp_m3s"] > 0


def test_hietograma_para_efetiva_soma_igual_total():
    p = [10, 20, 30, 10]
    pe = h.hietograma_para_efetiva(p, 75)
    assert sum(pe) == pytest.approx(h.chuva_efetiva(70, 75))


def test_gumbel_momentos_e_aviso():
    # serie sintetica com media 50 e desvio conhecido
    serie = [40, 45, 50, 55, 60] * 4  # n=20
    mu, beta = h.gumbel_parametros(serie)
    s = math.sqrt(sum((x - 50) ** 2 for x in serie) / 19)
    assert beta == pytest.approx(s * math.sqrt(6) / math.pi)
    assert mu == pytest.approx(50 - 0.5772156649 * beta)
    assert h.gumbel_P_TR(serie, 100) > h.gumbel_P_TR(serie, 10) > h.gumbel_P_TR(serie, 2)
    # v0.2: sem n o aviso de amostra infinita sempre aparece; com n=len(serie) nao ha aviso (n=20)
    assert not h.gumbel_P_TR(serie, 10, detalhado=True, n=len(serie))["avisos"]
    assert any("sem n" in x for x in h.gumbel_P_TR(serie, 10, detalhado=True)["avisos"])
    assert any("< 20" in a for a in h.gumbel_P_TR(serie[:10], 10, detalhado=True)["avisos"])


def test_cli_json():
    cmd = [sys.executable, "-m", "tools.dren.hidrologia", "--json",
           json.dumps({"funcao": "racional", "args": {"C": 0.3, "i": 60, "A": 3.0}})]
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    out = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", env=env,
                         cwd=RAIZ, stdin=subprocess.DEVNULL).stdout
    d = json.loads(out)
    assert d["saidas"]["Q_m3s"] == pytest.approx(15.0)
    assert d["avisos"] and d["versao"]


# ------------------------------------------------- (b) gabaritos dos casos
def test_csb_gumbel_iuiu_pdia():
    # Iuiu 1051:318,320: P = 65,02 - (1/0,051763) ln ln(TR/(TR-1)); tol 1 %
    mu, beta = 65.02, 1 / 0.051763
    ref = {5: 94.00, 10: 108.49, 25: 126.81, 50: 140.40, 100: 153.89}
    for tr, p in ref.items():
        assert h.gumbel_quantil(mu, beta, tr) == pytest.approx(p, rel=0.005)


def test_csb_bacia45_racional():
    # doc 1341:145: A=211 ha, L=2,9 km, H=12 m, grupo 1, TR=100; Q=9,58 (tol 3 %)
    tc = h.kirpich_modificada_dnit(2.9, 12.0)
    assert tc == pytest.approx(114.09, rel=0.03)
    i = h.idf_potencial(100, tc, 5590.88, 0.241, 40.11, 1.091)
    assert i == pytest.approx(69.54, rel=0.03)
    C = h.coef_c_para_tr(0.20, 100)
    Cd = h.coef_distribuicao(2.11)
    assert C == pytest.approx(0.2536, rel=0.01)
    assert Cd == pytest.approx(0.93, rel=0.01)
    Q = h.racional(C * Cd, i, 211, "ha", limite_km2=3.5)
    assert Q == pytest.approx(9.58, rel=0.03)


def test_iuiu_dp08_racional():
    # doc 1051:318,322: A=20 ha, L=0,61 km, H=3,97 m (suposicao do caso), TR=10, C=0,3 -> 0,83
    tc = h.kirpich(610, 3.97 / 610)
    assert tc == pytest.approx(18.9, rel=0.03)
    p = 108.49
    i = 2.31 * p * tc ** -0.55
    assert i == pytest.approx(49.8, rel=0.03)
    assert h.racional(0.3, i, 20, "ha") == pytest.approx(0.83, rel=0.03)


@pytest.mark.xfail(reason="DP11 t1 (1051:322): S e Tc da bacia nao informados; hipotese S=i do dreno, "
                          "Tc Kirpich e i=P/Tc; divergencia > 5 % (ver DIVERGENCIAS.md)",
                   strict=True)
def test_iuiu_dp11_mcmath():
    A, L, S = 189.0, 4670.0, 0.0028
    tc = h.kirpich(L, S)
    i = 108.49 / (tc / 60.0)
    assert h.mcmath(0.3, i, A, S) == pytest.approx(2.34, rel=0.05)


def test_iuiu_criterio_media():
    assert h.vazao_adotada_iuiu(189, 1.0, 2.34, 3.87) == pytest.approx(3.1, rel=0.01)
    assert h.vazao_adotada_iuiu(20, 0.83) == 0.83


def test_xingo_kirpich_s1():
    # doc 1419:28: L=35,67 km, S=0,36 % -> Kirpich 8,91 h (tol 3 %)
    tc_h = h.kirpich(35670, 0.0036) / 60.0
    assert tc_h == pytest.approx(8.91, rel=0.03)


def test_baixio_hu_geometria_e_qp():
    # doc 902:1: A=323,4 ha, CN=62,04, Tc=0,9633 h, d=0,16055 h
    assert h.retencao_S(62.04) == pytest.approx(155.39, rel=0.001)
    hu = h.hidrograma_unitario_triangular(3.234, 0.9633, 0.16055)
    assert hu["tlag_h"] == pytest.approx(0.578, rel=0.01)
    assert hu["tp_h"] == pytest.approx(0.658, rel=0.01)
    assert hu["tb_h"] == pytest.approx(1.758, rel=0.01)
    assert 10 * hu["qp_m3s_por_mm"] == pytest.approx(10.22, rel=0.01)


@pytest.mark.xfail(reason="Baixio 902:1: hietograma (tabela T-K, ordenamento) nao recuperavel do acervo; "
                          "hipotese: blocos alternados com P=55,56 mm distribuida em 12 blocos de d. "
                          "Pico depende do ordenamento (ver DIVERGENCIAS.md)", strict=True)
def test_baixio_hut_pico_tr25():
    hu = h.hidrograma_unitario_triangular(3.234, 0.9633, 0.16055)
    # hietograma triangular (maior bloco no centro), total 55,56 mm em 12 blocos
    w = [1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1]
    p = [55.56 * x / sum(w) for x in w]
    pe = h.hietograma_para_efetiva(p, 62.04)
    r = h.convolucao_hu(pe, hu)
    assert r["Qp_m3s"] == pytest.approx(6.03, rel=0.05)


# ====================== v0.2.0: correcoes da redacao da skill ======================
import warnings  # noqa: E402

SERIE10 = [60, 72, 55, 90, 110, 65, 70, 80, 95, 58]  # gabaritos-numericos.md (HDS-2)


def test_dnos_forma_dnit_p89():
    # DNIT-HIDRO p. 89: Tc = (10/K) A^0,3 L^0,2 / I^0,4 (A ha, L m, I %); caso 45,5 min
    assert h.dnos(100, 2000, 1.0, 4.0) == pytest.approx(45.5, rel=0.01)
    assert h.dnos(100, 2000, 1.0, terreno="argiloso_vegetacao_absorcao_media") == pytest.approx(45.5, rel=0.01)
    # K maior da Tc menor (K divide)
    assert h.dnos(100, 2000, 1.0, 5.5) < h.dnos(100, 2000, 1.0, 2.0)
    assert h.dnos(100, 2000, 1.0, 2.0) == pytest.approx(2 * h.dnos(100, 2000, 1.0, 4.0), rel=1e-9)
    with pytest.raises(ValueError):
        h.dnos(100, 2000, 1.0, terreno="inexistente")


def test_dnos_legado_19_3_min():
    assert h.dnos_legado(1.0, 2.0, 1.0, 4.0) == pytest.approx(19.3, rel=0.01)
    # a forma nova e a antiga divergem mais de 2x no caso (45,5 x 19,3 min)
    assert h.dnos(100, 2000, 1.0, 4.0) > 2 * h.dnos_legado(1.0, 2.0, 1.0, 4.0)


def test_tc_dnos_e_legado_via_dispatcher():
    r = h.tc_com_avisos("dnos", A=100, L=2000, I=1.0, K=4.0)
    assert r["saidas"]["tc_min"] == pytest.approx(45.5, rel=0.01)
    r2 = h.tc_com_avisos("dnos_legado", A=1.0, L=2.0, I=1.0, K=4.0)
    assert r2["saidas"]["tc_min"] == pytest.approx(19.3, rel=0.01)
    assert any("nao confirmada" in a for a in r2["avisos"])


def test_kirpich_modificada_e_1_5_kirpich():
    # DNIT-HIDRO p. 90: 1,42 ~ 1,5 x 0,95 (diferenca 0,35 %)
    L_km, H = 2.9, 12.0
    kirp = 60.0 * 0.95 * (L_km ** 3 / H) ** 0.385
    assert h.kirpich_modificada_dnit(L_km, H) == pytest.approx(1.5 * kirp, rel=0.005)
    assert h.kirpich_modificada_dnit(L_km, H) == pytest.approx(
        h.kirpich(L_km * 1000, H / (L_km * 1000)) * 1.5, rel=0.02)


def test_mcmath_constante_por_unidade_de_S():
    # conversao exata do USBR (p. 57): 0,02832/25,4 * 2,471^0,8 * 1000^0,2
    k_mm = 0.02832 / 25.4 * 2.471 ** 0.8 * 1000 ** 0.2
    k_mkm = 0.02832 / 25.4 * 2.471 ** 0.8
    assert k_mm == pytest.approx(0.0091, rel=0.01)
    assert k_mkm == pytest.approx(0.0023, rel=0.01)
    # mesma bacia: S = 0,0028 m/m = 2,8 m/km -> Q coincide dentro de 1 % (arredondamento das constantes)
    q1 = h.mcmath(0.3, 40, 189, 0.0028)
    q2 = h.mcmath(0.3, 40, 189, 2.8, S_unidade="m/km")
    assert q2 == pytest.approx(q1, rel=0.01)
    r = h.mcmath(0.3, 40, 189, 2.8, detalhado=True, S_unidade="m/km")
    assert r["saidas"]["constante"] == 0.0023 and r["avisos"] == []
    with pytest.raises(ValueError):
        h.mcmath(0.3, 40, 189, 0.0028, S_unidade="%")


def test_mcmath_aviso_declividade_do_dreno():
    with pytest.warns(UserWarning, match="canal principal"):
        r = h.mcmath(0.3, 40, 189, 0.0028, detalhado=True, S_tipo="dreno")
    assert any("canal principal" in a for a in r["avisos"])


def test_iuiu_dp11_mcmath_sensibilidade_ao_S_do_canal():
    # Reteste com a interpretacao correta (S = canal principal). O caso nao informa o S do canal
    # principal (0,0028 e o do dreno). Com Tc de Kirpich consistente, S ~ 0,0020 m/m reproduz 2,34
    # dentro de 5 %: o S necessario e plausivel, mas NAO e dado do projeto (ver DIVERGENCIAS.md).
    A, L = 189.0, 4670.0

    def q(S):
        tc = h.kirpich(L, S)
        return h.mcmath(0.3, 108.49 / (tc / 60.0), A, S)

    assert q(0.0028) == pytest.approx(2.90, rel=0.01)  # com o S do dreno: +24 % (mantido)
    assert q(0.0020) == pytest.approx(2.34, rel=0.05)


def test_gumbel_K_n10_hds2_tab_5_13():
    # FHWA-HDS2 p. 132, Tab. 5.13: n=10, prob. 0,04 (TR 25) -> K = 2,8468; TR 100 -> 4,3228
    assert h.gumbel_K(25, 10) == pytest.approx(2.8468, rel=0.001)
    assert h.gumbel_K(100, 10) == pytest.approx(4.3228, rel=0.001)
    assert h.gumbel_K(25, 20) == pytest.approx(2.5169, rel=0.001)
    assert h.gumbel_K(25, 30) == pytest.approx(2.3933, rel=0.001)
    assert h.gumbel_K(25) == pytest.approx(2.04, rel=0.005)  # amostra infinita
    yn, sn = h.gumbel_yn_sn(10)
    assert yn == pytest.approx(0.4952, abs=5e-4) and sn == pytest.approx(0.9496, abs=5e-4)


def test_gumbel_P_TR_com_n_serie_do_gabarito():
    # media 75,5; K de n da ~126,8 mm; forma infinita da ~112,3 mm (-11 %)
    p_n = h.gumbel_P_TR(SERIE10, 25, n=10)
    with pytest.warns(UserWarning, match="sem n"):
        p_inf = h.gumbel_P_TR(SERIE10, 25)
    assert p_n == pytest.approx(126.8, rel=0.01)
    assert p_inf == pytest.approx(112.3, rel=0.01)
    assert p_inf < p_n
    r = h.gumbel_P_TR(SERIE10, 25, detalhado=True, n=10)
    assert r["saidas"]["K"] == pytest.approx(2.8468, rel=0.001)
    assert any("< 20" in a for a in r["avisos"])


def test_chuva_efetiva_lam005_converte_cn_e_avisa():
    # CN_0,05 = 100/(1,879 (100/CN - 1)^1,15 + 1): CN 80 -> 72,4 (NEH-630 cap. 10 p. 10: Ia != 0,2S exige novo CN)
    assert h.cn_para_lambda_005(80) == pytest.approx(72.38, abs=0.05)
    assert h.cn_para_lambda_005(100) == pytest.approx(100.0)
    with pytest.warns(UserWarning, match="convertido"):
        q = h.chuva_efetiva(100, 80, lam=0.05)
    cn2 = h.cn_para_lambda_005(80)
    S = h.retencao_S(cn2)
    assert q == pytest.approx((100 - 0.05 * S) ** 2 / (100 - 0.05 * S + S), rel=1e-9)
    # com CN convertido o escoamento fica proximo do de lam=0,2 (e nao muito maior, como sem conversao)
    q02 = h.chuva_efetiva(100, 80, lam=0.2)
    q_sem = h.chuva_efetiva(100, 80, lam=0.05, ajustar_cn=False)
    assert abs(q - q02) < abs(q_sem - q02)
    with warnings.catch_warnings():
        warnings.simplefilter("error")  # ajustar_cn=False nao avisa
        h.chuva_efetiva(100, 80, lam=0.05, ajustar_cn=False)


def test_hietograma_efetiva_lam005_converte_uma_vez():
    p = [10, 20, 30, 10]
    with pytest.warns(UserWarning):
        pe = h.hietograma_para_efetiva(p, 75, lam=0.05)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        assert sum(pe) == pytest.approx(h.chuva_efetiva(70, 75, lam=0.05))


def test_risco_hidrologico_e_tr_para_risco():
    assert h.risco_hidrologico(25, 50) == pytest.approx(1 - 0.96 ** 50, rel=1e-12)  # 0,870
    assert h.risco_hidrologico(100, 1) == pytest.approx(0.01)
    assert h.risco_hidrologico(1, 10) == pytest.approx(1.0)
    J = h.risco_hidrologico(50, 30)
    assert h.tr_para_risco(J, 30) == pytest.approx(50, rel=1e-9)
    assert h.tr_para_risco(0.1, 50) == pytest.approx(475.06, rel=1e-3)
    with pytest.raises(ValueError):
        h.tr_para_risco(1.0, 10)


def test_blocos_alternados_wilken_tr5_pmsp_v2():
    # PMSP-DRENURB-V2 p. 21-22, Tab. 1.1: i = 57,71 TR^0,172/(t+22)^1,025 mm/min; t 10..100, dt 10
    par = {"a": 57.71 * 60, "b": 0.172, "c": 22.0, "d": 1.025}
    r = h.blocos_alternados(par, 5, 100, 10)
    esperado = [21.8, 33.0, 39.7, 44.2, 47.5, 49.9, 51.7, 53.2, 54.4, 55.3]
    assert r["P_acum_mm"] == pytest.approx(esperado, rel=0.01)
    hiet = [1.2, 1.8, 3.2, 6.7, 21.8, 11.2, 4.5, 2.4, 1.4, 0.9]
    assert r["hietograma_mm"] == pytest.approx(hiet, abs=0.15)
    assert sum(r["hietograma_mm"]) == pytest.approx(r["P_total_mm"])
    assert max(r["hietograma_mm"]) == r["hietograma_mm"][4]
    r2 = h.blocos_alternados(lambda tr, t: h.idf_potencial(tr, t, **par), 5, 100, 10)
    assert r2["hietograma_mm"] == pytest.approx(r["hietograma_mm"])
    r3 = h.blocos_alternados(par, 5, 90, 10)  # n impar: maior no centro
    assert max(r3["hietograma_mm"]) == r3["hietograma_mm"][4]
    with pytest.raises(ValueError):
        h.blocos_alternados(par, 5, 95, 10)


def test_racional_dnit_p130_exemplo():
    # DNIT-HIDRO p. 130: c = 0,1828; i = 67,33*60/40 = 101,0 mm/h; A = 2,4 km2 -> 12,31 m3/s
    # (divisor 3,6; o texto extraido imprime 6,3)
    assert 67.33 * 60 / 40 == pytest.approx(101.0, rel=0.001)
    assert h.racional(0.1828, 101.0, 2.4) == pytest.approx(12.31, rel=0.01)


def test_nrcs_ex_16_1_hu_triangular_em_si():
    # NRCS-NEH630-CH16 ex. 16-1 (marcador fisico p. 13-15): A = 4,6 mi2, Tc = 2,3 h, dD = 0,3 h
    # -> Tp = 1,53 h, qp = 1.455 cfs por 1 pol. Conversao: 1 mi2 = 2,58999 km2, 1 pol = 25,4 mm,
    # 1 ft3/s = 0,0283168 m3/s.
    A_km2 = 4.6 * 2.58999
    hu = h.hidrograma_unitario_triangular(A_km2, 2.3, 0.3)
    assert hu["tp_h"] == pytest.approx(1.53, rel=0.01)
    qp_cfs = hu["qp_m3s_por_mm"] * 25.4 / 0.0283168
    assert qp_cfs == pytest.approx(1455, rel=0.01)
    assert hu["tb_h"] == pytest.approx(2.67 * 1.53, rel=1e-9)


def test_nrcs_ch10_ex_10_3_escoamento_em_polegadas():
    # NRCS-NEH630-CH10 ex. 10-3 (marcador fisico p. 17; o gabarito citava p. 19):
    # P = 5,1 pol, CN 75 -> 2,53 pol; CN 69 -> 2,03 pol
    P_mm = 5.1 * 25.4
    assert h.chuva_efetiva(P_mm, 75) / 25.4 == pytest.approx(2.53, rel=0.01)
    assert h.chuva_efetiva(P_mm, 69) / 25.4 == pytest.approx(2.03, rel=0.01)
    assert h.retencao_S(74) / 25.4 == pytest.approx(3.51, rel=0.01)  # Tab. 10-1


def test_abder_p69_racional_com_retardo():
    # ABDER-APOSTILA p. 69: Q = 0,00278 C I A(ha) phi, phi = 1/(100 A)^(1/n), A em km2 e
    # n = 6 (declividade > 1 %, p. 59); A = 8,5 km2, C = 0,35, I = 65,89 mm/h -> 17,9 m3/s.
    A_km2 = 8.5
    phi = 1.0 / (100 * A_km2) ** (1 / 6)
    assert phi == pytest.approx(0.325, rel=0.01)
    Q = h.racional(0.35, 65.89, A_km2, "km2", limite_km2=10.0) * phi
    assert Q == pytest.approx(17.9, rel=0.02)


def test_cli_v02_funcoes_novas():
    env = dict(os.environ, PYTHONIOENCODING="utf-8")

    def run(req):
        out = subprocess.run([sys.executable, "-m", "tools.dren.hidrologia", "--json", json.dumps(req)],
                             capture_output=True, text=True, encoding="utf-8", env=env,
                             cwd=RAIZ, stdin=subprocess.DEVNULL).stdout
        return json.loads(out)

    assert h.VERSAO == "0.3.0"
    d = run({"funcao": "risco_hidrologico", "TR": 25, "vida_util": 50})
    assert d["saidas"]["J"] == pytest.approx(0.8701, rel=1e-3) and d["versao"] == "0.3.0"
    d = run({"funcao": "chuva_efetiva", "P": 100, "CN": 80, "lam": 0.05})
    assert d["saidas"]["CN_usado"] == pytest.approx(72.38, abs=0.05) and d["avisos"]
    d = run({"funcao": "gumbel", "serie_maximos_anuais": SERIE10, "TR": 25, "n": 10})
    assert d["saidas"]["P"] == pytest.approx(126.8, rel=0.01)
    d = run({"funcao": "blocos_alternados", "TR": 5, "duracao_total": 100, "dt": 10,
             "a": 57.71 * 60, "b": 0.172, "c": 22, "d": 1.025})
    assert d["saidas"]["P_total_mm"] == pytest.approx(55.3, rel=0.01)


# ====================== v0.3.0 (F5/M1): conferencia no primario e gabaritos G1 ======================
FT = 0.3048
POL = 25.4
CFS = 0.0283168


def _run_cli(req):
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    out = subprocess.run([sys.executable, "-m", "tools.dren.hidrologia", "--json", json.dumps(req)],
                         capture_output=True, text=True, encoding="utf-8", env=env,
                         cwd=RAIZ, stdin=subprocess.DEVNULL).stdout
    return json.loads(out)


# ---- livro: formulas de Tc conferidas no primario (tolerancia 1 %)
def test_kirpich_equivale_as_formas_do_pmsp_e_do_mccuen():
    # PMSP-DRENURB-V2 p. 56 Eq. 1.28: 3,989 L^0,77 S^-0,385 (L km); McCuen Eq. 3-55: 0,0078 L^0,77 S^-0,385 (L ft)
    L_m, S = 1000.0, 0.01
    assert h.kirpich(L_m, S) == pytest.approx(3.989 * 1.0 ** 0.77 * S ** -0.385, rel=0.01)
    assert h.kirpich(L_m, S) == pytest.approx(0.0078 * (L_m / FT) ** 0.77 * S ** -0.385, rel=0.01)
    # California Culverts (Kirpich com S = H/L) = DNIT-HIDRO p. 88 (0,95 h) = 57 min
    assert h.california_culverts(1.0, 10.0) == pytest.approx(h.kirpich(1000.0, 10.0 / 1000.0), rel=0.01)
    assert 0.95 * 60 == pytest.approx(57.0)


def test_kirpich_aviso_L_maior_que_10_km():
    r = h.kirpich(12000, 0.05, detalhado=True)
    assert any("10 km" in a for a in r["avisos"])
    assert not any("10 km" in a for a in h.kirpich(9000, 0.05, detalhado=True)["avisos"])


def test_ime_p29_exemplo_picking_chow_california():
    # IME p. 29: L 5 km, I 0,06 (H 300 m): California 41 min, Ven Te Chow 39,8 min (I 6 %), Picking 40 min
    # (valores impressos arredondados; tolerancia = arredondamento do livro)
    assert h.california_culverts(5.0, 300.0) == pytest.approx(41.0, abs=0.8)
    assert h.ven_te_chow(5.0, 6.0) == pytest.approx(39.8, abs=0.1)
    assert h.picking(5.0, 0.06) == pytest.approx(40.0, abs=0.5)
    with pytest.raises(ValueError):
        h.picking(5.0, 0.0)
    with pytest.raises(ValueError):
        h.ven_te_chow(0.0, 6.0)


def test_picking_e_chow_coerentes_com_tabela_de_velocidades_do_dnit():
    # DNIT-HIDRO p. 97 (forma unificada, V = L/Tc em km/h): Picking V = 1,1320 H^0,333;
    # Ven Te Chow V = 1,1396 L^0,04 H^0,320. A comparacao so fecha com Picking em MINUTOS (o DNIT
    # imprime "horas" na p. 88: divergencia de unidade).
    L, H = 5.0, 300.0
    I = H / (L * 1000)
    assert L / (h.picking(L, I) / 60) == pytest.approx(1.1320 * H ** 0.333, rel=0.01)
    assert L / (h.ven_te_chow(L, 100 * I) / 60) == pytest.approx(1.1396 * L ** 0.04 * H ** 0.320, rel=0.01)
    # Kirpich do DNIT (0,95 h): V = 1,0526 L^-0,155 H^0,385
    tc_kirp_min = h.california_culverts(L, H)
    assert L / (tc_kirp_min / 60) == pytest.approx(1.0526 * L ** -0.155 * H ** 0.385, rel=0.01)


def test_dooge_forma_pmsp_p57_unidades_e_faixa():
    # PMSP-DRENURB-V2 p. 57 Eq. 1.34: tc[min] = 21,88 A^0,41 S^-0,17 (A km2, S m/m; 140 a 930 km2)
    assert h.dooge(500.0, 0.001) == pytest.approx(21.88 * 500 ** 0.41 * 0.001 ** -0.17, rel=1e-12)
    r = h.tc_com_avisos("dooge", A=500.0, S=0.001)
    assert r["saidas"]["tc_min"] == pytest.approx(h.dooge(500.0, 0.001))
    assert not any("fora de 140-930" in a for a in r["avisos"])
    assert any("fora de 140-930" in a for a in h.tc_com_avisos("dooge", A=5.0, S=0.01)["avisos"])


def test_giandotti_forma_dnit_e_aviso_de_faixa():
    # DNIT-HIDRO p. 91-92: TC[h] = (4 raiz(A) + 1,5 L)/(0,8 raiz(H)); sem faixa de area no corpus
    assert h.giandotti(36.0, 10.0, 100.0) == pytest.approx((24 + 15) / 8.0, rel=1e-12)
    r = h.tc_com_avisos("giandotti", A=36.0, L=10.0, Hm=100.0)
    assert r["saidas"]["tc_min"] == pytest.approx(39 / 8.0 * 60)
    assert any("170" in a and "nao consta" in a for a in r["avisos"])
    r2 = h.tc_com_avisos("giandotti", A=500.0, L=40.0, Hm=300.0)
    assert not any("170" in a for a in r2["avisos"])


def test_dnos_tabela_K_por_terreno_dnit_p89():
    assert set(h.DNOS_K_TERRENO.values()) == {2.0, 3.0, 4.0, 4.5, 5.0, 5.5}
    for terreno, k in h.DNOS_K_TERRENO.items():
        assert h.dnos(100, 2000, 1.0, terreno=terreno) == pytest.approx(
            10 / k * 100 ** 0.3 * 2000 ** 0.2, rel=1e-12)


def test_kirpich_modificada_fator_142_dnit_p90():
    # DNIT-HIDRO p. 90: TC = 1,42 (L^3/H)^0,385 h = 1,5 x 0,95 (1,425; diferenca 0,35 %)
    assert h.kirpich_modificada_dnit(2.9, 12.0) == pytest.approx(
        1.42 * 60 * (2.9 ** 3 / 12.0) ** 0.385, rel=1e-12)
    assert 1.42 / (1.5 * 0.95) == pytest.approx(1.0, abs=0.004)


def test_kerby_mccuen_eq_3_53_equivalencia_5pct():
    # McCuen Eq. 3-53: 0,83 (nL/S^0,5)^0,47 min (L ft) x forma em m (1,44, expoente 0,467): ate ~3 %
    n, L_m, S = 0.4, 100.0, 0.01
    assert h.kerby(L_m, n, S) == pytest.approx(0.83 * (n * L_m / FT / math.sqrt(S)) ** 0.47, rel=0.05)


# ---- livro: McCuen cap. 3 e NEH-630 cap. 15
def test_mccuen_ex_3_12_onda_cinematica_e_scs():
    # McCuen Ex. 3-12 (p. 146 impressa): n 0,15, L 120 ft, S 0,002; i 8 -> 14,9; 5,1 -> 17,9; 4,7 -> 18,5; 4,6 -> 18,6 min
    L = 120 * FT
    for i, tt in [(8.0, 14.9), (5.1, 17.9), (4.7, 18.5), (4.6, 18.6)]:
        assert h.tc_onda_cinematica(0.15, L, 0.002, i * POL) == pytest.approx(tt, rel=0.01)
    # versao SCS (Eq. 3-48): P2 3,12 pol -> 28,8 min
    assert h.tc_laminar_neh(0.15, L, 3.12 * POL, 0.002) * 60 == pytest.approx(28.8, rel=0.01)
    # coeficiente 0,938 (livro) x 0,933 (planilhas): 0,5 %
    assert h.tc_onda_cinematica(0.15, L, 0.002, 8 * POL, coef=0.933) == pytest.approx(
        h.tc_onda_cinematica(0.15, L, 0.002, 8 * POL) * 0.933 / 0.938, rel=1e-12)


def test_neh630_cap15_laminar_e_velocidade_p18_21():
    # NEH-630 cap. 15 p. 18: lamina 100 ft, n 0,15, P2 3,6 pol, S 0,08 -> 0,09 h (calc. 0,089)
    assert h.tc_laminar_neh(0.15, 100 * FT, 3.6 * POL, 0.08) == pytest.approx(0.089, rel=0.01)
    # R-2: 6000 ft a 5,2 ft/s = 0,32 h
    assert h.tempo_viagem_min(6000 * FT, 5.2 * FT) / 60 == pytest.approx(0.32, rel=0.01)
    # Tc = R-1 + R-2 + R-3 = 1,00 + 0,32 + 0,43 = 1,75 h
    assert 1.00 + h.tempo_viagem_min(6000 * FT, 5.2 * FT) / 60 + 0.43 == pytest.approx(1.75, rel=0.01)


def test_neh630_tab_15_3_velocidade_escoamento_concentrado():
    # Tab. 15-3: V = 20,328 S^0,5 ft/s (pavimento), k*0,3048 em m/s
    assert h.velocidade_concentrado_neh("pavimento_ravinas", 0.02) / FT == pytest.approx(
        20.328 * 0.02 ** 0.5, rel=1e-9)
    assert h.velocidade_concentrado_neh("floresta_serapilheira_feno", 0.01) == pytest.approx(
        2.516 * FT * 0.1, rel=1e-9)
    assert set(h.VELOCIDADE_CONCENTRADO_NEH_K.values()) == {20.328, 16.135, 9.965, 8.762, 6.962, 5.032, 2.516}
    with pytest.raises(ValueError):
        h.velocidade_concentrado_neh("inexistente", 0.01)


def test_mccuen_ex_3_13_metodo_da_velocidade():
    # Ex. 3-13 (pos-desenvolvimento): tubo 15 pol, n 0,011, S 0,009, V a secao plena 5,9 ft/s
    D = 15 * 0.0254
    assert h.velocidade_manning(D / 4, 0.009, 0.011) / FT == pytest.approx(5.9, rel=0.01)
    # antes: 140/0,25 + 260/1,40 + 480/2,1 = 975 s = 16,2 min
    seg = [(140, 0.25), (260, 1.40), (480, 2.1)]
    tc = sum(h.tempo_viagem_min(L * FT, V * FT) for L, V in seg)
    assert tc == pytest.approx(16.2, rel=0.01)
    # depois: 238 + 24 + 214 + 71 = 547 s = 9,1 min
    assert (238 + 24 + 214 + 71) / 60 == pytest.approx(9.1, rel=0.01)


def test_lag_scs_neh_p18_e_mccuen_ex_9_23():
    # NEH-630 cap. 15 p. 18: L 3.865 ft, Y 4,79 %, CN 63 -> Tc 1,14 h
    assert h.tc_lag_scs(3865 * FT, 63, 4.79) == pytest.approx(1.14, rel=0.01)
    # McCuen Ex. 9-23: L 6.500 ft, S 1,3 %, CN 92 -> tc 1,34 h
    assert h.tc_lag_scs(6500 * FT, 92, 1.3) == pytest.approx(1.34, rel=0.01)
    # equivalencia com McCuen Eq. 3-56: tc[min] = 0,00526 L^0,8 (1000/CN - 9)^0,7 S^-0,5 (L ft, S ft/ft)
    L_ft, CN, S = 4000.0, 75.0, 0.03
    eq356 = 0.00526 * L_ft ** 0.8 * (1000 / CN - 9) ** 0.7 * S ** -0.5
    assert h.tc_lag_scs(L_ft * FT, CN, S * 100) * 60 == pytest.approx(eq356, rel=0.01)
    with pytest.raises(ValueError):
        h.tc_lag_scs(1000, 120, 1.0)
    r = h.tc_com_avisos("lag_scs", L=1000.0, CN=40, Y=2.0)
    assert any("CN fora" in a for a in r["avisos"])


def test_mccuen_ex_9_23_hut_triangular_726():
    # A = 300 ac, tc 1,34 h, D = 0,133 tc: tp 0,893 h; tb 2,38 h; qp = 254 cfs (726 A/tc; 484 A/tp)
    hu = h.hidrograma_unitario_triangular(300 / 640 * 2.58999, 1.34, 0.133 * 1.34)
    assert hu["tp_h"] == pytest.approx(0.893, rel=0.01)
    assert hu["tb_h"] == pytest.approx(2.381, rel=0.01)
    assert hu["qp_m3s_por_mm"] * POL / CFS == pytest.approx(254.0, rel=0.01)


def test_mccuen_racional_ex_7_9_e_7_11():
    # Ex. 7-9: A 2,4 ac, C 0,95, i 8,6 pol/h -> 19,6 ft3/s (1 ac.pol/h = 1,0083 cfs)
    q = h.racional(0.95, 8.6 * POL, 2.4 * 0.00404686) / CFS
    assert q == pytest.approx(19.6, rel=0.01)
    # Ex. 7-11: C = 0,2/0,4/0,6 em 5,3/7,2/6,4 ac -> 0,412; i 4,8 pol/h, 18,9 ac -> 37,4 ft3/s
    C = h.c_ponderado([0.2, 0.4, 0.6], [5.3, 7.2, 6.4])
    assert C == pytest.approx(0.412, rel=0.01)
    assert h.racional(C, 4.8 * POL, 18.9 * 0.00404686) / CFS == pytest.approx(37.4, rel=0.01)
    with pytest.raises(ValueError):
        h.c_ponderado([0.2], [1.0, 2.0])


def test_mccuen_scs_ex_7_15_a_7_18_e_ponderacao_do_escoamento():
    # Ex. 7-15: P 7 pol, CN 75 -> S 3,333; Ia 0,667; Q 4,15 pol. Ex. 7-18: CN 55/70/83 -> 2,12/3,62/5,03 pol
    P = 7 * POL
    assert h.retencao_S(75) / POL == pytest.approx(3.333, rel=0.001)
    for cn, q in [(75, 4.15), (55, 2.12), (70, 3.62), (83, 5.03)]:
        assert h.chuva_efetiva(P, cn) / POL == pytest.approx(q, rel=0.01)
    # pondera-se o escoamento, nao o CN: CN 55 e 83 em areas iguais
    q_pond = h.escoamento_ponderado(P, [55, 83], [1.0, 1.0])
    assert q_pond / POL == pytest.approx((2.12 + 5.03) / 2, rel=0.01)
    assert q_pond > h.chuva_efetiva(P, 69)  # o CN medio subestima o escoamento


# ---- planilhas internas (escoamento plano; aba "FAA": onda cinematica com coef 0,933)
def test_planilhas_escoamento_plano_001_e_redencao():
    # planilha-001: n 0,13; L 150 m; i 186 mm/h; S 0,15 -> Tti 9,0114 min; Vti 0,27743 m/s
    t1 = h.tc_onda_cinematica(0.13, 150.0, 0.15, 186.0, coef=0.933)
    assert t1 == pytest.approx(9.0114, rel=0.001)
    assert 150.0 / (t1 * 60) == pytest.approx(0.27743, rel=0.001)
    # Redencao: n 0,011; L 141,86 m; S 0,0097 -> 4,5032 min; 0,52503 m/s
    t2 = h.tc_onda_cinematica(0.011, 141.86, 0.0097, 186.0, coef=0.933)
    assert t2 == pytest.approx(4.5032, rel=0.001)
    assert 141.86 / (t2 * 60) == pytest.approx(0.52503, rel=0.001)
    # IDF da aba (T 5 anos, t 7 min): i = 8460,202 T^0,177/(t+41,05)^1,092 = 163,94 mm/h
    assert h.idf_potencial(5, 7, 8460.202, 0.177, 41.05, 1.092) == pytest.approx(163.94, rel=0.001)
    # a planilha viola o limite de lamina (L > 100 ft; n L/raiz(S) > 100): o aviso tem de aparecer
    assert len(h.tc_escoamento_aviso_lamina(0.13, 150.0, 0.15)) == 2


def test_aviso_limite_de_lamina_neh_100_ft():
    assert h.tc_escoamento_aviso_lamina(0.15, 25.0, 0.05) == []  # 82 ft; nL/raiz(S) = 55
    av = h.tc_escoamento_aviso_lamina(0.15, 40.0, 0.002)
    assert any("100 ft" in a for a in av) and any("McCuen e Spiess" in a for a in av)
    r = h.tc_com_avisos("onda_cinematica", n=0.15, L=40.0, S=0.002, i=100.0)
    assert r["avisos"] and r["saidas"]["tc_min"] > 0


# ---- acervo (sem marca humana): Delmiro Gouveia BHD1 TR 50 (tolerancia 5 %)
def test_delmiro_bhd1_cadeia_tc_s_pe_hut():
    J = 32.0 / 13210 * 100
    tc = h.bransby_williams(13.21, 36.34, J)
    assert tc == pytest.approx(7.53, rel=0.05)
    assert h.retencao_S(75.2) == pytest.approx(83.77, rel=0.001)
    assert h.chuva_efetiva(112.40, 75.2) == pytest.approx(50.99, rel=0.01)
    hu = h.hidrograma_unitario_triangular(36.34, tc, 0.941)
    assert hu["tp_h"] == pytest.approx(4.990, rel=0.01)
    assert hu["tb_h"] == pytest.approx(13.32, rel=0.01)
    # o projeto imprime 15,149 "m3/s por mm" com Qp = 2,08 A/ta: isso e por 10 mm (1 cm); por mm = 0,208 A/ta
    assert 10 * hu["qp_m3s_por_mm"] == pytest.approx(15.149, rel=0.01)


def test_delmiro_bhd1_tempo_do_pico_com_chuva_uniforme():
    hu = h.hidrograma_unitario_triangular(36.34, 7.53, 0.941)
    pe = h.hietograma_para_efetiva([112.40 / 8] * 8, 75.2)
    r = h.convolucao_hu(pe, hu)
    assert r["tp_pico_h"] == pytest.approx(10.36, rel=0.05)


@pytest.mark.xfail(strict=True, reason="Delmiro BHD1 TR 50 (1494:64): pico 58,71 m3/s depende do hietograma "
                                       "(polinomio cubico por faixa, Quadro 3.3, nao recuperavel). Com chuva "
                                       "uniforme em 8 blocos o pico sai 61,8 m3/s (+5,3 %); divergencia > 5 % "
                                       "registrada em DIVERGENCIAS (sessao interativa pendente)")
def test_delmiro_bhd1_pico_58_71():
    hu = h.hidrograma_unitario_triangular(36.34, 7.53, 0.941)
    pe = h.hietograma_para_efetiva([112.40 / 8] * 8, 75.2)
    assert h.convolucao_hu(pe, hu)["Qp_m3s"] == pytest.approx(58.71, rel=0.05)


def test_delmiro_nerc_x_kirpich_rotulo_e_velocidade():
    # caso delmiro_gouveia_tc_rotulos: NERC 7,65 h (impresso como "Kirpich"); Kirpich de livro 4,92 h
    L_km, H = 13.21, 32.0
    assert h.nerc(L_km, H) == pytest.approx(7.65, rel=0.01)
    tc_kirpich = h.kirpich(L_km * 1000, H / (L_km * 1000)) / 60
    assert tc_kirpich == pytest.approx(4.92, rel=0.05)
    assert h.nerc(L_km, H) > 1.5 * tc_kirpich
    # velocidade em m/s abaixo do minimo de 0,5 m/s do memorial (1492:155): 0,48 e 0,49
    assert L_km * 1000 / (h.nerc(L_km, H) * 3600) == pytest.approx(0.48, rel=0.02)
    J = H / (L_km * 1000) * 100
    tc_bw = h.bransby_williams(L_km, 36.34, J)
    v_bw = L_km * 1000 / (tc_bw * 3600)
    assert v_bw == pytest.approx(0.49, rel=0.02)
    assert v_bw < 0.5


def test_cli_v03_metodos_novos_de_tc():
    d = _run_cli({"funcao": "tc", "metodo": "picking", "L": 5.0, "I": 0.06})
    assert d["saidas"]["tc_min"] == pytest.approx(39.6, rel=0.01) and d["avisos"] and d["versao"] == "0.3.0"
    d = _run_cli({"funcao": "tc", "metodo": "lag_scs", "L": 3865 * FT, "CN": 63, "Y": 4.79})
    assert d["saidas"]["tc_min"] == pytest.approx(1.14 * 60, rel=0.01)
    d = _run_cli({"funcao": "tc", "metodo": "ven_te_chow", "L": 5.0, "I": 6.0})
    assert d["saidas"]["tc_min"] == pytest.approx(39.8, rel=0.01)
    d = _run_cli({"funcao": "tc", "metodo": "nerc", "L": 13.21, "H": 32.0})
    assert d["saidas"]["tc_min"] == pytest.approx(7.65 * 60, rel=0.01)
