"""Drenagem subsuperficial: espacamento de drenos (Hooghoudt, Donnan, Ernst, Glover-Dumm),
vazao e capacidade de tubos drenos, dreno de fundo de canal revestido (subpressao), furo em
geomembrana, criterio de filtro (Terzaghi) e tabelas indicativas.

Unidades SI: m, m/d (recarga q e condutividade K, como em ILRI/USBR), m3/s para vazoes de tubo;
tempo em dias. Apenas stdlib. CLI: python -m tools.dren.drenos --json '{"funcao":
"hooghoudt_espacamento", "q": 0.002, "K": 1.0, "h": 0.6, "D": 5.0, "r": 0.1}'

Fontes (corpus local, referencias/):
- USBR, Drainage Manual (1993), cap. V: secao 5-5 (profundidade equivalente de Hooghoudt, forma de
  Moody, p. 154-155 do livro, PDF 173-174), 5-8 (exemplo transiente, p. 168), 5-11 (Donnan, p. 169-170).
- ILRI Pub. 16 (Drainage Principles and Applications) NAO esta no corpus: Ernst e a forma de
  Glover-Dumm com fator 1,16 estao declarados "a confirmar" nas docstrings.
- FAO Irrig. & Drainage Paper 38 NAO esta no corpus: tabelas indicativas marcadas "a confirmar".
Gabaritos dos casos: casos/drenagem_dissipadores (CSB doc 1341, Xingo doc 1419, Iuiu doc 1051).
"""
import math

VERSAO = "0.1.0"
G = 9.81

# ==========================================================================
# Hooghoudt / Donnan (regime permanente)
# ==========================================================================


def d_equivalente_hooghoudt(d, L, r):
    """Profundidade equivalente de Hooghoudt d_e [m] (forma de Moody, 1966).

    d_e = d / (1 + (d/L)(2,55 ln(d/r) - C)),  C = 3,55 - 1,6 d/L + 2 (d/L)^2,   0 < d/L <= 0,31
    d_e = L / (2,55 (ln(L/r) - 1,15)),                                           d/L  > 0,31
    d = distancia dreno-barreira [m]; L = espacamento [m]; r = raio efetivo do dreno (tubo mais
    envoltorio) [m]. 2,55 = 8/pi. Fonte: USBR Drainage Manual (1993), secao 5-5, p. 155 (PDF 174);
    as curvas Fig. 5-5/5-6 do manual foram feitas para r = 0,18 m. Verificacao: K=0,305 m/d,
    d=6,1 m, L=91 m, r=0,18 m -> d_e = 4,45 m (manual: 4,4 m, p. 168).
    Validade: d_e <= d (limitado); r << d. Regime permanente.
    """
    if d <= 0:
        return 0.0
    if L <= 0 or r <= 0:
        raise ValueError("L e r devem ser positivos")
    x = d / L
    if x <= 0.31:
        C = 3.55 - 1.6 * x + 2.0 * x * x
        de = d / (1.0 + x * (2.55 * math.log(d / r) - C))
    else:
        de = L / (2.55 * (math.log(L / r) - 1.15))
    return min(de, d)


