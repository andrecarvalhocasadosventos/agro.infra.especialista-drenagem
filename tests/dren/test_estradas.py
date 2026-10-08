"""Testes de tools.dren.estradas.

(a) livro: HEC-12 (gabaritos 4-7 do mapa, 1 %; nomograma 5 %), consistencia do IME;
(b) acervo SEM check humano (check-h): Xingo Lote I VPC-1 (5 %), rotulados "acervo, sem check-h".
Divergencia > 5 % => xfail(strict=True) (nenhuma ocorreu neste modulo).
"""
import json
import math
import os
import subprocess
import sys

import pytest

from tools.dren import estradas as E

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
FT = 0.3048
CONTRIB_VPC1 = [(0.9, 0.60), (0.3, 10.0)]


# ---------------------------------------------------------------- (a) livro
def test_hec12_gabarito4_gutter_triangular():
    # HEC-12 p. 41 Ex. 4: T 8 ft, Sx 0,025, S 0,01, n 0,015 -> Q = 2,0 ft3/s
    q = E.sarjeta_triangular(0.025, 0.01, 0.015, T=8 * FT)["saidas"]["Q_m3s"]
    assert q / FT**3 == pytest.approx(2.0, rel=0.01)


def test_hec12_gabarito5_nomograma():
    # HEC-12 p. 40: n 0,016, Sx 0,03, S 0,04, T 6 ft -> Q = 2,4 ft3/s
    q = E.sarjeta_triangular(0.03, 0.04, 0.016, T=6 * FT)["saidas"]["Q_m3s"]
    assert q / FT**3 == pytest.approx(2.4, rel=0.01)


def test_hec12_gabarito6_espalhamento():
    # HEC-12 p. 46 Ex. 6: Q 3,0 ft3/s -> T = 12 ft impresso (Chart 3), 11,6 recalculado; tolerancia 5 %
    t = E.sarjeta_triangular(0.025, 0.003, 0.015, Q=3.0 * FT**3)["saidas"]["T_m"]
    assert t / FT == pytest.approx(12.0, rel=0.05)
    assert t / FT == pytest.approx(11.6, rel=0.01)


def test_hec12_gabarito7_composta():
    # HEC-12 p. 41-43 Ex. 5: T 8 ft, Sx 0,025, depressao 2 in em W = 2 ft (Sw 0,108), S 0,01, n 0,015
    # impresso Eo = 0,69 (Chart 4, grafico) e Q = 3,0 ft3/s (reproduz-se 3,06 com Eo 0,69): 5 %
    r = E.sarjeta_composta(0.025, 0.025 + (2 / 12) / 2, 2 * FT, 0.015, 0.01, T=8 * FT)["saidas"]
    assert r["Eo"] == pytest.approx(0.69, rel=0.02)
    assert r["Q_m3s"] / FT**3 == pytest.approx(3.0, rel=0.05)
    assert r["Qw_m3s"] / FT**3 == pytest.approx(2.1, rel=0.05)


def test_composta_inverte_e_limite_triangular():
    r = E.sarjeta_composta(0.025, 0.108, 0.6, 0.015, 0.01, Q=0.08)["saidas"]
    r2 = E.sarjeta_composta(0.025, 0.108, 0.6, 0.015, 0.01, T=r["T_m"])["saidas"]
    assert r2["Q_m3s"] == pytest.approx(0.08, rel=1e-6)
    # Sw -> Sx: recupera Izzard triangular
    tri = E.sarjeta_triangular(0.025, 0.01, 0.015, T=2.4)["saidas"]["Q_m3s"]
    comp = E.sarjeta_composta(0.025, 0.02500001, 0.5, 0.015, 0.01, T=2.4)["saidas"]["Q_m3s"]
    assert comp == pytest.approx(tri, rel=0.01)  # Izzard usa 1,67/2,67 arredondados; integral exata usa 5/3, 8/3


def test_manning_trapezoidal_roundtrip_e_froude():
    r = E.valeta_manning(0.5, 1.5, 0.016, 0.01, y=0.3)["saidas"]
    r2 = E.valeta_manning(0.5, 1.5, 0.016, 0.01, Q=r["Q_m3s"])["saidas"]
    assert r2["y_m"] == pytest.approx(0.3, rel=1e-6)
    assert r["Froude"] == pytest.approx(r["V_m_s"] / math.sqrt(9.81 * r["A_m2"] / r["T_m"]), rel=1e-9)  # A/T, nunca y


def test_manning_retangular_conferido_a_mao():
    # b 1 m, y 0,5 m, n 0,013, S 0,002: A 0,5; P 2; R 0,25
    q = E.valeta_manning(1.0, 0.0, 0.013, 0.002, y=0.5)["saidas"]["Q_m3s"]
    assert q == pytest.approx(0.5 * 0.25 ** (2 / 3) * math.sqrt(0.002) / 0.013, rel=1e-9)


