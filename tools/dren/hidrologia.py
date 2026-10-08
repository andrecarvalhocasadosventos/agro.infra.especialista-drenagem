"""Hidrologia de projeto para drenagem (Especialista Hidraulica).

Unidades SI nas interfaces, salvo onde indicado no nome/docstring (minutos para
duracao de chuva e tempo de concentracao, mm/h para intensidade, km2 ou ha para
area, declarados em cada funcao).

Fontes (citadas apenas ao nivel de obra quando a pagina nao e conhecida com
seguranca):
- DNIT IPR-715, Manual de Hidrologia Basica para Estruturas de Drenagem.
- NRCS (SCS) National Engineering Handbook, Part 630 Hydrology, cap. 10
  (Estimation of Direct Runoff from Storm Rainfall) e cap. 16 (Hydrographs).
- Tucci, C.E.M. (org.), Hidrologia: Ciencia e Aplicacao; Silveira (2005),
  RBRH, comparacao de formulas de tempo de concentracao.
- DAEE-SP (Instrucao Tecnica DPO 11/2017, Pluviometria e drenagem).
- Casos do acervo: casos/drenagem_dissipadores/*.md.

CLI: python -m tools.dren.hidrologia --json '{"funcao": "racional", "args": {...}}'

CHANGELOG
0.3.0 (F5/M1: conferencia no primario das formulas de Tc; paginas = marcador fisico do PDF):
  - Conferidas por renderizacao do PDF: Kirpich, Picking, Ven Te Chow, DNOS, Kirpich modificada e
    Giandotti [DNIT-HIDRO p. 88-92], Dooge e Kirpich [PMSP-DRENURB-V2 p. 56-57], McCuen Eq. 3-47,
    3-48, 3-53 a 3-56 [McCuen p. 165, 172-173]. Unidade de S do Dooge confirmada (m/m, A km2, min).
  - Novas: picking, ven_te_chow, nerc, bransby_williams, tc_onda_cinematica (McCuen 3-47; coef 0,938 ou
    0,933 das planilhas), tc_laminar_neh (NEH-630 cap. 15 Eq. 15-8 / McCuen 3-48), tc_lag_scs
    (NEH Eq. 15-4b / McCuen 3-56), velocidade_concentrado_neh (Tab. 15-3), velocidade_manning,
    tempo_viagem_min, c_ponderado, escoamento_ponderado.
  - avisos: Kirpich com L > 10 km (PMSP p. 56), Giandotti em bacia pequena (DNIT p. 92), Dooge fora de
    140-930 km2, DNIT-HIDRO marca Picking em "horas" (divergencia: o exemplo IME e a tabela de
    velocidades do proprio DNIT exigem minutos).
0.2.0 (achados da redacao da skill hidrologia-de-projeto-para-drenagem; paginas = marcador
      fisico do PDF em referencias/_texto):
  - dnos: agora a forma do DNIT, Tc = (10/K)*A^0,3*L^0,2/I^0,4 (A ha, L m, I %), tabela de K
    [DNIT-HIDRO p. 89]. A forma antiga ficou como dnos_legado (nao confirmada em fonte).
  - mcmath: parametros S_unidade ("m/m" -> 0,0091; "m/km" -> 0,0023) e S_tipo (aviso se
    nao for a declividade do canal principal) [USBR-DRAINAGE p. 57; EMBRAPA-DREN-SUP p. 5].
  - gumbel_P_TR: parametro n (fator de frequencia K(n, TR) de amostra finita, HDS-2 p. 132
    Tab. 5.13); sem n continua amostra infinita, com aviso. Novas: gumbel_K, gumbel_yn_sn.
  - chuva_efetiva / hietograma_para_efetiva: lam=0,05 converte o CN (ajustar_cn=True,
    padrao) e avisa; ajustar_cn=False restaura o comportamento anterior.
  - Novas: blocos_alternados [PMSP-DRENURB-V2 p. 21-22], risco_hidrologico, tr_para_risco
    [DNIT-HIDRO p. 24], cn_para_lambda_005.
  - kirpich_modificada_dnit: docstring conferida (1,42 ~ 1,5 x 0,95) [DNIT-HIDRO p. 90].
"""
from __future__ import annotations

import argparse
import bisect
import json
import math
import sys
import warnings

VERSAO = "0.3.0"

# Limites de area do metodo racional adotados em projetos do acervo (divergencia
# de criterios, documentada em racional()).
LIMITES_RACIONAL_ACERVO_KM2 = {
    "iuiu_2002": 0.5,  # A <= 50 ha (Racional); 50-400 ha media McMath/CN
    "baixio_irece_2008": 1.0,  # A <= 100 ha
    "csb_geohidro_2016": 3.5,  # A <= 350 ha
    "xingo_lote1": 2.0,  # A < 2 km2 ou Tc < 1 h
}


# --------------------------------------------------------------------------
# Utilitarios
# --------------------------------------------------------------------------
def _resultado(entradas, saidas, metodo, avisos):
    return {
        "entradas": entradas,
        "saidas": saidas,
        "metodo": metodo,
        "avisos": list(avisos),
        "versao": VERSAO,
    }


def _positivo(**kw):
    for k, v in kw.items():
        if not (v > 0):
            raise ValueError(f"{k} deve ser > 0 (recebido {v!r})")


# --------------------------------------------------------------------------
# IDF
# --------------------------------------------------------------------------
def idf_potencial(TR, t, a, b, c, d, faixa_TR=None, faixa_t=None, detalhado=False):
    """Intensidade de chuva i = a * TR**b / (t + c)**d  [mm/h].

    TR em anos, t em minutos. Forma geral das equacoes de chuvas intensas
    brasileiras (Plúvio 2.1/UFV, IDF DAEE). Ex.: CSB grupo 1 (doc 1341:36):
    a=5590,88; b=0,241; c=40,11; d=1,091.
    Validade: faixas de TR e t do ajuste original (passe faixa_TR=(min,max) e
    faixa_t=(min,max) para obter aviso de extrapolacao).
    Fonte: DAEE-SP IT DPO 11/2017; Tucci (Hidrologia), cap. de chuvas intensas.
    Retorna i (float) ou, com detalhado=True, o dict padrao com avisos.
    """
    _positivo(TR=TR, t=t, a=a, d=d)
    if t + c <= 0:
        raise ValueError("t + c deve ser > 0")
    i = a * TR ** b / (t + c) ** d
    avisos = []
    if faixa_TR and not (faixa_TR[0] <= TR <= faixa_TR[1]):
        avisos.append(f"TR={TR} fora da faixa de ajuste {faixa_TR}: extrapolacao")
    if faixa_t and not (faixa_t[0] <= t <= faixa_t[1]):
        avisos.append(f"t={t} min fora da faixa de ajuste {faixa_t}: extrapolacao")
    if not detalhado:
        return i
    return _resultado(
        {"TR": TR, "t": t, "a": a, "b": b, "c": c, "d": d},
        {"i_mm_h": i},
        "IDF potencial i=a*TR^b/(t+c)^d",
        avisos,
    )