def hooghoudt_espacamento(q, h, D, r, K=None, K_acima=None, K_abaixo=None, tol=1e-6, itmax=200):
    """Espacamento de drenos L [m] por Hooghoudt (regime permanente), com d_e iterativo.

    q = recarga (descarga especifica) [m/d]; h = carga no meio-vao acima do nivel do dreno [m];
    D = profundidade da camada impermeavel abaixo do dreno [m]; r = raio efetivo do dreno [m];
    K = condutividade [m/d] (solo homogeneo) ou K_acima (entre o nivel do dreno e o freatico) e
    K_abaixo (abaixo do dreno).
        L^2 = (8 K_abaixo d_e h + 4 K_acima h^2) / q
    d_e (Moody) vem de d_equivalente_hooghoudt e depende de L: iteracao de ponto fixo ate variacao
    relativa < tol. Fonte: Hooghoudt (1940); USBR Drainage Manual (1993) 5-5 e 5-11 (Donnan com d
    trocado por d_e); d_e pela forma de Moody (USBR p.155). Alternativa: tabelas do ILRI (nao no corpus).
    Validade: drenos paralelos equidistantes, solo com K constante por camada, regime permanente
    (recarga constante). Espacamentos muito pequenos (< ~10 m) invalidam a hipotese permanente.
    """
    if K is not None:
        K1 = K2 = K
    else:
        if K_acima is None or K_abaixo is None:
            raise ValueError("informe K ou (K_acima e K_abaixo)")
        K1, K2 = K_acima, K_abaixo
    if min(q, h, K1, K2, r) <= 0 or D < 0:
        raise ValueError("q, h, K, r devem ser positivos e D >= 0")
    L = math.sqrt(4.0 * K1 * h * h / q + 8.0 * K2 * D * h / q)  # semente: d_e = D
    de = D
    it = 0
    for it in range(1, itmax + 1):
        de = d_equivalente_hooghoudt(D, L, r) if D > 0 else 0.0
        Ln = math.sqrt((8.0 * K2 * de * h + 4.0 * K1 * h * h) / q)
        if abs(Ln - L) <= tol * L:
            L = Ln
            break
        L = 0.5 * (L + Ln)
    avisos = []
    if L < 10.0:
        avisos.append("L=%.1f m < 10 m: hipotese de regime permanente e recarga uniforme pouco confiavel" % L)
    if D > 0 and de < 0.2 * D:
        avisos.append("d_e << D: dreno pouco eficiente em camada espessa; confira r e D")
    avisos.append("regime permanente: recarga q constante (ver glover_dumm_* para nao permanente)")
    return {"L": L, "d_e": de, "iteracoes": it, "q": q, "h": h, "D": D,
            "metodo": "Hooghoudt L^2=(8 K2 d_e h+4 K1 h^2)/q, d_e Moody (USBR Drainage Manual 5-5)",
            "avisos": avisos}


def donnan_espacamento(K, a, b, q, dreno_na_barreira=False):
    """Formula de Donnan (USBR): L^2 = 4 K (b^2 - a^2) / q  [m].

    a = distancia dreno-barreira; b = distancia freatico maximo-barreira (b = a + h);
    q = recarga [m/d]; para dreno SOBRE a barreira (a=0) o USBR divide a recarga por 2
    (dreno_na_barreira=True). Fonte: USBR Drainage Manual (1993), secao 5-11, p. 169-171.
    Exemplo do manual: K=3,05 m/d, a=6,7, b=7,92, q=0,025/14 m/d -> L = 347 m.
    Concorda com o metodo transiente em +-20 % segundo o manual; deve ser corrigido por convergencia
    (trocar a por d_e de Hooghoudt)."""
    if min(K, q) <= 0 or b <= a:
        raise ValueError("K, q > 0 e b > a")
    qq = q / 2.0 if dreno_na_barreira else q
    L = math.sqrt(4.0 * K * (b * b - a * a) / qq)
    return {"L": L, "metodo": "Donnan L^2=4K(b^2-a^2)/q (USBR 5-11)",
            "avisos": ["sem correcao de convergencia; usar d_e (Hooghoudt) no lugar de a para dreno acima da barreira"]}


