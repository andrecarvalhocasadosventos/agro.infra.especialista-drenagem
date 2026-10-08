"""Canais de drenagem (terra, revestidos, rip-rap, composto): Manning, profundidade normal e critica,
Froude com profundidade hidraulica A/T, velocidade admissivel, n e D50 de rip-rap, borda livre,
verificacao tirante x altura da secao e reconciliacao de extensoes.

SI (m, m3/s, m/s). Apenas stdlib. CLI: python -m tools.dren.canais_drenagem --json '{"funcao":
"canal_trapezoidal", "Q": 0.518, "b": 0.6, "z": 1.5, "n": 0.025, "S": 0.00368}'

Fontes (corpus local, referencias/_texto/):
- Manning: Q = A R^(2/3) S^(1/2) / n (SI). Conferido por reproducao de USACE-EM1110-2-1601 App. H Tab. H-1 p. 179
  e das planilhas Salitre/Delmiro (casos de acervo, sem checagem humana).
- Froude: Fr = V / sqrt(g A/T). Nunca com y no lugar de A/T (secao nao retangular).
- USACE-EM1110-2-1601 (Change 1, 1994): Tab. 2-5 p. 25 (velocidades medias maximas, fps), Eq. 3-2 p. 29 (n de
  rip-rap = K D90(min)^(1/6), D em ft, K 0,034/0,036/0,038).
- FHWA-HEC11 (1989): Eq. 6, 7, 8, 9 p. 48-49 (PDF; expoente de C_sf conferido na imagem: 1,5), Exemplo 1 p. 78
  (D50 = 0,43 ft), Eq. 20 p. 166 (n = 0,0395 D50^(1/6), D em ft), faixa de Froude instavel 0,89-1,13 p. 38.
- DNIT-DREN (IPR-724) Tab. 31 p. 131: importada de tools.dren.bueiros (limite_velocidade).
NAO implementado: D30 do EM-1601 Eq. 3-3 (Sf, Cs, CV, CT nao ficam todos impressos); dissipador de saida de
bueiro (D3 do Hidraulico); velocidade admissivel por tensao (HEC-15) por falta de pagina confirmada.
"""
import math

from tools.dren import bueiros as _bue

VERSAO = "0.1.0"
G = 9.81
FT = 0.3048  # m por ft

PROVISORIO_FOLGA = "padrao provisorio (25 % do tirante, criterio do memorial de Delmiro Gouveia), decisao F7"


def _res(saidas, metodo, avisos):
    d = dict(saidas)
    d["metodo"] = metodo
    d["avisos"] = list(avisos)
    return d


def _pos(**kw):
    for k, v in kw.items():
        if v is None or not (v > 0):
            raise ValueError("%s deve ser > 0 (recebido %r)" % (k, v))


# ==========================================================================
# Secao trapezoidal / retangular
# ==========================================================================
def geometria_trapezio(b, z, y):
    """(A, P, T) da secao trapezoidal: A = (b + z y) y; P = b + 2 y sqrt(1+z^2); T = b + 2 z y.
    z = H:V do talude (0 = retangular). Unidades m."""
    if b < 0 or z < 0 or y < 0 or (b == 0 and z == 0):
        raise ValueError("b >= 0, z >= 0, y >= 0 e (b, z) nao ambos nulos")
    return (b + z * y) * y, b + 2 * y * math.sqrt(1 + z * z), b + 2 * z * y


def manning_trapezoidal(b, z, y, n, S):
    """Escoamento uniforme (Manning) numa secao trapezoidal/retangular com tirante y.
    V = R^(2/3) S^(1/2) / n; Fr = V / sqrt(g A/T) (profundidade hidraulica A/T, nunca y).
    Fonte: Manning SI; USACE-EM1110-2-1601 Tab. H-1 p. 179 (conferencia). Validade: n 0,010-0,100; S > 0.
    Saidas: A, P, R, T, Dh (=A/T), V, Q, Fr."""
    _pos(n=n, S=S)
    A, P, T = geometria_trapezio(b, z, y)
    if A <= 0:
        raise ValueError("y deve ser > 0")
    R = A / P
    V = R ** (2.0 / 3.0) * math.sqrt(S) / n
    Dh = A / T
    return {"A": A, "P": P, "R": R, "T": T, "Dh": Dh, "V": V, "Q": V * A, "Fr": V / math.sqrt(G * Dh)}


