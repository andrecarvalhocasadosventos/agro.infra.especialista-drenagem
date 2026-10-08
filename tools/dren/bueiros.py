"""Bueiros: controle de entrada, controle de saida e dimensionamento.

Base: FHWA HDS-5, Hydraulic Design of Highway Culverts, 3a ed. (FHWA-HIF-12-026,
2012): cap. 3 (secoes de controle de entrada/saida, eqs. 3.1 a 3.4) e Apendice A
(equacoes de regressao de controle de entrada: eqs. A.1 a A.3 e Tabela A.1,
PDF p.190-198 do exemplar em referencias/08_FHWA); Apendice C, Tabela C.2
(coeficientes de perda de entrada Ke). As constantes K, M, c, Y foram conferidas
contra a Tabela A.1 (e A.2 para arcos de chapa corrugada).

SI em toda a interface: Q [m3/s], dimensoes [m], declividade [m/m], HW [m]
acima da geratriz inferior (invert) da secao de controle. n_celulas divide Q
igualmente entre barris iguais.

Metodos legados do acervo (Baixio de Irece, CSB, Xingo): verificacao por
orificio (Q = Cd*A*sqrt(2 g h), Cd = 0,62) e por Manning em secao plena/lamina
fixa. Mantidos para comparacao com o HDS-5 (funcao comparar_legado_hds5); nao
sao recomendados como metodo principal (ignoram contracao de entrada, perdas
de entrada/saida e a transicao entre regimes).

CLI: python -m tools.dren.bueiros --json '{"funcao": "controle_de_entrada", ...}'

CHANGELOG
0.3.0 (2026-10-08), fase F5:
- tubo_parcialmente_cheio: Manning circular por geometria exata (segmento circular), com y/D,
  Fr = V/sqrt(g A/T) (profundidade hidraulica, nunca y) e limite y/D como argumento
  (padrao provisorio 0,75, criterio do acervo Delmiro 1492:164; decisao F7). Reproduz
  BUC-2..5 do caso Delmiro (TR 20 e TR 50) sem ajuste.
- regime_critico_tubular_ime: regime critico do tubular com Ec = D (IME p. 151-152,
  theta_c = 4,0335 rad, A_c = 0,601 D2, Vc = 2,56 D^0,5, Ic = 32,82 n2/D^(1/3)). A_c = 0,60 D2
  do legado DNIT deixa de ser "ajuste proprio": e a formula impressa do IME arredondada
  (0,2 %); valor numerico de vazao_critica_legado_dnit mantido.
- Testes novos: V de saida do HDS-5 p. 280 (6,47 m/s), HDS-3 Ex. 10-17 (circular parcial),
  Delmiro, Xingo legado = n 0,0093 (caso negativo). Classe de tubo: ver tubos.py.
0.2.0 (2026-10-01), conforme achados da skill bueiros-e-drenagem-superficial:
- dissipador_necessario passa a usar a Tabela 31 do DNIT-DREN (IPR-724, p. 131)
  por padrao (LIMITE_VELOCIDADE_DNIT, faixas min-max; criterio "min" = conservador);
  a tabela simplificada anterior fica em LIMITE_VELOCIDADE_MATERIAL_LEGADO
  (alias LIMITE_VELOCIDADE_MATERIAL mantido) e e usada so com fonte="legado" ou
  para materiais sem equivalente no DNIT (cascalho_grosso, enrocamento; com aviso).
- Aviso de afastamento entre celulas em dimensionar_bueiro cita DNIT-ES023 p. 4
  (folga 0,30 m entre tubos; 0,40 m lateral) e DNIT-ES025 p. 5 (0,50 m lateral)
  em vez da fonte inexistente "HDS-5/HEC-14".
- Parametro opcional fonte_ke="hds5"|"dnit" (padrao hds5) em dimensionar_bueiro e
  comparar_legado_hds5; ke_entrada(). Muro de ala paralelo: HDS-5 p. 216 = 0,7;
  DNIT-DREN p. 130 (Tab. 30) = 0,2 (DIVERGENCIAS.md).
- vazao_critica_legado_dnit (Tabelas 1 e 2 do DNIT-DREN p. 55-56; Vc = 2,56 D^0,5,
  ~7 % acima da exata no tubular) e vazao_critica_exata.
- sarjeta_triangular_izzard (HEC-22 p. 79-80, eqs. 5.2 e 5.4, Ku = 0,376 SI).
- Constante Y da linha arco_corrugado_projetante: mantida a da Tabela A.2 (0,57,
  HDS-5 p. 198); o exemplo A.3.1 (p. 191) usa 0,53 (DIVERGENCIAS.md).
0.1.0: versao inicial (HDS-5 controle de entrada/saida, dimensionamento, legados).
"""
from __future__ import annotations

import argparse
import json
import math
import sys

VERSAO = "0.3.0"
G = 9.81
KU_SI = 1.811  # HDS-5 Eq. A.1-A.3 (conversao para SI)
KU_ATRITO_SI = 19.63  # HDS-5 Eq. 3.4b (29 em unidades inglesas)
X_NAO_SUBMERSA_MAX = 3.5  # Ku*Q/(A*D^0.5) ate o qual vale a eq. nao submersa
X_SUBMERSA_MIN = 4.0  # a partir do qual vale a eq. submersa

