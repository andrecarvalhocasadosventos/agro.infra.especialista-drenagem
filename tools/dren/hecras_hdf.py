"""Leitura SOMENTE LEITURA de resultados HEC-RAS (`.pNN.hdf`, `.gNN.hdf`) com h5py.

Nao executa o HEC-RAS, nao escreve no arquivo, nao importa nada do arquivo (so le datasets e atributos).
Extrai: versao e unidades, parametros do plano (equacao 2D, theta, tolerancias, passo), malha 2D (area de celula,
n de Manning), maximos de NA e de velocidade por celula/face (2D) e por secao (1D), estabilizacao, Courant
estimado, contornos e um relatorio de verificacao com `avisos`.

Convencoes: unidades do proprio arquivo (atributo `Units System`; o HEC-RAS grava SI ou imperial, a calculadora
NAO converte); g = 9,80665 (SI) ou 32,174 (imperial) quando o plano nao traz `Gravity`.
Fontes dos criterios (corpus local, referencias/_texto/):
- Courant: C = V dT / dX; SWE-ELM: alvo 1,0 e ate 3,0 se o evento varia devagar; difusao: ate 5,0; partida a seco
  ou onda rapida pedem ~1,0 [USACE-HECRAS-2DUM-66 p. 200-201]. Metodo do HEC-RAS por face (velocidade da face x
  dT / distancia entre centros) [USACE-HECRAS-2DUM-66 p. 203-204]; aqui a distancia e estimada por sqrt(area da
  celula): e ESTIMATIVA, nao o numero do programa.
- Estabilizacao (dNA <= 0,01 m em 2 h) e rotulo do caso HR-02 (premissa do treinamento, sem fonte normativa).
- Teste de consistencia de malha e passo: [USACE-HECRAS-2DUM-66 p. 201].
LAYOUT 1D (secoes): os caminhos de `Results/.../Cross Sections` seguem a convencao do HEC-RAS 6.x e foram
verificados APENAS contra fixture sintetica (os arquivos reais da TPF sao 2D). Se o caminho nao existir, a
funcao devolve aviso e nao inventa numero.
CLI: python -m tools.dren.hecras_hdf --funcao verificar --arquivo "<...>.p01.hdf"
"""
import math
import os
import re

VERSAO = "0.1.0"
G_SI = 9.80665
G_IMP = 32.174

_BASE = "Results/Unsteady/Output/Output Blocks/Base Output/"
_TS = _BASE + "Unsteady Time Series/"
_SUM = _BASE + "Summary Output/"
_COMP = "Results/Unsteady/Output/Output Blocks/Computation Block/"


# ----------------------------------------------------------------------------- utilidades
def _h5():
    try:
        import h5py  # noqa
    except ImportError as e:  # pragma: no cover
        raise ImportError("hecras_hdf exige h5py (pip install h5py no venv do squad)") from e
    return h5py


def _np():
    import numpy
    return numpy


def abrir(caminho):
    """Abre o .hdf em modo leitura. Devolve h5py.File."""
    if not os.path.isfile(caminho):
        raise ValueError("arquivo nao encontrado: %r" % caminho)
    return _h5().File(caminho, "r")


def _txt(v):
    np = _np()
    if isinstance(v, (bytes, np.bytes_)):
        return v.decode("utf-8", "replace").strip()
    if isinstance(v, np.ndarray):
        if v.ndim == 0:
            return _txt(v[()])
        if v.size == 1:
            return _txt(v.ravel()[0])
        return [_txt(x) for x in v.ravel()]
    if isinstance(v, (np.floating, float)):
        return float(v)
    if isinstance(v, (np.integer, int)) and not isinstance(v, bool):
        return int(v)
    return v


def _atributos(grupo):
    return {k: _txt(v) for k, v in grupo.attrs.items()}


def _um(v):
    """Primeiro elemento se lista de 1 (os atributos de plano 2D vem em vetor por area)."""
    if isinstance(v, list) and len(v) == 1:
        return v[0]
    return v