def _bissecao(f, lo, hi, alvo, it=200):
    # f crescente em y
    while f(hi) < alvo:
        hi *= 2.0
        if hi > 1e4:
            raise ValueError("sem solucao fisica (Q muito grande)")
    for _ in range(it):
        mid = 0.5 * (lo + hi)
        if f(mid) < alvo:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def profundidade_normal(Q, b, z, n, S):
    """Tirante normal y_n [m] por bissecao de Q = A R^(2/3) S^(1/2)/n. Fonte: Manning (SI).
    Validade: Q, n, S > 0."""
    _pos(Q=Q, n=n, S=S)
    return _bissecao(lambda y: manning_trapezoidal(b, z, y, n, S)["Q"], 1e-9, max(1.0, b), Q)


def profundidade_critica(Q, b, z):
    """Tirante critico y_c [m]: Q^2/g = A^3/T (Fr = 1 com profundidade hidraulica A/T).
    Fonte: energia especifica minima (HDS-3; Chow). Validade: Q > 0."""
    _pos(Q=Q)

    def f(y):
        A, _, T = geometria_trapezio(b, z, y)
        return A ** 3 / T
    return _bissecao(f, 1e-9, max(1.0, b), Q * Q / G)


def canal_trapezoidal(Q, b, z, n, S, h_secao=None, fracao_folga=0.25):
    """Canal trapezoidal/retangular de drenagem: tirante normal, critico, V, Fr, regime e (se h_secao) folga.
    Formulas: Manning; Fr = V/sqrt(g A/T). Regime por Fr (sub < 1 < super); aviso na faixa 0,89-1,13
    (FHWA-HEC11 p. 38, escoamento instavel). Folga minima = fracao_folga * y_n (padrao provisorio 25 %,
    decisao F7). Saidas em m, m/s."""
    yn = profundidade_normal(Q, b, z, n, S)
    yc = profundidade_critica(Q, b, z)
    m = manning_trapezoidal(b, z, yn, n, S)
    av = []
    if 0.89 <= m["Fr"] <= 1.13:
        av.append("Fr entre 0,89 e 1,13: escoamento instavel (FHWA-HEC11 p. 38); evitar essa faixa")
    out = {"yn": yn, "yc": yc, "V": m["V"], "A": m["A"], "P": m["P"], "R": m["R"], "T": m["T"],
           "Dh": m["Dh"], "Fr": m["Fr"], "regime": "subcritico" if m["Fr"] < 1 else "supercritico"}
    if h_secao is not None:
        out["verificacao_secao"] = verificar_secao(yn, h_secao, fracao_folga)
        av += out["verificacao_secao"]["avisos"]
    return _res(out, "Manning, y normal e critico, Fr com A/T", av)


def capacidade_trapezoidal(b, z, h, n, S):
    """Capacidade de Manning da secao cheia ate h (planilhas 'Q DRENO'): Q = A R^(2/3) S^(1/2)/n.
    Fonte: Manning SI. Saidas: Q, V, A, Fr."""
    m = manning_trapezoidal(b, z, h, n, S)
    return _res({"Q": m["Q"], "V": m["V"], "A": m["A"], "Fr": m["Fr"]}, "capacidade de Manning a altura h", [])


