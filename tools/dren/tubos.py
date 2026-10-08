"""Tubos de concreto (NBR 8890): selecao INDICATIVA de classe PA/EA pela carga de Marston.

Fluxo (ABTC/IBTS "Projeto de tubos circulares de concreto armado", El Debs, 2003, citado
como TUBOS; ABTC "Como especificar tubos em licitacao", ESPEC; ABTC "Alteracoes da
NBR 8890:2020", ALTERACOES; USACE EM 1110-2-2902, EM):

  q   = carga vertical do solo [kN/m]     vala: q = Cv g bv^2, Cv = (1 - e^(-a' lv))/a'  [TUBOS p. 17, eqs. 2.1-2.2]
                                          aterro, projecao positiva: q = Cap g de^2       [TUBOS p. 19-20, eqs. 2.3-2.8]
  qm  = sobrecarga (trafego) [kN/m] x coeficiente de impacto (TUBOS Tab. 3.3, p. 33)
  Fens = (q + qm) g_s / a_eq                                          [TUBOS p. 45, eqs. 5.1-5.2]
         g_s = 1,0 (fissura) e 1,5 (ruptura); a_eq = fator de equivalencia (berco)
  classe = menor classe cuja forca isenta de fissura >= Fens(1,0) e cuja ruptura >= Fens(1,5)
           (ESPEC Tab. 2, p. 4 = TUBOS Tab. 5.1, p. 46; ruptura = 1,5 x fissura)

Unidades: m, kN, kN/m3, kN/m (forca por metro de tubo). DN em mm (diametro interno).
Todas as funcoes sao INDICATIVAS (anteprojeto): nao substituem o software da ABTC nem o
projeto estrutural. Lacunas do corpus: nao ha tabela de altura maxima de aterro por classe e DN
(so no software da ABTC); a sobrecarga qm deve ser informada (veiculo-tipo, TUBOS cap. 3,
p. 25-36, nao implementado); projecao negativa e vala induzida nao implementadas.

Padroes provisorios (decisao F7): fator de berco de classe A em vala = 2,25 (minimo da faixa
2,25-3,4 do TUBOS Tab. 4.1; o EM usa 2,5); diametro externo estimado pela espessura PA2
(ALTERACOES Tab. 1) quando de nao e informado.

CLI: python -m tools.dren.tubos --json '{"funcao": "classe_de_tubo", "DN_mm": 1200, "F_kN_m": 65}'

CHANGELOG
0.1.0 (2026-10-08): versao inicial (fase F5).
"""
from __future__ import annotations

import math

VERSAO = "0.1.0"

# --------------------------------------------------------------------------
# Tabelas transcritas (paginas conferidas no _texto; Tab. 4.2/4.3 conferidas na imagem p. 43)
# --------------------------------------------------------------------------
# TUBOS Tab. 1.1 [p. 16]: tipo -> (k_mu = k_mu', gamma kN/m3)
SOLOS_TAB_1_1 = {
    1: (0.192, 19.0),  # material sem coesao
    2: (0.165, 17.6),  # areia e pedregulho
    3: (0.150, 19.2),  # solo saturado
    4: (0.130, 19.2),  # argila
    5: (0.110, 21.0),  # argila saturada
}

# TUBOS Tab. 4.1 [p. 37] (vala); classe A: faixa (min, max). EM Tab. 3-1 [p. 27]: 1,5 / 1,9 / 2,5.
FATOR_BERCO_VALA = {"A": (2.25, 3.4), "B": 1.9, "C": 1.5, "D": 1.1}
FATOR_BERCO_VALA_EM2902 = {"C": 1.5, "B": 1.9, "A": 2.5}  # ordinario, primeira classe, berco de concreto

# TUBOS Tab. 4.2 [p. 43] e EM Tab. 3-2 [p. 27]: eta por classe de base (aterro)
ETA_BASE = {"A": 0.505, "B": 0.707, "C": 0.840, "D": 1.310}
# TUBOS Tab. 4.3 [p. 43] = EM Tab. 3-2: chi por taxa de projecao (rho, classe A, classes B/C/D)
CHI_TAB_4_3 = [(0.0, 0.150, 0.000), (0.3, 0.743, 0.217), (0.5, 0.856, 0.423),
               (0.7, 0.811, 0.594), (0.9, 0.678, 0.655), (1.0, 0.638, 0.638)]