def _estat(a, ndig=4):
    np = _np()
    a = np.asarray(a, dtype=float)
    a = a[np.isfinite(a)]
    if a.size == 0:
        return {"n": 0}
    return {"n": int(a.size), "min": round(float(a.min()), ndig), "mediana": round(float(np.median(a)), ndig),
            "media": round(float(a.mean()), ndig), "p95": round(float(np.percentile(a, 95)), ndig),
            "max": round(float(a.max()), ndig)}


def _passo_s(txt):
    """'10SEC' -> 10.0; '1MIN' -> 60; '30MIN' -> 1800; '1HOUR' -> 3600; None se nao reconhecer."""
    m = re.match(r"^\s*(\d+(?:\.\d+)?)\s*([A-Za-z]+)\s*$", txt or "")
    if not m:
        return None
    f = {"SEC": 1, "MIN": 60, "HOUR": 3600, "DAY": 86400}.get(m.group(2).upper())
    return float(m.group(1)) * f if f else None


def _unidades(f):
    u = _txt(f.attrs.get("Units System", b""))
    return u if u else None


def _gravidade(f, plano):
    g = plano.get("Gravity")
    if isinstance(g, float) and g > 1:
        return g
    return G_IMP if (_unidades(f) or "").lower().startswith("us") else G_SI


def _areas_2d(f):
    if "Geometry/2D Flow Areas" not in f:
        return []
    out = []
    for nm in f["Geometry/2D Flow Areas"].keys():
        g = f["Geometry/2D Flow Areas/" + nm]
        if hasattr(g, "keys") and "Cells Surface Area" in g:
            out.append(nm)
    return out


# ----------------------------------------------------------------------------- plano
def info_plano(f):
    """Versao, unidades, projecao, janela, passos e parametros do plano (equacao, theta, tolerancias)."""
    av = []
    raiz = _atributos(f)
    pi = _atributos(f["Plan Data/Plan Information"]) if "Plan Data/Plan Information" in f else {}
    pp = _atributos(f["Plan Data/Plan Parameters"]) if "Plan Data/Plan Parameters" in f else {}
    ru = _atributos(f["Results/Unsteady"]) if "Results/Unsteady" in f else {}
    versao = ru.get("Program Version") or raiz.get("File Version")
    d = {
        "tipo_arquivo": raiz.get("File Type"),
        "versao_programa": versao,
        "unidades": raiz.get("Units System"),
        "projecao": (raiz.get("Projection") or "")[:80] or None,
        "plano": pi.get("Plan Title"),
        "geometria": pi.get("Geometry Title"),
        "vazao": pi.get("Flow Title"),
        "janela": pi.get("Time Window"),
        "passo_base_calculo": pi.get("Computation Time Step Base"),
        "intervalo_saida": pi.get("Base Output Interval"),
        "tipo_execucao": ru.get("Type of Run"),
        "equacao_2d": _um(pp.get("2D Equation Set")),
        "theta_2d": _um(pp.get("2D Theta")),
        "tol_nivel_2d": _um(pp.get("2D Water Surface Tolerance")),
        "tol_volume_2d": _um(pp.get("2D Volume Tolerance")),
        "max_iteracoes_2d": _um(pp.get("2D Maximum Iterations")),
        "solver_matriz_2d": _um(pp.get("2D Matrix Solver")),
        "turbulencia_2d": _um(pp.get("2D Turbulence Formulation")),
        "coriolis_2d": _um(pp.get("2D Coriolis")),
        "rampa_condicao_inicial_h": _um(pp.get("2D Initial Conditions Ramp Up Time (hrs)")),
        "so_2d": pp.get("2D Only"),
        "theta_1d": pp.get("1D Theta"),
        "tol_nivel_1d": pp.get("1D Water Surface Elevation Tolerance"),
        "metodo_1d": pp.get("1D Methodology"),
        "gravidade": pp.get("Gravity"),
    }
    d["passo_base_s"] = _passo_s(d["passo_base_calculo"])
    d["intervalo_saida_s"] = _passo_s(d["intervalo_saida"])
    if not versao:
        av.append("versao do programa nao encontrada no arquivo")
    if d["equacao_2d"] and "diff" in str(d["equacao_2d"]).lower():
        av.append("equacao 2D = difusao: so planicie lenta e como teste; onda rapida ou partida a seco pedem SWE "
                  "[USACE-HECRAS-2DUM-66 p. 200-201]")
    return {"plano": d, "metodo": "atributos de Plan Data e Results", "avisos": av}