# ==========================================================================
# Secao composta (canal principal + bermas), metodo da secao dividida
# ==========================================================================
def manning_composto(y, b, z, n, S, h_main, b_berma, z_berma, n_berma):
    """Secao composta simetrica por secao dividida (divided channel): canal principal trapezoidal (b, z, altura
    h_main, n) + duas bermas planas de largura b_berma com talude externo z_berma e rugosidade n_berma.
    Acima de h_main o fluxo se divide por linhas verticais sobre os topos dos taludes do canal (linha de
    interface NAO entra no perimetro molhado). Q = soma de Qi, Qi = Ai Ri^(2/3) S^(1/2)/ni.
    Fr = V/sqrt(g A/T) sobre a secao inteira. Metodo corrente (Chow, cap. 6); sem teste de livro: verificacao
    por consistencia. Aviso se y <= h_main (bermas secas)."""
    _pos(n=n, S=S, n_berma=n_berma, h_main=h_main)
    if y <= 0 or b_berma <= 0 or z_berma < 0:
        raise ValueError("y > 0, b_berma > 0, z_berma >= 0")
    av = []
    hm = min(y, h_main)
    A1, P1, T1 = geometria_trapezio(b, z, hm)
    d = max(0.0, y - h_main)
    A1 += T1 * d
    Q1 = A1 * (A1 / P1) ** (2 / 3) * math.sqrt(S) / n
    A, Q, T = A1, Q1, T1
    if d > 0:
        Ab = (b_berma + z_berma * d / 2.0) * d
        Pb = b_berma + d * math.sqrt(1 + z_berma ** 2)
        Qb = Ab * (Ab / Pb) ** (2 / 3) * math.sqrt(S) / n_berma
        A += 2 * Ab
        Q += 2 * Qb
        T = T1 + 2 * (b_berma + z_berma * d)
    else:
        av.append("y <= h_main: bermas secas; equivale a canal trapezoidal simples")
    V = Q / A
    Fr = V / math.sqrt(G * A / T)
    return _res({"A": A, "T": T, "Dh": A / T, "V": V, "Q": Q, "Fr": Fr},
                "Manning por secao dividida (canal principal + bermas)", av)


def profundidade_normal_composta(Q, b, z, n, S, h_main, b_berma, z_berma, n_berma):
    """Tirante normal [m] da secao composta (bissecao sobre manning_composto)."""
    _pos(Q=Q)
    return _bissecao(lambda y: manning_composto(y, b, z, n, S, h_main, b_berma, z_berma, n_berma)["Q"],
                     1e-6, max(1.0, h_main), Q)


# ==========================================================================
# Velocidade admissivel
# ==========================================================================
# USACE-EM1110-2-1601 Tab. 2-5 (p. 25), fps -> m/s. Nota 2: gramado, manter < 5 fps sem manutencao.
_TAB_2_5_FPS = {
    "areia_fina": 2.0, "areia_grossa": 4.0, "cascalho_fino": 6.0,
    "terra_silte_arenoso": 2.0, "terra_silte_argiloso": 3.5, "terra_argila": 6.0,
    "bermuda_silte_arenoso": 6.0, "bermuda_silte_argiloso": 8.0,
    "kentucky_silte_arenoso": 5.0, "kentucky_silte_argiloso": 7.0,
    "rocha_ruim": 10.0, "arenito_mole": 8.0, "xisto_mole": 3.5, "rocha_boa": 20.0,
}
LIMITE_EM1601 = {k: v * FT for k, v in _TAB_2_5_FPS.items()}
FONTE_EM1601 = "USACE-EM1110-2-1601 Tab. 2-5 p. 25"


def velocidade_admissivel(material, fonte="dnit", criterio="min"):
    """Velocidade media maxima admissivel [m/s]. fonte "dnit": Tab. 31 do DNIT-DREN p. 131 (via
    bueiros.limite_velocidade; criterio min/max da faixa); fonte "em1601": Tab. 2-5 p. 25 (fps -> m/s, valor
    unico). As duas tabelas divergem (ex.: areia fina 0,30-0,40 DNIT x 0,61 EM-1601): informar a escolhida."""
    if fonte == "dnit":
        lim, txt, av = _bue.limite_velocidade(material, "dnit", criterio)
        return _res({"V_adm": lim, "fonte": txt}, "velocidade admissivel (DNIT)", av)
    if fonte == "em1601":
        if material not in LIMITE_EM1601:
            raise ValueError("material desconhecido; opcoes: " + ", ".join(sorted(LIMITE_EM1601)))
        av = []
        if material.startswith(("bermuda", "kentucky")):
            av.append("EM-1601 Tab. 2-5 nota 2: manter V < 5,0 fps (1,52 m/s) sem boa cobertura e manutencao")
        return _res({"V_adm": LIMITE_EM1601[material], "fonte": FONTE_EM1601}, "velocidade admissivel (EM-1601)", av)
    raise ValueError("fonte deve ser 'dnit' ou 'em1601'")