# TUBOS Tab. 3.3 [p. 33]: coeficiente de impacto por cobrimento (limite superior de hs, phi)
IMPACTO_TAB_3_3 = [(0.30, 1.3), (0.60, 1.2), (0.90, 1.1)]  # hs > 0,90 m: 1,0
HS_MIN_TRAFEGO = 0.6  # m, TUBOS p. 29 (trafego normal)
Q_MULTIDAO_KN_M2 = 5.0  # kN/m2, TUBOS eq. 3.19 [p. 33]

CLASSES = {"pluvial": ("PA1", "PA2", "PA3", "PA4"), "esgoto": ("EA2", "EA3", "EA4")}
# ESPEC Tab. 2 [p. 4] = TUBOS Tab. 5.1 [p. 46]: DN -> forca minima isenta de fissura [kN/m]
# (ruptura = 1,5 x fissura, arredondada na norma: tabela de ruptura abaixo transcrita)
_FISSURA = {  # DN: (PA1, PA2, PA3, PA4)
    300: (12, 18, 27, 36), 400: (16, 24, 36, 48), 500: (20, 30, 45, 60), 600: (24, 36, 54, 72),
    700: (28, 42, 63, 84), 800: (32, 48, 72, 96), 900: (36, 54, 81, 108), 1000: (40, 60, 90, 120),
    1100: (44, 66, 99, 132), 1200: (48, 72, 108, 144), 1500: (60, 90, 135, 180),
    1750: (70, 105, 158, 210), 2000: (80, 120, 180, 240),
}
_RUPTURA = {
    300: (18, 27, 41, 54), 400: (24, 36, 54, 72), 500: (30, 45, 68, 90), 600: (36, 54, 81, 108),
    700: (42, 63, 95, 126), 800: (48, 72, 108, 144), 900: (54, 81, 122, 162), 1000: (60, 90, 135, 180),
    1100: (66, 99, 149, 198), 1200: (72, 108, 162, 216), 1500: (90, 135, 203, 270),
    1750: (105, 158, 237, 315), 2000: (120, 180, 270, 360),
}
# esgoto: EA2, EA3, EA4 tem as mesmas forcas de PA2, PA3, PA4 nas duas tabelas (Tab. 2 de ESPEC)
FORCAS_PLUVIAL = {dn: {c: (f, r) for c, f, r in zip(CLASSES["pluvial"], _FISSURA[dn], _RUPTURA[dn])}
                  for dn in _FISSURA}
FORCAS_ESGOTO = {dn: {c: (f, r) for c, f, r in zip(CLASSES["esgoto"], _FISSURA[dn][1:], _RUPTURA[dn][1:])}
                 for dn in _FISSURA}
# ALTERACOES Tab. 1 [p. 2]: espessura minima de parede PA2, ponta e bolsa, mm (para estimar de)
_ESPESSURA_PA2_MM = {300: 45, 400: 45, 500: 50, 600: 60, 700: 66, 800: 72, 900: 75, 1000: 80,
                     1100: 90, 1200: 96, 1500: 120, 1750: 140, 2000: 160}


def _res(saidas, metodo, avisos):
    r = dict(saidas)
    r["metodo"] = metodo
    r["avisos"] = list(avisos)
    return r


def _solo(tipo_solo, gamma, k_mu):
    if tipo_solo is not None:
        if tipo_solo not in SOLOS_TAB_1_1:
            raise ValueError("tipo_solo deve ser 1 a 5 (TUBOS Tab. 1.1)")
        k0, g0 = SOLOS_TAB_1_1[tipo_solo]
        gamma = g0 if gamma is None else gamma
        k_mu = k0 if k_mu is None else k_mu
    if gamma is None or k_mu is None:
        raise ValueError("informar tipo_solo (1-5) ou gamma [kN/m3] e k_mu")
    if gamma <= 0 or k_mu <= 0:
        raise ValueError("gamma e k_mu devem ser > 0")
    return float(gamma), float(k_mu)