def ernst_espacamento(q, h, Dv, Kv, KD_h, Dr, Kr, r, a=1.0, L_max=2000.0):
    """Espacamento L [m] de Ernst (1962) para solo estratificado, por bisseccao em
        h = q Dv/Kv + q L^2/(8 KD_h) + q L W_r/(pi Kr),   W_r = ln(a Dr / u),  u = 2 pi r.

    Resistencias vertical (Dv espessura onde o fluxo e vertical, Kv media vertical [m/d]), horizontal
    (KD_h = soma K_i D_i das camadas que transmitem fluxo horizontal [m2/d]) e radial (Dr espessura da
    zona radial [m]; Kr [m/d]; a = fator geometrico, 1 para solo homogeneo; u = perimetro molhado [m]).
    h = carga no meio-vao acima do nivel do dreno [m]; q em m/d. Fonte: Ernst (1962), conforme ILRI
    Pub. 16 (cap. de drenagem de solos estratificados) -- A CONFIRMAR: ILRI 16 nao esta no corpus;
    forma conferida por equivalencia com o termo radial de Hooghoudt (h_r ~ q L ln(L/(pi r))/(pi K)).
    Validade: drenos paralelos, regime permanente; para varios solos o fator a vem de tabela do ILRI.
    """
    if min(q, h, Kv, KD_h, Kr, r, Dr) <= 0 or Dv < 0:
        raise ValueError("parametros positivos")
    u = 2.0 * math.pi * r
    Wr = math.log(a * Dr / u)
    if Wr <= 0:
        raise ValueError("a*Dr/u <= 1: resistencia radial nao positiva; revise Dr, r")

    def hcalc(L):
        return q * Dv / Kv + q * L * L / (8.0 * KD_h) + q * L * Wr / (math.pi * Kr)

    if hcalc(0.0) >= h:
        raise ValueError("resistencia vertical q Dv/Kv ja excede h: nao existe L positivo")
    lo, hi = 0.0, L_max
    if hcalc(hi) < h:
        raise ValueError("L > L_max=%g m" % L_max)
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if hcalc(mid) < h:
            lo = mid
        else:
            hi = mid
    L = 0.5 * (lo + hi)
    return {"L": L, "h_vertical": q * Dv / Kv, "h_horizontal": q * L * L / (8.0 * KD_h),
            "h_radial": q * L * Wr / (math.pi * Kr), "W_r": Wr,
            "metodo": "Ernst h = h_v + h_h + h_r (a confirmar em ILRI 16)",
            "avisos": ["Ernst: fonte primaria (ILRI 16) fora do corpus; a confirmar",
                       "regime permanente; Kirkham nao implementado (usar Hooghoudt/Ernst)"]}


# ==========================================================================
# Glover-Dumm (nao permanente)
# ==========================================================================
def glover_dumm_altura(t, h0, K, d_med, mu, L):
    """Altura do freatico no meio-vao no instante t [m] (Glover-Dumm, 1o termo):
        h_t = 1,16 h0 exp(-t/j),  j = mu L^2 / (pi^2 K d_med).
    h0 = carga inicial [m]; K [m/d]; d_med = profundidade media de fluxo [m] (d_e + h0/2 conforme
    USBR, ou d_e do Hooghoudt); mu = porosidade drenavel (rendimento especifico); L [m]; t [d].
    Fonte: Glover (em Dumm, 1954); fator 1,16 conforme a forma usual do ILRI (A CONFIRMAR); o
    manual do USBR (Drainage Manual 5-10, p. 168) usa a curva equivalente KD't/(S L^2)=0,096
    para y/y0=0,444 (pi^2*0,096 = 0,95 ~ ln(1,16/0,444) = 0,96). Validade: t/j > ~0,2; drenos
    paralelos acima de barreira; recarga nula no periodo."""
    if min(K, d_med, mu, L, h0) <= 0:
        raise ValueError("parametros positivos")
    j = mu * L * L / (math.pi ** 2 * K * d_med)
    return 1.16 * h0 * math.exp(-t / j)


def glover_dumm_tempo(h0, ht, K, d_med, mu, L):
    """Tempo de rebaixamento t [d] para o freatico no meio-vao ir de h0 a ht (inverso de
    glover_dumm_altura): t = j ln(1,16 h0/ht). Exemplo USBR (5-10, ex.1): K=0,305, d_e=4,4 m, h0=2,7 m
    (D'=d_e+h0/2=5,75 m), mu=0,07, L=91 m, ht=1,2 m -> t = 32 d (manual 31,8 d)."""
    if ht >= 1.16 * h0:
        return {"t": 0.0, "avisos": ["ht >= 1,16 h0: sem rebaixamento"], "metodo": "Glover-Dumm"}
    j = mu * L * L / (math.pi ** 2 * K * d_med)
    t = j * math.log(1.16 * h0 / ht)
    av = []
    if t / j < 0.2:
        av.append("t/j < 0,2: fora da validade do 1o termo da serie")
    return {"t": t, "j": j, "metodo": "Glover-Dumm h_t=1,16 h0 exp(-t/j) (1o termo; a confirmar em ILRI 16)",
            "avisos": av}


