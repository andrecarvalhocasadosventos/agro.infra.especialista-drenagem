"""Drenagem subsuperficial: espacamento de drenos (Hooghoudt, Donnan, Ernst, Glover-Dumm),
vazao e capacidade de tubos drenos, dreno de fundo de canal revestido (subpressao), furo em
geomembrana, criterio de filtro (Terzaghi) e tabelas indicativas.

Unidades SI: m, m/d (recarga q e condutividade K, como em ILRI/USBR), m3/s para vazoes de tubo;
tempo em dias. Apenas stdlib. CLI: python -m tools.dren.drenos --json '{"funcao":
"hooghoudt_espacamento", "q": 0.002, "K": 1.0, "h": 0.6, "D": 5.0, "r": 0.1}'

Fontes (corpus; PDF = pagina fisica, marcador `<!-- p. N -->` do _texto; impressa = PDF - 2 no ILRI-16):
- USBR, Drainage Manual (1993), cap. V: secao 5-5 (profundidade equivalente de Hooghoudt, forma de
  Moody, p. 154-155 do livro, PDF 173-174), 5-8 (exemplo transiente, p. 168), 5-11 (Donnan, p. 169-170).
- ILRI Pub. 16 (Drainage Principles and Applications), corpus do Hidraulico
  (../Especialista Hidraulica/referencias/_texto/ILRI-DPA16.md): d_e exato Eq. 8.9-8.13 (PDF 268),
  Tab. 8.1 (PDF 267), Ernst Eq. 8.17-8.23 e Tab. 8.2 (PDF 270-275), Exemplos 8.1-8.4 (PDF 276-281),
  Glover-Dumm Eq. 8.28-8.33 com o fator 1,16 (PDF 283-284; impr. 285-286).
- ILRI Pub. 56 (Envelope Design, 2000): necessidade de envoltorio (Fig. 7, PDF 47), pontos de controle do
  envoltorio granular (PDF 66-68), Tab. 14 de K por textura (PDF 175), coeficientes tipicos (PDF 42).
- NRCS NEH 624 cap. 4 (PDF 63-66): equacao da elipse (Eq. 4-8) e Exemplo 1 (202 ft).
- Embrapa Manicoba (1988) p. 2-3 (Hooghoudt d=0 e Glover-Dumm 1,16); WATERLOG-ENDRAIN p. 7-10 (exemplos de
  Ritzema, ILRI-16 cap. 8).
- FAO Irrig. & Drainage Paper 38 NAO esta no corpus: tabelas indicativas antigas marcadas "a confirmar".
Gabaritos dos casos: casos/drenagem (CSB doc 1341, Xingo doc 1419, Iuiu doc 1051, Delmiro doc 1492).
"""
import math

VERSAO = "0.2.0"
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


def d_equivalente_serie(D, L, r0):
    """Profundidade equivalente d [m] pela solucao exata (van der Molen e Wesseling, 1991), ILRI-16.

    d = (pi L / 8) / (ln(L/(pi r0)) + F(x)),   x = 2 pi D / L
    F(x) = 2 sum_{n>=1} ln coth(n x)  (= sum_{n=1,3,5..} 4 e^{-2nx}/(n (1 - e^{-2nx})), x > 0,5)
    F(x) = pi^2/(4x) + ln(x/(2 pi))   (aproximacao de Dagan, x <= 0,5).
    D = profundidade da barreira abaixo do dreno [m]; L = espacamento [m]; r0 = raio equivalente [m]
    (r0 = u/pi, u = perimetro molhado; Eq. 8.14). Fonte: ILRI-DPA16 Eq. 8.9-8.13, PDF p. 268 (impr. 270);
    Exemplo 8.2 (D=4,8, L=72, r0=0,61 -> d=4,16 m, PDF 278). Validade: drenos paralelos acima de camada
    impermeavel, solo homogeneo. Fica 2-3 % abaixo da Tab. 8.1 de Hooghoudt (r0=0,1) e 0,2 % de Ex. 8.2.
    """
    if D <= 0:
        return 0.0
    if L <= 0 or r0 <= 0:
        raise ValueError("L e r0 devem ser positivos")
    x = 2.0 * math.pi * D / L
    if x <= 0.5:
        F = math.pi ** 2 / (4.0 * x) + math.log(x / (2.0 * math.pi))
    else:
        F = 0.0
        for n in range(1, 400, 2):
            e = math.exp(-2.0 * n * x)
            if e < 1e-18:
                break
            F += 4.0 * e / (n * (1.0 - e))
    return min((math.pi * L / 8.0) / (math.log(L / (math.pi * r0)) + F), D)


