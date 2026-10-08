"""Extrai o texto do corpus para referencias/_texto/<id>.md com marcadores de pagina.

- PDFs: PyMuPDF, pagina a pagina, com marcador "<!-- p. N -->" (N = pagina fisica do PDF, 1-based).
  Os bookmarks do PDF (se houver) entram no topo como "Sumario (bookmarks)".
- .md gerados a partir de HTML (legislacao, sumulas, paginas): copiados com cabecalho.
- Duplicatas (campo duplicata_de no catalogo) nao sao extraidas de novo.
- PDFs escaneados (media < LIMIAR caracteres/pagina) sao marcados; nao ha OCR.
Gera referencias/_texto/_indice.yaml. Idempotente (pula se o sha256 da fonte e os metadados do cabecalho nao mudaram;
a 1a linha e '<!-- id: X | sha256: Y | meta: Z -->').

Uso:
    python tools/extrair_texto.py [--forcar]
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

import pymupdf
import yaml

RAIZ = Path(__file__).resolve().parents[1]
REF = RAIZ / "referencias"
CATALOGO = REF / "_catalogo.yaml"
SAIDA = REF / "_texto"
INDICE = SAIDA / "_indice.yaml"
PREV: dict[str, dict] = {}  # indice da execucao anterior (preenchido em main)
LIMIAR = 80  # caracteres/pagina abaixo disso -> provavel escaneado


CAMPOS_META = ("titulo", "tipo", "vigencia", "temas", "fonte")
PRIMEIRA_LINHA_RE = re.compile(r"^<!-- id: (?P<id>.+?) \| sha256: (?P<sha>\S+)(?: \| meta: (?P<meta>\S+))? -->\s*$")


def hash_meta(doc: dict) -> str:
    """Hash curto (12 hex) dos metadados exibidos no cabecalho (titulo, tipo, vigencia, temas, fonte)."""
    dados = {c: doc.get(c) for c in CAMPOS_META}
    bruto = json.dumps(dados, ensure_ascii=False, sort_keys=True, default=str)
    return hashlib.sha256(bruto.encode("utf-8")).hexdigest()[:12]


def cabecalho(doc: dict, extra: str = "") -> str:
    return (
        f"<!-- id: {doc['id']} | sha256: {doc.get('sha256')} | meta: {hash_meta(doc)} -->\n"
        f"# {doc['id']} - {doc.get('titulo')}\n\n"
        f"- Fonte: {doc.get('fonte')} | Tipo: {doc.get('tipo')} | Vigencia: {doc.get('vigencia')} | Temas: {', '.join(doc.get('temas') or [])}\n"
        f"- Arquivo: referencias/{doc.get('arquivo')}\n"
        f"- URL: {doc.get('url')}\n{extra}\n"
    )


def ja_extraido(dest: Path, doc: dict) -> bool:
    """True se o texto existe e a primeira linha traz o sha256 e o hash de metadados atuais."""
    sha = doc.get("sha256")
    if not dest.exists() or not sha:
        return False
    with dest.open(encoding="utf-8") as f:
        m = PRIMEIRA_LINHA_RE.match(f.readline())
    return bool(m) and m["sha"] == str(sha) and m["meta"] == hash_meta(doc)


def extrair_pdf(doc: dict, dest: Path) -> dict:
    src = REF / doc["arquivo"]
    info = {"id": doc["id"], "texto": dest.relative_to(REF).as_posix(), "paginas": 0, "caracteres": 0}
    ocr: dict[int, str] = {}
    oj = REF / "_ocr" / f"{doc['id']}.jsonl"
    if oj.exists():
        for ln in oj.read_text(encoding="utf-8").splitlines():
            if ln.strip():
                o = json.loads(ln)
                ocr[o["p"]] = o["texto"]
    info["ocr_paginas"] = 0
    info["caracteres_nativo"] = 0
    with pymupdf.open(src) as pdf:
        info["paginas"] = pdf.page_count
        toc = pdf.get_toc(simple=True)
        partes: list[str] = []
        vazias = 0
        # PDF 100% escaneado (indice anterior: 0 caracteres nativos) com OCR de todas as paginas: dispensa reler o PDF
        so_ocr = len(ocr) >= pdf.page_count and (lambda q: q.get("caracteres_nativo", q.get("caracteres")))(PREV.get(doc["id"]) or {}) == 0
        for i, pg in enumerate(pdf, start=1):
            t = "" if so_ocr else pg.get_text("text", sort=True)
            t = re.sub(r"[ \t]+\n", "\n", t)
            t = re.sub(r"\n{3,}", "\n\n", t).strip()
            info["caracteres_nativo"] += len(t)
            marca = f"<!-- p. {i} -->"
            if len(t) < 20 and i in ocr and ocr[i].strip():
                t = ocr[i].strip()
                info["ocr_paginas"] += 1
                marca += "\n<!-- ocr -->"
            elif len(t) < 20:
                vazias += 1
            info["caracteres"] += len(t)
            partes.append(f"{marca}\n{t}\n")
    info["caracteres_por_pagina"] = round(info["caracteres"] / max(info["paginas"], 1))
    info["paginas_sem_texto"] = vazias
    info["escaneado"] = info["caracteres_nativo"] / max(info["paginas"], 1) < LIMIAR
    info["bookmarks"] = len(toc)
    extra = f"- Paginas: {info['paginas']} | Caracteres: {info['caracteres']}"
    if info["escaneado"]:
        extra += " | ATENCAO: provavel PDF escaneado (sem camada de texto nativa)"
    if info["ocr_paginas"]:
        extra += f" | OCR local (RapidOCR) em {info['ocr_paginas']} pagina(s); trechos marcados com <!-- ocr -->"
    extra += "\n"
    if toc:
        linhas = [f"{'  ' * (nivel - 1)}- {titulo.strip()} (p. {pag})" for nivel, titulo, pag in toc[:400]]
        extra += "\n## Sumario (bookmarks do PDF)\n\n" + "\n".join(linhas) + "\n"
    dest.write_text(cabecalho(doc, extra) + "\n## Texto\n\n" + "\n".join(partes), encoding="utf-8")
    return info


def copiar_md(doc: dict, dest: Path) -> dict:
    src = REF / doc["arquivo"]
    t = src.read_text(encoding="utf-8")
    dest.write_text(cabecalho(doc, "- Paginas: n/a (documento HTML/texto)\n") + "\n## Texto\n\n" + t, encoding="utf-8")
    return {"id": doc["id"], "texto": dest.relative_to(REF).as_posix(), "paginas": None,
            "caracteres": len(t), "escaneado": False}


def copiar_docx(doc: dict, dest: Path) -> dict:
    """Extrai o texto de .docx (Office Open XML) com a stdlib: um paragrafo por linha, tabelas com ' | '."""
    import html
    import zipfile

    src = REF / doc["arquivo"]
    with zipfile.ZipFile(src) as z:
        xml = z.read("word/document.xml").decode("utf-8", errors="replace")
    xml = re.sub(r"</w:tc>", " | ", xml)
    xml = re.sub(r"</w:p>|</w:tr>", "\n", xml)
    xml = re.sub(r"<w:tab/>", "\t", xml)
    t = html.unescape(re.sub(r"<[^>]+>", "", xml))
    t = re.sub(r"[ \t]+\n", "\n", t)
    t = re.sub(r"\n{3,}", "\n\n", t).strip()
    corpo = cabecalho(doc, "- Paginas: n/a (documento .docx)\n") + "\n## Texto\n\n" + t + "\n"
    dest.write_text(corpo, encoding="utf-8")
    return {"id": doc["id"], "texto": dest.relative_to(REF).as_posix(), "paginas": None,
            "caracteres": len(t), "escaneado": False}


def copiar_xlsx(doc: dict, dest: Path) -> dict:
    """Planilha: uma secao por aba, celulas nao vazias como 'A1: valor' (formulas e valores em cache)."""
    import openpyxl

    NL = chr(10)
    src = REF / doc["arquivo"]
    linhas: list[str] = []
    for modo in (False, True):  # False = formulas; True = valores calculados
        wb = openpyxl.load_workbook(src, data_only=modo)
        linhas.append(NL + "### " + ("Valores calculados" if modo else "Formulas") + NL)
        for ws in wb.worksheets:
            linhas.append(NL + "#### Aba: " + ws.title + NL)
            for row in ws.iter_rows():
                for c in row:
                    if c.value is not None:
                        linhas.append(f"{c.coordinate}: {c.value}")
    t = NL.join(linhas)
    dest.write_text(cabecalho(doc, "- Paginas: n/a (planilha .xlsx)" + NL) + NL + "## Texto" + NL + NL + t + NL, encoding="utf-8")
    return {"id": doc["id"], "texto": dest.relative_to(REF).as_posix(), "paginas": None,
            "caracteres": len(t), "escaneado": False}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--forcar", action="store_true")
    a = ap.parse_args()
    cat = yaml.safe_load(CATALOGO.read_text(encoding="utf-8"))["documentos"]
    SAIDA.mkdir(parents=True, exist_ok=True)
    antigo: dict[str, dict] = {}
    if INDICE.exists():
        antigo = {x["id"]: x for x in (yaml.safe_load(INDICE.read_text(encoding="utf-8")) or {}).get("documentos", [])}
        PREV.update(antigo)
    indice: list[dict] = []
    nao_extraidos: list[dict] = []
    for doc in cat:
        if doc.get("status") == "pendente_ocr":
            nao_extraidos.append({"id": doc["id"], "motivo": "pendente_ocr (sem camada de texto; OCR local a fazer)"})
            continue
        if doc.get("status") != "ok" or not doc.get("arquivo"):
            continue
        ext = Path(doc["arquivo"]).suffix.lower()
        if doc.get("duplicata_de"):
            nao_extraidos.append({"id": doc["id"], "motivo": f"duplicata de {doc['duplicata_de']}"})
            continue
        if ext not in (".pdf", ".md", ".docx", ".xlsx"):
            if ext not in (".7z", ".rar", ".zip"):
                nao_extraidos.append({"id": doc["id"], "motivo": f"formato {ext} nao extraido"})
            continue
        dest = SAIDA / f"{doc['id']}.md"
        if not a.forcar and ja_extraido(dest, doc) and doc["id"] in antigo:
            indice.append(antigo[doc["id"]])
            continue
        try:
            if ext == ".pdf":
                info = extrair_pdf(doc, dest)
            elif ext == ".xlsx":
                info = copiar_xlsx(doc, dest)
            elif ext == ".docx":
                info = copiar_docx(doc, dest)
            else:
                info = copiar_md(doc, dest)
        except Exception as ex:  # noqa: BLE001
            nao_extraidos.append({"id": doc["id"], "motivo": f"erro: {ex}"[:300]})
            continue
        indice.append(info)
        print(f"{doc['id']}: {info.get('paginas')} p., {info['caracteres']} car." + (" [ESCANEADO]" if info.get("escaneado") else ""), flush=True)
    esc = [x["id"] for x in indice if x.get("escaneado")]
    INDICE.write_text(
        "# Indice da extracao de texto -- gerado por tools/extrair_texto.py\n"
        + yaml.safe_dump({"total_extraidos": len(indice), "escaneados_sem_texto": esc,
                          "nao_extraidos": nao_extraidos, "documentos": indice},
                         allow_unicode=True, sort_keys=False, width=200),
        encoding="utf-8",
    )
    print(f"extraidos: {len(indice)} | escaneados: {len(esc)} | nao extraidos: {len(nao_extraidos)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