# --------------------------------------------------------------------------
# Constantes de controle de entrada (HDS-5 Tabela A.1 / A.2)
# forma: 1 -> HW/D = Hc/D + K X^M + Ks S ; 2 -> HW/D = K X^M ; X = Ku Q/(A D^0.5)
# submersa: HW/D = c X^2 + Y + Ks S ; Ks = -0.5 (mitrado: +0.7)
# --------------------------------------------------------------------------
ENTRADAS = {
    # circular de concreto (Chart 1)
    "circ_concreto_aresta_viva_muro": dict(forma="circular", eq=1, K=0.0098, M=2.0, c=0.0398, Y=0.67, Ke=0.5, mitrado=False, chart="1/1"),
    "circ_concreto_boca_sino_muro": dict(forma="circular", eq=1, K=0.0018, M=2.0, c=0.0292, Y=0.74, Ke=0.2, mitrado=False, chart="1/2"),
    "circ_concreto_boca_sino_projetante": dict(forma="circular", eq=1, K=0.0045, M=2.0, c=0.0317, Y=0.69, Ke=0.2, mitrado=False, chart="1/3"),
    # circular corrugado (Chart 2)
    "circ_corrugado_muro": dict(forma="circular", eq=1, K=0.0078, M=2.0, c=0.0379, Y=0.69, Ke=0.5, mitrado=False, chart="2/1"),
    "circ_corrugado_mitrado": dict(forma="circular", eq=1, K=0.0210, M=1.33, c=0.0463, Y=0.75, Ke=0.7, mitrado=True, chart="2/2"),
    "circ_corrugado_projetante": dict(forma="circular", eq=1, K=0.0340, M=1.50, c=0.0553, Y=0.54, Ke=0.9, mitrado=False, chart="2/3"),
    # circular com chanfro/bisel (Chart 3)
    "circ_bisel_45": dict(forma="circular", eq=1, K=0.0018, M=2.50, c=0.0300, Y=0.74, Ke=0.2, mitrado=False, chart="3/A"),
    "circ_bisel_33_7": dict(forma="circular", eq=1, K=0.0018, M=2.50, c=0.0243, Y=0.83, Ke=0.2, mitrado=False, chart="3/B"),
    # retangular de concreto (Charts 8 e 10)
    "ret_alas_30_75": dict(forma="retangular", eq=1, K=0.026, M=1.0, c=0.0347, Y=0.81, Ke=0.4, mitrado=False, chart="8/1"),
    "ret_alas_90_15": dict(forma="retangular", eq=1, K=0.061, M=0.75, c=0.0400, Y=0.80, Ke=0.5, mitrado=False, chart="8/2"),
    "ret_alas_0": dict(forma="retangular", eq=1, K=0.061, M=0.75, c=0.0423, Y=0.82, Ke=0.7, mitrado=False, chart="8/3"),
    "ret_muro_chanfro_3_4": dict(forma="retangular", eq=2, K=0.515, M=0.667, c=0.0375, Y=0.79, Ke=0.5, mitrado=False, chart="10/1"),
    "ret_muro_bisel_45": dict(forma="retangular", eq=2, K=0.495, M=0.667, c=0.0314, Y=0.82, Ke=0.2, mitrado=False, chart="10/2"),
    # arco/pipe-arch corrugado (Tabela A.2, charts 41-43, FHWA 1974)
    "arco_corrugado_muro": dict(forma="arco", eq=1, K=0.0083, M=2.0, c=0.0379, Y=0.69, Ke=0.5, mitrado=False, chart="41-43/1"),
    "arco_corrugado_mitrado": dict(forma="arco", eq=1, K=0.0300, M=1.0, c=0.0473, Y=0.75, Ke=0.7, mitrado=True, chart="41-43/2"),
    "arco_corrugado_projetante": dict(forma="arco", eq=1, K=0.0340, M=1.5, c=0.0496, Y=0.57, Ke=0.9, mitrado=False, chart="41-43/3"),
}

# Ke do DNIT (IPR-724, Tabela 30, DNIT-DREN p. 130) onde difere do HDS-5 (Tabela C.2,
# p. 216) para as chaves de ENTRADAS: muros de ala paralelos (caixa), geratriz reta.
KE_DNIT_DIFERENTE = {"ret_alas_0": 0.2}
FONTES_KE = ("hds5", "dnit")

# Velocidades maximas admissiveis para a agua [m/s], faixa (min, max):
# DNIT-DREN (IPR-724) Tabela 31, p. 131 (pagina fisica do PDF; impressa 127).
LIMITE_VELOCIDADE_DNIT = {
    "grama_comum": (1.50, 1.80),
    "tufos_grama_solo_exposto": (0.60, 1.20),
    "argila": (0.80, 1.30),
    "argila_coloidal": (1.30, 1.80),
    "lodo": (0.35, 0.85),
    "areia_fina": (0.30, 0.40),
    "areia_media": (0.35, 0.45),
    "cascalho_fino": (0.50, 0.80),
    "silte": (0.70, 1.20),
    "alvenaria_tijolos": (2.50, 2.50),
    "concreto": (4.50, 4.50),
    "aglomerados_consistentes": (2.00, 2.00),
    "revestimento_betuminoso": (3.00, 4.00),
}
FONTE_VELOCIDADE_DNIT = "DNIT-DREN (IPR-724) Tabela 31, p. 131"
# nomes da tabela antiga -> linha equivalente da Tabela 31 (None: sem equivalente)
_ALIAS_LEGADO_DNIT = {
    "areia_fina": "areia_fina", "silte_argiloso": "silte", "argila_rija": "argila",
    "cascalho_fino": "cascalho_fino", "cascalho_grosso": None, "grama": "grama_comum",
    "enrocamento": None, "concreto": "concreto",
}

# Velocidade media admissivel a jusante [m/s] (valores tipicos simplificados de
# Fortier & Scobey, via HEC-15/HEC-14 e DNIT IPR-724; CONFERIR antes de uso).
# LEGADO: ate 2x mais permissiva que a Tabela 31 do DNIT (areia, cascalho, concreto).
LIMITE_VELOCIDADE_MATERIAL_LEGADO = {
    "areia_fina": 0.75,
    "silte_argiloso": 0.9,
    "argila_rija": 1.4,
    "cascalho_fino": 1.5,
    "cascalho_grosso": 1.8,
    "grama": 1.8,
    "enrocamento": 3.0,
    "concreto": 6.0,
}
LIMITE_VELOCIDADE_MATERIAL = LIMITE_VELOCIDADE_MATERIAL_LEGADO  # alias de compatibilidade (0.1.0)


# --------------------------------------------------------------------------
# Geometria e hidraulica interna minima (Manning, profundidade critica)
# --------------------------------------------------------------------------
def _resultado(entradas, saidas, metodo, avisos):
    return {"entradas": entradas, "saidas": saidas, "metodo": metodo,
            "avisos": list(avisos), "versao": VERSAO}


def _geo(forma, dim):
    if forma == "circular":
        D = float(dim)
        if D <= 0:
            raise ValueError("D deve ser > 0")
        return {"forma": forma, "D": D, "B": D, "H": D}
    if forma in ("retangular", "arco"):
        B, H = (float(x) for x in dim)
        if B <= 0 or H <= 0:
            raise ValueError("B e H devem ser > 0")
        return {"forma": forma, "B": B, "H": H}
    raise ValueError("forma deve ser circular, retangular ou arco")