def passo_de_tempo(f):
    """Passo de calculo efetivo (s) a partir do Computation Block (todos os passos) ou da serie de saida."""
    np = _np()
    for cam in (_COMP + "Global/Time",):
        if cam in f:
            t = np.asarray(f[cam][()], dtype=float)
            if t.size > 2:
                dt = np.diff(t) * 86400.0
                dt = dt[dt > 0]
                if dt.size:
                    return {"n_passos": int(t.size), "dt_min_s": float(dt.min()), "dt_mediano_s": float(np.median(dt)),
                            "dt_max_s": float(dt.max()), "origem": "Computation Block"}
    for nm in _areas_2d(f):
        cam = _TS + "2D Flow Areas/%s/Computations/Time Step" % nm
        if cam in f:
            dt = np.asarray(f[cam][()], dtype=float).ravel()
            dt = dt[dt > 0]
            if dt.size:
                return {"n_passos": int(dt.size), "dt_min_s": float(dt.min()), "dt_mediano_s": float(np.median(dt)),
                        "dt_max_s": float(dt.max()), "origem": "Time Step da serie de saida"}
    return None


# ----------------------------------------------------------------------------- malha 2D
def malha_2d(f):
    """Por area 2D: numero de celulas, area de celula (mediana, media, p95, max), tamanho equivalente sqrt(A),
    n de Manning (valores distintos e contagem) e parametros de malha/tolerancia gravados na geometria."""
    np = _np()
    av = []
    res = {}
    for nm in _areas_2d(f):
        base = "Geometry/2D Flow Areas/" + nm
        area = np.asarray(f[base + "/Cells Surface Area"][()], dtype=float)
        pos = area > 0
        d = {"celulas": int(area.size), "celulas_area_nao_positiva": int((~pos).sum()),
             "area_celula": _estat(area, 3), "tamanho_equivalente": _estat(np.sqrt(area[pos]), 3)}
        med = float(np.median(area))
        if med > 0:
            d["razao_max_mediana_area"] = round(float(area.max()) / med, 1)
            if d["razao_max_mediana_area"] > 100:
                av.append("%s: celula maxima %.0fx a mediana: malha muito heterogenea; confira o refinamento "
                          "(2 resolucoes, [USACE-HECRAS-2DUM-66 p. 201])" % (nm, d["razao_max_mediana_area"]))
        if base + "/Cells Center Manning's n" in f:
            n = np.asarray(f[base + "/Cells Center Manning's n"][()], dtype=float)
            vals, cont = np.unique(np.round(n, 5), return_counts=True)
            d["manning_n"] = {"distintos": int(vals.size),
                              "valores": [{"n": float(v), "celulas": int(c)} for v, c in
                                          sorted(zip(vals, cont), key=lambda x: -x[1])[:10]]}
            if vals.size == 1:
                av.append("%s: n de Manning unico (%.3f) em todas as celulas: sem mapa de uso do solo; exigir "
                          "calibracao ou sensibilidade de n (+-20 %%) (casos HR-03, HR-05)" % (nm, vals[0]))
        # atributos da area (aba de tolerancias)
        ga = "Geometry/2D Flow Areas/Attributes"
        if ga in f:
            a = f[ga][()]
            nomes = [_txt(x) for x in a["Name"]]
            if nm in nomes:
                reg = a[nomes.index(nm)]
                d["parametros_geometria"] = {c: _txt(reg[c]) for c in a.dtype.names if c != "Name"}
        res[nm] = d
    if not res:
        av.append("nenhuma area de fluxo 2D com 'Cells Surface Area' no arquivo")
    return {"areas": res, "metodo": "Geometry/2D Flow Areas", "avisos": av}


# ----------------------------------------------------------------------------- resultados 2D
def _cel_min_elev(f, nm):
    return _np().asarray(f["Geometry/2D Flow Areas/%s/Cells Minimum Elevation" % nm][()], dtype=float)