def _interp_loglog(x, xs, ys):
    """Interpolacao linear em log-log; extrapola pelo segmento extremo."""
    if len(xs) < 2:
        raise ValueError("sao necessarios >= 2 pontos")
    k = bisect.bisect_left(xs, x)
    k = min(max(k, 1), len(xs) - 1)
    x0, x1, y0, y1 = xs[k - 1], xs[k], ys[k - 1], ys[k]
    if min(x0, x1, y0, y1, x) <= 0:
        raise ValueError("valores devem ser > 0 para interpolacao log")
    f = (math.log(x) - math.log(x0)) / (math.log(x1) - math.log(x0))
    return math.exp(math.log(y0) + f * (math.log(y1) - math.log(y0)))


def idf_tabela(pontos, t, TR=None, detalhado=False):
    """Intensidade [mm/h] por interpolacao log-log numa tabela IDF.

    pontos: lista de (t_min, i_mm_h) (curva unica) ou dict {TR: [(t_min, i), ...]}.
    Interpola ln(i) linear em ln(t) e, no caso de dict, linear em ln(TR).
    Avisa quando t ou TR saem da faixa tabelada (extrapolacao pelo segmento extremo).
    """
    avisos = []

    def curva(lst):
        lst = sorted(lst)
        return [p[0] for p in lst], [p[1] for p in lst]

    if isinstance(pontos, dict):
        if TR is None:
            raise ValueError("TR e obrigatorio quando pontos e um dict por TR")
        trs = sorted(float(k) for k in pontos)
        vals = []
        for tr in trs:
            key = next(k for k in pontos if float(k) == tr)
            xs, ys = curva(pontos[key])
            if t < xs[0] or t > xs[-1]:
                avisos.append(f"t={t} min fora da faixa da curva TR={tr:g} [{xs[0]}, {xs[-1]}]")
            vals.append(_interp_loglog(t, xs, ys))
        if TR < trs[0] or TR > trs[-1]:
            avisos.append(f"TR={TR} fora da faixa tabelada [{trs[0]:g}, {trs[-1]:g}]")
        i = _interp_loglog(TR, trs, vals)
    else:
        xs, ys = curva(pontos)
        if t < xs[0] or t > xs[-1]:
            avisos.append(f"t={t} min fora da faixa tabelada [{xs[0]}, {xs[-1]}]")
        i = _interp_loglog(t, xs, ys)
    avisos = sorted(set(avisos))
    if not detalhado:
        return i
    return _resultado({"t": t, "TR": TR}, {"i_mm_h": i}, "IDF tabelada, interpolacao log-log", avisos)


# --------------------------------------------------------------------------
# Tempo de concentracao (todas retornam minutos, exceto onde dito)
# --------------------------------------------------------------------------
def kirpich(L, S, detalhado=False):
    """Tc [min] = 0,0195 * L**0,77 * S**-0,385 (L em m, S em m/m).

    Equivalente a 0,0195*K**0,77, K=(L^3/H)^0,5 (forma do Iuiu, doc 1051:316).
    Conferida: PMSP-DRENURB-V2 p. 56 (Eq. 1.28: 3,989 L^0,77 S^-0,385, L em km) e McCuen Eq. 3-55
    (p. 172 fisica: 0,0078 L^0,77 S^-0,385, L em ft, Tennessee; 0,0078*3,28084^0,77 = 0,01946);
    DNIT-HIDRO p. 88 (0,95 (L^3/H)^0,385 h, L km, H m) reproduz o mesmo coeficiente (57/60 = 0,95; California Culverts).
    Validade: 7 bacias agricolas do Tennessee, ate 0,5 km2 (PMSP p. 56; McCuen: 1 a 112 acres; o DNIT
    diz < 0,8 km2) e declividades 3 a 10 %; com L > 10 km a formula subestima Tc (PMSP p. 56).
    Fora disso emite aviso. McCuen: multiplicar por 0,4 (superficie de concreto/asfalto) ou 0,2 (canal
    revestido); a variante Pensilvania (0,0013 L^0,77 S^-0,5) nao esta implementada.
    """
    _positivo(L=L, S=S)
    tc = 0.0195 * L ** 0.77 * S ** -0.385
    avisos = []
    if S < 0.03 or S > 0.10:
        avisos.append("Kirpich: declividade fora de 3-10 % (faixa de ajuste original)")
    if L > 10000:
        avisos.append("Kirpich: L > 10 km, a formula subestima Tc (PMSP-DRENURB-V2 p. 56)")
    avisos.append("Kirpich: valido para bacias < 0,5 km2 (area nao verificada aqui)")
    return tc if not detalhado else _resultado({"L_m": L, "S": S}, {"tc_min": tc}, "Kirpich", avisos)


def kirpich_modificada_dnit(L_km, H):
    """Tc [min] = 60 * 1,42 * (L**3 / H)**0,385 (L em km, H em m).

    Conferida (imagem do PDF) em DNIT-HIDRO p. 90 (marcador fisico; p. 86 impressa): "tempos de
    concentracao 50 % maiores" que os de Kirpich, para o HU triangular do SCS
    reproduzir cheias observadas em bacias medias e grandes. Logo e
    1,5 x Kirpich (0,95 x 1,5 = 1,425; o manual imprime 1,42, diferenca de 0,35 %).
    Indicada pelo DNIT para "uma grande faixa de areas" (p. 90) e adotada na falta de dados
    observados. Mesma unidade de L que california_culverts (km). Reproduz o Tc da bacia 45
    do CSB com 1,9 % de diferenca.
    """
    _positivo(L_km=L_km, H=H)
    return 60.0 * 1.42 * (L_km ** 3 / H) ** 0.385


def california_culverts(L, H):
    """Tc [min] = 57 * (L**3 / H)**0,385 (L em km, H em m de desnivel).

    California Culverts Practice (1942), forma adotada pelo DNIT/DER para
    bacias pequenas; e Kirpich com S = H/L: 57 L^1,155 H^-0,385 [PMSP-DRENURB-V2 p. 56, Eq. 1.29;
    IME p. 29, Eq. 3.6: L 5 km, H 300 m -> 41 min]. Mesma faixa de validade do Kirpich.
    """
    _positivo(L=L, H=H)
    return 57.0 * (L ** 3 / H) ** 0.385


def giandotti(A, L, Hm):
    """Tc [h] = (4*sqrt(A) + 1,5*L) / (0,8*sqrt(Hm)).

    A em km2, L em km (talvegue), Hm em m = altitude media da bacia menos a
    altitude da secao de saida. Forma conferida na imagem do PDF [DNIT-HIDRO p. 91-92 (impressas
    87-88): TC = (4 raiz(A) + 1,5 L)/(0,8 raiz(H)), TC em horas, H = desnivel maximo].
    Validade: o DNIT NAO da faixa de area; so diz que a velocidade media resultante (2,1 km/h nas bacias
    pequenas, 5,0 nas maiores) fica abaixo da media das outras formulas, "pouco recomendavel" para
    bacias pequenas (p. 92). A faixa de 170 a 70.000 km2 (original italiano, via Tucci) NAO consta do
    corpus: nao conferida; tc_com_avisos emite aviso. Retorna horas.
    """
    _positivo(A=A, L=L, Hm=Hm)
    return (4.0 * math.sqrt(A) + 1.5 * L) / (0.8 * math.sqrt(Hm))