def area_cheia(g):
    if g["forma"] == "circular":
        return math.pi * g["D"] ** 2 / 4
    if g["forma"] == "retangular":
        return g["B"] * g["H"]
    return math.pi * g["B"] * g["H"] / 4  # arco ~ elipse (aproximacao)


def perimetro_cheio(g):
    if g["forma"] == "circular":
        return math.pi * g["D"]
    if g["forma"] == "retangular":
        return 2 * (g["B"] + g["H"])
    a, b = g["B"] / 2, g["H"] / 2  # Ramanujan
    return math.pi * (3 * (a + b) - math.sqrt((3 * a + b) * (a + 3 * b)))


def _secao(g, y):
    """(A, P, T) para lamina y (m); arco tratado como elipse (numerico)."""
    H = g["H"]
    y = min(max(y, 1e-9), H)
    if g["forma"] == "circular":
        D = g["D"]
        th = 2 * math.acos(1 - 2 * y / D)
        return D * D / 8 * (th - math.sin(th)), D * th / 2, D * math.sin(th / 2)
    if g["forma"] == "retangular":
        return g["B"] * y, g["B"] + 2 * y, g["B"]
    # elipse de semi-eixos B/2 (horizontal) e H/2 (vertical), centro em H/2
    n = 200
    a, b = g["B"] / 2, H / 2
    hw = lambda yy: a * math.sqrt(max(0.0, 1 - ((yy - b) / b) ** 2))
    dy = y / n
    xs = [hw(i * dy) for i in range(n + 1)]
    A = sum((xs[i] + xs[i + 1]) * dy for i in range(n))  # largura total = 2*x
    P = 2 * sum(math.hypot(dy, xs[i + 1] - xs[i]) for i in range(n))
    return A, P, 2 * xs[-1]


def manning_lamina(forma, dim, y, n, S0):
    """Escoamento uniforme (Manning) numa celula com lamina y [m].
    V = (1/n) R^(2/3) S0^(1/2); retorna dict A, P, R, V, Q, Froude.
    Formula de Manning (SI); validade: n 0,010-0,035; S0 > 0."""
    g = _geo(forma, dim)
    if n <= 0 or S0 <= 0:
        raise ValueError("n e S0 devem ser > 0")
    A, P, T = _secao(g, y)
    R = A / P
    V = R ** (2 / 3) * math.sqrt(S0) / n
    return {"A": A, "P": P, "R": R, "V": V, "Q": V * A, "Fr": V / math.sqrt(G * A / T)}


def manning_cheia(forma, dim, n, S0, n_celulas=1):
    """Capacidade em secao plena (Manning): Q = A R^(2/3) S0^(1/2) / n (total)."""
    g = _geo(forma, dim)
    A, P = area_cheia(g), perimetro_cheio(g)
    V = (A / P) ** (2 / 3) * math.sqrt(S0) / n
    return {"Q": V * A * n_celulas, "V": V, "A_total": A * n_celulas}


def profundidade_critica(Q_cel, forma, dim):
    """dc [m] por bissecao de Q^2/g = A^3/T. Se nao ha raiz < D, retorna D."""
    g = _geo(forma, dim)
    H = g["H"]
    f = lambda y: (lambda s: s[0] ** 3 / s[2] - Q_cel ** 2 / G)(_secao(g, y))
    if f(0.9995 * H) < 0:
        return H
    lo, hi = 1e-6, H
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if f(mid) < 0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def profundidade_normal(Q_cel, forma, dim, n, S0):
    """yn [m] (Manning). Retorna D (H) se Q >= capacidade plena."""
    g = _geo(forma, dim)
    H = g["H"]
    if Q_cel >= manning_cheia(forma, dim, n, S0)["Q"]:
        return H
    ymax = 0.82 * H if g["forma"] == "circular" else H
    lo, hi = 1e-6, ymax
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if manning_lamina(forma, dim, mid, n, S0)["Q"] < Q_cel:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def _carga_critica(Q_cel, g, forma, dim):
    dc = profundidade_critica(Q_cel, forma, dim)
    A, _, _ = _secao(g, dc)
    return dc + (Q_cel / A) ** 2 / (2 * G), dc


# --------------------------------------------------------------------------
# Controle de entrada
# --------------------------------------------------------------------------
def _hw_nao_submersa(Q_cel, g, forma, dim, c, S0):
    D, A = g["H"], area_cheia(g)
    X = KU_SI * Q_cel / (A * math.sqrt(D))
    Ks = 0.7 if c["mitrado"] else -0.5
    if c["eq"] == 1:
        Hc, _ = _carga_critica(Q_cel, g, forma, dim)
        r = Hc / D + c["K"] * X ** c["M"] + Ks * S0
    else:
        r = c["K"] * X ** c["M"]
    return r * D


def _hw_submersa(Q_cel, g, c, S0):
    D, A = g["H"], area_cheia(g)
    X = KU_SI * Q_cel / (A * math.sqrt(D))
    Ks = 0.7 if c["mitrado"] else -0.5
    return (c["c"] * X ** 2 + c["Y"] + Ks * S0) * D


