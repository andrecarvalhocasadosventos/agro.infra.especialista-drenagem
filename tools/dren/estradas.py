"""Drenagem de estradas: sarjeta (triangular e composta), valeta trapezoidal, comprimento critico de
sarjeta/valeta (racional por metro x Manning), caixa coletora com grelha e dreno profundo longitudinal.

Unidades SI: m, m3/s, m/m, mm/h para intensidade. Apenas stdlib. CLI:
    python -m tools.dren.estradas --json '{"funcao": "valeta_comprimento_critico", ...}'

Fontes (corpus local, referencias/_texto/; paginas = marcador `<!-- p. N -->` do _texto):
- HEC-12 (FHWA-HEC12) p. 39-41 (Izzard, K = 0,56 ingles = 0,376 SI), p. 41-43 (gutter composto), p. 86
  (grelha em sag: eqs. 17-18; Cw = 1,66 SI, Co = 0,67); sarjeta triangular reutilizada de bueiros.py (HEC-22).
- LOC-IME p. 53-55 (racional por m, sequencia com Manning, folga), p. 82-85 (dreno profundo: Darcy, Scobey,
  Hazen-Williams, comprimento critico L = Q/q).
- Caso Xingo Lote I (acervo, SEM check humano): casos/drenagem/2026-10-08_xingo_lote1_valetas_protecao_comprimento_critico.md.
- Descida d'agua em degraus/rapida: NAO implementada (so desenhos no Album p. 40-47 e especificacoes; sem formula
  com pagina no corpus). Interface: Manning da secao de descida (valeta_manning) + dissipador (Hidraulico, D3).

Decisoes abertas (D-n): TR e Tc minimo entram como ARGUMENTOS com padrao provisorio (TR 10 anos, Tc 5 min;
IPR726 p. 258, WSDOT p. 102, H14). Divergentes: 6 min (Album p. 214) e 10 min (IS-239, IPR726 p. 463).
Padrao provisorio, decisao F7.

CHANGELOG
0.1.1 (2026-10-08, revisao de formula F5): caixa_coletora_grelha avisa que na transicao vertedor-orificio a
capacidade real e menor que as duas equacoes (HEC-12 p. 87); formulas inalteradas.
"""
from __future__ import annotations

import math

from tools.dren import _cli
from tools.dren.bueiros import sarjeta_triangular_izzard, KU_IZZARD_SI

VERSAO = "0.1.1"
G = 9.81
TC_MIN_PADRAO = 5.0     # min, provisorio (decisao F7)
TR_PADRAO = 10          # anos, provisorio (decisao F7)
DECL_MIN_DERPR = 0.005  # DERPR-ES-DR-01-23 p. 10
DECL_MIN_HEC12 = 0.003  # HEC-12 p. 19 (0,2 % em terreno muito plano)


def _res(entradas, saidas, metodo, avisos):
    return {"entradas": entradas, "saidas": saidas, "metodo": metodo, "avisos": list(avisos), "versao": VERSAO}


def _pos(**kw):
    for k, v in kw.items():
        if v is None or not v > 0:
            raise ValueError("%s deve ser > 0 (recebido %r)" % (k, v))


def _aviso_decl(i):
    if i < DECL_MIN_HEC12:
        return ["declividade %.4f < 0,3 %% (HEC-12 p. 19) e < 0,5 %% (DERPR-ES-DR-01-23 p. 10): abaixo do minimo "
                "de ambas as fontes (divergencia 6 do mapa); confirmar" % i]
    if i < DECL_MIN_DERPR:
        return ["declividade %.4f < 0,5 %% (DERPR-ES-DR-01-23 p. 10; HEC-12 p. 19 aceita 0,3 %%): divergencia 6" % i]
    return []