def dooge(A, S):
    """Tc [min] = 21,88 * A**0,41 * S**-0,17 (A em km2, S em m/m).

    Conferida: PMSP-DRENURB-V2 p. 57 (impressa 55), Eq. 1.34, com a legenda da p. 56: tc em min,
    A em km2, S declividade do talvegue em m/m. Calibrada com 10 bacias rurais da Irlanda de 140 a
    930 km2 (bacias medias, escoamento em canais); fora disso tc_com_avisos emite aviso.
    """
    _positivo(A=A, S=S)
    return 21.88 * A ** 0.41 * S ** -0.17


# K do DNOS por tipo de terreno [DNIT-HIDRO p. 89 (marcador fisico; p. 85 impressa)].
DNOS_K_TERRENO = {
    "areno_argiloso_vegetacao_intensa": 2.0,
    "comum_vegetacao": 3.0,
    "argiloso_vegetacao_absorcao_media": 4.0,
    "argiloso_vegetacao_media_pouca_absorcao": 4.5,
    "rocha_escassa_vegetacao": 5.0,
    "rochoso_vegetacao_rala": 5.5,
}


def dnos(A, L, I, K=4.0, terreno=None):
    """Tc [min] = (10 / K) * A**0,3 * L**0,2 / I**0,4  (DNOS, DNIT-HIDRO p. 89).

    A em ha, L em m (curso d'agua), I declividade em %, K conforme o terreno
    (DNOS_K_TERRENO; K maior => Tc menor, pois K divide): 2,0 areno-argiloso com
    vegetacao intensa; 3,0 comum; 4,0 argiloso com vegetacao (condicao media, "aceitavel
    para qualquer tamanho de bacia"); 4,5; 5,0 rocha; 5,5 rochoso, vegetacao rala.
    `terreno` (chave de DNOS_K_TERRENO) sobrescreve K. Forma conferida contra a forma
    unificada do manual (p. 97) e na imagem do PDF (p. 89). Caso: A=100 ha, L=2000 m, I=1 %, K=4 -> 45,5 min
    (a forma antiga, dnos_legado, daria 19,3 min com A=1 km2, L=2 km).
    """
    if terreno is not None:
        if terreno not in DNOS_K_TERRENO:
            raise ValueError(f"terreno desconhecido: {terreno!r}; use {list(DNOS_K_TERRENO)}")
        K = DNOS_K_TERRENO[terreno]
    _positivo(A=A, L=L, I=I, K=K)
    return (10.0 / K) * A ** 0.3 * L ** 0.2 / I ** 0.4


def dnos_legado(A, L, I, K, coef=4.2):
    """Forma antiga (v0.1): Tc [min] = coef * A**0,3 * L**0,2 * K / I**0,4.

    Forma nao confirmada em fonte (A km2, L km; K multiplica, contrario ao DNIT).
    Mantida apenas para testes antigos; NAO usar em projeto (usar dnos).
    """
    _positivo(A=A, L=L, I=I, K=K)
    return coef * A ** 0.3 * L ** 0.2 * K / I ** 0.4


def kerby(L, n, S):
    """Tc [min] = 1,44 * (L*n / sqrt(S))**0,467 para escoamento superficial.

    L em m (comprimento do escoamento, <= 365 m), S em m/m, n = coeficiente de
    retardancia de Kerby (0,02 liso impermeavel; 0,10 solo nu; 0,20 pasto ralo;
    0,40 pasto denso; 0,60-0,80 floresta). Fonte: Kerby (1959); FHWA HDS-2.
    """
    _positivo(L=L, n=n, S=S)
    return 1.44 * (L * n / math.sqrt(S)) ** 0.467


FT = 0.3048  # m por ft
POL = 25.4  # mm por pol


def picking(L_km, I):
    """Tc [min] = 5,3 * (L**2 / I)**(1/3)  (L em km, I declividade media em m/m).

    Fonte: IME (Drenagem Urbana em Rodovias) p. 29, Eq. 3.5 e exemplo Eq. 3.8 (L 5 km, I 0,06 ->
    40 min; calculada 39,6). DNIT-HIDRO p. 88 (impressa 84) imprime a mesma expressao com TC "em
    horas": divergencia de unidade. A unidade correta e MINUTO: o exemplo IME so fecha em minutos e a
    tabela de velocidades do proprio DNIT (V = 1,132 H^0,333 km/h, p. 97) so e coerente com
    minutos (L 5 km, H 300 m -> 7,6 km/h = 5 km/40 min). DNIT: velocidade media 5,4 km/h nas bacias
    pequenas e 8,6 nas maiores, "nao indicada" para as maiores. Revisao F5: essas velocidades, impressas na
    mesma p. 88, so sao possiveis com Tc em minutos (em horas o exemplo do IME daria 0,13 km/h).
    """
    _positivo(L_km=L_km, I=I)
    return 5.3 * (L_km ** 2 / I) ** (1.0 / 3.0)


def ven_te_chow(L_km, I_pct):
    """Tc [min] = 25,2 * (L / sqrt(I))**0,64  (L em km, I declividade em %).

    Conferida na imagem do DNIT-HIDRO p. 89 (impressa 85; o _texto perde a raiz) e pelo exemplo IME
    p. 29, Eq. 3.4/3.7 (L 5 km, I 6 % -> 39,8 min). DNIT: velocidade media 4,9 km/h nas bacias
    pequenas e 9,4 nas maiores, "nao recomendada" para as maiores.
    """
    _positivo(L_km=L_km, I_pct=I_pct)
    return 25.2 * (L_km / math.sqrt(I_pct)) ** 0.64


def nerc(L_km, H_m):
    """Tc [h] = 2,8 * (L / sqrt(H/L))**0,47  (L em km, H/L em m/km).

    Forma do NERC (1975, apud Watkins e Fiddes, 1984), conforme o caso do acervo Delmiro Gouveia
    (memorial doc 1492:155; planilha 1494:64: L 13,21 km, desnivel 32 m -> 7,650 h). NAO conferida no
    primario (nao ha NERC no corpus); o rotulo "Kirpich" da planilha do projeto esta errado (Kirpich
    daria 4,92 h). Fonte: caso 2026-10-08_delmiro_gouveia_tc_rotulos_velocidade_declividade (sem
    marca humana).
    """
    _positivo(L_km=L_km, H_m=H_m)
    return 2.8 * (L_km / math.sqrt(H_m / L_km)) ** 0.47


def bransby_williams(L_km, A_km2, J_pct, coef=0.615):
    """Tc [h] = coef * L / (A**0,1 * J**0,2)  (L em km, A em km2, J declividade em %).

    coef = 0,615 reproduz o Tc do caso Delmiro Gouveia (BHD1: L 13,21 km, A 36,34 km2, J 0,2422 % ->
    7,53 h; doc 1494:31). A constante NAO foi conferida no primario (nao esta no corpus); a forma
    classica de Bransby-Williams usa outra constante (21,3 min). Usar so para reproduzir o projeto.
    Revisao F5: a forma SI usual na literatura (Tc = 58 L/(A^0,1 S^0,2) min, S em m/km; Pilgrim e Cordery,
    FORA do corpus) da 58/60/10^0,2 = 0,610 com J em %: 0,615 fica 0,8 % acima. Coerente, mas sem pagina
    primaria no corpus: continua "nao conferida" (pendente F7).
    """
    _positivo(L_km=L_km, A_km2=A_km2, J_pct=J_pct, coef=coef)
    return coef * L_km / (A_km2 ** 0.1 * J_pct ** 0.2)


