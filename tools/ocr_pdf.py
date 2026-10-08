# -*- coding: utf-8 -*-
"""OCR local (RapidOCR/onnx, sem LLM) de PDF escaneado de pagina unica por folha.

Uso: python tools/ocr_pdf.py --id ID [--paginas 1-20,100] [--dpi 200] [--workers 4]
Le o PDF do catalogo (referencias/_catalogo.yaml) e grava incrementalmente
referencias/_ocr/<ID>.jsonl (uma linha por pagina: p, texto, conf, chars). Retoma de onde parou.
O texto entra em _texto/ por tools/extrair_texto.py (que usa o jsonl nas paginas sem camada de texto).
"""
import argparse
import json
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import numpy as np
import pymupdf
import yaml

RAIZ = Path(__file__).resolve().parents[1]
REF = RAIZ / "referencias"
OCR = REF / "_ocr"
_tl = threading.local()
_lock = threading.Lock()


def engine():
    if not hasattr(_tl, "e"):
        from rapidocr_onnxruntime import RapidOCR
        _tl.e = RapidOCR()
    return _tl.e


def linhas(res):
    its = []
    for box, t, c in res:
        ys = [p[1] for p in box]
        xs = [p[0] for p in box]
        its.append((sum(ys) / 4, min(xs), max(ys) - min(ys), t, float(c)))
    if not its:
        return [], 0.0
    its.sort(key=lambda r: r[0])
    hs = sorted(r[2] for r in its)
    tol = max(6, hs[len(hs) // 2] * 0.6)
    grupos = []
    for r in its:
        if grupos and abs(r[0] - grupos[-1]["y"]) <= tol:
            g = grupos[-1]
            g["it"].append(r)
            g["y"] = sum(x[0] for x in g["it"]) / len(g["it"])
        else:
            grupos.append({"y": r[0], "it": [r]})
    out = []
    for g in grupos:
        g["it"].sort(key=lambda r: r[1])
        out.append(" ".join(r[3] for r in g["it"]))
    return out, float(np.mean([r[4] for r in its]))


def pagina(args):
    pdf, p, dpi = args
    with pymupdf.open(pdf) as d:
        pix = d[p - 1].get_pixmap(dpi=dpi, colorspace=pymupdf.csGRAY)
    img = np.frombuffer(pix.samples, np.uint8).reshape(pix.height, pix.width)
    rgb = np.stack([img] * 3, -1)
    res, _ = engine()(np.ascontiguousarray(rgb))
    ls, conf = linhas(res or [])
    t = "\n".join(ls)
    return {"p": p, "texto": t, "conf": round(conf, 3), "chars": len(t)}


def parse(s, n):
    if not s:
        return list(range(1, n + 1))
    out = []
    for x in s.split(","):
        a, _, b = x.partition("-")
        out += range(int(a), int(b or a) + 1)
    return [p for p in out if 1 <= p <= n]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--id", required=True)
    ap.add_argument("--paginas")
    ap.add_argument("--vazias", action="store_true", help="so paginas com < 20 caracteres de texto nativo")
    ap.add_argument("--dpi", type=int, default=200)
    ap.add_argument("--workers", type=int, default=4)
    a = ap.parse_args()
    cat = {d["id"]: d for d in yaml.safe_load((REF / "_catalogo.yaml").read_text(encoding="utf-8"))["documentos"]}
    pdf = REF / cat[a.id]["arquivo"]
    OCR.mkdir(exist_ok=True)
    saida = OCR / f"{a.id}.jsonl"
    feitas = set()
    if saida.exists():
        feitas = {json.loads(l)["p"] for l in saida.read_text(encoding="utf-8").splitlines() if l.strip()}
    with pymupdf.open(pdf) as d:
        n = d.page_count
        vazias = [i + 1 for i, pg in enumerate(d) if len(pg.get_text().strip()) < 20] if a.vazias else None
    alvo = [p for p in parse(a.paginas, n) if p not in feitas and (vazias is None or p in vazias)]
    print(f"{a.id}: {n} paginas; a fazer {len(alvo)}; ja feitas {len(feitas)}", flush=True)
    t0 = time.time()

    def tarefa(p):
        r = pagina((str(pdf), p, a.dpi))
        with _lock:
            with saida.open("a", encoding="utf-8") as f:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        return r

    k = 0
    with ThreadPoolExecutor(a.workers) as ex:
        for r in ex.map(tarefa, alvo):
            k += 1
            if k % 10 == 0:
                print(f"{k}/{len(alvo)} ({time.time() - t0:.0f}s)", flush=True)
    print(f"fim: {len(alvo)} paginas em {time.time() - t0:.0f}s", flush=True)


if __name__ == "__main__":
    main()