def controle_de_entrada(Q, forma, dim, tipo_de_entrada, S0, n_celulas=1, detalhado=False):
    """Carga de montante HW [m] por controle de entrada (HDS-5, Apendice A).

    Nao submersa, Forma 1:  HW/D = Hc/D + K (Ku Q/(A D^0.5))^M + Ks S0    (A.1)
    Nao submersa, Forma 2:  HW/D = K (Ku Q/(A D^0.5))^M                     (A.2)
    Submersa:               HW/D = c (Ku Q/(A D^0.5))^2 + Y + Ks S0         (A.3)
    Ku = 1,811 (SI), Ks = -0,5 (mitrado: +0,7), Hc = dc + Vc^2/2g.
    Faixas: nao submersa ate X = Ku Q/(A D^0.5) = 3,5; submersa a partir de 4,0;
    na zona de transicao (3,5 < X < 4,0) interpola-se linearmente entre os dois
    pontos-limite (o HDS-5 traca uma curva tangente; a diferenca e pequena
    porque a zona e curta).
    forma: 'circular' (dim = D), 'retangular' ou 'arco' (dim = (B, H)).
    arco usa area de elipse (aproximacao; usar dimensoes do fabricante).
    Q total [m3/s]; dividido igualmente em n_celulas. HW acima do invert na
    entrada. Validade: S0 < ~0,10; constantes da Tabela A.1/A.2.
    """
    if tipo_de_entrada not in ENTRADAS:
        raise ValueError("tipo_de_entrada desconhecido; opcoes: " + ", ".join(ENTRADAS))
    c = ENTRADAS[tipo_de_entrada]
    if c["forma"] != forma:
        raise ValueError(f"tipo_de_entrada {tipo_de_entrada} e para forma {c['forma']}")
    if Q <= 0:
        raise ValueError("Q deve ser > 0")
    g = _geo(forma, dim)
    D, A = g["H"], area_cheia(g)
    Qc = Q / n_celulas
    X = KU_SI * Qc / (A * math.sqrt(D))
    avisos = []
    if X <= X_NAO_SUBMERSA_MAX:
        regime, hw = "nao_submersa", _hw_nao_submersa(Qc, g, forma, dim, c, S0)
    elif X >= X_SUBMERSA_MIN:
        regime, hw = "submersa", _hw_submersa(Qc, g, c, S0)
    else:
        regime = "transicao"
        Qu = X_NAO_SUBMERSA_MAX * A * math.sqrt(D) / KU_SI
        Qs = X_SUBMERSA_MIN * A * math.sqrt(D) / KU_SI
        hu = _hw_nao_submersa(Qu, g, forma, dim, c, S0)
        hs = _hw_submersa(Qs, g, c, S0)
        hw = hu + (hs - hu) * (Qc - Qu) / (Qs - Qu)
    if forma == "arco":
        avisos.append("arco: area de elipse adotada (aproximacao)")
    if S0 > 0.10:
        avisos.append("S0 > 10 %: fora da faixa de validade das regressoes")
    if not detalhado:
        return hw
    return _resultado(
        {"Q": Q, "forma": forma, "dim": dim, "tipo_de_entrada": tipo_de_entrada, "S0": S0,
         "n_celulas": n_celulas},
        {"HW_m": hw, "HW_sobre_D": hw / D, "X": X, "regime": regime, "constantes": c},
        "HDS-5 controle de entrada (Apendice A, eqs. A.1-A.3)", avisos)


# --------------------------------------------------------------------------
# Controle de saida
# --------------------------------------------------------------------------
def controle_de_saida(Q, forma, dim, n, Ke, L, S0, TW, n_celulas=1, detalhado=False):
    """Carga de montante HW [m] por controle de saida (equacao da energia).

    HW = ho + H - L*S0                                          (HDS-5 eq. 3.1)
    H  = (1 + Ke + KU n^2 L / R^1,33) V^2/2g = Ke V^2/2g + Hf + Ho   (eq. 3.4)
    Hf = 19,63 n^2 L / R^1,33 * V^2/2g (secao plena); Ho = V^2/2g (perda de
    saida, velocidade de jusante desprezada); R = A/P plena.
    ho = TW se TW >= D, senao max(TW, (dc + D)/2) (dc <= D). TW [m] acima do
    invert de saida. Q total, dividido em n_celulas.
    Validade: barril fluindo cheio. Se TW < D (saida livre) a equacao e uma
    aproximacao (HDS-5 cap. 3): avisa-se e recomenda-se perfil de remanso.
    Retorna HW em m acima do invert de entrada.
    """
    if min(Q, n, L) <= 0 or Ke < 0:
        raise ValueError("Q, n, L devem ser > 0 e Ke >= 0")
    g = _geo(forma, dim)
    D, A, P = g["H"], area_cheia(g), perimetro_cheio(g)
    Qc = Q / n_celulas
    V = Qc / A
    R = A / P
    hv = V * V / (2 * G)
    He = Ke * hv
    Hf = KU_ATRITO_SI * n ** 2 * L / R ** 1.33 * hv
    Ho = hv
    _, dc = _carga_critica(Qc, g, forma, dim)
    ho = TW if TW >= D else max(TW, (min(dc, D) + D) / 2)
    hw = ho + He + Hf + Ho - L * S0
    avisos = []
    if TW < D:
        avisos.append("saida livre (TW < D): equacao de energia e aproximada; "
                      "verificar perfil de remanso (HDS-5 cap. 3)")
    if hw < D:
        avisos.append("HW de saida < D: barril pode nao fluir cheio; resultado conservador/nao aplicavel")
    if dc >= D:
        avisos.append("dc >= D: bueiro funciona a seccao cheia criticamente")
    if forma == "arco":
        avisos.append("arco: area/perimetro de elipse (aproximacao)")
    if not detalhado:
        return hw
    return _resultado(
        {"Q": Q, "forma": forma, "dim": dim, "n": n, "Ke": Ke, "L": L, "S0": S0, "TW": TW,
         "n_celulas": n_celulas},
        {"HW_m": hw, "ho_m": ho, "dc_m": dc, "He_m": He, "Hf_m": Hf, "Ho_m": Ho, "V_m_s": V},
        "HDS-5 controle de saida (eqs. 3.1, 3.4)", avisos)


# --------------------------------------------------------------------------
# Velocidade de saida e dissipador
# --------------------------------------------------------------------------
def velocidade_de_saida(Q, forma, dim, n, S0, TW=0.0, n_celulas=1, controle="entrada"):
    """Velocidade na saida [m/s], lamina e Froude.

    Criterio adotado (aproximacao de HDS-5 cap. 4 / pratica do HY-8): barril
    cheio (yn >= D ou TW >= D) -> V = Q/A; declividade forte (yn < dc) -> lamina
    normal; declividade fraca -> lamina = max(dc, min(TW, D)) em controle de saida
    e max(dc, min(TW, yn)) em controle de entrada (yn se TW = 0).
    """
    g = _geo(forma, dim)
    Qc = Q / n_celulas
    D = g["H"]
    yn = profundidade_normal(Qc, forma, dim, n, S0)
    dc = profundidade_critica(Qc, forma, dim)
    if TW >= D or yn >= D:
        y = D
    elif yn < dc:
        y = yn
    elif controle == "saida":
        y = max(dc, min(TW, D))
    else:
        y = max(dc, min(TW, yn)) if TW > 0 else yn
    A, _, T = _secao(g, y)
    V = Qc / A
    return {"V_m_s": V, "lamina_m": y, "yn_m": yn, "dc_m": dc, "Fr": V / math.sqrt(G * A / T)}