def hooghoudt_espacamento(q, h, D, r, K=None, K_acima=None, K_abaixo=None, tol=1e-6, itmax=200,
                          metodo_de="moody"):
    """Espacamento de drenos L [m] por Hooghoudt (regime permanente), com d_e iterativo.

    q = recarga (descarga especifica) [m/d]; h = carga no meio-vao acima do nivel do dreno [m];
    D = profundidade da camada impermeavel abaixo do dreno [m]; r = raio efetivo do dreno [m];
    K = condutividade [m/d] (solo homogeneo) ou K_acima (entre o nivel do dreno e o freatico) e
    K_abaixo (abaixo do dreno).
        L^2 = (8 K_abaixo d_e h + 4 K_acima h^2) / q
    d_e (Moody) vem de d_equivalente_hooghoudt e depende de L: iteracao de ponto fixo ate variacao
    relativa < tol. Fonte: Hooghoudt (1940); USBR Drainage Manual (1993) 5-5 e 5-11 (Donnan com d
    trocado por d_e); d_e pela forma de Moody (USBR p.155). Alternativa: tabelas do ILRI (nao no corpus).
    metodo_de = "moody" (padrao, USBR) ou "serie" (ILRI-16 Eq. 8.9-8.13, d_equivalente_serie).
    Exemplos ILRI-DPA16 (PDF 276-279): Ex. 8.1 (q=0,001, h=1,0, D=4,8, r0=0,10, K=0,14 -> 65 m; serie 64 m);
    Ex. 8.3 (duas camadas, interface no dreno, K_acima=0,06, K_abaixo=0,30 -> 95 m); Ex. 8.2 (vala, r0=0,61 ->
    72 m com a serie). Hooghoudt vale com dreno na interface das camadas; dreno dentro da camada superior pede
    Ernst (ILRI-16 8.2.3). O termo (Di-Dd) da nota WATERLOG-DRAINAGE-EQUATION p. 2 e inconsistente: nao usado.
    Validade: drenos paralelos equidistantes, solo com K constante por camada, regime permanente
    (recarga constante). Espacamentos muito pequenos (< ~10 m) invalidam a hipotese permanente. Vies de campo:
    Hooghoudt superestima L (Embrapa Manicoba, 13-35 %) e em laboratorio subestima (Embrapa 1990, -21 %).
    """
    if metodo_de not in ("moody", "serie"):
        raise ValueError("metodo_de: 'moody' ou 'serie'")
    _de = d_equivalente_hooghoudt if metodo_de == "moody" else d_equivalente_serie
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
        de = _de(D, L, r) if D > 0 else 0.0
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
            "metodo": "Hooghoudt L^2=(8 K2 d_e h+4 K1 h^2)/q, d_e %s" % (
                "Moody (USBR Drainage Manual 5-5)" if metodo_de == "moody" else "serie (ILRI-16 8.9-8.13)"),
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


def elipse_espacamento(K, m, a, q):
    """Equacao da elipse (NRCS NEH 624, Eq. 4-8): S = sqrt(4 K (m^2 + 2 a m) / q)  [mesma unidade de m, a].

    K = condutividade media; q = coeficiente de drenagem (K e q na MESMA unidade, ex. pol/h); m = carga
    no meio-vao acima do dreno; a = profundidade da barreira abaixo do dreno. Equivale a Donnan com
    b = a + m (4 K (b^2 - a^2) / q). Fonte: NRCS-NEH624-CH04 PDF p. 63-65; Exemplo 1 (K=2 pol/h, q=0,01 pol/h,
    a=7 ft, m=3 ft -> S = 202 ft; grafico 203 ft; PDF 65-66). Validade: fluxo essencialmente horizontal,
    barreira a profundidade <= 2x a do dreno, dreno com envoltorio de brita ou vala (pouca convergencia);
    senao usar Hooghoudt/Ernst. O exemplo 2 do NEH (196 ft) e solucao grafica da elipse modificada
    (Fig. 4-29), nao implementada.
    """
    if min(K, q) <= 0 or m <= 0 or a < 0:
        raise ValueError("K, q, m > 0 e a >= 0")
    S = math.sqrt(4.0 * K * (m * m + 2.0 * a * m) / q)
    av = ["elipse: so para fluxo horizontal (barreira rasa, vala ou envoltorio de brita); NEH 624 admite ajuste de 5 %"]
    if a > 8.0 * m:
        av.append("a >> m: barreira profunda; elipse nao considera convergencia radial")
    return {"S": S, "metodo": "elipse S=sqrt(4K(m^2+2am)/q) (NEH 624 Eq. 4-8)", "avisos": av}


# Tabela 8.2 do ILRI-16 (PDF 272, impr. 274): fator geometrico a da resistencia radial de Ernst, dreno na camada
# superior. Linhas: Kb/Kt; colunas: Db/Dt.
_ERNST_A_COLS = (1.0, 2.0, 4.0, 8.0, 16.0, 32.0)
_ERNST_A_ROWS = (1.0, 2.0, 3.0, 5.0, 10.0, 20.0, 50.0)
_ERNST_A_TAB = (
    (2.0, 3.0, 5.0, 9.0, 15.0, 30.0),
    (2.4, 3.2, 4.6, 6.2, 8.0, 10.0),
    (2.6, 3.3, 4.5, 5.5, 6.8, 8.0),
    (2.8, 3.5, 4.4, 4.8, 5.6, 6.2),
    (3.2, 3.6, 4.2, 4.5, 4.8, 5.0),
    (3.6, 3.7, 4.0, 4.2, 4.4, 4.6),
    (3.8, 4.0, 4.0, 4.0, 4.2, 4.6),
)


def _interp1(x, xs, ys):
    if x <= xs[0]:
        return ys[0]
    if x >= xs[-1]:
        return ys[-1]
    for i in range(len(xs) - 1):
        if xs[i] <= x <= xs[i + 1]:
            return ys[i] + (ys[i + 1] - ys[i]) * (x - xs[i]) / (xs[i + 1] - xs[i])