def verificar_velocidade(V, V_max, V_min=None):
    """V <= V_max e (se informado) V >= V_min. V_min nao tem padrao: criterio 'nao informado' deve ser pedido
    ao projetista (casos Delmiro D4 e Salitre N2). Saidas: ok, razoes."""
    _pos(V_max=V_max)
    razoes = []
    if V > V_max:
        razoes.append("V %.3f > V_max %.3f m/s" % (V, V_max))
    if V_min is not None and V < V_min:
        razoes.append("V %.3f < V_min %.3f m/s" % (V, V_min))
    av = [] if V_min is not None else ["V_min nao informada: verificacao de sedimentacao nao feita"]
    return _res({"ok": not razoes, "razoes": razoes}, "verificacao de velocidade", av)


def verificar_limites_alternativos(V, limites):
    """Quando o documento traz dois limites (Salitre: 1,2 do memorial x 1,5 da planilha), reporta o resultado
    para cada um e sinaliza conflito se divergirem. limites: lista de V_max [m/s]."""
    if not limites:
        raise ValueError("informe ao menos um limite")
    res = {str(L): V <= L for L in limites}
    conflito = len(set(res.values())) > 1
    av = ["resultado depende do limite adotado: pedir ao projetista qual vale"] if conflito else []
    return _res({"resultado": res, "conflito": conflito}, "limites alternativos de velocidade", av)


# ==========================================================================
# Rip-rap
# ==========================================================================
K_EM1601 = {"velocidade": 0.034, "media": 0.036, "capacidade": 0.038}


def n_riprap(D, metodo="em1601", uso="media"):
    """n de Manning de rip-rap por Strickler, D em m (convertido para ft: as formulas sao em ft).
    em1601: n = K D90(min)^(1/6), K = 0,034 (velocidade e tamanho de pedra), 0,036 (media) ou 0,038 (capacidade
    e borda livre); D = D90 da curva minima da graduacao [USACE-EM1110-2-1601 Eq. 3-2 p. 29; so S < 2 %;
    nao inclui perdas de forma; +15 % se lancado sob agua].
    hec11: n = 0,0395 D50^(1/6) [FHWA-HEC11 Eq. 20 p. 166 (Anderson et al.)]; D = D50.
    Diametros representativos diferentes (D90 min x D50): divergencia registrada, nao se concilia."""
    _pos(D=D)
    Df = D / FT
    if metodo == "em1601":
        if uso not in K_EM1601:
            raise ValueError("uso deve ser: " + ", ".join(K_EM1601))
        n = K_EM1601[uso] * Df ** (1.0 / 6.0)
        av = ["EM-1601 Eq. 3-2: valida para S < 2 %; D = D90 da curva minima da graduacao"]
    elif metodo == "hec11":
        n = 0.0395 * Df ** (1.0 / 6.0)
        av = ["HEC-11 Eq. 20: D = D50; expoente 1/6 lido do OCR (conferido com a forma de Strickler)"]
    else:
        raise ValueError("metodo deve ser 'em1601' ou 'hec11'")
    return _res({"n": n}, "Strickler (%s)" % metodo,
                av + ["divergencia EM-1601 x HEC-11 (D90 min x D50): ver DIVERGENCIAS"])


