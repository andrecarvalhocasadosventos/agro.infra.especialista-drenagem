"""Pos-processa referencias/_catalogo.yaml: acrescenta tem_texto, ocr, paginas_ocr, caracteres, escaneado
a partir de referencias/_texto/_indice.yaml (extrair_texto.py) e referencias/_ocr/*.jsonl (ocr_pdf.py).

Ordem de uso: baixar_referencias.py -> (ocr_pdf.py) -> extrair_texto.py [--forcar] -> catalogar.py
Campos finais por documento: id, titulo, orgao, ano, arquivo, sha256, paginas, tem_texto, ocr, licenca,
prioridade, temas, origem (+ fonte, tipo, url, bytes, status, obs, escaneado, paginas_ocr, caracteres).
"""
from __future__ import annotations

import datetime as dt
from pathlib import Path

import yaml

RAIZ = Path(__file__).resolve().parents[1]
REF = RAIZ / "referencias"
CAT = REF / "_catalogo.yaml"
IDX = REF / "_texto" / "_indice.yaml"


def main() -> int:
    c = yaml.safe_load(CAT.read_text(encoding="utf-8"))
    idx = {x["id"]: x for x in yaml.safe_load(IDX.read_text(encoding="utf-8"))["documentos"]}
    for d in c["documentos"]:
        x = idx.get(d["id"])
        if not x:
            d.update(tem_texto=False, ocr="nao")
            continue
        ocrp = x.get("ocr_paginas") or 0
        paginas = x.get("paginas") or 0
        d["caracteres"] = x["caracteres"]
        d["escaneado"] = bool(x.get("escaneado"))
        sem = x.get("paginas_sem_texto") or 0  # paginas ainda sem texto (nativo ou OCR) < 20 caracteres
        frac = sem / max(paginas, 1)
        d["paginas_ocr"] = ocrp
        d["paginas_sem_texto"] = sem
        d["tem_texto"] = x["caracteres"] > 200
        if ocrp:
            d["ocr"] = "completo" if frac <= 0.05 else "parcial"
            d["ocr_motor"] = "rapidocr-onnx (local), 200 dpi"
        else:
            d["ocr"] = "pendente" if (x.get("escaneado") or frac > 0.20) else "nao-necessario"
    st = c["metadados"]["por_status"]
    c["metadados"]["gerado_em"] = dt.datetime.now().isoformat(timespec="seconds")
    c["metadados"]["pos_processado_por"] = "tools/catalogar.py"
    CAT.write_text("# Catalogo do corpus de referencias -- gerado por tools/baixar_referencias.py + tools/catalogar.py; nao editar a mao.\n"
                   + yaml.safe_dump(c, allow_unicode=True, sort_keys=False, width=200), encoding="utf-8")
    print(f"catalogo: {len(c['documentos'])} documentos; status {st}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