def limite_velocidade(material_jusante, fonte="dnit", criterio="min"):
    """(limite [m/s], texto da fonte, avisos). fonte "dnit" (padrao): Tabela 31 do
    DNIT-DREN p. 131; criterio "min" (conservador) ou "max" da faixa. Aceita as
    chaves da Tabela 31 e as chaves da tabela antiga (mapeadas). fonte "legado":
    LIMITE_VELOCIDADE_MATERIAL_LEGADO."""
    if fonte not in ("dnit", "legado"):
        raise ValueError("fonte deve ser 'dnit' ou 'legado'")
    if criterio not in ("min", "max"):
        raise ValueError("criterio deve ser 'min' ou 'max'")
    m = material_jusante
    avisos = []
    if fonte == "dnit":
        chave = m if m in LIMITE_VELOCIDADE_DNIT else None
        if chave is None and m in _ALIAS_LEGADO_DNIT:
            chave = _ALIAS_LEGADO_DNIT[m]
            if chave is None:
                avisos.append(f"{m}: sem linha equivalente na Tabela 31 do DNIT; usado o limite legado "
                              "(HEC-14/15 simplificado; conferir)")
                return LIMITE_VELOCIDADE_MATERIAL_LEGADO[m], "legado (sem equivalente na Tab. 31 do DNIT)", avisos
            if m != chave:
                avisos.append(f"{m} mapeado para '{chave}' da Tabela 31 do DNIT")
        if chave is None:
            raise ValueError("material_jusante desconhecido; opcoes: "
                             + ", ".join(sorted(set(LIMITE_VELOCIDADE_DNIT) | set(LIMITE_VELOCIDADE_MATERIAL_LEGADO))))
        lo, hi = LIMITE_VELOCIDADE_DNIT[chave]
        return (lo if criterio == "min" else hi), f"{FONTE_VELOCIDADE_DNIT} ({chave}: {lo:g}-{hi:g} m/s, criterio {criterio})", avisos
    if m not in LIMITE_VELOCIDADE_MATERIAL_LEGADO:
        raise ValueError("material_jusante desconhecido; opcoes: " + ", ".join(LIMITE_VELOCIDADE_MATERIAL_LEGADO))
    return LIMITE_VELOCIDADE_MATERIAL_LEGADO[m], "tabela legada simplificada (Fortier-Scobey; nao e a do DNIT)", avisos


def dissipador_necessario(V, material_jusante, fonte="dnit", criterio="min"):
    """Indica se ha necessidade de dissipador/protecao: V > limite admissivel do
    material a jusante. Padrao: Tabela 31 do DNIT-DREN p. 131 (criterio "min" da
    faixa = conservador); fonte="legado" usa a tabela antiga. Nao substitui o
    dimensionamento de HEC-14 (Fr, bacia). Retorna tambem 'metodo' (cita a fonte)."""
    lim, texto, av = limite_velocidade(material_jusante, fonte, criterio)
    return {"necessario": V > lim, "V_m_s": V, "limite_m_s": lim, "material": material_jusante,
            "metodo": "limite de velocidade: " + texto, "avisos": av}


# --------------------------------------------------------------------------
# Dimensionamento
# --------------------------------------------------------------------------
def _catalogo_padrao(forma):
    if forma == "circular":
        return [(d, k) for d in (0.6, 0.8, 1.0, 1.2, 1.5, 1.8, 2.0, 2.5) for k in (1, 2, 3, 4)]
    return [((b, h), k) for (b, h) in ((1.0, 1.0), (1.5, 1.5), (2.0, 1.5), (2.0, 2.0),
                                       (2.5, 2.0), (2.5, 2.5), (3.0, 2.0), (3.0, 2.5), (3.0, 3.0))
            for k in (1, 2, 3, 4)]


def ke_entrada(tipo_de_entrada, fonte_ke="hds5"):
    """Ke de entrada. "hds5" (padrao): Tabela C.2, HDS-5 p. 216 (campo Ke de ENTRADAS).
    "dnit": Tabela 30 do DNIT-DREN p. 130; difere so em muros de ala paralelos
    (0,2 contra 0,7 do HDS-5; ver DIVERGENCIAS.md)."""
    if fonte_ke not in FONTES_KE:
        raise ValueError("fonte_ke deve ser 'hds5' ou 'dnit'")
    if tipo_de_entrada not in ENTRADAS:
        raise ValueError("tipo_de_entrada desconhecido; opcoes: " + ", ".join(ENTRADAS))
    if fonte_ke == "dnit":
        return KE_DNIT_DIFERENTE.get(tipo_de_entrada, ENTRADAS[tipo_de_entrada]["Ke"])
    return ENTRADAS[tipo_de_entrada]["Ke"]