# --------------------------------------------------------------------------
# Cargas do solo (Marston-Spangler)
# --------------------------------------------------------------------------
def carga_solo_vala(hs, bv, tipo_solo=None, gamma=None, k_mu=None):
    """Carga vertical do solo em vala, q [kN/m] (TUBOS p. 17, eqs. 2.1-2.2; EM Ap. B p. 68 eq. 2-5/2-7).

    q = Cv g bv^2 ; Cv = (1 - exp(-a' hs/bv)) / a' ; a' = 2 k_mu' .
    hs = altura de terra sobre o topo do tubo [m]; bv = largura da vala ao nivel do topo [m]
    (TUBOS Fig. 2.3). Solo por tipo_solo (1-5, Tab. 1.1) ou gamma e k_mu explicitos.
    Gabarito EM: k_mu' = 0,15, H = 2,44, Bd = 1,52, g = 18,85 -> Cd = 1,274; We = 55,483 kN/m.
    Faixa: vala estreita; quando bv cresce a carga nao pode superar a do aterro (TUBOS p. 18):
    o aviso lembra de verificar. Retorna dict (Cv, q_kN_m, lambda, alfa)."""
    if hs <= 0 or bv <= 0:
        raise ValueError("hs e bv devem ser > 0 [m]")
    g, k = _solo(tipo_solo, gamma, k_mu)
    a = 2.0 * k
    lam = hs / bv
    cv = (1.0 - math.exp(-a * lam)) / a
    avisos = ["vala: a carga nao pode exceder a de aterro (projecao positiva); adotar a menor (TUBOS p. 18)"]
    if hs < HS_MIN_TRAFEGO:
        avisos.append("hs < 0,6 m: cobrimento minimo para trafego normal (TUBOS p. 29)")
    return _res({"Cv": cv, "q_kN_m": cv * g * bv * bv, "lambda": lam, "alfa_linha": a},
                "Marston vala, TUBOS eqs. 2.1-2.2", avisos)


def carga_solo_aterro_positiva(hs, de, rho, r_ap, tipo_solo=None, gamma=None, k_mu=None):
    """Carga do solo em aterro com projecao positiva, q [kN/m] (TUBOS p. 19-20, eqs. 2.3-2.8).

    q = Cap g de^2 ; a = 2 k_mu ; lam = hs/de ; lam_e = he/de (plano de igual recalque):
    e^(a lam_e) = a lam_e + a rho r_ap + 1                              (2.6, sinal + : r_ap > 0)
    hs < he : Cap = (e^(a lam) - 1)/a                                   (2.4)
    hs > he : Cap = (e^(a lam_e) - 1)/a + (lam - lam_e) e^(a lam_e)     (2.5)
    rho = ha/de (taxa de projecao, 0-1); r_ap = razao de recalque (Tab. 2.1, p. 21: +1,0 rocha;
    +0,5 a +0,8 solo comum, ATHA 0,5; 0 a +0,5 solo deformavel, ATHA 0,3). Apenas r_ap >= 0
    (todos os valores recomendados sao positivos); r_ap = 0 da Cap = hs/de (peso do prisma).
    Eq. 2.6 e forma Spangler/Marston (sinais +/- ilegiveis no _texto; conferido na imagem p. 19).
    Sem exemplo numerico no TUBOS: testado por consistencia (limites e continuidade)."""
    if hs <= 0 or de <= 0:
        raise ValueError("hs e de devem ser > 0 [m]")
    if not 0.0 <= rho <= 1.0:
        raise ValueError("rho (taxa de projecao) deve estar em 0-1")
    if r_ap < 0:
        raise ValueError("r_ap < 0 (projecao negativa/ alivio) nao implementado; usar r_ap >= 0")
    g, k = _solo(tipo_solo, gamma, k_mu)
    a = 2.0 * k
    lam = hs / de
    c = a * rho * r_ap + 1.0
    f = lambda x: math.exp(a * x) - a * x - c
    if f(0.0) >= 0.0:  # r_ap*rho = 0: plano de igual recalque na geratriz superior
        lam_e = 0.0
    else:
        lo, hi = 0.0, 1.0
        while f(hi) < 0.0:
            hi *= 2.0
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            if f(mid) < 0.0:
                lo = mid
            else:
                hi = mid
        lam_e = 0.5 * (lo + hi)
    if lam < lam_e:
        cap = (math.exp(a * lam) - 1.0) / a
    else:
        cap = (math.exp(a * lam_e) - 1.0) / a + (lam - lam_e) * math.exp(a * lam_e)
    avisos = []
    if hs < HS_MIN_TRAFEGO:
        avisos.append("hs < 0,6 m: cobrimento minimo para trafego normal (TUBOS p. 29)")
    return _res({"Cap": cap, "q_kN_m": cap * g * de * de, "lambda": lam, "lambda_e": lam_e, "he_m": lam_e * de,
                 "alfa": a},
                "Marston aterro com projecao positiva, TUBOS eqs. 2.3-2.8", avisos)