def glover_dumm_espacamento(h0, ht, t, K, d_med, mu):
    """Espacamento L [m] que rebaixa o freatico de h0 a ht em t dias (Glover-Dumm):
    L = pi sqrt(K d_med t / (mu ln(1,16 h0/ht))). d_med = d_e + h0/2 (aproximacao; d_e depende de L,
    use d_equivalente_hooghoudt para iterar). Mesma validade de glover_dumm_altura."""
    if ht >= 1.16 * h0:
        raise ValueError("ht >= 1,16 h0")
    L = math.pi * math.sqrt(K * d_med * t / (mu * math.log(1.16 * h0 / ht)))
    return {"L": L, "metodo": "Glover-Dumm (1o termo)",
            "avisos": ["d_med fixo: iterar com d_equivalente_hooghoudt se d_e variar com L"]}


def tempo_de_drenagem(h0, ht, K, D, r, mu, L):
    """Tempo (d) de rebaixamento para espacamento L dado: calcula d_e (Moody) e d_med = d_e + h0/2 e
    aplica glover_dumm_tempo. D = profundidade da barreira abaixo do dreno [m]."""
    de = d_equivalente_hooghoudt(D, L, r)
    res = glover_dumm_tempo(h0, ht, K, de + h0 / 2.0, mu, L)
    res["d_e"] = de
    return res


# ==========================================================================
# Vazao e tubos
# ==========================================================================
def vazao_de_dreno(L, q, comprimento):
    """Vazao de um dreno lateral: Q = q L comprimento  [m3/d] e [m3/s]; q em m/d, L e comprimento em m
    (area drenada = espacamento x comprimento do dreno)."""
    Qd = q * L * comprimento
    return {"Q_m3_dia": Qd, "Q": Qd / 86400.0, "area_m2": L * comprimento,
            "metodo": "Q = q L comprimento", "avisos": []}


def _manning_cheio(D, S, n):
    return 0.31169 / n * D ** (8.0 / 3.0) * math.sqrt(S)  # (1/n)(pi D^2/4)(D/4)^(2/3) S^0.5


def capacidade_tubo_dreno(D, S, n=0.016, formula="manning"):
    """Capacidade Q [m3/s] de tubo dreno circular (D [m], S [m/m]).

    formula = 'manning': secao plena, Q = (0,3117/n) D^(8/3) S^0,5 (n = 0,016 corrugado; 0,011 liso).
    formula = 'xingo' : LEGADO Q = 33,5 D^2,67 S^0,5 (Xingo Lote I, doc 1419:21, tubo PEAD perfurado,
    y/d = 0,938; D em m, Q em m3/s -- unidades A CONFIRMAR; reproduz 0,0135 m3/s para D=0,30, S=1e-4;
    equivale a Manning pleno com n ~ 0,0093 e nao e uma formula de Manning).
    Fonte: Manning (Chow, cap. 5); caso Xingo. Validade: tubo reto, S constante, sem entrada de ar.
    """
    f = formula.lower()
    if D <= 0 or S <= 0:
        raise ValueError("D e S positivos")
    if f == "manning":
        Q = _manning_cheio(D, S, n)
        av = ["Manning pleno; para drenos agricolas ILRI/USBR usam fracao do cheio e perdas de entrada"]
    elif f == "xingo":
        Q = 33.5 * D ** 2.67 * math.sqrt(S)
        n_imp = 0.31169 * D ** (8.0 / 3.0) * math.sqrt(S) / Q
        av = ["legado Xingo: unidades a confirmar; n pleno implicito=%.4f" % n_imp]
    else:
        raise ValueError("formula: 'manning' ou 'xingo'")
    return {"Q": Q, "metodo": "capacidade de tubo dreno (%s)" % f, "avisos": av}


def diametro_minimo_dreno(Q, S, n=0.016, formula="manning", comerciais=(0.05, 0.065, 0.08, 0.10, 0.125,
                                                                        0.15, 0.20, 0.25, 0.30, 0.40,
                                                                        0.50, 0.60)):
    """Diametro minimo [m] para a vazao Q [m3/s] (inversao de capacidade_tubo_dreno por bisseccao) e
    o primeiro diametro comercial >= calculado (lista indicativa de diametros nominais)."""
    lo, hi = 1e-3, 5.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if capacidade_tubo_dreno(mid, S, n, formula)["Q"] < Q:
            lo = mid
        else:
            hi = mid
    Dm = 0.5 * (lo + hi)
    com = next((d for d in comerciais if d >= Dm), None)
    av = [] if com else ["acima do maior diametro comercial listado: use tubos em paralelo"]
    return {"D_minimo": Dm, "D_comercial": com, "metodo": "inversao de capacidade_tubo_dreno (%s)" % formula,
            "avisos": av}


