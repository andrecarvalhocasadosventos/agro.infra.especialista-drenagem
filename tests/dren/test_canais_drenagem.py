"""Testes de tools.dren.canais_drenagem.

(a) livro: USACE-EM1110-2-1601 App. H Tab. H-1 p. 179, FHWA-HEC11 Exemplo 1 p. 78 e Eq. 7/20 (tolerancia 1 %);
(b) acervo, sem checagem humana (sem marca h): Salitre Etapa 2, Delmiro Gouveia, RETROANALISE gabiao
    (tolerancia 5 %, rotulados "acervo, sem h");
(c) consistencia e casos negativos (reconciliacao, transbordo, limites duplicados).
Divergencia > 5 % => xfail(strict=True); nada foi ajustado ao gabarito.
"""
import json
import math
import os
import subprocess
import sys

import pytest

from tools.dren import bueiros as B
from tools.dren import canais_drenagem as C

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
FT = 0.3048
CFS = FT ** 3


# ---------------------------------------------------------------- (a) livro
@pytest.mark.parametrize("n,y_ft,V_fps", [(0.034, 10.6, 7.9), (0.036, 11.0, 7.6), (0.038, 11.3, 7.3)])
def test_em1601_tab_h1_profundidade_normal(n, y_ft, V_fps):
    # EM 1110-2-1601 App. H Tab. H-1 p. 179: b = 140 ft, 1V:2H, S = 0,0017, Q = 13 500 cfs (impresso com 1 casa)
    y = C.profundidade_normal(13500 * CFS, 140 * FT, 2, n, 0.0017)
    assert y / FT == pytest.approx(y_ft, rel=0.01)
    m = C.manning_trapezoidal(140 * FT, 2, y, n, 0.0017)
    assert m["V"] / FT == pytest.approx(V_fps, rel=0.01)


def test_em1601_h1_recalculo_n036():
    # mapa G9: recalculo y = 11 ft, V = 7,59 fps, Q = 13 527 cfs com y = 11 ft
    m = C.manning_trapezoidal(140 * FT, 2, 11.0 * FT, 0.036, 0.0017)
    assert m["V"] / FT == pytest.approx(7.59, rel=0.01)
    assert m["Q"] / CFS == pytest.approx(13527, rel=0.01)


def test_hec11_exemplo1_d50():
    # HEC-11 p. 78: V = 9,7 ft/s, d = 11,8 ft, K1 = 0,73, Ss 2,65, SF 1,2 -> D50 = 0,43 ft (recalculo 0,426)
    r = C.d50_riprap_hec11(9.7 * FT, 11.8 * FT, K1=0.73)
    assert r["C"] == pytest.approx(1.0, abs=0.01)
    assert r["D50"] / FT == pytest.approx(0.426, rel=0.01)
    assert r["D50"] / FT == pytest.approx(0.43, abs=0.005)


def test_hec11_exemplo2_d50_com_correcao_c16():
    # Revisao F5 (livro, leitura de grafico, 5 %): HEC-11 Ex. 2 (p. 84-85 do _texto): Va 12,6 ft/s, d 12,0 ft,
    # K1 0,73 -> D50 0,9 ft (Chart 1); Ss 2,60, SF 1,6 -> C = 1,6 (Chart 2) -> D50 = 1,44 ft (0,44 m).
    # Recalculo exato: D50 base 0,926 ft, C 1,613, D50 1,493 ft (+3,7 %, leitura dos graficos).
    r = C.d50_riprap_hec11(12.6 * FT, 12.0 * FT, Ss=2.60, SF=1.6, K1=0.73)
    assert r["C"] == pytest.approx(1.6, rel=0.01)
    # Chart 2 (p. 79): C = 1,61 SF^1,5/(Ss-1)^1,5 e a mesma coisa que Csg*Csf (Eq. 8 x Eq. 9)
    assert r["C"] == pytest.approx(1.61 * 1.6 ** 1.5 / 1.6 ** 1.5, rel=0.002)
    assert r["D50_base_m"] / FT == pytest.approx(0.9, rel=0.05)
    assert r["D50"] / FT == pytest.approx(1.44, rel=0.05)
    assert r["D50"] == pytest.approx(0.44, rel=0.05)