def tc_onda_cinematica(n, L_m, S, i_mm_h, coef=0.938):
    """Tempo de percurso em lamina [min] = coef * (n*L/sqrt(S))**0,6 / i**0,4  (L em ft, i em pol/h).

    McCuen Eq. 3-47 (p. 146 impressa, 165 fisica; Ex. 3-12): coef = 0,938. As planilhas internas
    (LOC-PLANILHA-ESCOAMENTO-PLANO-001/-REDENCAO, aba "FAA") usam 0,933 (0,5 % menor): passe
    coef=0,933 para reproduzi-las (divergencia 2 do mapa; decisao F7). Aqui L em m e i em mm/h
    (convertidos). Limites: n*L/sqrt(S) <= ~100 (McCuen e Spiess) e L <= 100 ft (NEH); a funcao
    retorna float: use tc_escoamento_aviso_lamina para checar o limite.
    Revisao F5: 0,938 e a constante exata da deducao (Manning 1,49 com R = i t; 720^0,4/89,4^0,6 = 0,9378);
    FHWA-HDS2 3a ed. Eq. 3.6 (p. 70 do _texto do Hidraulico) imprime 0,93 (CU) e 6,9 (SI); 0,933 e
    arredondamento publicado (HEC-22 2a ed., fora do corpus). Diferenca 0,5 % no Tt, sem efeito pratico.
    """
    _positivo(n=n, L_m=L_m, S=S, i_mm_h=i_mm_h, coef=coef)
    L_ft = L_m / FT
    return coef * (n * L_ft / math.sqrt(S)) ** 0.6 / (i_mm_h / POL) ** 0.4


def tc_escoamento_aviso_lamina(n, L_m, S):
    """Avisos do escoamento em lamina: L > 100 ft (30,48 m; NEH-630 cap. 15 p. 12) e n*L/sqrt(S) > 100
    com L em ft (McCuen e Spiess, McCuen p. 146; NEH Eq. 15-9: L_max = 100 sqrt(S)/n)."""
    _positivo(n=n, L_m=L_m, S=S)
    L_ft = L_m / FT
    av = []
    if L_ft > 100:
        av.append(f"escoamento em lamina com L = {L_ft:.0f} ft > 100 ft (NEH-630 cap. 15 p. 12)")
    if n * L_ft / math.sqrt(S) > 100:
        av.append(f"n*L/sqrt(S) = {n * L_ft / math.sqrt(S):.0f} > 100: limite de McCuen e Spiess; "
                  f"L maximo = {100 * math.sqrt(S) / n * FT:.1f} m")
    return av


def tc_laminar_neh(n, L_m, P2_mm, S):
    """Tempo de percurso em lamina [h] = 0,007 * (n*L)**0,8 / (P2**0,5 * S**0,4)  (L em ft, P2 em pol).

    NEH-630 cap. 15 Eq. 15-8 (p. 12 fisica), Welle e Woodward (1986); equivale a McCuen Eq. 3-48
    (0,42 min). n da Tab. 15-1 (liso 0,011; relva curta 0,15; relva densa 0,24; bosque 0,40-0,80).
    P2 = chuva de 2 anos e 24 h. Aqui L em m, P2 em mm (convertidos). Limite L <= 100 ft (use
    tc_escoamento_aviso_lamina). Retorna horas. Caso NEH p. 18: n 0,15, 100 ft, P2 3,6 pol, S 0,08
    -> 0,09 h; McCuen Ex. 3-12: n 0,15, 120 ft, P2 3,12 pol, S 0,002 -> 28,8 min.
    """
    _positivo(n=n, L_m=L_m, P2_mm=P2_mm, S=S)
    return 0.007 * (n * L_m / FT) ** 0.8 / ((P2_mm / POL) ** 0.5 * S ** 0.4)


def tc_lag_scs(L_m, CN, Y_pct):
    """Tc [h] = L_ft**0,8 * (1000/CN - 9)**0,7 / (1140 * Y**0,5)  (L em ft, Y declividade em %).

    Metodo do lag do NRCS: lag = L^0,8 (S+1)^0,7 / (1900 Y^0,5) [NEH-630 cap. 15 Eq. 15-4a, p. 11
    fisica], S = 1000/CN - 10 (pol), Tc = lag/0,6 (Eq. 15-4b; McCuen Eq. 3-56 usa tc = 1,67 lag e
    S em ft/ft: tc[min] = 0,00526 L^0,8 (1000/CN - 9)^0,7 S^-0,5). Aqui L em m. Faixa: CN de 50 a 95;
    bacias de 1,3 acres a 9,2 mi2 (maioria < 2.000 acres = 8 km2; ate ~19 mi2 = 49 km2 segundo Folmar e
    Miller); McCuen: ate 4.000 acres. Retorna horas. Caso NEH p. 18: L 3.865 ft, Y 4,79 %, CN 63 ->
    1,14 h; McCuen Ex. 9-23: L 6.500 ft, S 1,3 %, CN 92 -> 1,34 h.
    """
    _positivo(L_m=L_m, Y_pct=Y_pct)
    if not (0 < CN <= 100):
        raise ValueError("CN deve estar em (0, 100]")
    L_ft = L_m / FT
    return L_ft ** 0.8 * (1000.0 / CN - 9.0) ** 0.7 / (1140.0 * math.sqrt(Y_pct))


# k de V = k * S**0,5 (V em ft/s, S em ft/ft) [NEH-630 cap. 15 Tab. 15-3, p. 14 fisica]
VELOCIDADE_CONCENTRADO_NEH_K = {
    "pavimento_ravinas": 20.328,
    "canal_gramado": 16.135,
    "solo_nu_leque_aluvial": 9.965,
    "cultivo_linhas_retas": 8.762,
    "pastagem_curta": 6.962,
    "cultivo_minimo_bosque": 5.032,
    "floresta_serapilheira_feno": 2.516,
}


def velocidade_concentrado_neh(tipo, S):
    """Velocidade [m/s] do escoamento raso concentrado, V = k*S**0,5 (Tab. 15-3, k em ft/s), k*0,3048.

    S em m/m. Tab. 15-3 vale para S < 0,005 e como equacao da Fig. 15-4 nas demais declividades.
    """
    if tipo not in VELOCIDADE_CONCENTRADO_NEH_K:
        raise ValueError(f"tipo desconhecido: {tipo!r}; use {list(VELOCIDADE_CONCENTRADO_NEH_K)}")
    _positivo(S=S)
    return VELOCIDADE_CONCENTRADO_NEH_K[tipo] * FT * math.sqrt(S)


def velocidade_manning(R, S, n):
    """V [m/s] = R**(2/3) * S**0,5 / n (SI; NEH Eq. 15-10 e McCuen em ft usam 1,49)."""
    _positivo(R=R, S=S, n=n)
    return R ** (2.0 / 3.0) * math.sqrt(S) / n