def resultados_2d(f, janela_h=2.0, molhada_m=0.01):
    """Por area 2D: NA maximo (serie de saida, celulas molhadas), velocidade maxima de FACE (resumo), estabilizacao
    (maior variacao de NA nas ultimas `janela_h` horas, celulas molhadas) e NA/profundidade no ultimo passo.
    Celula molhada = profundidade > `molhada_m`. A velocidade e a maxima da FACE (pode ser artefato de borda ou
    degrau de terreno: nao e a velocidade do canal)."""
    np = _np()
    av = []
    res = {}
    for nm in _areas_2d(f):
        d = {}
        zmin = _cel_min_elev(f, nm)
        cts = _TS + "2D Flow Areas/%s/Water Surface" % nm
        if cts in f:
            ws = f[cts]
            tt = np.asarray(f[_TS + "Time"][()], dtype=float) * 24.0  # dias -> h
            nt = ws.shape[0]
            ult = np.asarray(ws[nt - 1, :], dtype=float)
            molh = (ult - zmin) > molhada_m
            d["passos_saida"] = int(nt)
            d["duracao_h"] = round(float(tt[-1] - tt[0]), 3)
            d["celulas_molhadas_fim"] = int(molh.sum())
            d["NA_fim_celulas_molhadas"] = _estat(ult[molh], 3)
            d["profundidade_fim"] = _estat((ult - zmin)[molh], 3)
            # maximo no tempo: varre por blocos para nao carregar tudo
            mx = np.full(ws.shape[1], -np.inf)
            for i in range(0, nt, 16):
                blk = np.asarray(ws[i:i + 16, :], dtype=float)
                mx = np.maximum(mx, np.where(np.isfinite(blk), blk, -np.inf).max(axis=0))
            mxm = (mx - zmin) > molhada_m
            d["NA_maximo_no_tempo"] = _estat(mx[mxm], 3)
            d["celula_NA_maximo"] = int(np.argmax(np.where(mxm, mx, -np.inf)))
            # estabilizacao
            alvo = tt[-1] - janela_h
            if tt[-1] - tt[0] >= janela_h and nt >= 3:
                i0 = int(np.argmin(np.abs(tt - alvo)))
                w0 = np.asarray(ws[i0, :], dtype=float)
                dif = np.abs(ult - w0)[molh]
                dif = dif[np.isfinite(dif)]
                if dif.size:
                    d["estabilizacao"] = {"janela_h": round(float(tt[-1] - tt[i0]), 3),
                                          "dNA_max_m": round(float(dif.max()), 4),
                                          "dNA_p99_m": round(float(np.percentile(dif, 99)), 6),
                                          "celulas_acima_0_01m": int((dif > 0.01).sum())}
                    if dif.max() > 0.01:
                        av.append("%s: NA ainda varia %.3f m nas ultimas %.1f h (>0,01 m) em %d celula(s): "
                                  "estabilizacao nao demonstrada nessas celulas (caso HR-02)"
                                  % (nm, dif.max(), tt[-1] - tt[i0], int((dif > 0.01).sum())))
            else:
                av.append("%s: simulacao mais curta que %.1f h ou com < 3 saidas: estabilizacao nao avaliavel"
                          % (nm, janela_h))
            # NA inicial (condicao inicial efetiva)
            w_ini = np.asarray(ws[0, :], dtype=float)
            mi = (w_ini - zmin) > molhada_m
            d["NA_inicial_celulas_molhadas"] = _estat(w_ini[mi], 3) if mi.any() else {"n": 0}
            d["celulas_molhadas_inicio"] = int(mi.sum())
        else:
            av.append("%s: serie 'Water Surface' ausente (arquivo sem saida de resultados?)" % nm)
        cvm = _SUM + "2D Flow Areas/%s/Maximum Face Velocity" % nm
        if cvm in f:
            v = np.asarray(f[cvm][0, :], dtype=float)
            v = v[np.isfinite(v)]
            d["velocidade_maxima_face"] = _estat(v, 3)
            d["velocidade_unidade"] = "m/s" if (_unidades(f) or "").upper().startswith("SI") else "ft/s"
            if v.size and np.percentile(v, 95) > 0 and v.max() > 3 * np.percentile(v, 95) and v.max() > 3.0:
                av.append("%s: velocidade maxima de face %.2f contra p95 %.2f: pico isolado (borda, degrau de "
                          "terreno ou instabilidade); nao citar como velocidade do canal (caso HR-02)"
                          % (nm, v.max(), np.percentile(v, 95)))
        else:
            av.append("%s: 'Maximum Face Velocity' ausente do resumo" % nm)
        cvol = _TS + "2D Flow Areas/%s/Computations/Volume Error" % nm
        cvv = _TS + "2D Flow Areas/%s/Computations/Volume" % nm
        if cvol in f:
            ve = np.asarray(f[cvol][()], dtype=float).ravel()
            d["erro_volume_final"] = float(ve[-1])
            d["erro_volume_max_abs"] = float(np.abs(ve).max())
            d["erro_volume_unidade"] = _txt(f[cvol].attrs.get("Units", b"")) or None
            if cvv in f:
                vol = np.asarray(f[cvv][()], dtype=float).ravel()
                d["volume_final"] = float(vol[-1])
                d["volume_unidade"] = _txt(f[cvv].attrs.get("Units", b"")) or None
        res[nm] = d
    return {"areas": res, "metodo": "series de saida e resumo (so leitura)", "avisos": av}