# --------------------------------------------------------------------------
# Fator de equivalencia (berco)
# --------------------------------------------------------------------------
def fator_berco_vala(classe, alfa_A=None, fonte="abtc"):
    """Fator de equivalencia em vala (TUBOS Tab. 4.1, p. 37; EM Tab. 3-1, p. 27).

    classe A (berco de concreto), B (primeira classe), C (comum), D (condenavel).
    fonte "abtc": A 2,25-3,4 (padrao provisorio 2,25, minimo, a favor da seguranca; alfa_A
    sobrescreve), B 1,9, C 1,5, D 1,1. fonte "em2902": A 2,5, B 1,9, C 1,5 (D inadmissivel)."""
    classe = str(classe).upper()
    avisos = []
    if fonte == "em2902":
        if classe == "D":
            raise ValueError("EM 1110-2-2902: base classe D e inadmissivel")
        if classe not in FATOR_BERCO_VALA_EM2902:
            raise ValueError("classe deve ser A, B ou C na fonte em2902")
        return _res({"alfa_eq": FATOR_BERCO_VALA_EM2902[classe]}, "EM 1110-2-2902 Tab. 3-1", avisos)
    if fonte != "abtc":
        raise ValueError("fonte deve ser 'abtc' ou 'em2902'")
    if classe not in FATOR_BERCO_VALA:
        raise ValueError("classe deve ser A, B, C ou D")
    v = FATOR_BERCO_VALA[classe]
    if classe == "A":
        lo, hi = v
        if alfa_A is None:
            alfa = lo
            avisos.append(f"classe A: faixa {lo}-{hi} conforme execucao e compactacao do enchimento; "
                          f"adotado o minimo {lo} (padrao provisorio, decisao F7; EM usa 2,5)")
        else:
            if not lo <= alfa_A <= hi:
                raise ValueError(f"alfa_A fora da faixa {lo}-{hi} (TUBOS Tab. 4.1)")
            alfa = float(alfa_A)
    else:
        alfa = v
    if classe == "D":
        avisos.append("base classe D (condenavel): evitar em projeto (EM 1110-2-2902 a declara inadmissivel)")
    return _res({"alfa_eq": alfa}, "TUBOS Tab. 4.1 (vala)", avisos)


def chi_aterro(rho, classe):
    """chi (TUBOS Tab. 4.3 = EM Tab. 3-2), interpolacao linear em rho; classe A (concreto) ou B/C/D."""
    if not 0.0 <= rho <= 1.0:
        raise ValueError("rho deve estar em 0-1")
    col = 1 if str(classe).upper() == "A" else 2
    for (r0, *c0), (r1, *c1) in zip(CHI_TAB_4_3, CHI_TAB_4_3[1:]):
        if r0 <= rho <= r1:
            t = (rho - r0) / (r1 - r0)
            return c0[col - 1] + t * (c1[col - 1] - c0[col - 1])
    raise ValueError("rho fora da tabela")  # inalcancavel