def d50_riprap_hec11(V, d, Ss=2.65, SF=1.2, z=None, phi=None, K1=None):
    """D50 de rip-rap de revestimento de canal [m] (FHWA-HEC11 Eq. 6-9, p. 48-49):
        D50 = C * 0,001 V^3 / (d^0,5 K1^1,5)  (V em ft/s, d em ft, D50 em ft; aqui convertidos de SI)
        K1 = [1 - sin^2(theta)/sin^2(phi)]^0,5 (Eq. 7);  C = Csg Csf; Csg = 2,12/(Ss-1)^1,5 (Eq. 8);
        Csf = (SF/1,2)^1,5 (Eq. 9; expoente conferido na imagem do PDF).
    V = velocidade media do canal principal [m/s]; d = profundidade media [m]; z = talude H:V (theta = atan(1/z));
    phi = angulo de repouso [graus]; ou K1 direto. SF padrao 1,2 (Tab. 1 p. 31: 1,0-1,2 reto; ver R/W p. 50).
    Validade: escoamento uniforme/gradualmente variado, canal reto ou curva suave; nao vale para dissipador de
    bueiro (D3 do Hidraulico). Exige theta < phi."""
    _pos(V=V, d=d, Ss=Ss, SF=SF)
    if Ss <= 1:
        raise ValueError("Ss deve ser > 1")
    av = []
    if K1 is None:
        if z is None or phi is None:
            raise ValueError("informe K1 ou (z e phi)")
        _pos(z=z, phi=phi)
        th = math.atan(1.0 / z)
        ph = math.radians(phi)
        if th >= ph:
            raise ValueError("talude mais ingreme que o angulo de repouso: rip-rap instavel (theta >= phi)")
        K1 = math.sqrt(1.0 - math.sin(th) ** 2 / math.sin(ph) ** 2)
    _pos(K1=K1)
    if z is not None and z < 1.5:
        av.append("talude mais ingreme que 1V:1,5H: HEC-11/EM-1601 recomendam 1,5H:1V ou mais suave")
    if SF < 1.0:
        av.append("SF < 1: instavel por definicao (HEC-11 p. 49)")
    Vf, df = V / FT, d / FT
    d50 = 0.001 * Vf ** 3 / (math.sqrt(df) * K1 ** 1.5)
    C = 2.12 / (Ss - 1) ** 1.5 * (SF / 1.2) ** 1.5
    return _res({"D50": d50 * C * FT, "K1": K1, "C": C, "D50_base_m": d50 * FT},
                "HEC-11 Eq. 6 (D50 de rip-rap)",
                av + ["SF por curvatura: R/W > 30 -> 1,2; 30-10 -> 1,3-1,6; < 10 -> 1,7 (p. 50)"])


# ==========================================================================
# Borda livre e verificacoes
# ==========================================================================
def borda_livre(y, fracao=0.25):
    """Folga minima = fracao * y [m]. Padrao provisorio 0,25 (memorial de Delmiro Gouveia, doc 1520 p. 129:
    'folga minima de 25 % do tirante'); NAO e norma: decisao F7. Outros criterios de borda livre de canal
    (USBR, EM-1601 p. 18-23) sao do Hidraulico/consulta direta."""
    _pos(y=y, fracao=fracao)
    return _res({"folga_min": fracao * y, "altura_min": y * (1 + fracao)}, "borda livre = fracao x tirante",
                [PROVISORIO_FOLGA] if fracao == 0.25 else [])


def verificar_secao(y, h_secao, fracao_folga=0.25):
    """Tirante x altura da secao: folga = h_secao - y; falha se folga < 0 (transborda) ou < fracao * y.
    Caso Delmiro DT-2.23.1: ZTT01 h 0,20 m com y 0,331 m (folga -0,131). Saidas: folga, folga_min, ok,
    transborda."""
    _pos(y=y, h_secao=h_secao)
    folga = h_secao - y
    fmin = fracao_folga * y
    av = []
    if folga < 0:
        av.append("tirante %.3f m maior que a altura da secao %.3f m: transborda" % (y, h_secao))
    elif folga < fmin:
        av.append("folga %.3f m menor que o minimo %.3f m (%g %% do tirante)" % (folga, fmin, 100 * fracao_folga))
    if fracao_folga == 0.25:
        av.append(PROVISORIO_FOLGA)
    return _res({"folga": folga, "folga_min": fmin, "ok": folga >= fmin, "transborda": folga < 0},
                "verificacao tirante x altura da secao", av)