# ----------------------------------------------------------------------------- Courant
def courant_2d(f, dt_s=None, molhada_m=0.01):
    """Courant ESTIMADO por celula: C = (V + sqrt(g h)) dT / dX, com V = maior velocidade de face da celula
    (resumo de maximos), h = NA maximo - cota minima da celula, dX = sqrt(area). Usa `dt_s` ou o maior passo
    efetivo do Computation Block. Tambem devolve C so com V (como o programa, mas com dX estimado).
    Criterio: 1,0 (alvo SWE), ate 3,0 se o evento varia devagar; 5,0 na difusao [USACE-HECRAS-2DUM-66 p. 200-201]."""
    np = _np()
    av = []
    pl = info_plano(f)["plano"]
    g = _gravidade(f, {"Gravity": pl.get("gravidade")})
    pt = passo_de_tempo(f)
    if dt_s is None:
        dt_s = (pt or {}).get("dt_max_s") or pl.get("passo_base_s")
    if not dt_s:
        return {"areas": {}, "metodo": "Courant estimado", "avisos": ["passo de tempo nao encontrado; informe dt_s"]}
    adaptativo = bool(pt and pt["dt_max_s"] > pt["dt_min_s"] * 1.0001)
    res = {}
    for nm in _areas_2d(f):
        base = "Geometry/2D Flow Areas/%s/" % nm
        cmax = _SUM + "2D Flow Areas/%s/Maximum Face Velocity" % nm
        cws = _SUM + "2D Flow Areas/%s/Maximum Water Surface" % nm
        if cmax not in f or cws not in f:
            av.append("%s: resumo de maximos ausente; Courant nao estimado" % nm)
            continue
        area = np.asarray(f[base + "Cells Surface Area"][()], dtype=float)
        zmin = _cel_min_elev(f, nm)
        vf = np.asarray(f[cmax][0, :], dtype=float)
        ci = np.asarray(f[base + "Faces Cell Indexes"][()], dtype=int)
        vc = np.zeros(area.size)
        for col in (0, 1):
            ok = (ci[:, col] >= 0) & (ci[:, col] < area.size) & np.isfinite(vf)
            np.maximum.at(vc, ci[ok, col], np.abs(vf[ok]))
        wsm = np.asarray(f[cws][0, :], dtype=float)
        h = np.clip(wsm - zmin, 0.0, None)
        molh = h > molhada_m
        molh = molh & (area > 0)
        dx = np.sqrt(np.where(area > 0, area, np.nan))
        cel = (vc + np.sqrt(g * h)) * dt_s / dx
        cv = vc * dt_s / dx
        cel_m, cv_m = cel[molh], cv[molh]
        if cel_m.size == 0:
            av.append("%s: nenhuma celula molhada no resumo" % nm)
            continue
        d = {"dt_usado_s": float(dt_s), "passo_adaptativo": adaptativo, "celulas_molhadas": int(cel_m.size),
             "courant_celeridade": _estat(cel_m, 3), "courant_so_velocidade": _estat(cv_m, 3),
             "celulas_C_celeridade_acima_1": int((cel_m > 1).sum()),
             "celulas_C_celeridade_acima_3": int((cel_m > 3).sum())}
        res[nm] = d
        eq = str(pl.get("equacao_2d") or "")
        lim = 5.0 if "diff" in eq.lower() else 3.0
        if cv_m.max() > lim:
            av.append("%s: Courant estimado (so velocidade, como o programa) max %.2f > %.1f em %.2f %% das celulas "
                      "molhadas com dT = %.1f s (%s) [USACE-HECRAS-2DUM-66 p. 201, 203]; confira no Mapper: se for "
                      "face isolada, trate a borda; se for ampla, reduza dT ou use passo por Courant"
                      % (nm, cv_m.max(), lim, (cv_m > lim).mean() * 100, dt_s, eq or "equacao nao informada"))
        elif cv_m.max() > 1.0:
            av.append("%s: Courant estimado (so velocidade) max %.2f entre 1,0 e %.1f: aceitavel so se o evento "
                      "varia devagar e a malha nao partiu a seco [USACE-HECRAS-2DUM-66 p. 201]" % (nm, cv_m.max(), lim))
        if np.percentile(cel_m, 95) > lim:
            av.append("%s: pelo criterio da celeridade (V + sqrt(g h), formula da p. 200) o Courant p95 e %.1f > %.1f "
                      "(informativo; o HEC-RAS usa so a velocidade, e o esquema implicito tolera C > 1; "
                      "teste dT menor como sensibilidade) [USACE-HECRAS-2DUM-66 p. 200-201]"
                      % (nm, np.percentile(cel_m, 95), lim))
    return {"areas": res, "gravidade": g, "metodo": "Courant estimado com sqrt(area) como dX (nao e o do programa)",
            "avisos": av}