# ---------------------------------------------------------------- criterio de projeto
def criterio_projeto(tc_calculado_min, tc_min=TC_MIN_PADRAO, TR=TR_PADRAO):
    """Tc adotado = max(tc calculado, tc_min) [min] e eco do TR [anos].

    Padrao provisorio (decisao F7): tc_min = 5 min, TR = 10 anos [IPR726 p. 258; WSDOT p. 102; IME p. 53].
    Divergencias: 6 min [Album p. 214 (OCR)]; 10 min [IPR726 p. 463, IS-239]; TR 25 anos ENGEFER [IME p. 53]."""
    _pos(tc_calculado_min=tc_calculado_min, tc_min=tc_min, TR=TR)
    av = ["padrao provisorio, decisao F7 (tc_min 5 min, TR 10 anos); divergem: 6 min (Album p. 214), "
          "10 min (IS-239, IPR726 p. 463); TR 25 anos ENGEFER (IME p. 53)"]
    return _res({"tc_calculado_min": tc_calculado_min, "tc_min": tc_min, "TR": TR},
                {"tc_adotado_min": max(tc_calculado_min, tc_min), "TR_anos": TR,
                 "minimo_comanda": tc_calculado_min < tc_min},
                "tc adotado = max(tc, tc_min)", av)


# ---------------------------------------------------------------- sarjeta triangular (reuso)
def sarjeta_triangular(Sx, SL, n, Q=None, T=None):
    """Sarjeta triangular de Izzard (HEC-22 p. 79-80 eq. 5.2; HEC-12 p. 39 eq. 4):
    Q = (Ku/n) Sx^1,67 SL^0,5 T^2,67, Ku = 0,376 (SI; 0,56 ingles). Reutiliza bueiros.sarjeta_triangular_izzard.
    Dar Q -> T, ou T -> Q. Validade: secao rasa (T/y > 40), sem resistencia do meio-fio. Unidades: m, m3/s, m/m."""
    r = sarjeta_triangular_izzard(Sx, SL, n, Q=Q, T=T)
    r["avisos"] = list(r["avisos"]) + _aviso_decl(SL)
    return r


# ---------------------------------------------------------------- sarjeta composta
def _q_composta(T, Sx, Sw, W, n, SL):
    if W >= T:
        raise ValueError("W (largura da depressao) deve ser < T (espalhamento)")
    y1 = Sx * (T - W)
    d = y1 + Sw * W
    k = KU_IZZARD_SI / n * math.sqrt(SL)
    i1 = (d ** (8 / 3) - y1 ** (8 / 3)) / Sw
    i2 = y1 ** (8 / 3) / Sx
    return k * (i1 + i2), k * i1, d


def sarjeta_composta(Sx, Sw, W, n, SL, T=None, Q=None):
    """Gutter composto (depressao de largura W e declividade transversal Sw junto ao meio-fio; Sx alem de W).

    Integracao de Izzard (q = y^(5/3) SL^0,5 / n por unidade de largura, R ~ y), exata por trechos:
      Q = (Ku/n) SL^0,5 { [d^(8/3) - y1^(8/3)]/Sw + y1^(8/3)/Sx },  y1 = Sx (T-W),  d = y1 + Sw W
      Eo = Qw/Q (parcela na depressao). Ku = 0,376 (SI), como na triangular (Sw = Sx recupera Izzard).
    Fonte: HEC-12 p. 41-43 (Ex. 5; la Eo vem da Chart 4, grafico; aqui e calculado). Dar T -> Q, ou
    Q -> T (bisseccao). Unidades: m, m3/s, m/m. Validade: secao rasa; T > W."""
    _pos(Sx=Sx, Sw=Sw, W=W, n=n, SL=SL)
    if (T is None) == (Q is None):
        raise ValueError("informar exatamente um entre T e Q")
    av = _aviso_decl(SL)
    if Sw <= Sx:
        av.append("Sw <= Sx: nao ha depressao; resultado equivale a sarjeta triangular")
    if Q is not None:
        _pos(Q=Q)
        lo, hi = W * 1.0000001, W + 1.0
        while _q_composta(hi, Sx, Sw, W, n, SL)[0] < Q:
            hi *= 2
            if hi > 1e4:
                raise ValueError("Q fora de faixa")
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            if _q_composta(mid, Sx, Sw, W, n, SL)[0] < Q:
                lo = mid
            else:
                hi = mid
        T = 0.5 * (lo + hi)
    else:
        _pos(T=T)
    q, qw, d = _q_composta(T, Sx, Sw, W, n, SL)
    return _res({"Sx": Sx, "Sw": Sw, "W": W, "n": n, "SL": SL, "T": T, "Q": Q},
                {"T_m": T, "Q_m3s": q, "Qw_m3s": qw, "Eo": qw / q, "d_meio_fio_m": d},
                "Izzard integrado por trechos (HEC-12 p. 41-43)", av)