def test_hec11_k1_eq7_talude_2h1v_phi41():
    # p. 78: talude 2:1, phi ~ 41 graus -> K1 = 0,73
    r = C.d50_riprap_hec11(3.0, 3.0, z=2, phi=41)
    assert r["K1"] == pytest.approx(0.73, rel=0.01)


def test_hec11_correcoes_c_sg_c_sf():
    base = C.d50_riprap_hec11(3.0, 3.0, K1=0.8)["D50"]
    # Eq. 9: SF 1,6 -> (1,6/1,2)^1,5 ; Eq. 8: Ss 2,8 -> 2,12/(1,8)^1,5
    sf = C.d50_riprap_hec11(3.0, 3.0, K1=0.8, SF=1.6)["D50"]
    assert sf / base == pytest.approx((1.6 / 1.2) ** 1.5, rel=1e-9)
    ss = C.d50_riprap_hec11(3.0, 3.0, K1=0.8, Ss=2.8)["D50"]
    assert ss / base == pytest.approx((2.12 / 1.8 ** 1.5) / (2.12 / 1.65 ** 1.5), rel=1e-9)


def test_hec11_talude_acima_do_repouso_erro():
    with pytest.raises(ValueError):
        C.d50_riprap_hec11(3.0, 3.0, z=1.0, phi=30)


def test_n_riprap_strickler_forma_e_divergencia():
    # D = 1 ft: n = K (EM-1601) e 0,0395 (HEC-11)
    assert C.n_riprap(FT, "em1601", "media")["n"] == pytest.approx(0.036, rel=1e-9)
    assert C.n_riprap(FT, "em1601", "velocidade")["n"] == pytest.approx(0.034, rel=1e-9)
    assert C.n_riprap(FT, "em1601", "capacidade")["n"] == pytest.approx(0.038, rel=1e-9)
    assert C.n_riprap(FT, "hec11")["n"] == pytest.approx(0.0395, rel=1e-9)
    # mesmo D: os dois metodos divergem (D90 min x D50), a calculadora avisa e nao concilia
    a, b = C.n_riprap(0.3, "em1601"), C.n_riprap(0.3, "hec11")
    assert a["n"] != b["n"]
    assert any("divergencia" in s for s in a["avisos"])
    with pytest.raises(ValueError):
        C.n_riprap(0.3, "xx")


# ---------------------------------------------------------------- (b) acervo, sem h
def test_acervo_salitre_dt416a_manning():
    # caso salitre_etapa2_macrodrenos (acervo, sem h): DT 4.1.6/A b 2,50, h 0,90, 1:1, n 0,030, I 0,00227
    m = C.manning_trapezoidal(2.5, 1, 0.9, 0.03, 0.00227)
    assert m["A"] == pytest.approx(3.060, rel=0.05)
    assert m["P"] == pytest.approx(5.046, rel=0.05)
    assert m["R"] == pytest.approx(0.606, rel=0.05)
    assert m["V"] == pytest.approx(1.139, rel=0.05)
    assert m["Q"] == pytest.approx(3.484, rel=0.05)


@pytest.mark.parametrize("b,z,h,S,V,Q", [(7.80, 1, 0.9, 0.00084, 0.804, 6.295),
                                          (56.0, 1.5, 1.5, 0.00096, 1.307, 114.194),
                                          (3.60, 1, 0.9, 0.00159, 1.005, 4.071)])
def test_acervo_salitre_outros_trechos(b, z, h, S, V, Q):
    r = C.capacidade_trapezoidal(b, z, h, 0.030, S)
    assert r["V"] == pytest.approx(V, rel=0.05)
    assert r["Q"] == pytest.approx(Q, rel=0.05)


def test_acervo_delmiro_ds11c_tirante_froude():
    # caso delmiro_drenos_lotes (acervo, sem h): ZTT04 b 0,60, 1,5:1, n 0,025, Io 0,00368, Q 0,518
    r = C.canal_trapezoidal(0.518, 0.6, 1.5, 0.025, 0.00368, h_secao=0.45)
    assert r["yn"] == pytest.approx(0.43, rel=0.05)
    assert r["A"] == pytest.approx(0.538, rel=0.05)
    assert r["P"] == pytest.approx(2.156, rel=0.05)
    assert r["R"] == pytest.approx(0.250, rel=0.05)
    assert r["V"] == pytest.approx(0.962, rel=0.05)
    assert r["Fr"] == pytest.approx(0.576, rel=0.05)
    assert r["regime"] == "subcritico"
    # folga adotada na planilha 0,02 m; recomendada 0,11 m (25 % do tirante)
    assert r["verificacao_secao"]["folga_min"] == pytest.approx(0.11, rel=0.05)