def fator_geometrico_ernst(Kb_Kt, Db_Dt):
    """Fator geometrico a de Ernst (dreno na camada SUPERIOR), ILRI-16 Tab. 8.2 (PDF 272), interpolacao bilinear.

    Kb/Kt < 0,1 -> a = 1 (camada inferior tratada como impermeavel); Kb/Kt > 50 -> a = 4; entre 0,1 e 50 usa a
    tabela (Kb/Kt: 1-50; Db/Dt: 1-32; fora da grade fixa no limite, com aviso). Para Kb/Kt entre 0,1 e 1 a
    tabela nao fornece valor: usa-se a linha Kb/Kt = 1 (aviso). Dreno na camada inferior: a = 1.
    Exemplo 8.4 (ILRI-16 PDF 281): Kb/Kt = 4, Db/Dt = 2,96 -> a = 3,9 (media simples dos 4 vizinhos; bilinear 3,90).
    """
    if Kb_Kt <= 0 or Db_Dt <= 0:
        raise ValueError("Kb/Kt e Db/Dt devem ser positivos")
    av = []
    if Kb_Kt < 0.1:
        return {"a": 1.0, "metodo": "Ernst Tab. 8.2: Kb/Kt<0,1 -> a=1", "avisos": av}
    if Kb_Kt > 50.0:
        return {"a": 4.0, "metodo": "Ernst Tab. 8.2: Kb/Kt>50 -> a=4", "avisos": av}
    if Kb_Kt < 1.0:
        av.append("0,1 < Kb/Kt < 1: fora da grade da Tab. 8.2; usada a linha Kb/Kt=1")
    if Db_Dt < 1.0 or Db_Dt > 32.0:
        av.append("Db/Dt fora de 1-32: valor da borda da tabela")
    col = [_interp1(Kb_Kt, _ERNST_A_ROWS, [row[j] for row in _ERNST_A_TAB]) for j in range(len(_ERNST_A_COLS))]
    a = _interp1(Db_Dt, _ERNST_A_COLS, col)
    return {"a": a, "metodo": "Ernst Tab. 8.2 (interpolacao bilinear)", "avisos": av}


def ernst_espacamento(q, h, Dv, Kv, KD_h, Dr, Kr, r, a=1.0, L_max=2000.0, u=None):
    """Espacamento L [m] de Ernst (1962) para solo estratificado, por bisseccao em
        h = q Dv/Kv + q L^2/(8 KD_h) + q L ln(a Dr / u) / (pi Kr)            (ILRI-16 Eq. 8.17-8.21)

    Resistencias vertical (Dv espessura onde o fluxo e vertical, Kv media vertical [m/d]), horizontal
    (KD_h = soma K_i D_i das camadas que transmitem fluxo horizontal [m2/d], com D_i <= L/4) e radial
    (Dr espessura da zona radial [m], Kr [m/d], a = fator geometrico: 1 em solo homogeneo ou dreno na camada
    inferior; Tab. 8.2 com dreno na superior, ver fator_geometrico_ernst; u = perimetro molhado do dreno [m]).
    u padrao = pi r (semicirculo, dreno meio cheio e sem resistencia de entrada, ILRI-16 Eq. 8.14, PDF 268;
    a versao 0.1.0 usava 2 pi r, o que subestimava a resistencia radial: corrigido contra o Exemplo 8.4).
    h = carga no meio-vao acima do nivel do dreno [m]; q em m/d.
    Fonte: ILRI-DPA16 Eq. 8.17-8.21 PDF p. 270-272 (impr. 272-274). Exemplo 8.4 (PDF 280-281, dreno na camada
    superior, q=0,007, h=0,70, Kt=0,5, Kb=2,0, Do=1,0, Db=4,0, r0=0,05): L = 38 m com a = 3,9 (use
    ernst_duas_camadas_dreno_no_topo). Na nota WATERLOG-ENDRAIN p. 10 (51,8 m) o fator a foi omitido (a=1).
    Validade: drenos paralelos, regime permanente; D_i < L/4 (verificado: aviso).
    """
    if min(q, h, Kv, KD_h, Kr, r, Dr) <= 0 or Dv < 0:
        raise ValueError("parametros positivos")
    if u is None:
        u = math.pi * r
    if u <= 0:
        raise ValueError("u deve ser positivo")
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
    av = ["regime permanente; Kirkham nao implementado (usar Hooghoudt/Ernst)"]
    if Dr > L / 4.0:
        av.append("Dr > L/4: ILRI-16 limita a espessura de fluxo radial a L/4; revise Dr")
    return {"L": L, "h_vertical": q * Dv / Kv, "h_horizontal": q * L * L / (8.0 * KD_h),
            "h_radial": q * L * Wr / (math.pi * Kr), "W_r": Wr, "u": u,
            "metodo": "Ernst h = h_v + h_h + h_r (ILRI-16 Eq. 8.21)",
            "avisos": av}