# ---------------------------------------------------------------- valeta trapezoidal (Manning)
def _trap(b, z, y):
    A = y * (b + z * y)
    P = b + 2 * y * math.sqrt(1 + z * z)
    T = b + 2 * z * y
    return A, P, T


def valeta_manning(b, z, n, S, y=None, Q=None, v_max=None):
    """Valeta/canal trapezoidal por Manning: Q = A R^(2/3) S^0,5 / n. Dar y -> Q, ou Q -> y normal (bisseccao).
    b = base [m] (0 = triangular); z = talude H:V; Froude = V / sqrt(g A/T) (profundidade hidraulica, nunca y).
    Fonte: Manning; sequencia de calculo IME p. 53-54. Unidades: m, m3/s, m/m. v_max [m/s] opcional gera aviso."""
    _pos(n=n, S=S)
    if b < 0 or z < 0 or (b == 0 and z == 0):
        raise ValueError("b >= 0, z >= 0 e nao ambos nulos")
    if (y is None) == (Q is None):
        raise ValueError("informar exatamente um entre y e Q")

    def cap(yy):
        A, P, _ = _trap(b, z, yy)
        return A * (A / P) ** (2 / 3) * math.sqrt(S) / n

    if Q is not None:
        _pos(Q=Q)
        lo, hi = 1e-6, 1.0
        while cap(hi) < Q:
            hi *= 2
            if hi > 1e3:
                raise ValueError("Q fora de faixa")
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            if cap(mid) < Q:
                lo = mid
            else:
                hi = mid
        y = 0.5 * (lo + hi)
    else:
        _pos(y=y)
    A, P, T = _trap(b, z, y)
    q = cap(y)
    V = q / A
    Fr = V / math.sqrt(G * A / T)
    av = _aviso_decl(S)
    if v_max is not None and V > v_max:
        av.append("V = %.2f m/s > v_max %.2f m/s do revestimento" % (V, v_max))
    if abs(Fr - 1) < 0.1:
        av.append("Froude %.2f dentro de +-10 %% do critico: evitar (IME p. 54)" % Fr)
    return _res({"b": b, "z": z, "n": n, "S": S, "y": y if Q is None else None, "Q": Q},
                {"y_m": y, "Q_m3s": q, "A_m2": A, "R_m": A / P, "T_m": T, "V_m_s": V, "Froude": Fr,
                 "regime": "supercritico" if Fr > 1 else "subcritico"},
                "Manning trapezoidal", av)


# ---------------------------------------------------------------- comprimento critico
def vazao_por_metro(I_mm_h, contribuicoes):
    """Vazao racional por metro de dispositivo [m3/s/m] = I [mm/h] x sum(C_i w_i) / 3,6e6.

    contribuicoes = [(C, w_m), ...] (largura de cada implúvio por metro de valeta). Racional Q = C I A / 3,6e6
    (I mm/h, A m2) [IME p. 53, eqs. 4.1-4.2, convertida]. Xingo VPC-1: 0,9x0,60 + 0,3x10,00 = 3,54 m."""
    _pos(I_mm_h=I_mm_h)
    cw = 0.0
    for c, w in contribuicoes:
        if not (0 <= c <= 1) or w <= 0:
            raise ValueError("cada contribuicao exige 0 <= C <= 1 e w > 0")
        cw += c * w
    if cw <= 0:
        raise ValueError("contribuicoes vazias")
    return I_mm_h * cw / 3.6e6


def comprimento_critico(Q_cap, q_por_m):
    """Comprimento critico L = Q_cap / q [m] (IME p. 84, eq. 4.19): L em que a vazao acumulada atinge a
    capacidade. Q_cap [m3/s]; q_por_m [m3/s/m]."""
    _pos(Q_cap=Q_cap, q_por_m=q_por_m)
    return Q_cap / q_por_m