# ==========================================================================
# Dreno de fundo de canal revestido (subpressao): CSB e Xingo
# ==========================================================================
# CSB GEOHIDRO 2016 (doc 1341:76): capacidade por tubo PVC ranhurado [m3/s] (min, max); valores sem
# ancoragem no extrator ("conferir pag. 76").
TUBOS_CSB = {0.150: (0.004, 0.005), 0.300: (0.025, 0.031), 0.400: (0.050, 0.064), 0.500: (0.082, 0.101)}


def selecionar_tubo_csb(Q_tubo):
    """Menor DN [m] da tabela CSB (TUBOS_CSB) com capacidade maxima >= Q_tubo. 'no_limite' = Q_tubo
    acima do limite inferior da faixa de capacidade (usar com cautela)."""
    for dn in sorted(TUBOS_CSB):
        lo, hi = TUBOS_CSB[dn]
        if Q_tubo <= hi:
            return {"DN": dn, "capacidade_faixa": (lo, hi), "no_limite": Q_tubo > lo}
    return {"DN": None, "capacidade_faixa": None, "no_limite": True}


def vazao_por_furo_geomembrana(d_furo, carga, Cd=0.634):
    """Vazao por furo em geomembrana: Q = Cd A sqrt(2 g H) [m3/s] (orificio), A = pi d^2/4.
    Cd = 0,634 (Porto, 1999, conforme Xingo doc 1419:20); d_furo = 0,008 m no caso. Exemplo: H=3 m ->
    2,44e-4 m3/s (g=9,81; o caso usa 9,8)."""
    A = math.pi * d_furo ** 2 / 4.0
    Q = Cd * A * math.sqrt(2.0 * G * carga)
    return {"Q_furo": Q, "A_furo": A, "metodo": "orificio Q=Cd A sqrt(2 g H)",
            "avisos": ["Cd e frequencia de furos sao premissas de projeto (1 furo/2400 m2 no Xingo)"]}


def vazao_infiltracao_geomembrana(d_furo, carga, area_por_m, area_por_furo=2400.0, Cd=0.634):
    """Vazao por metro de canal [m3/s/m]: Q1m = Qc A1 / area_por_furo (Xingo doc 1419:20).
    area_por_m = area de revestimento por metro de canal [m2/m]."""
    Qc = vazao_por_furo_geomembrana(d_furo, carga, Cd)["Q_furo"]
    return {"Q_por_m": Qc * area_por_m / area_por_furo, "Q_furo": Qc, "metodo": "Xingo Q1m=Qc A1/2400",
            "avisos": []}