def dimensionar_bueiro(Q, HW_max, TW, L, S0, n=0.015, forma="circular",
                       tipo_de_entrada="circ_concreto_aresta_viva_muro",
                       candidatas=None, Ke=None, material_jusante="argila_rija", v_max=None,
                       fonte_ke="hds5"):
    """HW controlante = max(entrada, saida) e alternativas que atendem HW_max.

    candidatas: lista de dicts {forma, dim, n_celulas[, tipo_de_entrada, n, Ke]}
    (dim = D ou (B,H)). Se None usa um catalogo padrao (circular DN 0,6-2,5 m;
    celulares 1x1 a 3x3 m; 1 a 4 celulas). Retorna dict padrao; saidas incluem
    'alternativas' (HW <= HW_max, ordenadas por area total) e 'melhor'.
    Ke padrao vem da Tabela C.2 do HDS-5 (campo Ke de ENTRADAS); fonte_ke="dnit"
    usa a Tabela 30 do DNIT-DREN p. 130 (muro de ala paralelo 0,2 em vez de 0,7).
    Velocidade de saida: ver velocidade_de_saida; dissipador conforme
    dissipador_necessario(material_jusante). v_max opcional gera aviso.
    """
    if fonte_ke not in FONTES_KE:
        raise ValueError("fonte_ke deve ser 'hds5' ou 'dnit'")
    avisos = []
    if candidatas is None:
        candidatas = [{"forma": forma, "dim": d, "n_celulas": k} for d, k in _catalogo_padrao(forma)]
    avals = []
    for cd in candidatas:
        f, dim, k = cd["forma"], cd["dim"], cd.get("n_celulas", 1)
        te = cd.get("tipo_de_entrada", tipo_de_entrada)
        if ENTRADAS[te]["forma"] != f:
            continue
        ke = cd.get("Ke", Ke if Ke is not None else ke_entrada(te, fonte_ke))
        nn = cd.get("n", n)
        hi = controle_de_entrada(Q, f, dim, te, S0, k)
        ho = controle_de_saida(Q, f, dim, nn, ke, L, S0, TW, k)
        hw = max(hi, ho)
        ctrl = "entrada" if hi >= ho else "saida"
        vs = velocidade_de_saida(Q, f, dim, nn, S0, TW, k, ctrl)
        g = _geo(f, dim)
        area = area_cheia(g) * k
        diss = dissipador_necessario(vs["V_m_s"], material_jusante)
        avisos.extend(a for a in diss["avisos"] if a not in avisos)
        avals.append({
            "forma": f, "dim": dim, "n_celulas": k, "tipo_de_entrada": te,
            "HW_entrada_m": hi, "HW_saida_m": ho, "HW_m": hw, "HW_sobre_D": hw / g["H"],
            "controle": ctrl, "V_saida_m_s": vs["V_m_s"], "Fr_saida": vs["Fr"],
            "area_total_m2": area, "dissipador": diss["necessario"],
            "atende": hw <= HW_max and (v_max is None or vs["V_m_s"] <= v_max),
        })
    alts = sorted([a for a in avals if a["atende"]], key=lambda a: (a["area_total_m2"], a["HW_m"]))
    if not alts:
        avisos.append("nenhuma alternativa atende HW_max; ampliar catalogo/numero de celulas")
    if any(a["n_celulas"] > 1 for a in alts[:1]):
        avisos.append("celulas paralelas: manter afastamento entre barris; tubular em vala: folga de 0,30 m "
                      "entre tubos e 0,40 m lateral por lado [DNIT-ES023 p. 4]; celular em vala: folga "
                      "lateral minima de 0,50 m por lado para as formas [DNIT-ES025 p. 5]. O HDS-5 nao "
                      "fixa afastamento")
    if TW < 0:
        avisos.append("TW < 0 ?")
    melhor = alts[0] if alts else None
    return _resultado(
        {"Q": Q, "HW_max": HW_max, "TW": TW, "L": L, "S0": S0, "n": n, "forma": forma,
         "tipo_de_entrada": tipo_de_entrada, "material_jusante": material_jusante},
        {"melhor": melhor, "alternativas": alts, "n_avaliadas": len(avals)},
        "HDS-5: HW = max(entrada, saida); Ke: " + ("HDS-5 Tab. C.2 p. 216" if fonte_ke == "hds5"
            else "DNIT-DREN Tab. 30 p. 130") + "; dissipador: " + FONTE_VELOCIDADE_DNIT, avisos)


# --------------------------------------------------------------------------
# Metodos legados (acervo: Baixio de Irece, CSB, Xingo)
# --------------------------------------------------------------------------
def verificacao_por_orificio(Q, A, Cd=0.62, h=None):
    """Orificio afogado (legado Baixio de Irece, doc 896:1): Q = Cd A sqrt(2 g h).
    Se h for None retorna h [m] = (Q/(Cd A))^2/2g, carga sobre o eixo (A = area
    total das celulas). Se Q for None e h dado retorna Q [m3/s]."""
    if h is None:
        return (Q / (Cd * A)) ** 2 / (2 * G)
    return Cd * A * math.sqrt(2 * G * h)


def hw_legado_orificio(Q, forma, dim, n_celulas=1, Cd=0.62):
    """HW [m] acima do invert pelo metodo legado: HW = H/2 + h (h sobre o eixo)."""
    g = _geo(forma, dim)
    return g["H"] / 2 + verificacao_por_orificio(Q, area_cheia(g) * n_celulas, Cd)


def verificacao_manning_plena(Q, forma, dim, n, S0, n_celulas=1):
    """Legado: capacidade em secao plena (Manning) vs Q."""
    c = manning_cheia(forma, dim, n, S0, n_celulas)
    return {"Q_cap_m3s": c["Q"], "V_m_s": c["V"], "relacao_Q_Qcap": Q / c["Q"], "atende": Q <= c["Q"]}


def comparar_legado_hds5(Q, forma, dim, tipo_de_entrada, n, L, S0, TW, n_celulas=1, Cd=0.62,
                         fonte_ke="hds5"):
    """Compara HW do metodo legado (orificio) com o HDS-5 (max entrada/saida)."""
    ke = ke_entrada(tipo_de_entrada, fonte_ke)
    hi = controle_de_entrada(Q, forma, dim, tipo_de_entrada, S0, n_celulas)
    ho = controle_de_saida(Q, forma, dim, n, ke, L, S0, TW, n_celulas)
    hw = max(hi, ho)
    hl = hw_legado_orificio(Q, forma, dim, n_celulas, Cd)
    return _resultado(
        {"Q": Q, "forma": forma, "dim": dim, "tipo_de_entrada": tipo_de_entrada},
        {"HW_legado_orificio_m": hl, "HW_hds5_m": hw, "HW_entrada_m": hi, "HW_saida_m": ho,
         "diferenca_relativa": (hl - hw) / hw},
        "legado (orificio Cd=0,62) x HDS-5", [
            "metodo legado ignora contracao/perdas de entrada e regime; comparar apenas como ordem de grandeza"])


# Legado DNIT: vazao critica (IPR-724, DNIT-DREN p. 54-56, Tabelas 1 e 2)
COEF_VC_DNIT = 2.56  # Vc = 2,56 H^0,5 (celular: velocidade critica do retangulo, E = H)
A_CRIT_TUBO_SOBRE_D2 = 0.60  # arredondamento de 0,601 (IME p. 151-152, theta_c = 4,0335); reproduz a Tabela 1 (p. 55)
THETA_CRITICO_IME = 4.0335  # rad: raiz de (3/2) A/T = D no circular (IME Anexo II, p. 152)


def vazao_critica_exata(forma, dim, n_celulas=1):
    """Vazao em que a energia especifica critica iguala a altura: dc + Vc^2/2g = H
    (seccao circular exata ou retangular). Total das n_celulas [m3/s]."""
    g = _geo(forma, dim)
    lo, hi = 1e-6, 1e3
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if _carga_critica(mid, g, forma, dim)[0] < g["H"]:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi) * n_celulas