def valeta_comprimento_critico(b, z, h, n, i, I_mm_h, contribuicoes, hmax=None, v_max=None,
                               tc_min=TC_MIN_PADRAO, TR=TR_PADRAO):
    """Comprimento critico de valeta de crista/pe (ou sarjeta trapezoidal): L = Q_Manning(hmax) / q_racional_por_m.

    Metodo do projetista (Xingo, acervo) = IME p. 53-55: Q1 = A R^(2/3) i^0,5 / n e Q2 = C I A2 (A2 = w L);
    L = Q1 / [I sum(C_i w_i) / 3,6e6]. hmax padrao = 0,8 h (regra observada no Xingo, nao declarada: aviso).
    b = base, z = talude H:V, h = altura, i = declividade [m/m], I em mm/h (1 mm/min = 60 mm/h).
    TR e tc_min sao argumentos (padrao provisorio, decisao F7); a intensidade I vem da IDF (Clima) para TR e tc."""
    _pos(h=h, I_mm_h=I_mm_h, tc_min=tc_min, TR=TR)
    av = ["TR %s anos e tc_min %.1f min: padrao provisorio, decisao F7; I deve corresponder a duracao >= tc_min "
          "(6 min Album; 10 min IS-239 divergem)" % (TR, tc_min)]
    if hmax is None:
        hmax = 0.8 * h
        av.append("hmax = 0,8 h (regra observada em VPC-1/2/3/5 do Xingo, nao declarada; folga IME p. 54: f = 0,2 h)")
    if hmax > h:
        raise ValueError("hmax > h")
    m = valeta_manning(b, z, n, i, y=hmax, v_max=v_max)
    q = vazao_por_metro(I_mm_h, contribuicoes)
    L = comprimento_critico(m["saidas"]["Q_m3s"], q)
    return _res({"b": b, "z": z, "h": h, "n": n, "i": i, "I_mm_h": I_mm_h, "contribuicoes": contribuicoes,
                 "hmax": hmax, "TR": TR, "tc_min": tc_min},
                {"L_critico_m": L, "Q_cap_m3s": m["saidas"]["Q_m3s"], "V_m_s": m["saidas"]["V_m_s"],
                 "q_por_m_m3s_m": q, "Froude": m["saidas"]["Froude"]},
                "L = Q_Manning / q_racional (IME p. 53-55, 84)", av + m["avisos"])


# ---------------------------------------------------------------- folga
_TAB_FOLGA_CONCRETO_IME = [(0.250, 0.10), (0.560, 0.13), (0.840, 0.14), (1.400, 0.15), (2.800, 0.18)]


def folga_valeta(h, Q=None, revestimento="terra"):
    """Folga (bordo livre) de valeta [m]. terra, Q <= 0,3 m3/s: f = 0,2 h (IME p. 54).
    concreto: Tab. 4.2 do IME p. 55 por faixa de Q (ate 250 l/s 10 cm ... 1400-2800 l/s 18 cm).
    Terra com 0,3 < Q <= 10 m3/s: formula do IME (EQ 4.7) ilegivel no texto: nao implementada (ValueError).
    WSDOT p. 109: 0,5 ft (~0,15 m) fixo, TR 10 (divergencia 11)."""
    _pos(h=h)
    if revestimento == "terra":
        if Q is not None and Q > 0.3:
            raise ValueError("terra com Q > 0,3 m3/s: formula EQ 4.7 do IME ilegivel; nao implementada")
        return _res({"h": h, "Q": Q, "revestimento": revestimento}, {"folga_m": 0.2 * h},
                    "f = 0,2 h (IME p. 54)", [])
    if revestimento == "concreto":
        _pos(Q=Q)
        for lim, f in _TAB_FOLGA_CONCRETO_IME:
            if Q <= lim:
                return _res({"h": h, "Q": Q, "revestimento": revestimento}, {"folga_m": f},
                            "Tab. 4.2 IME p. 55", ["tabela IME; WSDOT p. 109 adota 0,15 m fixos (divergencia 11)"])
        raise ValueError("Q > 2,8 m3/s fora da Tab. 4.2 do IME")
    raise ValueError("revestimento: 'terra' ou 'concreto'")