def test_acervo_delmiro_froude_nao_e_com_y():
    # Fr com y (errado) difere de Fr com A/T em secao trapezoidal
    r = C.canal_trapezoidal(0.518, 0.6, 1.5, 0.025, 0.00368)
    fr_y = r["V"] / math.sqrt(9.81 * r["yn"])
    assert abs(fr_y - r["Fr"]) / r["Fr"] > 0.15
    assert r["Fr"] == pytest.approx(r["V"] / math.sqrt(9.81 * r["A"] / r["T"]), rel=1e-12)


def test_acervo_gabiao_canal_retangular_e_tubo():
    # RETROANALISE CANAL GABIAO (fonte local D8): canal b 1,59, y 0,8, S 0,003, n 0,035 -> Q 1,0784
    assert C.manning_trapezoidal(1.59, 0, 0.8, 0.035, 0.003)["Q"] == pytest.approx(1.0784, rel=0.005)
    # tubo DN1000, y/D 0,85, n 0,010 -> 1,7591 (funcao circular e de bueiros.py, importada sem alterar)
    assert B.manning_lamina("circular", 1.0, 0.85, 0.01, 0.003)["Q"] == pytest.approx(1.7591, rel=0.005)


def test_acervo_gabiao_fracoes_da_grade():
    # fracao das 21 x 21 combinacoes de n em que o tubo (PEAD 0,009-0,011; concreto 0,011-0,015) escoa mais
    def frac(n0, n1):
        c = 0
        for i in range(21):
            for j in range(21):
                nc = 0.02 + 0.015 * i / 20
                nt = n0 + (n1 - n0) * j / 20
                qc = C.manning_trapezoidal(1.59, 0, 0.8, nc, 0.003)["Q"]
                qt = B.manning_lamina("circular", 1.0, 0.85, nt, 0.003)["Q"]
                c += qc < qt
        return c
    assert frac(0.009, 0.011) == pytest.approx(390, abs=441 * 0.05)
    assert frac(0.011, 0.015) == pytest.approx(210, abs=441 * 0.05)


def test_acervo_delmiro_d1_secao_menor_que_tirante():
    # caso negativo D1 (acervo, sem h): DT-2.23.1, Q 0,120, Io 0,00352, ZTT01 b 0,20 h 0,20 z 1, n 0,025
    yn = C.profundidade_normal(0.120, 0.2, 1, 0.025, 0.00352)
    assert yn == pytest.approx(0.331, rel=0.05)
    v = C.verificar_secao(yn, 0.20)
    assert v["transborda"] and not v["ok"]
    assert v["folga"] == pytest.approx(-0.131, rel=0.05)
    assert any("transborda" in a for a in v["avisos"])


def test_verificar_trechos_percentual_fora_do_criterio():
    trechos = [
        {"nome": "DT-2.23.1", "Q": 0.120, "b": 0.2, "z": 1, "n": 0.025, "S": 0.00352, "h": 0.20},
        {"nome": "DS-1.1/C", "Q": 0.518, "b": 0.6, "z": 1.5, "n": 0.025, "S": 0.00368, "h": 0.45},
        {"nome": "folgado", "Q": 0.518, "b": 0.6, "z": 1.5, "n": 0.025, "S": 0.00368, "h": 0.80},
    ]
    r = C.verificar_trechos(trechos)
    assert r["n_transbordam"] == 1
    assert r["n_falhas"] == 2          # transborda + folga 0,02 < 0,11
    assert r["pct_falhas"] == pytest.approx(200 / 3)
    assert [t["ok"] for t in r["trechos"]] == [False, False, True]


# ---------------------------------------------------------------- (c) consistencia
def test_normal_inverte_manning():
    for b, z in ((0.0, 1.5), (1.0, 0.0), (3.0, 2.0)):
        if b == 0:
            b = 1e-9  # triangular: b = 0 e permitido com z > 0
        y = C.profundidade_normal(2.0, b, z, 0.03, 0.002)
        assert C.manning_trapezoidal(b, z, y, 0.03, 0.002)["Q"] == pytest.approx(2.0, rel=1e-6)