def dreno_de_fundo_de_canal_revestido(q_por_m, comprimento, n_tubos=2, i=None, n=0.011,
                                      area_por_tubo=None, q_infiltracao_area=None, D=None):
    """Dreno longitudinal de fundo contra subpressao (CSB doc 1341:74-77; Xingo doc 1419:18-22).

    Vazao acumulada Q = q_por_m * comprimento [m3/s] (CSB: q = 6e-5 m3/s por m de canal, USBR
    0,0213 m3/m2/24 h); dividida em n_tubos (CSB: 2 trincheiras). Retorna Q por tubo, DN minimo da
    tabela CSB (TUBOS_CSB, faixa de capacidade) e, se i for dado, o D minimo por Manning pleno
    (n=0,011) e pela formula legada do Xingo. Alternativa: q_infiltracao_area [m3/m2/s] x
    area_por_tubo [m2] para obter Q do tubo (q_por_m=None). MVF (Flap Valve Weep, USBR): 30 % da
    extensao, 2 MVF a cada ~10 m => n_MVF = 2 ceil(0,30 L/10) por trecho (regra INTERPRETATIVA do
    gabarito). Validade: anteprojeto; capacidades dos tubos CSB sem ancoragem (conferir 1341:76).
    """
    if q_por_m is None:
        if q_infiltracao_area is None or area_por_tubo is None:
            raise ValueError("informe q_por_m ou (q_infiltracao_area e area_por_tubo)")
        Q_tubo = q_infiltracao_area * area_por_tubo
        Q = Q_tubo * n_tubos
    else:
        Q = q_por_m * comprimento
        Q_tubo = Q / n_tubos
    sel = selecionar_tubo_csb(Q_tubo)
    res = {"Q_total": Q, "Q_por_tubo": Q_tubo, "n_tubos": n_tubos, "tubo_csb": sel,
           "n_MVF": 2 * math.ceil(0.30 * comprimento / 10.0),
           "metodo": "dreno de fundo: Q = q L; DN pela tabela CSB (faixa)", "avisos": []}
    if sel["no_limite"] and sel["DN"] is not None:
        res["avisos"].append("Q por tubo acima do limite inferior da faixa de capacidade do DN%d" %
                             round(sel["DN"] * 1000))
    if sel["DN"] is None:
        res["avisos"].append("Q por tubo acima da tabela CSB: aumentar n_tubos ou criar saidas intermediarias")
    if i is not None:
        res["D_manning"] = diametro_minimo_dreno(Q_tubo, i, n, "manning")["D_minimo"]
        res["D_xingo_legado"] = diametro_minimo_dreno(Q_tubo, i, formula="xingo")["D_minimo"]
        res["avisos"].append("CSB aplica Manning com gradiente de pressao (nao a declividade do tubo): "
                             "D por declividade i e conservador")
    if D is not None and i is not None:
        res["capacidade_tubo_D"] = capacidade_tubo_dreno(D, i, n)["Q"]
    return res


# ==========================================================================
# Filtro (Terzaghi)
# ==========================================================================
def criterio_de_filtro_hidraulico(D15_filtro, D85_solo, D15_solo, fator=4.0):
    """Criterio de filtro de Terzaghi (granulometrico, hidraulico):
        retencao: D15f / D85s <= fator (4 a 5);   permeabilidade: D15f / D15s >= fator (4 a 5).
    fator = 4 (conservador) ou 5. Fonte: Terzaghi & Peck; USBR Drainage Manual (envoltorios) -- a
    confirmar a pagina. Adicional USBR: D15f/D15s <= 40 (nao entupir/segregar). So avalia razoes de
    D15/D85; nao substitui verificacao de D50, uniformidade, segregacao nem de solos dispersivos/
    argilosos. Envoltorio de geotextil: [DELEGAR: geotecnia]."""
    ret = D15_filtro / D85_solo
    per = D15_filtro / D15_solo
    ok_ret = ret <= fator
    ok_per = per >= fator
    av = ["geotextil como envoltorio: [DELEGAR: geotecnia]"]
    if per > 40.0:
        av.append("D15f/D15s > 40: filtro muito grosseiro (risco de migracao); conferir criterio USBR")
    return {"retencao_D15f_D85s": ret, "permeabilidade_D15f_D15s": per, "atende_retencao": ok_ret,
            "atende_permeabilidade": ok_per, "atende": ok_ret and ok_per,
            "metodo": "Terzaghi D15f<=%g D85s e D15f>=%g D15s" % (fator, fator), "avisos": av}


# ==========================================================================
# Tabelas indicativas
# ==========================================================================
# Porosidade drenavel mu (rendimento especifico), faixas indicativas. A CONFIRMAR (USBR Drainage Manual
# Fig. 2-4 relaciona mu a K; valores abaixo sao ordens de grandeza usuais).
POROSIDADE_DRENAVEL = {"areia": (0.15, 0.30), "areia_franca": (0.10, 0.20), "franco": (0.05, 0.12),
                       "franco_argiloso": (0.03, 0.08), "argila": (0.01, 0.05)}

# Profundidade e espacamento indicativos por classe de K [m/d] (ordem de grandeza FAO 38/ILRI; A CONFIRMAR).
# (K_min, K_max, profundidade_dreno_m, espacamento_m)
RECOMENDACAO_INDICATIVA = [
    (0.0, 0.1, (1.0, 1.5), (10.0, 20.0)),
    (0.1, 0.5, (1.2, 1.8), (20.0, 40.0)),
    (0.5, 2.0, (1.2, 2.0), (35.0, 80.0)),
    (2.0, 10.0, (1.5, 2.2), (60.0, 150.0)),
]