# ---------------------------------------------------------------- caixa coletora com grelha
def caixa_coletora_grelha(P, A, d=None, Q=None, Cw=1.66, Co=0.67):
    """Grelha/caixa coletora em ponto baixo (sag), HEC-12 p. 86 (eqs. 17 e 18), SI:
      vertedor: Qi = Cw P d^1,5,        Cw = 1,66 (3,0 ingles); P = perimetro da grelha sem barras e sem o lado do meio-fio [m]
      orificio: Qi = Co A (2 g d)^0,5,  Co = 0,67;              A = area livre de abertura [m2]
    Dar d -> capacidade = menor dos dois; Dar Q -> carga d necessaria (maior das duas). Unidades: m, m2, m3/s.
    ATENCAO (revisao F5): na transicao vertedor-orificio a capacidade real e MENOR que a das duas equacoes
    (HEC-12 p. 87; Chart 11, p. 88, curva desenhada entre as retas). O "menor dos dois" so e conservador longe
    da intersecao d* = [Co A sqrt(2g)/(Cw P)]^2; perto dela (aqui: 0,5 d* a 2 d*) a funcao emite aviso.
    Colmatacao nao incluida (HEC-12 Ex. 14, p. 87, adota 50 %); HEC-12 p. 86 desaconselha grelha isolada em sag."""
    _pos(P=P, A=A, Cw=Cw, Co=Co)
    if (d is None) == (Q is None):
        raise ValueError("informar exatamente um entre d e Q")
    av = ["sem fator de colmatacao (HEC-12 p. 86 desaconselha grelha isolada em sag; Ex. 14 p. 87 usa 50 %)",
          "transicao vertedor-orificio nao modelada: adotado o menor (capacidade) ou o maior (carga)"]
    d_int = (Co * A * math.sqrt(2 * G) / (Cw * P)) ** 2  # carga em que vertedor = orificio
    aviso_trans = ("carga na faixa de transicao (0,5-2 x d* = %.3f m): capacidade real MENOR que as duas equacoes "
                   "(HEC-12 p. 87); usar Chart 11 ou ensaio" % d_int)
    if Q is None:
        _pos(d=d)
        if 0.5 * d_int <= d <= 2.0 * d_int:
            av.append(aviso_trans)
        qw = Cw * P * d ** 1.5
        qo = Co * A * math.sqrt(2 * G * d)
        return _res({"d": d, "P": P, "A": A},
                    {"Q_vertedor_m3s": qw, "Q_orificio_m3s": qo, "Q_capacidade_m3s": min(qw, qo),
                     "controle": "vertedor" if qw <= qo else "orificio"}, "HEC-12 p. 86 eqs. 17-18", av)
    _pos(Q=Q)
    dw = (Q / (Cw * P)) ** (2 / 3)
    do = (Q / (Co * A)) ** 2 / (2 * G)
    if 0.5 * d_int <= max(dw, do) <= 2.0 * d_int:
        av.append(aviso_trans)
    return _res({"Q": Q, "P": P, "A": A},
                {"d_vertedor_m": dw, "d_orificio_m": do, "d_necessario_m": max(dw, do),
                 "controle": "vertedor" if dw >= do else "orificio"}, "HEC-12 p. 86 eqs. 17-18 invertidas", av)


# ---------------------------------------------------------------- dreno profundo longitudinal
def dreno_profundo_contribuicao(K, H, d, X):
    """Vazao de contribuicao de um lado do dreno de rebaixamento, por metro de dreno [m3/s/m]:
    q = K (H^2 - d^2) / (2 X)  (Darcy integrada, IME p. 82, eqs. 4.8-4.12).
    K [m/s]; H = altura maxima do lencol [m]; d = altura no dreno [m]; X = distancia dreno-ponto de H [m].
    Dois lados: multiplicar por 2. Validade: Dupuit, regime permanente. A correlacao K = 100 d10^2 do IME p. 83
    (unidade ambigua no texto) nao e implementada."""
    _pos(K=K, X=X)
    if H <= d or d < 0:
        raise ValueError("exige H > d >= 0")
    q = K * (H * H - d * d) / (2 * X)
    return _res({"K": K, "H": H, "d": d, "X": X}, {"q_por_m_m3s_m": q}, "Darcy, IME p. 82 eq. 4.12", [])