def ernst_duas_camadas_dreno_no_topo(q, h, Kt, Kb, Do, Db, r, u=None):
    """Ernst com dreno na camada SUPERIOR de perfil de duas camadas (ILRI-16 Eq. 8.23, PDF 275).

    Kt, Kb [m/d] = K das camadas superior e inferior; Do [m] = espessura da camada superior abaixo do dreno;
    Db [m] = espessura da camada inferior; h [m] = carga no meio-vao. Hipoteses do ILRI-16: Dv = h (nao ha
    fluxo vertical na camada inferior); Dr = Do; sum(KD) = Kb Db + Kt (Do + h/2); Kv = Kr = Kt; a pela Tab. 8.2
    com Kb/Kt e Db/(Do + h/2). Exemplo 8.4 (PDF 280-281): q=0,007, h=0,70, Kt=0,5, Kb=2,0, Do=1,0, Db=4,0,
    r0=0,05 -> sum(KD)=8,68, u=0,157, a=3,9, L = 38 m (h_v=0,01, h_h=0,15, h_r=0,54 m). Validade: Do, Db < L/4.
    """
    Dt = Do + 0.5 * h
    fa = fator_geometrico_ernst(Kb / Kt, Db / Dt)
    res = ernst_espacamento(q=q, h=h, Dv=h, Kv=Kt, KD_h=Kb * Db + Kt * Dt, Dr=Do, Kr=Kt, r=r, a=fa["a"], u=u)
    res["a"] = fa["a"]
    res["avisos"] = list(res["avisos"]) + fa["avisos"]
    if Db > res["L"] / 4.0:
        res["avisos"].append("Db > L/4: ILRI-16 restringe a espessura de fluxo horizontal a L/4")
    res["metodo"] = "Ernst dreno na camada superior (ILRI-16 Eq. 8.23)"
    return res


# ==========================================================================
# Glover-Dumm (nao permanente)
# ==========================================================================
def d_medio_glover_dumm(d_e, h0, ht, criterio="usbr"):
    """Profundidade media de fluxo D usada em Glover-Dumm [m], por criterio:
      "ilri"     D = d_e                          (ILRI-16 Eq. 8.29, PDF 284: d = profundidade equivalente);
      "usbr"     D = d_e + h0/2                   (USBR Drainage Manual 5-10 ex. 1, p. 168; padrao);
      "manicoba" D = d_e + (h0 + ht)/4            (Embrapa Manicoba 1988 p. 3: D0 + (h0+ht)/4, com D0 = d_e).
    Os tres dao tempos/espacamentos diferentes (ver DIVERGENCIAS); declare o criterio no parecer."""
    c = criterio.lower()
    if c == "ilri":
        return d_e
    if c == "usbr":
        return d_e + h0 / 2.0
    if c == "manicoba":
        return d_e + (h0 + ht) / 4.0
    raise ValueError("criterio: 'ilri', 'usbr' ou 'manicoba'")


def glover_dumm_altura(t, h0, K, d_med, mu, L, fator=1.16):
    """Altura do freatico no meio-vao no instante t [m] (Glover-Dumm, 1o termo):
        h_t = fator h0 exp(-alfa t),  alfa = pi^2 K d / (mu L^2)  (j = 1/alfa = mu L^2 / (pi^2 K d_med)).
    fator = 1,16 (freatico inicial em parabola de 4o grau, Dumm 1960; ILRI-16 Eq. 8.32, PDF 284, impr. 286)
    ou 4/pi = 1,27 (freatico inicial horizontal; ILRI-16 Eq. 8.31). h0 = carga inicial [m]; K [m/d];
    d_med = profundidade media de fluxo [m] (ver d_medio_glover_dumm); mu = porosidade drenavel; L [m]; t [d].
    O manual do USBR (Drainage Manual 5-10, p. 168) usa a curva equivalente KD't/(S L^2)=0,096
    para y/y0=0,444 (pi^2*0,096 = 0,95 ~ ln(1,16/0,444) = 0,96). Validade: alfa t > 0,2 (ILRI-16 Eq. 8.31);
    drenos paralelos acima de barreira; recarga nula no periodo; solo homogeneo."""
    if min(K, d_med, mu, L, h0) <= 0:
        raise ValueError("parametros positivos")
    j = mu * L * L / (math.pi ** 2 * K * d_med)
    return fator * h0 * math.exp(-t / j)


def glover_dumm_tempo(h0, ht, K, d_med, mu, L, fator=1.16):
    """Tempo de rebaixamento t [d] para o freatico no meio-vao ir de h0 a ht (inverso de
    glover_dumm_altura): t = j ln(fator h0/ht). Exemplo USBR (5-10, ex.1): K=0,305, d_e=4,4 m, h0=2,7 m
    (D'=d_e+h0/2=5,75 m), mu=0,07, L=91 m, ht=1,2 m -> t = 32 d (manual 31,8 d)."""
    if ht >= fator * h0:
        return {"t": 0.0, "avisos": ["ht >= fator*h0: sem rebaixamento"], "metodo": "Glover-Dumm"}
    j = mu * L * L / (math.pi ** 2 * K * d_med)
    t = j * math.log(fator * h0 / ht)
    av = []
    if t / j < 0.2:
        av.append("t/j < 0,2: fora da validade do 1o termo da serie")
    return {"t": t, "j": j, "metodo": "Glover-Dumm h_t=%.2f h0 exp(-t/j) (1o termo; ILRI-16 Eq. 8.32, PDF 284)" % fator,
            "avisos": av}