def vazao_critica_legado_dnit(forma, dim, n_celulas=1, detalhado=False):
    """Vazao critica pelo metodo LEGADO do DNIT-DREN (IPR-724) p. 54-56 (bueiro 'como canal').
    Celular (BSCC...): Q = (2/3) 2,56 B H^1,5 por celula (= 1,705 B H^1,5; Tabela 2 p. 56:
    2x2 = 9,64 e 3x3 = 26,58 m3/s; IME p. 152 imprime o mesmo 1,705). O coeficiente impresso
    1,638 (p. 54-55) nao e usado (armadilha 8 da skill). Tubular (BSTC...): Q = A_c 2,56 D^0,5
    com A_c = 0,60 D^2 (Tabela 1 p. 55). A origem e o IME p. 151-152: theta_c = 4,0335 rad
    resolve Ec = D com Ec = (3/2) A/T (exato so no retangular) e da A_c = 0,601 D^2,
    Vc = 2,56 D^0,5 (ver regime_critico_tubular_ime); 0,60 e o arredondamento (0,2 %). Como a
    energia critica do circulo e dc + A/(2T), nao 3/2 A/T, o resultado fica ~7 % ACIMA da vazao
    critica exata (contra a seguranca).
    Preferir o HDS-5. Retorna Q total [m3/s] (ou dict com a exata e o desvio)."""
    g = _geo(forma, dim)
    if forma == "retangular":
        q = 2.0 / 3.0 * COEF_VC_DNIT * g["B"] * g["H"] ** 1.5
    elif forma == "circular":
        q = A_CRIT_TUBO_SOBRE_D2 * g["D"] ** 2 * COEF_VC_DNIT * g["D"] ** 0.5
    else:
        raise ValueError("forma deve ser circular ou retangular")
    q *= n_celulas
    if not detalhado:
        return q
    ex = vazao_critica_exata(forma, dim, n_celulas)
    return _resultado({"forma": forma, "dim": dim, "n_celulas": n_celulas},
                      {"Q_legado_dnit_m3s": q, "Q_exata_m3s": ex, "desvio_relativo": q / ex - 1},
                      "legado DNIT-DREN Tab. 1/2 p. 55-56 (Vc = 2,56 D^0,5)",
                      ["metodo legado: vazao critica do tubular ~7 % acima da exata; usar HDS-5"])


# --------------------------------------------------------------------------
# Tubo circular parcialmente cheio e regime critico do tubular (IME)
# --------------------------------------------------------------------------
LIMITE_Y_SOBRE_D_PROVISORIO = 0.75  # criterio do acervo (Delmiro 1492:164); padrao provisorio, decisao F7


def tubo_parcialmente_cheio(Q, D, n, S0, n_celulas=1, limite_y_sobre_D=LIMITE_Y_SOBRE_D_PROVISORIO):
    """Escoamento uniforme (Manning) em tubo circular parcialmente cheio, geometria exata.

    A = D^2/8 (th - sen th), P = D th/2, T = D sen(th/2), th = 2 acos(1 - 2y/D);
    V = R^(2/3) S0^(1/2)/n ; Fr = V / sqrt(g A/T) (profundidade hidraulica A/T, nunca y).
    Q [m3/s] total, dividido em n_celulas linhas iguais; D [m]; S0 [m/m].
    Fontes: HDS-3 Chart 55 [FHWA-HDS3 p. 76 do PDF] e Ex. 10-17 [p. 53-55] (conferidos
    0,4 a 1,3 %); caso acervo Delmiro BUC-2 a BUC-5 (1493:282-285), sem ✓h.
    Faixa: n 0,010-0,035; S0 > 0; y/D <= 0,82 no ramo normal (Q <= Q plena). Se Q > Q plena, o
    tubo trabalha cheio/sob pressao: aviso e y = D. limite_y_sobre_D e padrao provisorio 0,75
    (criterio de projeto do acervo, decisao F7): acima dele, aviso.
    Retorna dict padrao (entradas, saidas, metodo, avisos, versao)."""
    if min(Q, D, n, S0) <= 0 or n_celulas < 1:
        raise ValueError("Q, D, n, S0 devem ser > 0 e n_celulas >= 1")
    avisos = []
    if not 0.010 <= n <= 0.035:
        avisos.append("n fora de 0,010-0,035 (faixa de validade da tabela de Manning usada)")
    Qc = Q / n_celulas
    cheia = manning_cheia("circular", D, n, S0)
    if Qc >= cheia["Q"]:
        avisos.append("Q por linha >= capacidade plena de Manning: tubo cheio; yn = D (verificar carga/HW)")
        y = D
    else:
        y = profundidade_normal(Qc, "circular", D, n, S0)
    m = manning_lamina("circular", D, y, n, S0)
    regime = "supercritico" if m["Fr"] > 1.0 else "subcritico"
    if 0.9 <= m["Fr"] <= 1.1:
        avisos.append("Fr entre 0,9 e 1,1: proximo do critico; lamina instavel, evitar projetar nessa faixa")
    if y / D > limite_y_sobre_D:
        avisos.append(f"y/D = {y / D:.3f} > {limite_y_sobre_D:g} (padrao provisorio, decisao F7)")
    if S0 > 0.10:
        avisos.append("S0 > 10 %: fora da faixa usual de Manning para bueiro")
    return _resultado(
        {"Q": Q, "D": D, "n": n, "S0": S0, "n_celulas": n_celulas, "limite_y_sobre_D": limite_y_sobre_D},
        {"y_m": y, "y_sobre_D": y / D, "A_m2": m["A"], "P_m": m["P"], "R_m": m["R"], "V_m_s": m["V"],
         "Fr": m["Fr"], "regime": regime, "Q_plena_m3s": cheia["Q"], "Q_sobre_Qplena": Qc / cheia["Q"]},
        "Manning, segmento circular exato (HDS-3 Chart 55 / Ex. 10-17)", avisos)