# ----------------------------------------------------------------------------- contornos
def contornos(f):
    """Condicoes de contorno gravadas em Event Conditions (hidrogramas, profundidade normal, NA, rating) e as
    linhas de contorno da geometria 2D."""
    np = _np()
    av = []
    out = {"linhas_geometria": [], "evento": {}}
    if "Geometry/Boundary Condition Lines/Attributes" in f:
        a = f["Geometry/Boundary Condition Lines/Attributes"][()]
        for r in a:
            out["linhas_geometria"].append({"nome": _txt(r["Name"]), "area": _txt(r["SA-2D"]), "tipo": _txt(r["Type"]),
                                            "comprimento": round(float(r["Length"]), 2)})
    base = "Event Conditions/Unsteady/Boundary Conditions"
    if base in f:
        for tipo in f[base].keys():
            for nm, ds in f[base + "/" + tipo].items():
                if not hasattr(ds, "shape"):
                    continue
                reg = {"tipo": tipo}
                arr = np.asarray(ds[()], dtype=float)
                if tipo.lower().startswith("normal"):
                    reg["declividade"] = float(arr.ravel()[0])
                    reg["declividade_pct"] = round(float(arr.ravel()[0]) * 100, 6)
                    av.append("contorno '%s' em profundidade normal (declividade %.6f = %.4f %%): so vale com "
                              "declividade MEDIDA e secao uniforme; sem barragem ou remanso a jusante "
                              "[USACE-HECRAS-2DUM-66 p. 144-145; caso HR-03]" % (nm, reg["declividade"],
                                                                                 reg["declividade_pct"]))
                elif arr.ndim == 2 and arr.shape[1] >= 2:
                    reg["pontos"] = int(arr.shape[0])
                    reg["valor_max"] = float(arr[:, 1].max())
                    reg["valor_min"] = float(arr[:, 1].min())
                    reg["constante"] = bool(np.allclose(arr[:, 1], arr[0, 1]))
                out["evento"][nm] = reg
    else:
        av.append("sem 'Event Conditions/Unsteady/Boundary Conditions' (arquivo de geometria ou execucao permanente)")
    return {**out, "metodo": "Event Conditions e Boundary Condition Lines", "avisos": av}