def dreno_profundo_capacidade(D, I, C=132.0, metodo="hazen"):
    """Capacidade do tubo dreno [m3/s], IME p. 83 (eqs. 4.13-4.16), SI:
      Scobey:         Q = 0,2113 C D^2,625 I^0,5
      Hazen-Williams: Q = 0,2785 C D^2,63  I^0,54   (C = 132 concreto bem acabado/ceramica, impresso)
    O texto diz 'fluxo a meia secao', mas 0,2113 = 0,269 pi/4: as formulas dao tubo CHEIO (divergencia 10).
    D [m]; I [m/m]. Retorna tambem V."""
    _pos(D=D, I=I, C=C)
    if metodo == "scobey":
        Q = 0.2113 * C * D ** 2.625 * I ** 0.5
    elif metodo == "hazen":
        Q = 0.2785 * C * D ** 2.63 * I ** 0.54
    else:
        raise ValueError("metodo: 'scobey' ou 'hazen'")
    return _res({"D": D, "I": I, "C": C, "metodo": metodo},
                {"Q_cheio_m3s": Q, "V_cheio_m_s": Q / (math.pi * D * D / 4)}, "IME p. 83 eqs. 4.13-4.16",
                ["formulas dao secao plena; texto IME diz meia secao (divergencia 10): fracao de seguranca e decisao de projeto",
                 "C = 132 impresso tambem para Scobey no IME (conferir na imagem)"])


def dreno_profundo_comprimento_critico(D, I, q_por_m, C=132.0, metodo="hazen", fator_capacidade=1.0):
    """Comprimento critico do dreno L = Q_adm / q [m] (IME p. 84, eq. 4.19). Q_adm = fator_capacidade x Q_cheio
    (fator < 1 para atender 'meia secao': decisao de projeto, nao fixada aqui)."""
    _pos(q_por_m=q_por_m, fator_capacidade=fator_capacidade)
    c = dreno_profundo_capacidade(D, I, C, metodo)
    Qadm = fator_capacidade * c["saidas"]["Q_cheio_m3s"]
    return _res({"D": D, "I": I, "q_por_m": q_por_m, "C": C, "metodo": metodo, "fator_capacidade": fator_capacidade},
                {"L_critico_m": Qadm / q_por_m, "Q_adm_m3s": Qadm}, "L = Q/q (IME p. 84 eq. 4.19)", c["avisos"])


def _f_vpm(I_mm_h, contribuicoes):
    return _res({"I_mm_h": I_mm_h}, {"q_por_m_m3s_m": vazao_por_metro(I_mm_h, contribuicoes)},
                "racional por metro (IME p. 53)", [])


def _f_lc(Q_cap, q_por_m):
    return _res({"Q_cap": Q_cap, "q_por_m": q_por_m}, {"L_m": comprimento_critico(Q_cap, q_por_m)},
                "L = Q/q (IME p. 84)", [])


def _plana(fn):
    """Adapta o retorno {entradas, saidas, metodo, avisos} ao formato de tools.dren._cli (saidas planas)."""
    def f(**k):
        r = fn(**k)
        return dict(r["saidas"], metodo=r["metodo"], avisos=r["avisos"])
    f.__doc__ = fn.__doc__
    f.__name__ = fn.__name__
    try:
        import inspect
        f.__signature__ = inspect.signature(fn)
    except (ValueError, TypeError):
        pass
    return f


_FUNCOES = {k: _plana(v) for k, v in {
    "criterio_projeto": criterio_projeto,
    "sarjeta_triangular": sarjeta_triangular,
    "sarjeta_composta": sarjeta_composta,
    "valeta_manning": valeta_manning,
    "vazao_por_metro": _f_vpm,
    "comprimento_critico": _f_lc,
    "valeta_comprimento_critico": valeta_comprimento_critico,
    "folga_valeta": folga_valeta,
    "caixa_coletora_grelha": caixa_coletora_grelha,
    "dreno_profundo_contribuicao": dreno_profundo_contribuicao,
    "dreno_profundo_capacidade": dreno_profundo_capacidade,
    "dreno_profundo_comprimento_critico": dreno_profundo_comprimento_critico,
}.items()}

if __name__ == "__main__":
    _cli.principal("tools.dren.estradas", VERSAO, _FUNCOES)