def glover_dumm_espacamento(h0, ht, t, K, d_med, mu, fator=1.16):
    """Espacamento L [m] que rebaixa o freatico de h0 a ht em t dias (Glover-Dumm, ILRI-16 Eq. 8.33):
    L = pi sqrt(K d_med t / (mu ln(fator h0/ht))). Fator 1,16 conferido: ILRI-16 PDF 284 e Embrapa Manicoba
    p. 2-3 (exemplo K=2,3, mu=0,15, h0=0,8, ht=0,4, t=3 d, D=0,3 -> L=12,72 m). d_med: ver d_medio_glover_dumm
    (d_e depende de L: iterar com d_equivalente_hooghoudt). Mesma validade de glover_dumm_altura."""
    if ht >= fator * h0:
        raise ValueError("ht >= fator*h0")
    L = math.pi * math.sqrt(K * d_med * t / (mu * math.log(fator * h0 / ht)))
    return {"L": L, "metodo": "Glover-Dumm (1o termo, ILRI-16 Eq. 8.33)",
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
    formula = 'wesseling': OPCAO (padrao continua 'manning' ate decisao do Andre, PARA_O_ANDRE_F7 item 20):
    Q = 89 d^2,714 s^0,571 [FAO-IDP62 p. 214], Q [m3/s], d = diametro interno [m], s = H/B = perda de carga
    admissivel por comprimento (m/m, gradiente com inflow continuo ao longo do dreno), NAO a declividade
    do tubo; n nao e usado. Dominio do texto: tubo "tecnicamente liso" (perfurado, cimento, ceramica; Blasius
    a = 0,40); para PEAD corrugado o FAO usa Manning com Km (Eq. 11) ou Blasius com a = 0,77 (ver
    `wesseling_coeficiente`, C ~ 62). O corrugado com 89 e extrapolacao: aviso emitido, decisao do Andre.
    Fonte: Manning (Chow, cap. 5); caso Xingo. Validade: tubo reto, S constante, sem entrada de ar.
    """
    f = formula.lower()
    if D <= 0 or S <= 0:
        raise ValueError("D e S positivos")
    if f == "manning":
        Q = _manning_cheio(D, S, n)
        av = ["Manning pleno; USBR mediu ate 1,2x o pleno com carga sobre o tubo (ILRI-56 PDF 46); ver capacidade_tubo_parcial"]
    elif f == "xingo":
        Q = 33.5 * D ** 2.67 * math.sqrt(S)
        n_imp = 0.31169 * D ** (8.0 / 3.0) * math.sqrt(S) / Q
        av = ["legado Xingo: unidades a confirmar; n pleno implicito=%.4f" % n_imp]
    elif f == "wesseling":
        Q = 89.0 * D ** 2.714 * S ** 0.571
        av = ["Wesseling (FAO-IDP62 p. 214): tubo tecnicamente liso (a = 0,40); S aqui e s = H/B (perda de carga "
              "admissivel / comprimento), nao a declividade; para corrugado e extrapolacao (usar Manning com Km "
              "ou wesseling_coeficiente(a=0,77)); n ignorado"]
    else:
        raise ValueError("formula: 'manning', 'xingo' ou 'wesseling'")
    return {"Q": Q, "metodo": "capacidade de tubo dreno (%s)" % f, "avisos": av}


def wesseling_coeficiente(a=0.40, nu=1.3e-6, g=9.81):
    """Coeficiente C de Q = C d^2,714 s^0,571 derivado de Blasius (lambda = a Re^-1/4) com inflow linear
    ao longo do dreno [FAO-IDP62 Eq. 1-9, p. 213-214]: C = [2 g (11/4) (pi/4)^(7/4) / (a nu^(1/4))]^(4/7).
    a = 0,3164 liso; 0,40 tecnicamente liso (C ~ 89,8 com nu = 1,3e-6 m2/s, 10 C; 93,2 com nu = 1e-6, o
    'aprox. 1e-6' do texto); 0,77 corrugado (Zuidema) (C ~ 62). nu em m2/s."""
    return (2.0 * g * 2.75 * (math.pi / 4.0) ** 1.75 / (a * nu ** 0.25)) ** (4.0 / 7.0)


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


def capacidade_tubo_parcial(D, S, n=0.016, y_D=0.5):
    """Vazao Q [m3/s] e velocidade V [m/s] de tubo circular parcialmente cheio por Manning, geometria exata.

    theta = 2 acos(1 - 2 y/D);  A = D^2 (theta - sen theta)/8;  P = D theta/2;  Q = (1/n) A (A/P)^(2/3) S^(1/2).
    D [m], S [m/m], n adim., y_D = y/D em (0, 1]. Meia secao (y/D = 0,5): Q = Q_pleno/2 (R = D/4). Caso Delmiro
    (doc 1492:105, dreno de fundo, PEAD n=0,016, S=0,0003, meia secao): D=0,149 -> 1,05e-3 m3/s; o memorial
    declara 1,518e-4 (6,9x menor; ver DIVERGENCIAS). USBR mediu ate 1,2x o Manning pleno com carga sobre o
    tubo (ILRI-56 PDF 46, nota 3). Validade: tubo reto, S constante, regime uniforme, sem entrada de ar.
    """
    if D <= 0 or S <= 0 or n <= 0:
        raise ValueError("D, S, n positivos")
    if not 0.0 < y_D <= 1.0:
        raise ValueError("y/D em (0, 1]")
    th = 2.0 * math.acos(1.0 - 2.0 * y_D)
    A = D * D * (th - math.sin(th)) / 8.0
    P = D * th / 2.0
    Q = A * (A / P) ** (2.0 / 3.0) * math.sqrt(S) / n
    return {"Q": Q, "V": Q / A, "A": A, "R": A / P, "y_D": y_D,
            "metodo": "Manning, circular parcialmente cheio (geometria exata)",
            "avisos": ["y/D > 0,82: Q passa por maximo em y/D ~ 0,94; nao extrapolar Manning para quase cheio"
                       if y_D > 0.82 else "uniforme, S constante"]}


def vazao_unitaria_darcy_dreno_fundo(K, H, X, lados=2):
    """Vazao unitaria afluente a dreno de fundo de canal (Darcy), qd = lados K H^2 / (2 X)  [m3/(s m)].

    K [m/s]; H [m] = carga do plano do tubo ate a superficie potencial do lencol; X [m] = distancia horizontal
    (metade da largura de raspagem). Forma RECONSTITUIDA do caso Delmiro (doc 1492:105; a equacao do PDF esta
    em imagem): dois lados -> K H^2 / X; K=1e-6 m/s, H=1,26, X=4,06 -> 3,91e-7 m3/(s m) (memorial 3,910e-7).
    Validade: rastro C no caso (forma exata nao legivel); so ordem de grandeza.
    """
    if min(K, H, X) <= 0 or lados not in (1, 2):
        raise ValueError("K, H, X positivos; lados 1 ou 2")
    qd = lados * K * H * H / (2.0 * X)
    return {"qd": qd, "metodo": "Darcy qd = lados K H^2/(2X) (reconstituido do caso Delmiro 1492:105)",
            "avisos": ["forma da equacao reconstituida (rastro C); K de ensaio nao citado no memorial"]}


def comprimento_maximo_dreno_fundo(Q_capacidade, qd, limite_manutencao=250.0):
    """Comprimento maximo de dreno de fundo Lmax = Q_capacidade / qd [m] e trecho adotado (limite de limpeza).

    Delmiro (doc 1492:105-106): Q = 1,518e-4 e 4,929e-4 m3/s, qd = 3,910e-7 -> Lmax = 388 e 1260 m;
    trechos de ate 250 m com poco de inspecao (limite de manutencao 200-300 m, texto do memorial)."""
    if Q_capacidade <= 0 or qd <= 0:
        raise ValueError("Q e qd positivos")
    Lmax = Q_capacidade / qd
    return {"L_max": Lmax, "L_trecho": min(Lmax, limite_manutencao), "metodo": "Lmax = Q/qd",
            "avisos": ["limite de manutencao governa" if Lmax > limite_manutencao else "capacidade governa"]}


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
    confirmar a pagina (ILRI-56 PDF 63-64: D15 do envoltorio equivale a O85-O95 dos poros; ponte permite razao 4-7;
    ver envoltorio_granular_pontos_controle para os pontos de controle do ILRI-56). Adicional USBR: D15f/D15s <= 40 (nao entupir/segregar). So avalia razoes de
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


def necessidade_envoltorio_ilri56(argila_pct, PI, Ks, q1max, Ap, SAR=None, Cu=None):
    """Necessidade de envoltorio, fluxograma da Fig. 7 do ILRI-56 (PDF 47, impr. 27).

    1) argila > 40 %: sem risco de assoreamento (so conferir HFG); 2) SAR > 8-12: possivel dispersao, segue HFG;
    3) argila > 25-30 %, ou PI > 12, ou Cu > 15: sem envoltorio filtrante (conferir HFG); 4) demais: metodo HFG.
    HFG = exp(0,332 - 0,132 K + 1,07 ln PI), K = Ks [m/d]; i_x = q1max/(Ks Apu), Apu = Ap/2 (agua entra so
    pela metade inferior do tubo). Ks [m/d]; q1max [m3/d por m de dreno] (equacao de espacamento com freatico
    na superficie); Ap [m2/m] = area de perfuracao por metro. i_x > HFG: envoltorio (ou volumoso, para reduzir
    resistencia de entrada) necessario. Limiares 25-30 % e 8-12 sao faixas do fluxograma: devolvidos como
    'indicadores', sem decisao dura. Fronteira com Geotecnia (D-86 do CDV): parecer indicativo.
    """
    if min(Ks, q1max, Ap) <= 0 or PI <= 0:
        raise ValueError("Ks, q1max, Ap, PI positivos")
    HFG = math.exp(0.332 - 0.132 * Ks + 1.07 * math.log(PI))
    ix = q1max / (Ks * 0.5 * Ap)
    ind = []
    if argila_pct > 40.0:
        ind.append("argila > 40 %: envoltorio nao requerido para evitar assoreamento")
    if SAR is not None and SAR > 8.0:
        ind.append("SAR > 8-12: dispersao possivel; envoltorio pode ser desejavel (experiencia local)")
    if 25.0 < argila_pct <= 40.0:
        ind.append("argila 25-30 a 40 %: criterio de argila indica nao requerido (confirmar por HFG)")
    if PI > 12.0 or (Cu is not None and Cu > 15.0):
        ind.append("PI > 12 ou Cu > 15: criterios de PI/Cu indicam nao requerido (confirmar por HFG)")
    return {"HFG": HFG, "i_x": ix, "envoltorio_necessario_por_HFG": ix > HFG, "indicadores": ind,
            "metodo": "ILRI-56 Fig. 7 (HFG = exp(0,332-0,132 K+1,07 ln PI); i_x = q1max/(Ks Ap/2))",
            "avisos": ["indicativo; K em m/d na formula do HFG; fronteira com Geotecnia (D-86)"]}


def envoltorio_granular_pontos_controle(d15_grosso, d85_fino, D15c_adotado=None, abertura_tubo=None):
    """Pontos de controle da faixa granulometrica de envoltorio granular, ILRI-56 (PDF 66-68, impr. 46-48).

    d15_grosso = d15 da fronteira GROSSA do solo-base; d85_fino = d85 da fronteira FINA do solo-base [mm].
      1  D15c <= 7 d85f (retencao)                  2  D50c = 5 D15c (guia de gradacao, Cu = 6)
      3  D100c <= 9,5 mm (segregacao)               4a D15f >= 4 d15c (hidraulico)
      4b D15f = D15c/5 (guia de faixa; se 4b > 4a usa 4b)       5  D5f > 0,074 mm (hidraulico)
      6  D60f = D60c/5 (guia de faixa)             7  D85 > abertura do tubo (retencao/ponte)
    D15c_adotado [mm]: se omitido, usa o maximo do ponto 1. O ILRI-56 chama 2, 4b e 6 de GUIAS, nao de criterios;
    a decisao final e do projetista (conflitos 1 x 4a: ponto 4a > ponto 1 => faixa impraticavel).
    Sem exemplo numerico completo no livro (so Figs. 11-12): teste = consistencia aritmetica.
    """
    if min(d15_grosso, d85_fino) <= 0:
        raise ValueError("d15 e d85 positivos")
    D15c_max = 7.0 * d85_fino
    D15c = D15c_max if D15c_adotado is None else D15c_adotado
    if D15c > D15c_max + 1e-12:
        raise ValueError("D15c adotado excede 7 d85f (ponto 1)")
    D15f_hid = 4.0 * d15_grosso
    D15f_guia = D15c / 5.0
    D15f = max(D15f_hid, D15f_guia)
    av = []
    if D15f_hid > D15c:
        av.append("ponto 4a > ponto 1: sem faixa viavel em D15; relaxar um criterio (ILRI-56 p. 44-45)")
    if D15f_guia < D15f_hid:
        av.append("4b < 4a: usar 4a se a faixa for praticavel e Cu > 2; senao algo entre 4b e 4a")
    if d15_grosso > 0.09:
        av.append("d15c > 0,09 mm: o ponto 4a funciona mal (ILRI-56 p. 47); prescrever D15f por faixa praticavel")
    res = {"D15c_max": D15c_max, "D15c": D15c, "D50c": 5.0 * D15c, "D100c_max": 9.5,
           "D15f_4a": D15f_hid, "D15f_4b": D15f_guia, "D15f": D15f, "D5f_min": 0.074,
           "metodo": "ILRI-56 pontos de controle 1-7 (envoltorio granular)", "avisos": av}
    if abertura_tubo is not None:
        res["D85_min"] = abertura_tubo
    return res


# ==========================================================================
# Tabelas indicativas
# ==========================================================================
# Porosidade drenavel mu (rendimento especifico), faixas indicativas POR TEXTURA SEM PAGINA (ordens de grandeza
# usuais). Unico ancoramento no corpus: ILRI-DPA16 PDF p. 44 (glossario): "menos de 5 % para materiais argilosos
# a 35 % para areias grossas e areias com cascalho"; mu depende da profundidade do freatico (ILRI-16 cap. 3 e
# 11.3.5, PDF 400-401; Exemplo 11.1: mu = 0,04). Embrapa Manicoba p. 3: mu = 0,15 (areia, de K); Fig. 2-4 do USBR
# nao foi conferida.
POROSIDADE_DRENAVEL = {"areia": (0.15, 0.30), "areia_franca": (0.10, 0.20), "franco": (0.05, 0.12),
                       "franco_argiloso": (0.03, 0.08), "argila": (0.01, 0.05)}

# Profundidade e espacamento indicativos por classe de K [m/d] (ordem de grandeza; SEM PAGINA: FAO 38 fora do
# corpus; a funcao coeficiente_drenagem_tipico traz os valores paginados do ILRI-56 p. 42).
# (K_min, K_max, profundidade_dreno_m, espacamento_m)
RECOMENDACAO_INDICATIVA = [
    (0.0, 0.1, (1.0, 1.5), (10.0, 20.0)),
    (0.1, 0.5, (1.2, 1.8), (20.0, 40.0)),
    (0.5, 2.0, (1.2, 2.0), (35.0, 80.0)),
    (2.0, 10.0, (1.5, 2.2), (60.0, 150.0)),
]


# ILRI-56 Tab. 14 (PDF 175, impr. 154; Vlotman et al. 1992, Smedema e Rycroft 1983): K [m/d] por textura.
K_POR_TEXTURA = {
    "cascalho_brita": (1500.0, 3500.0), "cascalho_natural": (100.0, 1500.0), "areia_cascalho": (5.0, 100.0),
    "areia_grossa_cascalhenta": (10.0, 50.0), "areia_media": (1.0, 5.0), "franco_arenoso_areia_fina": (1.0, 3.0),
    "franco_argila_bem_estruturada": (0.5, 2.0), "franco_arenoso_muito_fino": (0.2, 0.5),
    "argila_mal_estruturada": (0.002, 0.2), "argila_densa": (0.0, 0.002),
}

# ILRI-56 (PDF 42, impr. 22): coeficiente de drenagem de projeto q [mm/d] por clima.
COEF_DRENAGEM_TIPICO = {"umido": (7.0, 14.0), "moderado": (4.0, 7.0), "irrigado_com_alguma_chuva": (2.0, 4.0),
                        "irrigado_arido": (1.0, 2.0)}


def faixa_K_por_textura(textura):
    """Faixa de K [m/d] por classe textural, ILRI-56 Tab. 14 (PDF 175). Indicativo: medir K in situ (media geometrica
    das medidas e o valor de projeto, ILRI-56 p. 43)."""
    t = textura.lower()
    if t not in K_POR_TEXTURA:
        raise ValueError("textura: %s" % ", ".join(sorted(K_POR_TEXTURA)))
    lo, hi = K_POR_TEXTURA[t]
    return {"K_min": lo, "K_max": hi, "metodo": "ILRI-56 Tab. 14 (PDF 175)",
            "avisos": ["faixa de classe textural; usar K medido (furo de trado) no projeto"]}


def coeficiente_drenagem_tipico(clima):
    """Coeficiente de drenagem de projeto q [mm/d] e [m/d] por clima, ILRI-56 (PDF 42): umido 7-14, moderado 4-7,
    irrigado com alguma chuva 2-4, irrigado arido 1-2. O proprio texto chama as faixas de 'muito amplas'; exemplos
    de projeto brasileiros: Manicoba 8 mm/d (Embrapa 1988 p. 3), Bebedouro 3,6 mm/d medio (Embrapa 1986 p. 5)."""
    t = clima.lower()
    if t not in COEF_DRENAGEM_TIPICO:
        raise ValueError("clima: %s" % ", ".join(sorted(COEF_DRENAGEM_TIPICO)))
    lo, hi = COEF_DRENAGEM_TIPICO[t]
    return {"q_mm_d": (lo, hi), "q_m_d": (lo / 1000.0, hi / 1000.0), "metodo": "ILRI-56 PDF 42",
            "avisos": ["faixas muito amplas (ILRI-56): conferir experiencia local"]}


def porosidade_drenavel(textura):
    """Faixa indicativa (min, max) de porosidade drenavel por textura. TABELA INDICATIVA sem pagina por textura
    (ver comentario acima; ILRI-DPA16 PDF 44: <5 % argila a 35 % areia grossa). Medir in situ."""
    t = textura.lower()
    if t not in POROSIDADE_DRENAVEL:
        raise ValueError("textura: %s" % ", ".join(sorted(POROSIDADE_DRENAVEL)))
    lo, hi = POROSIDADE_DRENAVEL[t]
    return {"mu_min": lo, "mu_max": hi, "mu_medio": 0.5 * (lo + hi), "metodo": "tabela indicativa",
            "avisos": ["indicativo; medir in situ (ILRI-16 cap. 11.3.5); valores por textura sem pagina no corpus"]}


def recomendacao_indicativa(K):
    """Profundidade do dreno e espacamento tipicos por K [m/d]. SO INDICATIVO, SEM PAGINA (FAO 38 fora do corpus;
    ILRI-56 Tab. 14 e p. 42 trazem K por textura e q tipico, ver faixa_K_por_textura e coeficiente_drenagem_tipico):
    nao substitui dimensionamento por Hooghoudt/Ernst com recarga e carga de projeto."""
    for lo, hi, prof, esp in RECOMENDACAO_INDICATIVA:
        if lo <= K < hi:
            return {"profundidade_m": prof, "espacamento_m": esp, "metodo": "tabela indicativa por K",
                    "avisos": ["INDICATIVO: nao usar em projeto; sem pagina (FAO 38 fora do corpus)"]}
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
    "d_equivalente_serie": lambda D, L, r0: {"d_e": d_equivalente_serie(D, L, r0),
                                             "metodo": "serie ILRI-16 8.9-8.13", "avisos": []},
    "donnan_espacamento": donnan_espacamento,
    "elipse_espacamento": elipse_espacamento,
    "fator_geometrico_ernst": fator_geometrico_ernst,
    "ernst_espacamento": ernst_espacamento,
    "ernst_duas_camadas_dreno_no_topo": ernst_duas_camadas_dreno_no_topo,
    "d_medio_glover_dumm": lambda d_e, h0, ht, criterio="usbr": {
        "d_med": d_medio_glover_dumm(d_e, h0, ht, criterio), "metodo": "D medio Glover-Dumm (%s)" % criterio,
        "avisos": []},
    "glover_dumm_altura": lambda t, h0, K, d_med, mu, L, fator=1.16: {
        "h_t": glover_dumm_altura(t, h0, K, d_med, mu, L, fator), "metodo": "Glover-Dumm", "avisos": []},
    "glover_dumm_tempo": glover_dumm_tempo,
    "glover_dumm_espacamento": glover_dumm_espacamento,
    "tempo_de_drenagem": tempo_de_drenagem,
    "vazao_de_dreno": vazao_de_dreno,
    "capacidade_tubo_dreno": capacidade_tubo_dreno,
    "wesseling_coeficiente": wesseling_coeficiente,
    "diametro_minimo_dreno": diametro_minimo_dreno,
    "capacidade_tubo_parcial": capacidade_tubo_parcial,
    "vazao_unitaria_darcy_dreno_fundo": vazao_unitaria_darcy_dreno_fundo,
    "comprimento_maximo_dreno_fundo": comprimento_maximo_dreno_fundo,
    "necessidade_envoltorio_ilri56": necessidade_envoltorio_ilri56,
    "envoltorio_granular_pontos_controle": envoltorio_granular_pontos_controle,
    "faixa_K_por_textura": faixa_K_por_textura,
    "coeficiente_drenagem_tipico": coeficiente_drenagem_tipico,
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