# ----------------------------------------------------------------------------- 1D (secoes)
def _acha(f, raiz, padrao):
    """Datasets sob `raiz` cujo ultimo nome casa com `padrao` (regex, ignora caixa)."""
    achados = []
    if raiz not in f:
        return achados
    rx = re.compile(padrao, re.I)

    def _v(nome, obj):
        if hasattr(obj, "shape") and rx.search(nome.rsplit("/", 1)[-1]):
            achados.append(raiz + "/" + nome)
    f[raiz].visititems(_v)
    return achados


def secoes_1d(f):
    """Por secao transversal 1D (nao permanente ou permanente): rio, trecho, estacao, NA maximo e velocidade
    maxima (canal ou total). Layout verificado so com fixture sintetica (ver docstring do modulo)."""
    np = _np()
    av = []
    if "Geometry/Cross Sections/Attributes" not in f:
        return {"secoes": [], "metodo": "1D", "avisos": ["arquivo sem 'Geometry/Cross Sections/Attributes' (sem 1D)"]}
    a = f["Geometry/Cross Sections/Attributes"][()]
    nomes = a.dtype.names
    ns = len(a)
    rio = [_txt(x) for x in a["River"]] if "River" in nomes else [""] * ns
    trecho = [_txt(x) for x in a["Reach"]] if "Reach" in nomes else [""] * ns
    rs = [_txt(x) for x in a["RS"]] if "RS" in nomes else [str(i) for i in range(ns)]
    ws_max = None
    vel_max = None
    origem = None
    # nao permanente: serie no tempo (nt, ns) ou resumo
    for raiz in (_TS + "Cross Sections", _SUM + "Cross Sections"):
        for cam in _acha(f, raiz, r"^Water Surface$|^Maximum Water Surface$"):
            arr = np.asarray(f[cam][()], dtype=float)
            if arr.ndim == 2 and arr.shape[1] == ns:
                ws_max = arr.max(axis=0) if arr.shape[0] != 2 or "Maximum" not in cam else arr[0]
                origem = cam
                break
            if arr.ndim == 2 and arr.shape[0] == 2 and arr.shape[1] == ns:
                ws_max = arr[0]
                origem = cam
                break
        if ws_max is not None:
            break
    if ws_max is None:  # permanente: (perfis, secoes)
        raiz = "Results/Steady/Output/Output Blocks/Base Output/Steady Profiles/Cross Sections"
        for cam in _acha(f, raiz, r"^Water Surface$"):
            arr = np.asarray(f[cam][()], dtype=float)
            if arr.ndim == 2 and arr.shape[1] == ns:
                ws_max = arr.max(axis=0)
                origem = cam
                break
    for raiz in (_TS + "Cross Sections", _SUM + "Cross Sections",
                 "Results/Steady/Output/Output Blocks/Base Output/Steady Profiles/Cross Sections"):
        for cam in _acha(f, raiz, r"Velocity (Total|Channel)|Maximum Velocity"):
            arr = np.asarray(f[cam][()], dtype=float)
            if arr.ndim == 2 and arr.shape[1] == ns:
                vel_max = arr.max(axis=0)
                break
        if vel_max is not None:
            break
    if ws_max is None:
        av.append("secoes 1D sem NA de resultado em caminho conhecido: nada extraido (nao inventado)")
    if vel_max is None:
        av.append("velocidade por secao nao encontrada em caminho conhecido")
    out = []
    for i in range(ns):
        out.append({"rio": rio[i], "trecho": trecho[i], "estacao": rs[i],
                    "NA_max": None if ws_max is None else round(float(ws_max[i]), 3),
                    "V_max": None if vel_max is None else round(float(vel_max[i]), 3)})
    n1d = {}
    if "Geometry/Cross Sections/Manning's n Info" in f and "Geometry/Cross Sections/Manning's n Values" in f:
        vals = np.asarray(f["Geometry/Cross Sections/Manning's n Values"][()], dtype=float)
        if vals.ndim == 2 and vals.shape[1] >= 2:
            u = np.unique(np.round(vals[:, 1], 5))
            n1d = {"distintos": int(u.size), "min": float(u.min()), "max": float(u.max())}
            if u.size == 1:
                av.append("n de Manning unico em todas as secoes 1D: sem calibracao nem sensibilidade (+-20 %%) nao "
                          "se fixa cota de projeto [USACE-HECRAS-UM-66 p. 328]")
    return {"secoes": out, "origem_NA": origem, "manning_n_1d": n1d, "metodo": "1D (layout HEC-RAS 6.x)",
            "avisos": av}