def regime_critico_tubular_ime(D, n=0.015):
    """Regime critico do tubular com Ec = D, pelo IME (Anexo II, p. 151-152).

    (3/2) A/T = D  =>  theta_c = 4,0335 rad (231,1 graus); d_c = 0,716 D;
    A_c = D^2 (th - sen th)/8 = 0,601 D^2; Vc = sqrt(g A/T) = 2,56 D^0,5 (m/s);
    Qc = A_c Vc = 1,538 D^2,5 (IME imprime 1,533; diferenca 0,3 % de arredondamento);
    Ic = n^2 Vc^2/R^(4/3) = 32,82 n^2/D^(1/3) (m/m). D [m], n adim.
    Nota: Ec = (3/2) A/T e exato so no retangular; no circulo a energia critica e
    dc + A/(2T), e a vazao exata de Ec = D e ~7 % menor (vazao_critica_exata)."""
    if D <= 0 or n <= 0:
        raise ValueError("D e n devem ser > 0")
    th = THETA_CRITICO_IME
    A = D * D / 8 * (th - math.sin(th))
    T = D * math.sin(th / 2)
    Vc = math.sqrt(G * A / T)
    R = A / (D * th / 2)
    return _resultado({"D": D, "n": n},
                      {"theta_c_rad": th, "dc_m": D / 2 * (1 - math.cos(th / 2)), "A_c_m2": A,
                       "A_c_sobre_D2": A / D ** 2, "Vc_m_s": Vc, "Qc_m3s": A * Vc, "Ic": (n * Vc) ** 2 / R ** (4 / 3)},
                      "IME Anexo II p. 151-152 (Ec = D)",
                      ["criterio Ec = (3/2) A/T aproximado no circulo (~7 % acima da vazao critica exata)"])


# --------------------------------------------------------------------------
# Sarjeta triangular (HEC-22, 4a ed., p. 79-80)
# --------------------------------------------------------------------------
KU_IZZARD_SI = 0.376  # HEC-22 eq. 5.2 (0,56 em unidades inglesas)


def sarjeta_triangular_izzard(Sx, SL, n, Q=None, T=None):
    """Sarjeta triangular (Izzard, HEC-22 p. 79-80, eqs. 5.2 e 5.4, SI):
    Q = (Ku/n) Sx^1,67 SL^0,5 T^2,67 ; T = [Q n/(Ku Sx^1,67 SL^0,5)]^0,375, Ku = 0,376.
    Dar Q para obter o espalhamento T [m], ou T para obter Q [m3/s].
    Exemplo 5.1 (n 0,016; Sx 0,02; SL 0,01): Q 0,051 -> T 2,76 m; T 2,5 -> Q 0,0395.
    Ignora a resistencia da face do meio-fio; validade tipica T/y > 40 (secao rasa)."""
    if (Q is None) == (T is None):
        raise ValueError("informar exatamente um entre Q e T")
    if min(Sx, SL, n) <= 0:
        raise ValueError("Sx, SL e n devem ser > 0")
    k = KU_IZZARD_SI / n * Sx ** 1.67 * SL ** 0.5
    if Q is not None:
        if Q <= 0:
            raise ValueError("Q deve ser > 0")
        r = {"T_m": (Q / k) ** (1 / 2.67), "Q_m3s": Q}  # eq. 5.4 imprime 0,375 (~1/2,67)
    else:
        if T <= 0:
            raise ValueError("T deve ser > 0")
        r = {"T_m": T, "Q_m3s": k * T ** 2.67}
    r["y_m"] = r["T_m"] * Sx
    r["V_m_s"] = r["Q_m3s"] / (0.5 * r["T_m"] * r["y_m"])
    return _resultado({"Sx": Sx, "SL": SL, "n": n, "Q": Q, "T": T}, r,
                      "HEC-22 eqs. 5.2/5.4 (Izzard), Ku = 0,376 SI", [])


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------
def _dim(d):
    return tuple(d) if isinstance(d, (list, tuple)) else d


def _f_entrada(**k):
    k["dim"] = _dim(k["dim"])
    return controle_de_entrada(detalhado=True, **k)


def _f_saida(**k):
    k["dim"] = _dim(k["dim"])
    return controle_de_saida(detalhado=True, **k)


def _f_dim(**k):
    for c in k.get("candidatas") or []:
        c["dim"] = _dim(c["dim"])
    return dimensionar_bueiro(**k)


def _f_vel(**k):
    k["dim"] = _dim(k["dim"])
    r = velocidade_de_saida(**{x: v for x, v in k.items() if x != "material_jusante"})
    d = dissipador_necessario(r["V_m_s"], k.get("material_jusante", "argila_rija"))
    return _resultado(k, {**r, "dissipador": d}, "velocidade de saida + limite do material", [])


def _f_orificio(Q, A, Cd=0.62, h=None):
    r = verificacao_por_orificio(Q, A, Cd, h)
    return _resultado({"Q": Q, "A": A, "Cd": Cd, "h": h},
                      {"h_m" if h is None else "Q_m3s": r}, "orificio (legado)", [])


def _f_comp(**k):
    k["dim"] = _dim(k["dim"])
    return comparar_legado_hds5(**k)


def _f_vc(**k):
    k["dim"] = _dim(k["dim"])
    return vazao_critica_legado_dnit(detalhado=True, **k)


_FUNCOES = {"tubo_parcialmente_cheio": tubo_parcialmente_cheio,
            "regime_critico_tubular_ime": regime_critico_tubular_ime,
            "vazao_critica_legado_dnit": _f_vc, "sarjeta_triangular_izzard": sarjeta_triangular_izzard,
            "controle_de_entrada": _f_entrada, "controle_de_saida": _f_saida,
            "dimensionar_bueiro": _f_dim, "velocidade_de_saida": _f_vel,
            "orificio": _f_orificio, "comparar_legado_hds5": _f_comp}


def main(argv=None):
    ap = argparse.ArgumentParser(prog="python -m tools.dren.bueiros")
    ap.add_argument("--json", required=True,
                    help="JSON {'funcao': nome, ...args} ou {'funcao':..., 'args': {...}}; funcoes: "
                         + ", ".join(_FUNCOES))
    a = ap.parse_args(argv)
    req = json.loads(a.json)
    f = _FUNCOES.get(req.get("funcao"))
    if f is None:
        print(json.dumps({"erro": "funcao desconhecida", "disponiveis": list(_FUNCOES),
                          "versao": VERSAO}, ensure_ascii=False))
        return 2
    try:
        args = req["args"] if "args" in req else {k: v for k, v in req.items() if k != "funcao"}
        out = f(**args)
    except (ValueError, KeyError, TypeError) as e:
        print(json.dumps({"erro": str(e), "versao": VERSAO}, ensure_ascii=False))
        return 1
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