def tempo_viagem_min(L_m, V_ms):
    """Tempo de percurso [min] = L / (60 V) (NEH Eq. 15-1; metodo da velocidade, Tc = soma dos trechos)."""
    _positivo(L_m=L_m, V_ms=V_ms)
    return L_m / (60.0 * V_ms)


def tc_com_avisos(metodo, **kw):
    """Tc [min] com dict padrao (entradas, saidas, metodo, avisos, versao)."""
    avisos = []
    if metodo == "kirpich":
        r = kirpich(kw["L"], kw["S"], detalhado=True)
        return r
    if metodo == "california_culverts":
        tc = california_culverts(kw["L"], kw["H"])
    elif metodo == "kirpich_modificada_dnit":
        tc = kirpich_modificada_dnit(kw["L"], kw["H"])
        avisos.append("Kirpich modificada DNIT = 1,5 x Kirpich (DNIT-HIDRO p. 90); L em km")
    elif metodo == "giandotti":
        tc = giandotti(kw["A"], kw["L"], kw["Hm"]) * 60.0
        avisos.append("Giandotti (DNIT-HIDRO p. 91-92): TC em h convertido para min; velocidade media baixa "
                      "em bacia pequena, 'pouco recomendavel' ali")
        if kw["A"] < 170:
            avisos.append("Giandotti: A < 170 km2; a faixa de 170 a 70.000 km2 da literatura nao consta do "
                          "corpus (nao conferida)")
    elif metodo == "dooge":
        tc = dooge(kw["A"], kw["S"])
        avisos.append("Dooge [PMSP-DRENURB-V2 p. 57]: A km2, S m/m, tc em min")
        if not (140 <= kw["A"] <= 930):
            avisos.append("Dooge: A fora de 140-930 km2 (10 bacias da Irlanda)")
    elif metodo == "picking":
        tc = picking(kw["L"], kw["I"])
        avisos.append("Picking: L km, I m/m, tc em min (IME p. 29); o DNIT-HIDRO p. 88 imprime 'horas' "
                      "(divergencia)")
    elif metodo == "ven_te_chow":
        tc = ven_te_chow(kw["L"], kw["I"])
        avisos.append("Ven Te Chow: L km, I em %, tc em min (DNIT-HIDRO p. 89; IME p. 29)")
    elif metodo == "nerc":
        tc = nerc(kw["L"], kw["H"]) * 60.0
        avisos.append("NERC: forma do caso Delmiro Gouveia, nao conferida no primario; L km, H m")
    elif metodo == "bransby_williams":
        tc = bransby_williams(kw["L"], kw["A"], kw["J"], kw.get("coef", 0.615)) * 60.0
        avisos.append("Bransby-Williams: constante 0,615 do caso Delmiro Gouveia, nao conferida no primario")
    elif metodo == "onda_cinematica":
        tc = tc_onda_cinematica(kw["n"], kw["L"], kw["S"], kw["i"], kw.get("coef", 0.938))
        avisos.extend(tc_escoamento_aviso_lamina(kw["n"], kw["L"], kw["S"]))
        avisos.append("Onda cinematica (McCuen Eq. 3-47): L m, i mm/h (depende de tc: iterar); "
                      "coef 0,938 (livro) ou 0,933 (planilhas)")
    elif metodo == "laminar_neh":
        tc = tc_laminar_neh(kw["n"], kw["L"], kw["P2"], kw["S"]) * 60.0
        avisos.extend(tc_escoamento_aviso_lamina(kw["n"], kw["L"], kw["S"]))
        avisos.append("Laminar NEH-630 Eq. 15-8: L m, P2 mm (2 anos, 24 h)")
    elif metodo == "lag_scs":
        tc = tc_lag_scs(kw["L"], kw["CN"], kw["Y"]) * 60.0
        if not (50 <= kw["CN"] <= 95):
            avisos.append("Lag SCS: CN fora de 50-95 (NEH-630 cap. 15 p. 12)")
        avisos.append("Lag SCS: L m, Y em %; bacias ate ~8 km2 (McCuen ate 16 km2)")
    elif metodo == "dnos":
        tc = dnos(kw["A"], kw["L"], kw["I"], kw.get("K", 4.0), kw.get("terreno"))
        avisos.append("DNOS (DNIT-HIDRO p. 89): A em ha, L em m, I em %; K maior da Tc menor")
        if kw.get("terreno") is None and kw.get("K", 4.0) not in DNOS_K_TERRENO.values():
            avisos.append("DNOS: K fora da tabela do manual (2,0 a 5,5)")
    elif metodo == "dnos_legado":
        tc = dnos_legado(kw["A"], kw["L"], kw["I"], kw["K"])
        avisos.append("dnos_legado: forma nao confirmada em fonte; nao usar em projeto")
    elif metodo == "kerby":
        tc = kerby(kw["L"], kw["n"], kw["S"])
        if kw["L"] > 365:
            avisos.append("Kerby: L > 365 m fora da faixa de validade")
    else:
        raise ValueError(f"metodo de Tc desconhecido: {metodo}")
    return _resultado(dict(kw), {"tc_min": tc}, metodo, avisos)


# --------------------------------------------------------------------------
# Racional e McMath
# --------------------------------------------------------------------------
def racional(C, i, A, unidade_area="km2", limite_km2=2.0, detalhado=False):
    """Q [m3/s] = C * i * A / 3,6 (A em km2, i em mm/h)  ou  C*i*A/360 (A em ha).

    Fonte: DNIT IPR-715; Tucci. Validade usual: A <= 2-3 km2 (Tc curto, chuva
    uniforme). Divergencia de criterios no acervo (documentar em projeto):
      Iuiu 2002: Racional ate 50 ha; Baixio de Irece 2008: ate 100 ha;
      CSB 2016: ate 350 ha; Xingo Lote I: A < 2 km2 ou Tc < 1 h.
    Esta funcao avisa acima de limite_km2 (padrao 2 km2); para reproduzir um
    projeto use limite_km2 = LIMITES_RACIONAL_ACERVO_KM2[...].
    """
    if unidade_area not in ("km2", "ha"):
        raise ValueError("unidade_area deve ser 'km2' ou 'ha'")
    _positivo(C=C, i=i, A=A)
    if C > 1:
        raise ValueError("C deve estar entre 0 e 1")
    A_km2 = A if unidade_area == "km2" else A / 100.0
    Q = C * i * A_km2 / 3.6
    avisos = []
    if A_km2 > limite_km2:
        avisos.append(
            f"Racional: A={A_km2:.3g} km2 > {limite_km2:g} km2 (limite usual 2-3 km2); "
            "considerar hidrograma unitario (SCS)"
        )
    return Q if not detalhado else _resultado(
        {"C": C, "i_mm_h": i, "A": A, "unidade_area": unidade_area},
        {"Q_m3s": Q}, "Racional Q=C*i*A/3,6 (A km2)", avisos)


def coef_c_para_tr(C10, TR):
    """C_T = 0,8 * TR**0,1 * C10 (limitado a 1,0). Forma do CSB (doc 1341:47)."""
    _positivo(C10=C10, TR=TR)
    return min(1.0, 0.8 * TR ** 0.1 * C10)