# ----------------------------------------------------------------------------- relatorio
def verificar(arquivo, dt_s=None, janela_h=2.0):
    """Relatorio de verificacao de um `.hdf` de plano: plano, passo, malha, n, contornos, resultados 2D, estabilizacao,
    Courant estimado e secoes 1D, com `avisos` agregados. Somente leitura."""
    f = abrir(arquivo)
    try:
        partes = {}
        av = []
        tem2d = bool(_areas_2d(f))
        for nome, fn in (("plano", lambda: info_plano(f)), ("malha", lambda: malha_2d(f)),
                         ("contornos", lambda: contornos(f)),
                         ("resultados_2d", lambda: resultados_2d(f, janela_h=janela_h)),
                         ("courant", lambda: courant_2d(f, dt_s=dt_s)), ("secoes_1d", lambda: secoes_1d(f))):
            try:
                r = fn()
            except KeyError as e:  # layout diferente do esperado
                av.append("%s: caminho ausente no arquivo (%s)" % (nome, e))
                continue
            avs = r.pop("avisos", [])
            if nome == "secoes_1d" and tem2d and not r.get("secoes"):
                avs = []
            av.extend(avs)
            r.pop("metodo", None)
            partes[nome] = r
        pt = passo_de_tempo(f)
        if pt:
            partes["passo_efetivo"] = pt
        pl = partes.get("plano", {}).get("plano", {})
        if pl and not pl.get("equacao_2d") and partes.get("malha", {}).get("areas"):
            av.append("equacao 2D nao informada no plano")
        if not any(k in partes for k in ("resultados_2d",)) or not partes["resultados_2d"].get("areas"):
            if not partes.get("secoes_1d", {}).get("secoes"):
                av.append("arquivo sem resultados 2D nem 1D (so geometria?)")
        out = {"arquivo": os.path.basename(arquivo), **partes, "metodo": "verificacao somente leitura de .hdf do HEC-RAS",
               "avisos": av + ["o relatorio verifica coerencia do arquivo; NAO substitui calibracao, sensibilidade de "
                               "n/TR nem comparacao com dado observado"]}
        return out
    finally:
        f.close()


def _com_arquivo(fn):
    def _w(arquivo, **kw):
        f = abrir(arquivo)
        try:
            return fn(f, **kw)
        finally:
            f.close()
    _w.__doc__ = fn.__doc__
    _w.__name__ = fn.__name__
    return _w


def comparar(valor_arquivo, valor_relatorio, tol_rel=0.05):
    """Compara um numero lido do .hdf com o do relatorio/caso (tolerancia relativa, padrao 5 %)."""
    if valor_relatorio == 0:
        raise ValueError("valor_relatorio = 0: comparacao relativa indefinida")
    dif = (valor_arquivo - valor_relatorio) / abs(valor_relatorio)
    av = []
    if abs(dif) > tol_rel:
        av.append("diferenca %.1f %% acima da tolerancia %.1f %%" % (dif * 100, tol_rel * 100))
    return {"diferenca_rel": dif, "dentro_da_tolerancia": abs(dif) <= tol_rel, "metodo": "comparacao relativa",
            "avisos": av}


FUNCOES = {
    "verificar": verificar,
    "plano": _com_arquivo(info_plano),
    "malha": _com_arquivo(malha_2d),
    "resultados_2d": _com_arquivo(resultados_2d),
    "courant": _com_arquivo(courant_2d),
    "contornos": _com_arquivo(contornos),
    "secoes_1d": _com_arquivo(secoes_1d),
    "comparar": comparar,
}

if __name__ == "__main__":
    from tools.dren._cli import principal
    principal("tools.dren.hecras_hdf", VERSAO, FUNCOES)