def test_dreno_profundo_scobey_hazen_consistentes():
    # IME p. 83: 0,2113 = 0,269 pi/4 (tubo cheio); Scobey e HW concordam em ~10 % (D 0,2 m, I 1 %)
    s = E.dreno_profundo_capacidade(0.2, 0.01, metodo="scobey")["saidas"]
    h = E.dreno_profundo_capacidade(0.2, 0.01, metodo="hazen")["saidas"]
    assert 0.2113 == pytest.approx(0.269 * math.pi / 4, rel=2e-3)
    assert s["Q_cheio_m3s"] == pytest.approx(s["V_cheio_m_s"] * math.pi * 0.2**2 / 4, rel=1e-9)
    assert s["Q_cheio_m3s"] == pytest.approx(h["Q_cheio_m3s"], rel=0.10)
    assert any("meia" in a for a in E.dreno_profundo_capacidade(0.2, 0.01)["avisos"])


def test_dreno_profundo_comprimento_e_contribuicao():
    q = E.dreno_profundo_contribuicao(1e-4, 1.5, 0.5, 20.0)["saidas"]["q_por_m_m3s_m"]
    assert q == pytest.approx(1e-4 * (2.25 - 0.25) / 40.0, rel=1e-12)
    cap = E.dreno_profundo_capacidade(0.2, 0.01)["saidas"]["Q_cheio_m3s"]
    L = E.dreno_profundo_comprimento_critico(0.2, 0.01, 2 * q)["saidas"]["L_critico_m"]
    assert L == pytest.approx(cap / (2 * q), rel=1e-9)
    L2 = E.dreno_profundo_comprimento_critico(0.2, 0.01, 2 * q, fator_capacidade=0.5)["saidas"]["L_critico_m"]
    assert L2 == pytest.approx(L / 2, rel=1e-9)


def test_caixa_coletora_grelha_hec12_p86():
    r = E.caixa_coletora_grelha(P=2.0, A=0.5, d=0.1)["saidas"]
    assert r["Q_vertedor_m3s"] == pytest.approx(1.66 * 2.0 * 0.1**1.5, rel=1e-9)
    assert r["Q_orificio_m3s"] == pytest.approx(0.67 * 0.5 * math.sqrt(2 * 9.81 * 0.1), rel=1e-9)
    assert r["Q_capacidade_m3s"] == min(r["Q_vertedor_m3s"], r["Q_orificio_m3s"])
    inv = E.caixa_coletora_grelha(P=2.0, A=0.5, Q=r["Q_capacidade_m3s"])["saidas"]
    assert inv["d_necessario_m"] == pytest.approx(0.1, rel=1e-6)


def test_caixa_coletora_grelha_aviso_transicao_hec12_p87():
    # Revisao F5: HEC-12 p. 87: na transicao vertedor-orificio a capacidade e menor que as duas equacoes
    P, A = 2.0, 0.5
    d_int = (0.67 * A * math.sqrt(2 * 9.81) / (1.66 * P)) ** 2
    perto = E.caixa_coletora_grelha(P=P, A=A, d=d_int)
    longe = E.caixa_coletora_grelha(P=P, A=A, d=0.2 * d_int)
    assert any("p. 87" in a and "MENOR" in a for a in perto["avisos"])
    assert not any("faixa de transicao" in a for a in longe["avisos"])
    inv = E.caixa_coletora_grelha(P=P, A=A, Q=perto["saidas"]["Q_capacidade_m3s"])
    assert any("faixa de transicao" in a for a in inv["avisos"])


def test_folga_ime():
    assert E.folga_valeta(0.5, Q=0.1)["saidas"]["folga_m"] == pytest.approx(0.1)
    assert E.folga_valeta(0.5, Q=0.3, revestimento="concreto")["saidas"]["folga_m"] == 0.13
    with pytest.raises(ValueError):
        E.folga_valeta(0.5, Q=1.0)  # formula EQ 4.7 ilegivel


def test_criterio_projeto_padrao_provisorio():
    r = E.criterio_projeto(3.0)
    assert r["saidas"]["tc_adotado_min"] == 5.0 and r["saidas"]["TR_anos"] == 10
    assert "decisao F7" in r["avisos"][0]
    assert E.criterio_projeto(3.0, tc_min=10)["saidas"]["tc_adotado_min"] == 10
    assert E.criterio_projeto(12.0)["saidas"]["tc_adotado_min"] == 12.0