def verificar_trechos(trechos, fracao_folga=0.25):
    """Lista de trechos {"nome","Q","b","z","n","S","h"} -> tirante de Manning, folga e criterio; devolve a
    lista, a contagem e o percentual de trechos fora do criterio (em vez de aceitar 'folgas menores sao
    admitidas'). Trecho que transborda e tratado como falha (caso Delmiro D1/D2)."""
    if not trechos:
        raise ValueError("lista de trechos vazia")
    linhas, falhas, transb = [], 0, 0
    for t in trechos:
        yn = profundidade_normal(t["Q"], t["b"], t["z"], t["n"], t["S"])
        v = verificar_secao(yn, t["h"], fracao_folga)
        linhas.append({"nome": t.get("nome"), "yn": yn, "folga": v["folga"], "ok": v["ok"],
                       "transborda": v["transborda"]})
        falhas += (not v["ok"])
        transb += v["transborda"]
    pct = 100.0 * falhas / len(trechos)
    av = []
    if transb:
        av.append("%d trecho(s) com tirante > altura da secao" % transb)
    if falhas:
        av.append("%d de %d trechos (%.1f %%) fora do criterio de folga" % (falhas, len(trechos), pct))
    return _res({"trechos": linhas, "n_falhas": falhas, "n_transbordam": transb, "pct_falhas": pct},
                "verificacao em lote tirante x secao x folga", av)


def reconciliar_extensoes(parcelas, total_declarado, tol=0.01):
    """Soma de parcelas [m] x total declarado. Se divergem, informa a diferenca e se alguma parcela coincide
    com ela (caso Salitre N1: total 72.858,41 = Recreio + Tourao, falta Mulungu 2.026,00; soma correta
    74.884,41). tol em m. Saidas: soma, diferenca (soma - declarado), fecha, parcela_omitida."""
    if not parcelas:
        raise ValueError("parcelas vazias")
    soma = math.fsum(parcelas.values() if isinstance(parcelas, dict) else parcelas)
    dif = soma - total_declarado
    omit = None
    if abs(dif) > tol and isinstance(parcelas, dict):
        for k, v in parcelas.items():
            if abs(v - dif) <= tol:
                omit = k
    av = []
    if abs(dif) > tol:
        av.append("total declarado nao fecha: diferenca %.2f m%s" % (dif, " (= parcela '%s')" % omit if omit else ""))
    return _res({"soma": soma, "diferenca": dif, "fecha": abs(dif) <= tol, "parcela_omitida": omit},
                "reconciliacao de extensoes", av)


FUNCOES = {
    "canal_trapezoidal": canal_trapezoidal,
    "manning_trapezoidal": lambda b, z, y, n, S: _res(manning_trapezoidal(b, z, y, n, S), "Manning", []),
    "profundidade_normal": lambda Q, b, z, n, S: _res({"yn": profundidade_normal(Q, b, z, n, S)}, "Manning", []),
    "profundidade_critica": lambda Q, b, z: _res({"yc": profundidade_critica(Q, b, z)}, "Q2/g = A3/T", []),
    "capacidade_trapezoidal": capacidade_trapezoidal,
    "manning_composto": manning_composto,
    "profundidade_normal_composta": lambda **k: _res({"yn": profundidade_normal_composta(**k)}, "secao dividida", []),
    "velocidade_admissivel": velocidade_admissivel,
    "verificar_velocidade": verificar_velocidade,
    "verificar_limites_alternativos": verificar_limites_alternativos,
    "n_riprap": n_riprap,
    "d50_riprap_hec11": d50_riprap_hec11,
    "borda_livre": borda_livre,
    "verificar_secao": verificar_secao,
    "verificar_trechos": verificar_trechos,
    "reconciliar_extensoes": reconciliar_extensoes,
}

if __name__ == "__main__":
    from tools.dren._cli import principal
    principal("tools.dren.canais_drenagem", VERSAO, FUNCOES)