def fator_berco_aterro(classe, rho, hs, de, k, Cap, theta_fixo=None):
    """Fator de equivalencia em aterro com projecao positiva (TUBOS eqs. 4.1-4.2, p. 42-43; EM eq. 3-1).

    a_eq = 1,431 / (eta - theta chi) ;  theta = (rho k / Cap) (hs/de + rho/2) <= 0,33  (4.2)
    eta por classe (Tab. 4.2), chi por rho e classe (Tab. 4.3). k = coeficiente de empuxo
    (Rankine). theta_fixo: o EM 1110-2-2902 (eq. 3-1) usa theta = 1/3 fixo; passar 1/3 para
    reproduzi-lo (Bf = 6,098 no exemplo p. 71 com chi 0,811, eta 0,505).
    Classe B tem rho <= 0,7 (Fig. 4.8). Retorna dict (alfa_eq, theta, chi, eta)."""
    classe = str(classe).upper()
    if classe not in ETA_BASE:
        raise ValueError("classe deve ser A, B, C ou D")
    if min(hs, de, k, Cap) <= 0:
        raise ValueError("hs, de, k e Cap devem ser > 0")
    eta = ETA_BASE[classe]
    chi = chi_aterro(rho, classe)
    if theta_fixo is None:
        theta = min(rho * k / Cap * (hs / de + rho / 2.0), 0.33)
    else:
        theta = float(theta_fixo)
    den = eta - theta * chi
    if den <= 0:
        raise ValueError("eta - theta chi <= 0: parametros fora da faixa")
    avisos = []
    if classe == "B" and rho > 0.7:
        avisos.append("classe B: rho maximo 0,7 (TUBOS Fig. 4.8)")
    return _res({"alfa_eq": 1.431 / den, "theta": theta, "chi": chi, "eta": eta},
                "TUBOS eqs. 4.1-4.2 / EM eq. 3-1", avisos)


def d_load_em2902(W_T_N_m, Si_mm, Bf, Hf=1.3):
    """D0,01 [N/m/mm] = Hf W_T / (Si Bf)  (EM 1110-2-2902 eq. 3-2, p. 25; exemplo p. 71-72).
    W_T = W_E + W_F + W_L [N/m]; Si = diametro interno [mm]; Hf = fator hidraulico 1,3.
    Exemplo: W_L 145 940 + W_E 175 130 N/m, Si 1200, Bf 6,098 -> 57 N/m/mm (ASTM C76M classe III)."""
    if min(W_T_N_m, Si_mm, Bf, Hf) <= 0:
        raise ValueError("argumentos devem ser > 0")
    return Hf * W_T_N_m / (Si_mm * Bf)


# --------------------------------------------------------------------------
# Sobrecarga
# --------------------------------------------------------------------------
def coef_impacto(hs):
    """Coeficiente de impacto de trafego rodoviario (TUBOS Tab. 3.3, p. 33; ACPA):
    hs <= 0,30 m: 1,3 ; <= 0,60: 1,2 ; <= 0,90: 1,1 ; > 0,90: 1,0."""
    if hs <= 0:
        raise ValueError("hs deve ser > 0 [m]")
    for lim, phi in IMPACTO_TAB_3_3:
        if hs <= lim:
            return phi
    return 1.0


def sobrecarga_multidao(de, q_kN_m2=Q_MULTIDAO_KN_M2):
    """Sobrecarga minima de multidao qm = q de [kN/m] (TUBOS eq. 3.19, p. 33), q = 5 kN/m2.
    Piso, nao carga de veiculo: a de veiculo-tipo (cap. 3) deve ser informada pelo usuario."""
    if de <= 0 or q_kN_m2 < 0:
        raise ValueError("de > 0 e q >= 0")
    return q_kN_m2 * de


# --------------------------------------------------------------------------
# Forca de ensaio e classe
# --------------------------------------------------------------------------
def forca_de_ensaio(q, qm, alfa_eq, gamma_s=1.0):
    """Fens = gamma_s (q + qm) / alfa_eq [kN/m] (TUBOS eqs. 5.1-5.2, p. 45).
    gamma_s = 1,0 (fissura) ou 1,5 (ruptura). q e qm em kN/m (por metro de tubo)."""
    if q < 0 or qm < 0 or alfa_eq <= 0 or gamma_s <= 0:
        raise ValueError("q, qm >= 0; alfa_eq e gamma_s > 0")
    return gamma_s * (q + qm) / alfa_eq


