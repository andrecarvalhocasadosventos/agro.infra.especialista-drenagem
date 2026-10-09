"""Gera tools/fontes.yaml a partir de tools/fontes_candidatas.yaml (manifesto aprovado na F1) e,
com --copiar, copia as fontes locais (D8) para referencias/<pasta>/.

Uso:
    python tools/montar_fontes.py [--copiar]
Abertos -> metodo http; locais -> metodo local (arquivo ja copiado em referencias/).
Somente os itens listados em fontes_locais: sao copiados (nada mais da pasta de origem).
"""
from __future__ import annotations

import argparse
import re
import shutil
import unicodedata
from pathlib import Path

import yaml

RAIZ = Path(__file__).resolve().parents[1]
T = RAIZ / "tools"
REF = RAIZ / "referencias"

PASTA_ABERTA = [
    ("DNIT-", "01_BR-DNIT", "DNIT"),
    ("DERPR-", "02_BR-DER-PR", "DER/PR"),
    ("EMBRAPA-", "03_BR-EMBRAPA", "Embrapa"),
    ("FHWA-", "04_FHWA", "FHWA"),
    ("USACE-", "05_USACE", "USACE"),
    ("USGS-", "06_US-USGS-NRCS-DOT", "USGS"),
    ("NRCS-", "06_US-USGS-NRCS-DOT", "NRCS"),
    ("WSDOT-", "06_US-USGS-NRCS-DOT", "WSDOT"),
    ("FDOT-", "06_US-USGS-NRCS-DOT", "FDOT"),
    ("ILRI-", "07_ILRI-WATERLOG", "ILRI"),
    ("WATERLOG-", "07_ILRI-WATERLOG", "WATERLOG"),
]


# Itens que o servidor entrega corrompidos/truncados (ver PENDENTES_DOWNLOAD_MANUAL.md)
OVERRIDES = {
    "FDOT-DRAINAGE-MANUAL-2016": {
        "status": "manual_needed",
        "obs": "servidor entrega PDF truncado (1.844.371 bytes, sem xref/EOF; 0 paginas legiveis; 2 tentativas identicas); baixar no navegador ou obter edicao atual",
    },
}


def slug(t: str, n: int = 40) -> str:
    s = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    return re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-").lower()[:n].strip("-") or "arquivo"


def pasta_local(origem: str) -> tuple[str, str]:
    o = origem.upper()
    if "PFAFSTETTER" in o:
        return "10_LOCAL-PFAFSTETTER", "Pfafstetter/DNOS"
    if "\\ABTC\\" in o:
        return "11_LOCAL-ABTC", "ABTC"
    if "ROBSON" in o:
        return "15_LOCAL-CURSO-ROBSON", "Curso Robson"
    if "\\DNIT\\" in o:
        return "13_LOCAL-ESTRADAS", "DNIT"
    if "\\COMAER\\" in o:
        return "13_LOCAL-ESTRADAS", "COMAER"
    if "\\IME\\" in o:
        return "13_LOCAL-ESTRADAS", "IME"
    if "SISCCOH" in o or "GABI" in o:
        return "14_LOCAL-SOFTWARE-CASOS", "SisCCoH" if "SISCCOH" in o else "Estudos"
    return "12_LOCAL-HIDROLOGIA", "Estudos"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--copiar", action="store_true")
    a = ap.parse_args()
    d = yaml.safe_load((T / "fontes_candidatas.yaml").read_text(encoding="utf-8"))
    saida: list[dict] = []
    for i in d["itens"]:
        pasta, fonte = next((p, f) for pre, p, f in PASTA_ABERTA if i["id"].startswith(pre))
        r = {
            "id": i["id"], "titulo": i["titulo"], "fonte": fonte, "orgao": i.get("orgao"), "ano": i.get("ano"),
            "temas": i.get("temas"), "tipo": i.get("tipo"), "vigencia": i.get("vigencia"),
            "url": i["url"], "pasta": pasta, "arquivo": f"{i['id']}_{slug(i['titulo'])}.pdf",
            "prioridade": i.get("prioridade"), "licenca": i.get("licenca"), "metodo": i.get("metodo", "http"),
            "origem": "aberta/F1",
        }
        if i.get("alternativas"):
            r["alternativas"] = i["alternativas"]
        if r["metodo"] == "link_only":
            r["status"] = "link_only"
        r.update(OVERRIDES.get(i["id"], {}))
        saida.append({k: v for k, v in r.items() if v is not None})
    copiados = 0
    for i in d["fontes_locais"]:
        src = Path(i["origem"])
        pasta, fonte = pasta_local(i["origem"])
        ext = src.suffix.lower()
        arq = f"{i['id']}{ext}"
        r = {
            "id": i["id"], "titulo": i["titulo"], "fonte": fonte, "orgao": fonte, "temas": i.get("temas"),
            "tipo": "local", "origem": i["origem"], "pasta": pasta, "arquivo": arq, "prioridade": i.get("prioridade"),
            "licenca": i.get("licenca", "uso-interno"), "metodo": "local", "escaneado_f1": i.get("escaneado"),
            "obs": i.get("nota"),
        }
        saida.append({k: v for k, v in r.items() if v is not None})
        if a.copiar:
            dst = REF / pasta / arq
            dst.parent.mkdir(parents=True, exist_ok=True)
            if not dst.exists() or dst.stat().st_size != src.stat().st_size:
                shutil.copy2(src, dst)
                copiados += 1
    (T / "fontes.yaml").write_text(
        "# Manifesto de download - Especialista Drenagem (gerado por tools/montar_fontes.py a partir de fontes_candidatas.yaml)\n"
        + yaml.safe_dump(saida, allow_unicode=True, sort_keys=False, width=200), encoding="utf-8")
    print(f"fontes.yaml: {len(saida)} itens; copiados agora: {copiados}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