def test_validacoes():
    with pytest.raises(ValueError):
        E.valeta_manning(0.2, 1, 0.016, 0.01)  # sem y nem Q
    with pytest.raises(ValueError):
        E.sarjeta_triangular(0.02, 0.01, 0.016)
    with pytest.raises(ValueError):
        E.vazao_por_metro(100, [(1.5, 1.0)])
    with pytest.raises(ValueError):
        E.valeta_comprimento_critico(0.2, 1, 0.2, 0.016, 0.01, 100, CONTRIB_VPC1, hmax=0.3)


def test_aviso_declividade_minima():
    av = E.valeta_manning(0.2, 1, 0.016, 0.001, y=0.16)["avisos"]
    assert any("0,3" in a for a in av)


# ---------------------------------------------------------------- (b) acervo, sem check-h
@pytest.mark.parametrize("i,L", [(0.001, 162.54), (0.010, 514.00), (0.050, 1149.34), (0.060, 1259.04)])
def test_xingo_vpc1_acervo_sem_checkh(i, L):
    # Xingo Lote I doc 1419 p. 66: VPC-1 b 0,20, topo 0,60 (z = 1), h 0,20, hmax 0,16, n 0,016,
    # I = 2,353 mm/min (141,18 mm/h), C 0,9x0,60 + 0,3x10,00. Acervo, sem check-h; 5 %.
    r = E.valeta_comprimento_critico(0.2, 1.0, 0.2, 0.016, i, 2.353 * 60, CONTRIB_VPC1, hmax=0.16)["saidas"]
    assert r["L_critico_m"] == pytest.approx(L, rel=0.05)


def test_xingo_vpc1_vazao_por_metro_e_velocidade():
    # acervo, sem check-h: Qrac/m = 0,0001388; v(0,001) = 0,392 m/s; Q(0,001) = 0,023
    assert E.vazao_por_metro(2.353 * 60, CONTRIB_VPC1) == pytest.approx(0.0001388, rel=0.01)
    r = E.valeta_comprimento_critico(0.2, 1.0, 0.2, 0.016, 0.001, 2.353 * 60, CONTRIB_VPC1, hmax=0.16)["saidas"]
    assert r["V_m_s"] == pytest.approx(0.392, rel=0.01)
    assert r["Q_cap_m3s"] == pytest.approx(0.023, rel=0.05)


def test_xingo_razao_de_chuvas():
    # acervo, sem check-h: I 1,789 mm/min => L(0,001) = 213,76 m (razao 2,353/1,789)
    r = E.valeta_comprimento_critico(0.2, 1.0, 0.2, 0.016, 0.001, 1.789 * 60, CONTRIB_VPC1, hmax=0.16)["saidas"]
    assert r["L_critico_m"] == pytest.approx(213.76, rel=0.05)


def test_xingo_vpc7_hmax_08h_capacidade_maior_que_documento():
    # acervo, sem check-h (ponto de atencao 1): VPC-7 h 0,40, topo 1,20 (b 0,40, z 1): hmax = 0,8 h = 0,32 m
    # deve dar capacidade > 0,083 m3/s (valor do documento, que repete hmax 0,24 m)
    r = E.valeta_comprimento_critico(0.4, 1.0, 0.4, 0.016, 0.001, 2.353 * 60, CONTRIB_VPC1)
    assert r["saidas"]["Q_cap_m3s"] > 0.083
    assert any("0,8 h" in a for a in r["avisos"])


def test_tr_e_tc_sao_argumentos_com_aviso():
    r = E.valeta_comprimento_critico(0.2, 1.0, 0.2, 0.016, 0.01, 141.18, CONTRIB_VPC1, TR=25, tc_min=10)
    assert r["entradas"]["TR"] == 25 and r["entradas"]["tc_min"] == 10
    assert "decisao F7" in r["avisos"][0]


# ---------------------------------------------------------------- CLI
def test_cli_valeta_comprimento_critico():
    args = {"funcao": "valeta_comprimento_critico", "b": 0.2, "z": 1.0, "h": 0.2, "n": 0.016, "i": 0.001,
            "I_mm_h": 141.18, "contribuicoes": [[0.9, 0.6], [0.3, 10.0]], "hmax": 0.16}
    p = subprocess.run([sys.executable, "-m", "tools.dren.estradas", "--json", json.dumps(args)],
                       capture_output=True, text=True, cwd=RAIZ, encoding="utf-8", stdin=subprocess.DEVNULL)
    assert p.returncode == 0, p.stderr
    out = json.loads(p.stdout)
    assert out["versao"] == E.VERSAO and out["avisos"] and out["metodo"]
    assert out["saidas"]["L_critico_m"] == pytest.approx(162.54, rel=0.05)