def classe_de_tubo(DN_mm, F_kN_m, tipo="pluvial"):
    """Menor classe NBR 8890 (ESPEC Tab. 2 p. 4 = TUBOS Tab. 5.1 p. 46) para a forca de ensaio F.

    F [kN/m] = forca isenta de fissura exigida (Fens com gamma = 1,0); exige-se tambem
    ruptura tabelada >= 1,5 F. tipo "pluvial" (PA1-PA4) ou "esgoto" (EA2-EA4). DN em mm
    (300 a 2000 da tabela; DN 1300 nao consta). Se nenhuma classe atende, classe = None e
    aviso (acima de PA4/EA4: galeria celular NBR 15396, ALTERACOES p. 4).
    Exemplos ESPEC p. 6: DN1200/65 -> PA2; DN800 esgoto/85 -> EA4; DN400/37 -> PA4."""
    if tipo not in CLASSES:
        raise ValueError("tipo deve ser 'pluvial' ou 'esgoto'")
    tab = FORCAS_PLUVIAL if tipo == "pluvial" else FORCAS_ESGOTO
    dn = int(round(DN_mm))
    if dn not in tab:
        raise ValueError("DN_mm deve ser um de " + ", ".join(str(d) for d in sorted(tab)) + " (ESPEC Tab. 2)")
    if F_kN_m <= 0:
        raise ValueError("F_kN_m deve ser > 0")
    avisos = []
    escolhida = None
    for c in CLASSES[tipo]:
        fis, rup = tab[dn][c]
        if fis >= F_kN_m and rup >= 1.5 * F_kN_m:
            escolhida = c
            break
    if escolhida is None:
        avisos.append("nenhuma classe atende: acima de PA4/EA4 usar galeria celular (NBR 15396, "
                      "ALTERACOES p. 4) ou reduzir a carga (melhor berco, menor aterro)")
    if dn > 600:
        avisos.append("DN > 600: tubo obrigatoriamente armado (ou RF/RSF); RF so ate DN 1000 (NBR 8890:2020)")
    if dn < 500:
        avisos.append("DN < 500: encaixe ponta e bolsa (macho e femea so a partir de DN 500)")
    fis, rup = tab[dn][escolhida] if escolhida else (None, None)
    return _res({"classe": escolhida, "DN_mm": dn, "F_fissura_exigida_kN_m": F_kN_m,
                 "F_fissura_classe_kN_m": fis, "F_ruptura_classe_kN_m": rup,
                 "margem": (fis / F_kN_m - 1.0) if fis else None},
                "ESPEC Tab. 2 p. 4 / TUBOS Tab. 5.1 p. 46", avisos)