def coef_distribuicao(A_km2):
    """Cd = A**-0,10 (A em km2), coeficiente de distribuicao do CSB (doc 1341:47)."""
    _positivo(A_km2=A_km2)
    return min(1.0, A_km2 ** -0.10)


MCMATH_CONST = {"m/m": 0.0091, "m/km": 0.0023}


def mcmath(C, i, A, S, detalhado=False, S_unidade="m/m", S_tipo="canal_principal"):
    """Q [m3/s] = k * C * i * A**0,8 * S**0,2, com i em mm/h, A em ha.

    Constante k conforme a unidade de S (S_unidade):
      "m/m"  (padrao): k = 0,0091, conversao exata da formula do USBR (cfs, pol/h, acres,
              s em m por 1.000 m): 0,02832/25,4 * 2,471**0,8 * 1000**0,2 = 0,00915;
      "m/km": k = 0,0023 (mesma conversao sem o fator 1000**0,2; EMBRAPA-DREN-SUP p. 5,
              que imprime S como "m/m" mas a constante so fecha com S em m/km).
    S e a declividade do CANAL PRINCIPAL da bacia entre o ponto mais remoto e o ponto de
    concentracao [USBR-DRAINAGE p. 57 (marcador fisico), "units per 1,000 units"], nao a do
    dreno projetado nem a media da bacia. Use S_tipo="dreno" ou "media_bacia" para
    registrar o que foi passado; ha aviso nesses casos. C de McMath e a soma de vegetacao,
    solo e topografia (USBR-DRAINAGE p. 58, 0,20 a 0,75), nao o C do racional.
    Validade: 50 a 400 ha (pratica do Iuiu; o corpus nao da limite de area).
    """
    _positivo(C=C, i=i, A=A, S=S)
    if S_unidade not in MCMATH_CONST:
        raise ValueError("S_unidade deve ser 'm/m' ou 'm/km'")
    k = MCMATH_CONST[S_unidade]
    Q = k * C * i * A ** 0.8 * S ** 0.2
    avisos = []
    if A < 50 or A > 400:
        avisos.append("McMath: A fora da faixa 50-400 ha")
    if S_tipo != "canal_principal":
        msg = (f"McMath: S informado e {S_tipo!r}; a formula pede a declividade do canal "
               "principal da bacia (USBR-DRAINAGE p. 57). Resultado pode estar enviesado")
        avisos.append(msg)
        warnings.warn(msg, UserWarning, stacklevel=2)
    return Q if not detalhado else _resultado(
        {"C": C, "i_mm_h": i, "A_ha": A, "S": S, "S_unidade": S_unidade, "S_tipo": S_tipo},
        {"Q_m3s": Q, "constante": k},
        f"McMath Q={k}*C*i*A^0,8*S^0,2 (A ha, S {S_unidade})", avisos)


def vazao_adotada_iuiu(A_ha, q_racional, q_mcmath=None, q_cn=None):
    """Criterio do Iuiu (doc 1051:316): A<=50 ha Racional; 50-400 ha media de
    McMath e CN (ignorando valores < Racional); >400 ha CN."""
    if A_ha <= 50:
        return q_racional
    if A_ha > 400:
        return q_cn
    vals = [v for v in (q_mcmath, q_cn) if v is not None and v >= q_racional]
    return sum(vals) / len(vals) if vals else q_racional


# --------------------------------------------------------------------------
# SCS-CN
# --------------------------------------------------------------------------
def retencao_S(CN):
    """S [mm] = 25400/CN - 254 (NRCS NEH-630 cap. 10)."""
    if not (0 < CN <= 100):
        raise ValueError("CN deve estar em (0, 100]")
    return 25400.0 / CN - 254.0


def c_ponderado(C, A):
    """C do racional ponderado por area: sum(C_k*A_k)/sum(A_k) [McCuen p. 397, Ex. 7-11:
    0,2/0,4/0,6 em 5,3/7,2/6,4 ac -> 0,412]."""
    if len(C) != len(A) or not C:
        raise ValueError("C e A devem ter o mesmo tamanho (> 0)")
    _positivo(**{f"A[{k}]": a for k, a in enumerate(A)})
    return sum(c * a for c, a in zip(C, A)) / sum(A)


def escoamento_ponderado(P, CN, A):
    """Q [mm] ponderado por area: sum(Q(P, CN_k)*A_k)/sum(A_k) (pondera-se o ESCOAMENTO, nao o CN;
    McCuen Ex. 7-17/7-18 p. 408-409: CN 55/70/75/83 com P = 7 pol -> 2,12/3,62/4,15/5,03 pol; o CN
    medio da 0,28 pol contra 0,385 pol do Q medio no Ex. 7-17)."""
    if len(CN) != len(A) or not CN:
        raise ValueError("CN e A devem ter o mesmo tamanho (> 0)")
    _positivo(**{f"A[{k}]": a for k, a in enumerate(A)})
    return sum(chuva_efetiva(P, c) * a for c, a in zip(CN, A)) / sum(A)


def cn_para_lambda_005(CN02):
    """CN equivalente para Ia = 0,05*S a partir do CN tabelado (Ia = 0,2*S).

    Forma usual (Hawkins et al. 2009; FHWA-HDS2 eq. 7.6-7.7, p. 202-203, equacoes em
    imagem no _texto): CN_0,05 = 100 / (1,879 * (100/CN_0,2 - 1)**1,15 + 1), isto e,
    S_0,05 = 1,33 * S_0,2**1,15 (S em pol). NRCS NEH-630 cap. 10 p. 10 confirma que, com
    Ia diferente de 0,2 S, "um novo conjunto de CN deve ser desenvolvido".
    """
    if not (0 < CN02 <= 100):
        raise ValueError("CN deve estar em (0, 100]")
    return 100.0 / (1.879 * (100.0 / CN02 - 1.0) ** 1.15 + 1.0)


def chuva_efetiva(P, CN, lam=0.2, ajustar_cn=True):
    """Escoamento direto Q [mm] = (P - Ia)^2 / (P - Ia + S), P > Ia; Ia = lam*S.

    P em mm, CN adimensional (tabelado para Ia = 0,2 S), lam = 0,20 (classico, NEH-630
    cap. 10) ou 0,05. Com lam = 0,05 o CN e convertido por cn_para_lambda_005 (padrao,
    ajustar_cn=True) e emite UserWarning; ajustar_cn=False usa o CN como dado (so
    correto se ele ja for CN_0,05, caso contrario superestima o escoamento).
    Validade: CN 40-98; para P < Ia retorna 0.
    """
    if lam not in (0.2, 0.05):
        raise ValueError("lam deve ser 0,2 ou 0,05")
    if lam == 0.05 and ajustar_cn:
        cn_novo = cn_para_lambda_005(CN)
        warnings.warn(
            f"chuva_efetiva: lam=0,05; CN {CN:g} (Ia=0,2S) convertido para {cn_novo:.2f} "
            "(Hawkins et al. 2009; NEH-630 cap. 10 p. 10: Ia != 0,2S exige novo CN)",
            UserWarning, stacklevel=2)
        CN = cn_novo
    S = retencao_S(CN)
    Ia = lam * S
    if P <= Ia:
        return 0.0
    return (P - Ia) ** 2 / (P - Ia + S)


