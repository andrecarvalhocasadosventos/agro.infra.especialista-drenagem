"""Testes de tools.hid.hidrologia.

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

from tools.hid import hidrologia as h

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
    cmd = [sys.executable, "-m", "tools.hid.hidrologia", "--json",
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
                          "Tc Kirpich e i=P/Tc; divergencia > 5 % (ver DIVERGENCIAS_bueiros.md)",
                   strict=False)
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
                          "Pico depende do ordenamento (ver DIVERGENCIAS_bueiros.md)", strict=False)
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
    # dentro de 5 %: o S necessario e plausivel, mas NAO e dado do projeto (ver DIVERGENCIAS_bueiros.md).
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
        out = subprocess.run([sys.executable, "-m", "tools.hid.hidrologia", "--json", json.dumps(req)],
                             capture_output=True, text=True, encoding="utf-8", env=env,
                             cwd=RAIZ, stdin=subprocess.DEVNULL).stdout
        return json.loads(out)

    assert h.VERSAO == "0.2.0"
    d = run({"funcao": "risco_hidrologico", "TR": 25, "vida_util": 50})
    assert d["saidas"]["J"] == pytest.approx(0.8701, rel=1e-3) and d["versao"] == "0.2.0"
    d = run({"funcao": "chuva_efetiva", "P": 100, "CN": 80, "lam": 0.05})
    assert d["saidas"]["CN_usado"] == pytest.approx(72.38, abs=0.05) and d["avisos"]
    d = run({"funcao": "gumbel", "serie_maximos_anuais": SERIE10, "TR": 25, "n": 10})
    assert d["saidas"]["P"] == pytest.approx(126.8, rel=0.01)
    d = run({"funcao": "blocos_alternados", "TR": 5, "duracao_total": 100, "dt": 10,
             "a": 57.71 * 60, "b": 0.172, "c": 22, "d": 1.025})
    assert d["saidas"]["P_total_mm"] == pytest.approx(55.3, rel=0.01)