def test_critica_retangular_e_fr_unitario():
    Q, b = 3.0, 2.0
    yc = C.profundidade_critica(Q, b, 0)
    assert yc == pytest.approx(((Q / b) ** 2 / 9.81) ** (1 / 3), rel=1e-6)
    # Fr = 1 na profundidade critica de secao trapezoidal (com A/T)
    yc = C.profundidade_critica(2.0, 1.0, 1.5)
    A, _, T = C.geometria_trapezio(1.0, 1.5, yc)
    assert (2.0 / A) / math.sqrt(9.81 * A / T) == pytest.approx(1.0, rel=1e-6)


def test_regime_supercritico_e_aviso_instavel():
    r = C.canal_trapezoidal(2.0, 1.0, 1.5, 0.015, 0.05)
    assert r["regime"] == "supercritico" and r["yn"] < r["yc"]
    # Fr proximo de 1 (0,89-1,13): aviso de HEC-11 p. 38
    S = 0.0125
    # procura declividade com Fr ~ 1 por bissecao simples
    lo, hi = 0.001, 0.05
    for _ in range(60):
        S = 0.5 * (lo + hi)
        fr = C.canal_trapezoidal(2.0, 1.0, 1.5, 0.015, S)["Fr"]
        lo, hi = (S, hi) if fr < 1 else (lo, S)
    assert any("0,89" in a for a in C.canal_trapezoidal(2.0, 1.0, 1.5, 0.015, S)["avisos"])


def test_composto_equivale_ao_simples_sem_berma_molhada():
    r = C.manning_composto(0.8, 2.0, 1.5, 0.03, 0.002, 1.0, 3.0, 2.0, 0.05)
    s = C.manning_trapezoidal(2.0, 1.5, 0.8, 0.03, 0.002)
    assert r["Q"] == pytest.approx(s["Q"], rel=1e-9)
    assert r["Fr"] == pytest.approx(s["Fr"], rel=1e-9)
    assert any("bermas secas" in a for a in r["avisos"])


def test_composto_com_berma_aumenta_capacidade_e_inverte():
    h = 1.0
    cheio = C.manning_trapezoidal(2.0, 1.5, h, 0.03, 0.002)["Q"]
    r = C.manning_composto(1.5, 2.0, 1.5, 0.03, 0.002, h, 3.0, 2.0, 0.05)
    assert r["Q"] > cheio
    # com n_berma = n, a secao dividida pelo menos supera o canal sozinho e Fr usa A/T da secao toda
    assert r["Fr"] == pytest.approx(r["V"] / math.sqrt(9.81 * r["A"] / r["T"]), rel=1e-12)
    y = C.profundidade_normal_composta(r["Q"], 2.0, 1.5, 0.03, 0.002, h, 3.0, 2.0, 0.05)
    assert y == pytest.approx(1.5, rel=1e-5)


def test_composto_aviso_lamina_rasa_na_berma_em1601_p60():
    # Revisao F5: EM-1601 p. 60 (James e Brown 1977): 1,0 < y/h_main < 1,4 -> Manning impreciso sem ajuste
    raso = C.manning_composto(1.2, 2.0, 1.5, 0.03, 0.002, 1.0, 3.0, 2.0, 0.05)
    fundo = C.manning_composto(1.6, 2.0, 1.5, 0.03, 0.002, 1.0, 3.0, 2.0, 0.05)
    assert any("James e Brown" in a for a in raso["avisos"])
    assert not any("James e Brown" in a for a in fundo["avisos"])