def selecionar_tubo(DN_mm, hs, instalacao, base, tipo_solo=2, bv=None, rho=None, r_ap=0.5,
                    sobrecarga_kN_m=0.0, aplicar_impacto=True, de_m=None, tipo="pluvial",
                    alfa_A=None, gamma=None, k_mu=None):
    """Selecao INDICATIVA da classe do tubo (anteprojeto): carga do solo + sobrecarga -> Fens -> classe.

    instalacao "vala" (exige bv [m]) ou "aterro" (exige rho em 0-1; r_ap padrao 0,5 = solo comum,
    Tab. 2.1, padrao provisorio, decisao F7). base A-D (berco). sobrecarga_kN_m = carga de
    trafego ja por metro de tubo (veiculo-tipo nao e calculado aqui); se aplicar_impacto, e
    multiplicada por phi(hs) (Tab. 3.3). de_m (diametro externo) padrao = DN + 2 e_PA2
    (ALTERACOES Tab. 1; provisorio). Nao ha verificacao de altura maxima de aterro por classe
    (nao existe no corpus; usar o software ABTC)."""
    if instalacao not in ("vala", "aterro"):
        raise ValueError("instalacao deve ser 'vala' ou 'aterro'")
    dn = int(round(DN_mm))
    avisos = ["indicativo: confirmar no software da ABTC; sem verificacao de altura maxima de aterro"]
    if de_m is None:
        if dn not in _ESPESSURA_PA2_MM:
            raise ValueError("DN_mm fora da tabela (300-2000)")
        de_m = dn / 1000.0 + 2 * _ESPESSURA_PA2_MM[dn] / 1000.0
        avisos.append(f"de estimado {de_m:.3f} m pela espessura PA2 (padrao provisorio); informar de_m do fabricante")
    g, k = _solo(tipo_solo if gamma is None or k_mu is None else None, gamma, k_mu)
    if instalacao == "vala":
        if bv is None:
            raise ValueError("vala exige bv [m]")
        sol = carga_solo_vala(hs, bv, gamma=g, k_mu=k)
        alfa_r = fator_berco_vala(base, alfa_A)
    else:
        if rho is None:
            raise ValueError("aterro exige rho (taxa de projecao, 0-1)")
        sol = carga_solo_aterro_positiva(hs, de_m, rho, r_ap, gamma=g, k_mu=k)
        alfa_r = fator_berco_aterro(base, rho, hs, de_m, k, sol["Cap"])
    avisos += sol["avisos"] + alfa_r["avisos"]
    phi = coef_impacto(hs) if aplicar_impacto else 1.0
    qm = sobrecarga_kN_m * phi
    if sobrecarga_kN_m == 0.0:
        avisos.append("sobrecarga nao informada (qm = 0): em via com trafego informar qm; piso de multidao "
                      f"= {sobrecarga_multidao(de_m):.1f} kN/m (TUBOS eq. 3.19)")
    q = sol["q_kN_m"]
    alfa = alfa_r["alfa_eq"]
    f_fis = forca_de_ensaio(q, qm, alfa, 1.0)
    f_rup = forca_de_ensaio(q, qm, alfa, 1.5)
    cl = classe_de_tubo(dn, f_fis, tipo)
    avisos += cl["avisos"]
    return _res({"classe": cl["classe"], "DN_mm": dn, "de_m": de_m, "q_solo_kN_m": q, "qm_kN_m": qm,
                 "phi_impacto": phi, "alfa_eq": alfa, "F_fissura_kN_m": f_fis, "F_ruptura_kN_m": f_rup,
                 "F_fissura_classe_kN_m": cl["F_fissura_classe_kN_m"]},
                "Marston + Fens (TUBOS cap. 2, 4, 5) + ESPEC Tab. 2", avisos)


FUNCOES = {
    "carga_solo_vala": carga_solo_vala,
    "carga_solo_aterro_positiva": carga_solo_aterro_positiva,
    "fator_berco_vala": fator_berco_vala,
    "fator_berco_aterro": fator_berco_aterro,
    "d_load_em2902": lambda W_T_N_m, Si_mm, Bf, Hf=1.3: {
        "D001_N_m_mm": d_load_em2902(W_T_N_m, Si_mm, Bf, Hf), "metodo": "EM 1110-2-2902 eq. 3-2", "avisos": []},
    "coef_impacto": lambda hs: {"phi": coef_impacto(hs), "metodo": "TUBOS Tab. 3.3 p. 33", "avisos": []},
    "sobrecarga_multidao": lambda de, q_kN_m2=Q_MULTIDAO_KN_M2: {
        "qm_kN_m": sobrecarga_multidao(de, q_kN_m2), "metodo": "TUBOS eq. 3.19 p. 33", "avisos": []},
    "forca_de_ensaio": lambda q, qm, alfa_eq, gamma_s=1.0: {
        "F_kN_m": forca_de_ensaio(q, qm, alfa_eq, gamma_s), "metodo": "TUBOS eqs. 5.1-5.2 p. 45", "avisos": []},
    "classe_de_tubo": classe_de_tubo,
    "selecionar_tubo": selecionar_tubo,
}

if __name__ == "__main__":
    from tools.dren._cli import principal
    principal("tools.dren.tubos", VERSAO, FUNCOES)