def tlag_de_tc(Tc):
    """tlag = 0,6 * Tc (NRCS NEH-630 cap. 15/16). Mesmas unidades de Tc."""
    return 0.6 * Tc


def hidrograma_unitario_triangular(A_km2, Tc_h, D_h):
    """HU triangular SCS para chuva efetiva unitaria (1 mm) de duracao D.

    tlag = 0,6 Tc; tp = D/2 + tlag; tb = 2,67 tp; qp = 0,208 * A / tp
    [m3/s por mm] com A em km2 e tp em h (NEH-630 cap. 16). Retorna dict.
    Confere com Baixio de Irece (doc 902:1): A=323,4 ha, Tc=0,9633 h, D=0,16055 h
    -> tp=0,658 h, tb=1,758 h, qp(10 mm)=10,22 m3/s.
    """
    _positivo(A_km2=A_km2, Tc_h=Tc_h, D_h=D_h)
    tlag = tlag_de_tc(Tc_h)
    tp = D_h / 2.0 + tlag
    qp = 0.208 * A_km2 / tp
    return {"tlag_h": tlag, "tp_h": tp, "tb_h": 2.67 * tp, "qp_m3s_por_mm": qp,
            "D_h": D_h}


def convolucao_hu(pe_incremental_mm, hu):
    """Convolucao discreta do hietograma de chuva efetiva com o HU triangular.

    pe_incremental_mm: lista de lamina efetiva (mm) por intervalo de duracao
    hu["D_h"]. Retorna dict com tempos (h), vazoes (m3/s) e pico. O HU e
    amostrado no passo D (ordenadas pontuais da forma triangular, sem
    suavizacao); sujeito a erro de poucos % no pico se tp/D < 3.
    """
    dt = hu["D_h"]
    tp, tb, qp = hu["tp_h"], hu["tb_h"], hu["qp_m3s_por_mm"]

    def u(t):
        if t <= 0 or t >= tb:
            return 0.0
        return qp * t / tp if t <= tp else qp * (tb - t) / (tb - tp)

    n_u = int(math.ceil(tb / dt)) + 1
    n = len(pe_incremental_mm) + n_u
    q = [0.0] * n
    for j, pe in enumerate(pe_incremental_mm):
        if pe <= 0:
            continue
        for k in range(n_u):
            if j + k < n:
                q[j + k] += pe * u(k * dt)
    t = [k * dt for k in range(n)]
    ip = max(range(n), key=lambda k: q[k])
    return {"t_h": t, "Q_m3s": q, "Qp_m3s": q[ip], "tp_pico_h": t[ip]}


def hietograma_para_efetiva(P_incremental_mm, CN, lam=0.2, ajustar_cn=True):
    """Chuva efetiva incremental (mm) a partir da chuva incremental (mm),
    pelo acumulado SCS (NEH-630 cap. 10). Com lam=0,05 converte o CN uma vez
    (ver chuva_efetiva)."""
    if lam == 0.05 and ajustar_cn:
        cn_novo = cn_para_lambda_005(CN)
        warnings.warn(f"hietograma_para_efetiva: lam=0,05; CN {CN:g} convertido para "
                      f"{cn_novo:.2f}", UserWarning, stacklevel=2)
        CN = cn_novo
    acum, anterior, saida = 0.0, 0.0, []
    for p in P_incremental_mm:
        acum += p
        q = chuva_efetiva(acum, CN, lam, ajustar_cn=False)
        saida.append(q - anterior)
        anterior = q
    return saida