def porosidade_drenavel(textura):
    """Faixa indicativa (min, max) de porosidade drenavel por textura. TABELA INDICATIVA, a confirmar."""
    t = textura.lower()
    if t not in POROSIDADE_DRENAVEL:
        raise ValueError("textura: %s" % ", ".join(sorted(POROSIDADE_DRENAVEL)))
    lo, hi = POROSIDADE_DRENAVEL[t]
    return {"mu_min": lo, "mu_max": hi, "mu_medio": 0.5 * (lo + hi), "metodo": "tabela indicativa",
            "avisos": ["indicativo; medir in situ (USBR Drainage Manual cap. II) -- fonte a confirmar"]}


def recomendacao_indicativa(K):
    """Profundidade do dreno e espacamento tipicos por K [m/d]. SO INDICATIVO (FAO 38/ILRI, a confirmar):
    nao substitui dimensionamento por Hooghoudt/Ernst com recarga e carga de projeto."""
    for lo, hi, prof, esp in RECOMENDACAO_INDICATIVA:
        if lo <= K < hi:
            return {"profundidade_m": prof, "espacamento_m": esp, "metodo": "tabela indicativa por K",
                    "avisos": ["INDICATIVO: nao usar em projeto; FAO 38 fora do corpus (a confirmar)"]}
    raise ValueError("K fora de 0-10 m/d")


def diagnostico_drenabilidade(K, prof_barreira):
    """Teste de decisao de consistencia com o diagnostico do Vale do Iuiu 2002 (doc 1051:162-163):
    K entre ~0,4 e 2,1 m/d e barreira > 1,5 m => drenabilidade boa/restrita => sem drenagem subterranea
    parcelar. Limites do caso do projeto (NAO norma); K < 0,1 ou barreira < 1,0 m => pobre/critica."""
    if K >= 0.4 and prof_barreira > 1.5:
        classe, drenar = "boa/restrita", False
    elif K < 0.1 or prof_barreira < 1.0:
        classe, drenar = "pobre/critica", False
    else:
        classe, drenar = "restrita/pobre", True
    av = ["limites do projeto Iuiu 2002, nao de norma; a classe 'pobre/critica' indica outros usos (pastagem)"]
    if K > 2.1:
        av.append("K > 2,1 m/d: acima da faixa investigada no Iuiu")
    return {"classe": classe, "drenagem_subterranea_necessaria": drenar,
            "metodo": "diagnostico Iuiu 2002 (consistencia)", "avisos": av}


FUNCOES = {
    "hooghoudt_espacamento": hooghoudt_espacamento,
    "d_equivalente_hooghoudt": lambda d, L, r: {"d_e": d_equivalente_hooghoudt(d, L, r),
                                               "metodo": "Moody (USBR 5-5)", "avisos": []},
    "donnan_espacamento": donnan_espacamento,
    "ernst_espacamento": ernst_espacamento,
    "glover_dumm_altura": lambda t, h0, K, d_med, mu, L: {"h_t": glover_dumm_altura(t, h0, K, d_med, mu, L),
                                                         "metodo": "Glover-Dumm", "avisos": []},
    "glover_dumm_tempo": glover_dumm_tempo,
    "glover_dumm_espacamento": glover_dumm_espacamento,
    "tempo_de_drenagem": tempo_de_drenagem,
    "vazao_de_dreno": vazao_de_dreno,
    "capacidade_tubo_dreno": capacidade_tubo_dreno,
    "diametro_minimo_dreno": diametro_minimo_dreno,
    "dreno_de_fundo_de_canal_revestido": dreno_de_fundo_de_canal_revestido,
    "vazao_por_furo_geomembrana": vazao_por_furo_geomembrana,
    "vazao_infiltracao_geomembrana": vazao_infiltracao_geomembrana,
    "criterio_de_filtro_hidraulico": criterio_de_filtro_hidraulico,
    "porosidade_drenavel": porosidade_drenavel,
    "recomendacao_indicativa": recomendacao_indicativa,
    "diagnostico_drenabilidade": diagnostico_drenabilidade,
}

if __name__ == "__main__":
    from tools.dren._cli import principal
    principal("tools.dren.drenos", VERSAO, FUNCOES)