def test_velocidade_admissivel_dnit_e_em1601_divergem():
    d = C.velocidade_admissivel("areia_fina", "dnit", "min")
    assert d["V_adm"] == pytest.approx(0.30)
    e = C.velocidade_admissivel("areia_fina", "em1601")
    assert e["V_adm"] == pytest.approx(2.0 * FT, rel=1e-9)
    assert e["V_adm"] > 1.5 * d["V_adm"]   # Tab. 2-5 do EM-1601 mais permissiva que a Tab. 31 do DNIT
    assert C.velocidade_admissivel("terra_argila", "em1601")["V_adm"] == pytest.approx(6.0 * FT)
    assert C.velocidade_admissivel("concreto", "dnit")["V_adm"] == pytest.approx(4.5)
    assert C.velocidade_admissivel("bermuda_silte_arenoso", "em1601")["avisos"]
    with pytest.raises(ValueError):
        C.velocidade_admissivel("xyz", "em1601")
    with pytest.raises(ValueError):
        C.velocidade_admissivel("concreto", "outra")


def test_verificar_velocidade_vmin_sem_padrao():
    r = C.verificar_velocidade(0.29, 1.2)
    assert r["ok"] and any("V_min" in a for a in r["avisos"])
    r = C.verificar_velocidade(0.29, 1.2, V_min=0.5)   # DT-2.26.2 de Delmiro (0,292 m/s)
    assert not r["ok"] and r["avisos"] == []


def test_salitre_n2_dois_limites_de_velocidade():
    # DS-4.1/A V = 1,307: reprova com 1,2 (memorial) e passa com 1,5 (planilha)
    V = C.capacidade_trapezoidal(56.0, 1.5, 1.5, 0.030, 0.00096)["V"]
    r = C.verificar_limites_alternativos(V, [1.2, 1.5])
    assert r["conflito"] and r["resultado"] == {"1.2": False, "1.5": True}
    assert r["avisos"]
    assert not C.verificar_limites_alternativos(0.8, [1.2, 1.5])["conflito"]


def test_salitre_n1_reconciliacao_de_extensoes():
    parcelas = {"Mulungu": 2026.00, "Recreio": 51533.65, "Tourao": 21324.76}
    r = C.reconciliar_extensoes(parcelas, 72858.41)
    assert not r["fecha"]
    assert r["soma"] == pytest.approx(74884.41, abs=0.005)
    assert r["diferenca"] == pytest.approx(2026.00, abs=0.005)
    assert r["parcela_omitida"] == "Mulungu"
    ok = C.reconciliar_extensoes([2026.00, 51533.65, 21324.76], 74884.41)
    assert ok["fecha"] and ok["avisos"] == []


def test_borda_livre_provisoria_25_pct():
    r = C.borda_livre(0.43)
    assert r["folga_min"] == pytest.approx(0.1075) and r["altura_min"] == pytest.approx(0.5375)
    assert any("provisorio" in a for a in r["avisos"])
    assert C.borda_livre(0.43, 0.3)["avisos"] == []


def test_entradas_invalidas():
    with pytest.raises(ValueError):
        C.profundidade_normal(-1, 1, 1, 0.03, 0.001)
    with pytest.raises(ValueError):
        C.manning_trapezoidal(1, 1, 0.5, 0.0, 0.001)
    with pytest.raises(ValueError):
        C.manning_trapezoidal(0, 0, 0.5, 0.03, 0.001)
    with pytest.raises(ValueError):
        C.verificar_secao(0.0, 0.5)
    with pytest.raises(ValueError):
        C.d50_riprap_hec11(3.0, 3.0)  # sem K1 nem (z, phi)


def test_cli_json():
    cmd = [sys.executable, "-m", "tools.dren.canais_drenagem", "--json",
           json.dumps({"funcao": "canal_trapezoidal", "Q": 0.518, "b": 0.6, "z": 1.5, "n": 0.025, "S": 0.00368})]
    out = subprocess.run(cmd, cwd=RAIZ, capture_output=True, text=True, encoding="utf-8", check=True,
                         stdin=subprocess.DEVNULL, env=dict(os.environ, PYTHONIOENCODING="utf-8")).stdout
    d = json.loads(out)
    assert d["versao"] == C.VERSAO
    assert d["saidas"]["yn"] == pytest.approx(0.43, rel=0.05)
    assert set(d) >= {"entradas", "saidas", "metodo", "avisos", "versao"}
    cmd = [sys.executable, "-m", "tools.dren.canais_drenagem", "--listar"]
    lst = json.loads(subprocess.run(cmd, cwd=RAIZ, capture_output=True, text=True, check=True,
                                    stdin=subprocess.DEVNULL).stdout)
    assert "d50_riprap_hec11" in lst["funcoes"]