# --------------------------------------------------------------------------
# Hietograma por blocos alternados, risco hidrologico
# --------------------------------------------------------------------------
def blocos_alternados(idf, TR, duracao_total, dt, detalhado=False):
    """Hietograma de projeto pelo metodo dos blocos alternados [PMSP-DRENURB-V2 p. 21-22].

    idf: funcao (TR, t_min) -> i [mm/h], ou dict {"a","b","c","d"} de idf_potencial.
    duracao_total e dt em minutos (duracao_total multiplo de dt). Passos: i(t) para
    t = dt, 2dt, ..., td; altura acumulada P(t) = i*t/60; incrementos; o maior bloco vai ao
    centro e os demais em ordem decrescente alternadamente a direita e a esquerda
    (n par: o maior fica na posicao n/2 e o 2o logo a direita, como no exemplo Wilken
    TR 5, 100 min, dt 10: acumulados 21,8 ... 55,3 mm; blocos 1,2 1,8 3,2 6,7 21,8 11,2 ...).
    Retorna dict (t_min, P_acum_mm, incrementos_mm, hietograma_mm, P_total_mm, avisos);
    a lista hietograma_mm alimenta hietograma_para_efetiva.
    """
    _positivo(TR=TR, duracao_total=duracao_total, dt=dt)
    n = int(round(duracao_total / dt))
    if n < 1 or abs(n * dt - duracao_total) > 1e-9 * max(1.0, duracao_total):
        raise ValueError("duracao_total deve ser multiplo de dt")
    if isinstance(idf, dict):
        par = dict(idf)

        def f(tr, t):
            return idf_potencial(tr, t, par["a"], par["b"], par["c"], par["d"])
    else:
        f = idf
    t = [dt * (k + 1) for k in range(n)]
    acum = [f(TR, tk) * tk / 60.0 for tk in t]
    inc = [acum[0]] + [acum[k] - acum[k - 1] for k in range(1, n)]
    avisos = []
    if any(x < -1e-9 for x in inc):
        avisos.append("incrementos negativos: IDF inconsistente (altura acumulada decrescente)")
    ordem = sorted(inc, reverse=True)
    c = (n - 1) // 2
    pos = [c]
    for k in range(1, n):  # c+1, c-1, c+2, c-2, ...
        pos.append(c + (k + 1) // 2 if k % 2 == 1 else c - k // 2)
    hiet = [0.0] * n
    for bloco, p_ in zip(ordem, pos):
        hiet[p_] = bloco
    out = {"t_min": t, "P_acum_mm": acum, "incrementos_mm": inc, "hietograma_mm": hiet,
           "P_total_mm": acum[-1], "avisos": avisos}
    if not detalhado:
        return out
    return _resultado({"TR": TR, "duracao_total_min": duracao_total, "dt_min": dt}, out,
                      "Blocos alternados (PMSP-DRENURB-V2 p. 21-22)", avisos)


def risco_hidrologico(TR, vida_util):
    """Risco J = 1 - (1 - 1/TR)**n de a cheia de TR anos ser igualada ou excedida ao
    menos uma vez em n anos de vida util [DNIT-HIDRO p. 24; PMSP-DRENURB-V2 p. 29]."""
    _positivo(TR=TR, vida_util=vida_util)
    if TR < 1:
        raise ValueError("TR deve ser >= 1")
    return 1.0 - (1.0 - 1.0 / TR) ** vida_util


def tr_para_risco(J, n):
    """TR [anos] para risco admitido J (0 < J < 1) em n anos: TR = 1/(1 - (1-J)**(1/n))."""
    _positivo(n=n)
    if not (0 < J < 1):
        raise ValueError("J deve estar em (0, 1)")
    return 1.0 / (1.0 - (1.0 - J) ** (1.0 / n))


# --------------------------------------------------------------------------
# Gumbel
# --------------------------------------------------------------------------
def gumbel_parametros(serie):
    """(mu, beta) pelo metodo dos momentos: beta = s*sqrt(6)/pi; mu = media - 0,5772*beta."""
    n = len(serie)
    if n < 2:
        raise ValueError("serie precisa de >= 2 valores")
    m = sum(serie) / n
    s = math.sqrt(sum((x - m) ** 2 for x in serie) / (n - 1))
    beta = s * math.sqrt(6.0) / math.pi
    return m - 0.5772156649 * beta, beta


def gumbel_quantil(mu, beta, TR):
    """P(TR) = mu - beta * ln(-ln(1 - 1/TR)). Equivale a Iuiu 1051:318 com
    mu=65,02 e beta=1/0,051763."""
    if TR <= 1:
        raise ValueError("TR deve ser > 1")
    return mu - beta * math.log(-math.log(1.0 - 1.0 / TR))


def gumbel_yn_sn(n):
    """Media (yn) e desvio-padrao (sn, divisor n) da variavel reduzida de Gumbel numa
    amostra de n valores, com posicoes de plotagem i/(n+1). n=10: 0,4952 e 0,9496 (tabela
    classica de Gumbel); conferido contra HDS-2 Tab. 5.13 (K = 2,8468 para n=10, TR 25)."""
    if n < 2:
        raise ValueError("n deve ser >= 2")
    y = [-math.log(-math.log(k / (n + 1.0))) for k in range(1, int(n) + 1)]
    yn = sum(y) / len(y)
    sn = math.sqrt(sum((v - yn) ** 2 for v in y) / len(y))
    return yn, sn


def gumbel_K(TR, n=None):
    """Fator de frequencia K = (yT - yn)/sn, X_T = media + K*s [DNIT-HIDRO p. 35-37;
    FHWA-HDS2 p. 132 Tab. 5.13: n=10, TR 25 -> 2,8468]. n=None: amostra infinita
    (yn = 0,5772, sn = pi/sqrt(6); equivale ao ajuste por momentos)."""
    if TR <= 1:
        raise ValueError("TR deve ser > 1")
    yT = -math.log(-math.log(1.0 - 1.0 / TR))
    if n is None:
        return (yT - 0.5772156649) * math.sqrt(6.0) / math.pi
    yn, sn = gumbel_yn_sn(n)
    return (yT - yn) / sn


def gumbel_P_TR(serie_maximos_anuais, TR, detalhado=False, n=None):
    """Precipitacao de projeto P(TR) por Gumbel.

    n=None (padrao): ajuste por momentos de amostra INFINITA (K = 2,04 em TR 25), que
    subestima o quantil em amostra pequena (n=10, TR 25: 112,3 mm contra 126,8 mm); emite
    aviso (e UserWarning se nao detalhado). Com n (tamanho da amostra, normalmente
    len(serie)): X_T = media + K(n, TR)*s, com yn e sn da amostra finita (HDS-2 p. 132
    Tab. 5.13; DNIT-HIDRO p. 35-37). Aviso adicional para n < 20 e TR > 2n.
    Fonte: Gumbel (1958); DNIT IPR-715; FHWA HDS-2.
    """
    mu, beta = gumbel_parametros(serie_maximos_anuais)
    avisos = []
    if n is None:
        P = gumbel_quantil(mu, beta, TR)
        msg = ("Gumbel sem n: forma de amostra infinita (K de n=inf); subestima o quantil em "
               "amostra pequena; passe n=len(serie) para K(n, TR)")
        avisos.append(msg)
        if not detalhado:
            warnings.warn(msg, UserWarning, stacklevel=2)
        n_aviso = len(serie_maximos_anuais)
        K = gumbel_K(TR)
    else:
        m = sum(serie_maximos_anuais) / len(serie_maximos_anuais)
        s_ = beta * math.pi / math.sqrt(6.0)
        K = gumbel_K(TR, n)
        P = m + K * s_
        n_aviso = n
    if n_aviso < 20:
        avisos.append(f"amostra de {n_aviso} anos (< 20): incerteza elevada")
    if TR > 2 * n_aviso:
        avisos.append("TR > 2x o tamanho da amostra: extrapolacao")
    if not detalhado:
        return P
    return _resultado({"n": len(serie_maximos_anuais), "n_fator": n, "TR": TR},
                      {"P": P, "mu": mu, "beta": beta, "K": K},
                      "Gumbel por momentos" if n is None else "Gumbel com K(n, TR)", avisos)


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------
def _cli_chuva_efetiva(P, CN, lam, ajustar_cn):
    avisos = []
    cn_uso = CN
    if lam == 0.05 and ajustar_cn:
        cn_uso = cn_para_lambda_005(CN)
        avisos.append(f"lam=0,05: CN {CN:g} convertido para {cn_uso:.2f} (Hawkins et al. 2009)")
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        Q = chuva_efetiva(P, CN, lam, ajustar_cn)
    return _resultado({"P": P, "CN": CN, "lam": lam, "ajustar_cn": ajustar_cn},
                      {"Q_mm": Q, "S_mm": retencao_S(cn_uso), "CN_usado": cn_uso},
                      "SCS-CN", avisos)


_FUNCOES = {
    "idf_potencial": lambda **k: idf_potencial(detalhado=True, **k),
    "idf_tabela": lambda **k: idf_tabela(detalhado=True, **k),
    "tc": lambda metodo, **k: tc_com_avisos(metodo, **k),
    "racional": lambda **k: racional(detalhado=True, **k),
    "mcmath": lambda **k: mcmath(detalhado=True, **k),
    "gumbel": lambda serie_maximos_anuais, TR, n=None: gumbel_P_TR(
        serie_maximos_anuais, TR, detalhado=True, n=n),
    "chuva_efetiva": lambda P, CN, lam=0.2, ajustar_cn=True: _cli_chuva_efetiva(P, CN, lam, ajustar_cn),
    "blocos_alternados": lambda TR, duracao_total, dt, a, b, c, d: blocos_alternados(
        {"a": a, "b": b, "c": c, "d": d}, TR, duracao_total, dt, detalhado=True),
    "risco_hidrologico": lambda TR, vida_util: _resultado(
        {"TR": TR, "vida_util": vida_util}, {"J": risco_hidrologico(TR, vida_util)},
        "J = 1-(1-1/TR)^n", []),
    "tr_para_risco": lambda J, n: _resultado(
        {"J": J, "n": n}, {"TR": tr_para_risco(J, n)}, "TR = 1/(1-(1-J)^(1/n))", []),
    "hu_triangular": lambda A_km2, Tc_h, D_h: _resultado(
        {"A_km2": A_km2, "Tc_h": Tc_h, "D_h": D_h},
        hidrograma_unitario_triangular(A_km2, Tc_h, D_h), "HU triangular SCS", []),
}


def main(argv=None):
    ap = argparse.ArgumentParser(prog="python -m tools.dren.hidrologia")
    ap.add_argument("--json", required=True,
                    help='{"funcao": "racional", "args": {"C":0.3,"i":50,"A":1.2}}; funcoes: '
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
