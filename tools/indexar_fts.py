r"""Indice FTS5 por pagina do corpus proprio do Drenagem, FORA do Drive (SQLite corrompe em pasta sincronizada).

Uso: python tools/indexar_fts.py [--db C:\bibdren\db\corpus.sqlite]
Le referencias/_texto/*.md (marcadores '<!-- p. N -->'); para planilhas/HTML (sem marcador) grava pagina 0.
Tabelas: doc(id, titulo, arquivo, ocr), pagina(id, pagina, texto), busca_pagina (FTS5 sobre texto,
tokenizer unicode61 remove_diacritics 2; colunas nao indexadas: id, pagina).
Busca:  SELECT id, pagina, snippet(busca_pagina, 0, '[', ']', '...', 12) FROM busca_pagina WHERE busca_pagina MATCH 'sarjeta AND "tempo de concentracao"' ORDER BY rank LIMIT 10;
Cobre so os itens novos (lacunas abertas + locais); o corpus do Hidraulico segue pelo indice dele (C:\bibhid) e por caminho (D1).
Reconstruivel a qualquer momento: o script recria o banco do zero.
"""
from __future__ import annotations

import argparse
import re
import sqlite3
from pathlib import Path

import yaml

RAIZ = Path(__file__).resolve().parents[1]
REF = RAIZ / "referencias"
MARC = re.compile(r"<!-- p\. (\d+) -->")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=r"C:\bibdren\db\corpus.sqlite")
    a = ap.parse_args()
    db = Path(a.db)
    db.parent.mkdir(parents=True, exist_ok=True)
    db.unlink(missing_ok=True)
    cat = {d["id"]: d for d in yaml.safe_load((REF / "_catalogo.yaml").read_text(encoding="utf-8"))["documentos"]}
    c = sqlite3.connect(db)
    c.executescript("""
        CREATE TABLE doc (id TEXT PRIMARY KEY, titulo TEXT, arquivo TEXT, ocr TEXT, paginas INTEGER);
        CREATE TABLE pagina (id TEXT, pagina INTEGER, texto TEXT, PRIMARY KEY (id, pagina));
        CREATE VIRTUAL TABLE busca_pagina USING fts5(texto, id UNINDEXED, pagina UNINDEXED,
            tokenize = 'unicode61 remove_diacritics 2');
    """)
    n_doc = n_pag = 0
    for f in sorted((REF / "_texto").glob("*.md")):
        i = f.stem
        d = cat.get(i, {})
        t = f.read_text(encoding="utf-8")
        corpo = t.split("## Texto", 1)[-1]
        partes = MARC.split(corpo)
        paginas = [(0, corpo.strip())] if len(partes) == 1 else [
            (int(partes[k]), partes[k + 1].strip()) for k in range(1, len(partes), 2)]
        c.execute("INSERT INTO doc VALUES (?,?,?,?,?)", (i, d.get("titulo"), d.get("arquivo"), d.get("ocr"), d.get("paginas")))
        for p, txt in paginas:
            if not txt:
                continue
            c.execute("INSERT INTO pagina VALUES (?,?,?)", (i, p, txt))
            c.execute("INSERT INTO busca_pagina (texto, id, pagina) VALUES (?,?,?)", (txt, i, p))
            n_pag += 1
        n_doc += 1
    c.commit()
    c.close()
    print(f"{db}: {n_doc} documentos, {n_pag} paginas com texto, {db.stat().st_size / 1e6:.1f} MB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
