"""Baixa os materiais de referencia listados em tools/fontes.yaml.

Idempotente: arquivos ja baixados cujo sha256 confere com o catalogo nao sao
baixados de novo (use --forcar para rebaixar). Gera/atualiza
referencias/_catalogo.yaml.

Metodos suportados no manifesto:
    local            arquivo fornecido pelo usuario ja presente em referencias/ (sem download)
    http             download direto (pdf/7z/rar/zip), com verificacao de assinatura
    http_pagina_tcu  pagina do portal TCU (protegida por anti-robo -> manual_needed)
    tcu_acordao      API publica pesquisa.apps.tcu.gov.br -> PDF do inteiro teor
    tcu_sumula       API publica (base jurisprudencia-selecionada) -> .md com enunciado
    html_md          salva HTML bruto + conversao para Markdown

Uso:
    python tools/baixar_referencias.py [--ids PREFIXO ...] [--forcar]
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import re
import shutil
import subprocess
import sys
import time
import unicodedata
from pathlib import Path

import httpx
import yaml
from bs4 import BeautifulSoup
from markdownify import markdownify

RAIZ = Path(__file__).resolve().parents[1]
REF = RAIZ / "referencias"
MANIFESTO = RAIZ / "tools" / "fontes.yaml"
CATALOGO = REF / "_catalogo.yaml"
UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/128.0 Safari/537.36"
)
PAUSA = 1.5
TCU_API = "https://pesquisa.apps.tcu.gov.br/rest/publico/base"
ASSINATURAS = {
    "pdf": [b"%PDF"],
    "7z": [b"7z\xbc\xaf\x27\x1c"],
    "rar": [b"Rar!\x1a\x07"],
    "zip": [b"PK\x03\x04"],
}
ARQUIVOS_COMPACTADOS = {"7z", "rar", "zip"}
HOJE = dt.date.today().isoformat()


# ------------------------------------------------------------------ util
def slug(txt: str, n: int = 40) -> str:
    t = unicodedata.normalize("NFKD", txt).encode("ascii", "ignore").decode()
    t = re.sub(r"[^A-Za-z0-9]+", "-", t).strip("-").lower()
    return t[:n].strip("-") or "arquivo"


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for bloco in iter(lambda: f.read(1 << 20), b""):
            h.update(bloco)
    return h.hexdigest()


def paginas_pdf(p: Path) -> int | None:
    try:
        import pymupdf

        with pymupdf.open(p) as d:
            return d.page_count
    except Exception:  # noqa: BLE001 - PDF corrompido/protegido
        return None


def bsdtar() -> str:
    for c in ("bsdtar", r"C:\Windows\System32\tar.exe"):
        w = shutil.which(c)
        if w:
            return w
    raise RuntimeError("bsdtar nao encontrado (necessario para .7z/.rar)")


def rel(p: Path) -> str:
    return p.relative_to(REF).as_posix()


def log(msg: str) -> None:
    print(f"[{dt.datetime.now():%H:%M:%S}] {msg}", flush=True)


def detectar_formato(p: Path) -> str | None:
    with p.open("rb") as f:
        cab = f.read(1024)
    for fmt, sigs in ASSINATURAS.items():
        if any(cab.startswith(s) or (fmt == "pdf" and s in cab) for s in sigs):
            return fmt
    return None


def assinatura_ok(p: Path, ext: str) -> bool:
    if ext not in ASSINATURAS:
        return True
    with p.open("rb") as f:
        cab = f.read(1024)
    return any(s in cab for s in ASSINATURAS[ext])


# ------------------------------------------------------------------ rede
class Rede:
    def __init__(self) -> None:
        self.cli = httpx.Client(
            headers={"User-Agent": UA, "Accept": "text/html,application/pdf,*/*;q=0.8", "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8"},  # Accept explicito: CDNs (USACE) dao 403 sem ele
            cookies={"security": "true"},  # exigido pelo portal da CAIXA
            timeout=httpx.Timeout(180, connect=30),
            follow_redirects=True,
        )
        self._ultimo = 0.0

    def _pausa(self) -> None:
        falta = PAUSA - (time.monotonic() - self._ultimo)
        if falta > 0:
            time.sleep(falta)
        self._ultimo = time.monotonic()

    def get(self, url: str, **kw) -> httpx.Response:
        self._pausa()
        return self.cli.get(url, **kw)

    def baixar(self, url: str, destino: Path, tentativas: int = 3) -> tuple[Path, str]:
        """Baixa para <destino>.part (NAO substitui o destino); retorna (arquivo_temp, content-type).
        O chamador valida a assinatura e so entao faz tmp.replace(destino)."""
        destino.parent.mkdir(parents=True, exist_ok=True)
        tmp = destino.with_suffix(destino.suffix + ".part")
        erro: Exception | None = None
        for k in range(tentativas):
            try:
                self._pausa()
                with self.cli.stream("GET", url) as r:
                    r.raise_for_status()
                    with tmp.open("wb") as f:
                        for bloco in r.iter_bytes(1 << 16):
                            f.write(bloco)
                    ctype = r.headers.get("content-type", "")
                return tmp, ctype
            except Exception as ex:  # noqa: BLE001
                erro = ex
                time.sleep(3 * (k + 1))
        tmp.unlink(missing_ok=True)
        raise RuntimeError(f"falha apos {tentativas} tentativas: {erro}")


# ------------------------------------------------------------------ catalogo
def registro_base(it: dict) -> dict:
    campos = ("id", "titulo", "orgao", "fonte", "temas", "tipo", "vigencia", "edicao", "url", "landing", "familia", "data_portal", "ano", "prioridade", "licenca", "origem")
    r = {k: it[k] for k in campos if it.get(k) is not None}
    r.update(arquivo=None, sha256=None, bytes=None, paginas=None, data_download=None, status=None, obs=it.get("obs"))
    return r


def preencher_arquivo(r: dict, p: Path, antigo: dict | None) -> None:
    h = sha256(p)
    r["arquivo"] = rel(p)
    r["sha256"] = h
    r["bytes"] = p.stat().st_size
    r["paginas"] = paginas_pdf(p) if p.suffix.lower() == ".pdf" else None
    r["data_download"] = antigo["data_download"] if antigo and antigo.get("sha256") == h and antigo.get("data_download") else HOJE
    r["status"] = "ok"


def juntar_obs(*partes: str | None) -> str | None:
    t = " | ".join(p for p in partes if p)
    return t or None


# ------------------------------------------------------------------ extracao de compactados
def extrair(arq: Path, pai: dict, antigos: dict[str, dict], profundidade: int = 0) -> list[dict]:
    """Extrai arq para <pasta>/<id>/ com nomes ASCII; devolve registros-filho."""
    alvo = arq.parent / pai["id"]
    tmp = arq.parent / f"_tmp_{pai['id']}"
    shutil.rmtree(tmp, ignore_errors=True)
    tmp.mkdir(parents=True)
    if arq.suffix.lower() == ".7z":
        # bsdtar do Windows nao traz LZMA; py7zr cobre LZMA/LZMA2/BCJ.
        import py7zr

        try:
            with py7zr.SevenZipFile(arq, "r") as z:
                z.extractall(tmp)
        except Exception as ex:  # noqa: BLE001
            shutil.rmtree(tmp, ignore_errors=True)
            raise RuntimeError(f"py7zr falhou: {ex}") from ex
    else:
        proc = subprocess.run([bsdtar(), "-xf", str(arq), "-C", str(tmp)], capture_output=True, text=True)
        if proc.returncode != 0:
            shutil.rmtree(tmp, ignore_errors=True)
            raise RuntimeError(f"bsdtar falhou: {proc.stderr.strip()[:300]}")
    shutil.rmtree(alvo, ignore_errors=True)
    alvo.mkdir(parents=True)
    base = tmp.resolve()
    arquivos = sorted(
        p for p in tmp.rglob("*")
        if p.is_file() and not p.is_symlink() and p.resolve().is_relative_to(base)
        and "__MACOSX" not in p.parts and p.name.lower() not in ("thumbs.db", ".ds_store")
    )
    filhos: list[dict] = []
    for k, p in enumerate(arquivos, start=1):
        ext = re.sub(r"[^a-z0-9]", "", p.suffix.lower())[:5] or "bin"
        fid = f"{pai['id']}-{k:02d}"
        novo = alvo / f"{fid}_{slug(p.stem, 45)}.{ext}"
        shutil.move(str(p), novo)
        r = {
            "id": fid,
            "titulo": p.stem,
            "fonte": pai["fonte"],
            "temas": pai.get("temas"),
            "tipo": pai.get("tipo"),
            "edicao": pai.get("edicao"),
            "vigencia": pai.get("vigencia"),
            "url": pai.get("url"),
            "contido_em": pai["id"],
            "arquivo_original": p.relative_to(tmp).as_posix(),
        }
        r.update(arquivo=None, sha256=None, bytes=None, paginas=None, data_download=None, status=None, obs=None)
        preencher_arquivo(r, novo, antigos.get(fid))
        filhos.append(r)
        if ext in ARQUIVOS_COMPACTADOS and profundidade < 2:
            try:
                filhos += extrair(novo, r, antigos, profundidade + 1)
            except Exception as ex:  # noqa: BLE001
                r["obs"] = f"falha ao extrair compactado interno: {ex}"
    shutil.rmtree(tmp, ignore_errors=True)
    return filhos


def descendentes(regs: dict[str, dict], pai: str) -> list[dict]:
    out: list[dict] = []
    fila = [pai]
    while fila:
        atual = fila.pop()
        for v in regs.values():
            if v.get("contido_em") == atual:
                out.append(v)
                fila.append(v["id"])
    return out


def destino_de(it: dict) -> Path:
    """Caminho do arquivo do item, garantidamente dentro de referencias/."""
    p = REF / it["pasta"] / it["arquivo"]
    if not p.resolve().is_relative_to(REF.resolve()):
        raise ValueError(f"caminho fora de referencias/: {p}")
    return p


def reaproveitar(r: dict, destino: Path, antigo: dict | None, forcar: bool) -> bool:
    """Reusa arquivo existente cujo sha256 confere com o catalogo (idempotencia)."""
    if forcar or not destino.exists() or not antigo or antigo.get("sha256") != sha256(destino):
        return False
    preencher_arquivo(r, destino, antigo)
    for k in ("arquivo_html", "sha256_html", "url_arquivo"):
        if antigo.get(k):
            r[k] = antigo[k]
    return True


# ------------------------------------------------------------------ metodos
def m_http(rede: Rede, it: dict, r: dict, antigos: dict, forcar: bool) -> list[dict]:
    destino = destino_de(it)
    antigo = antigos.get(it["id"])
    if antigo and antigo.get("arquivo") and antigo.get("status") == "ok" and (REF / antigo["arquivo"]).exists():
        anterior = REF / antigo["arquivo"]
        if anterior.with_suffix("") == destino.with_suffix(""):
            destino = anterior  # mesma pasta/nome; extensao foi corrigida numa execucao anterior
        elif anterior.parent != destino.parent and not destino.with_suffix(anterior.suffix).exists():
            destino = destino.with_suffix(anterior.suffix)  # preserva extensao corrigida
            destino.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(anterior), destino)  # manifesto mudou a pasta (ex.: reclassificacao)
            velho_dir = anterior.parent / it["id"]
            if velho_dir.is_dir():
                shutil.rmtree(velho_dir)  # sera reextraido no novo local
                antigos = {k: v for k, v in antigos.items() if v.get("contido_em") != it["id"]}
    ext = destino.suffix.lower().lstrip(".")
    reaproveitado = (
        not forcar and destino.exists() and antigo and antigo.get("sha256") == sha256(destino)
    )
    if not reaproveitado:
        tmp, ctype = rede.baixar(it["url"], destino)
        real = detectar_formato(tmp)
        if real and real != ext and ext in ASSINATURAS:
            # o portal as vezes serve .zip com nome .rar: corrige a extensao
            destino, ext = destino.with_suffix("." + real), real
            it = {**it, "obs": juntar_obs(it.get("obs"), f"servidor entregou {real} (URL indica outra extensao)")}
        if not assinatura_ok(tmp, ext):
            tmp.unlink(missing_ok=True)
            bloqueio = "tcu.gov.br" in it["url"] or "text/html" in ctype
            r["status"] = "manual_needed" if bloqueio else "failed"
            r["obs"] = juntar_obs(it.get("obs"), f"servidor devolveu '{ctype}' em vez de {ext} (provavel pagina anti-robo/erro)")
            return []
        tmp.replace(destino)
    preencher_arquivo(r, destino, antigo)
    filhos: list[dict] = []
    if it.get("extrair") and ext in ARQUIVOS_COMPACTADOS:
        filhos_antigos = descendentes(antigos, it["id"])
        intactos = reaproveitado and filhos_antigos and all((REF / v["arquivo"]).exists() for v in filhos_antigos if v.get("arquivo"))
        if intactos:
            filhos = [dict(v) for v in filhos_antigos]
            for f in filhos:  # propaga metadados herdados do pai (ex.: mudanca de vigencia)
                for k in ("fonte", "temas", "tipo", "vigencia", "edicao", "url"):
                    if r.get(k) is not None:
                        f[k] = r[k]
        else:
            filhos = extrair(destino, r, antigos)
        r["obs"] = juntar_obs(it.get("obs"), f"compactado com {len(filhos)} arquivo(s) extraido(s) em {rel(destino.parent / it['id'])}/")
    return filhos


def m_pagina_tcu(rede: Rede, it: dict, r: dict, antigos: dict, forcar: bool) -> list[dict]:
    destino = destino_de(it)
    if destino.exists() and not forcar:
        preencher_arquivo(r, destino, antigos.get(it["id"]))
        return []
    resp = rede.get(it["url"])
    txt = resp.text
    pdfs = re.findall(r'href="([^"]+\.pdf)"', txt, re.I)
    if pdfs:
        url = httpx.URL(it["url"]).join(pdfs[0])
        tmp, _ = rede.baixar(str(url), destino)
        if assinatura_ok(tmp, "pdf"):
            tmp.replace(destino)
            preencher_arquivo(r, destino, antigos.get(it["id"]))
            r["url"] = str(url)
            return []
        tmp.unlink(missing_ok=True)
    r["status"] = "manual_needed"
    r["obs"] = juntar_obs(it.get("obs"), "baixar manualmente no navegador e salvar em " + rel(destino))
    return []


def _tcu_busca(rede: Rede, base: str, termo: str, qtd: int = 20, inicio: int = 0, ordenar: bool = True) -> dict:
    params = {"termo": termo, "quantidade": str(qtd), "inicio": str(inicio)}
    if ordenar:
        params["ordenacao"] = "DTRELEVANCIA desc"
    resp = rede.get(
        f"{TCU_API}/{base}/documento",
        params=params,
        headers={"Accept": "application/json"},
    )
    if "json" not in resp.headers.get("content-type", ""):
        raise RuntimeError(f"API TCU devolveu {resp.headers.get('content-type')} (bloqueio/rota inexistente)")
    return resp.json()


def _limpa(html: str | None) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html or "")).strip()


def m_tcu_acordao(rede: Rede, it: dict, r: dict, antigos: dict, forcar: bool) -> list[dict]:
    destino = destino_de(it)
    antigo = antigos.get(it["id"])
    d = _tcu_busca(rede, "acordao-completo", f"NUMACORDAO:{it['numero']} ANOACORDAO:{it['ano']}", 10)
    docs = [x for x in d.get("documentos", []) if "Plen" in (x.get("COLEGIADO") or "")]
    if not docs:
        r["status"] = "manual_needed"
        r["obs"] = juntar_obs(it.get("obs"), "acordao nao encontrado na API; pesquisar em https://pesquisa.apps.tcu.gov.br")
        return []
    x = docs[0]
    meta = f"sessao {x.get('DATASESSAO')}; relator {x.get('RELATOR')}; situacao {x.get('SITUACAO')}; sumario: {_limpa(x.get('SUMARIO'))[:600]}"
    if (x.get("SITUACAO") or "").upper() == "SIGILOSO":
        r["status"] = "manual_needed"
        r["obs"] = juntar_obs(it.get("obs"), "ACORDAO CLASSIFICADO COMO SIGILOSO NO TCU - inteiro teor indisponivel publicamente", meta)
        return []
    if not (destino.exists() and antigo and antigo.get("sha256") == sha256(destino) and not forcar):
        tmp, _ = rede.baixar(x["URLARQUIVOPDF"], destino)
        if not assinatura_ok(tmp, "pdf"):
            tmp.unlink(missing_ok=True)
            r["status"] = "manual_needed"
            r["obs"] = juntar_obs(it.get("obs"), "PDF do inteiro teor nao retornou PDF", meta)
            return []
        tmp.replace(destino)
    preencher_arquivo(r, destino, antigo)
    r["url_arquivo"] = x["URLARQUIVOPDF"]
    r["obs"] = juntar_obs(it.get("obs"), meta)
    return []


def m_tcu_sumula(rede: Rede, it: dict, r: dict, antigos: dict, forcar: bool) -> list[dict]:
    n = it["numero"]
    destino = destino_de(it)
    if reaproveitar(r, destino, antigos.get(it["id"]), forcar):
        return []
    padrao = re.compile(rf"S[UÚ]MULA\s+(?:TCU\s+)?(?:N[ºo.]*\s*)?{n}\b\s*[:\-–]", re.I)
    enunciado = None
    fonte_chave = None
    buscas = [(termo, ordenar) for termo in (f"SUMULA TCU {n}", f"SÚMULA TCU {n}") for ordenar in (False, True)]
    for termo, ordenar in buscas:
        d = _tcu_busca(rede, "jurisprudencia-selecionada", termo, 50, 0, ordenar)
        for doc in d.get("documentos", []):
            cands = [(doc.get("KEY"), doc.get("ENUNCIADO"))] + [
                (x.get("chave"), x.get("enunciado")) for x in doc.get("ENUNCIADOSRELACIONADOS") or []
            ]
            for chave, txt in cands:
                t = _limpa(txt)
                if padrao.match(t):
                    enunciado, fonte_chave = t, chave
                    break
            if enunciado:
                break
        if enunciado:
            break
    if not enunciado:
        r["status"] = "manual_needed"
        r["obs"] = juntar_obs(it.get("obs"), "enunciado nao localizado via API; consultar a URL no navegador")
        return []
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(
        f"# Sumula TCU {n}\n\n"
        f"- Fonte: API publica de pesquisa do TCU (base jurisprudencia-selecionada, chave {fonte_chave})\n"
        f"- Pagina oficial: {it['url']}\n\n"
        f"## Enunciado\n\n{enunciado}\n",
        encoding="utf-8",
    )
    preencher_arquivo(r, destino, antigos.get(it["id"]))
    return []


def charset_html(resp: httpx.Response) -> str:
    """Charset do cabecalho HTTP ou da meta tag; o Planalto declara windows-1252
    e a deteccao automatica do bs4 as vezes escolhe ISO-8859-2 (corrompe acentos)."""
    if resp.charset_encoding:
        return resp.charset_encoding
    m = re.search(rb"charset=[\"']?([A-Za-z0-9_-]+)", resp.content[:4096], re.I)
    if m:
        enc = m.group(1).decode().lower()
        return "windows-1252" if enc in ("iso-8859-1", "latin-1", "latin1") else enc
    try:
        resp.content.decode("utf-8")
        return "utf-8"
    except UnicodeDecodeError:
        return "windows-1252"


def m_html_md(rede: Rede, it: dict, r: dict, antigos: dict, forcar: bool) -> list[dict]:
    destino = destino_de(it)
    bruto = destino.with_suffix(".html")
    if reaproveitar(r, destino, antigos.get(it["id"]), forcar):
        return []
    resp = rede.get(it["url"])
    resp.raise_for_status()
    sopa = BeautifulSoup(resp.content, "lxml", from_encoding=charset_html(resp))
    texto = sopa.get_text(" ", strip=True)
    if "enable JavaScript" in texto or "testing whether you are a human" in texto or len(texto) < 200:
        r["status"] = "manual_needed"
        r["obs"] = juntar_obs(it.get("obs"), "pagina protegida por anti-robo/JavaScript; salvar manualmente")
        return []
    bruto.parent.mkdir(parents=True, exist_ok=True)
    bruto.write_bytes(resp.content)
    for tag in sopa(["script", "style", "noscript", "iframe", "svg"]):  # <form> preservado: ha paginas (DER-SP) com o conteudo dentro dele
        tag.decompose()
    corpo = sopa.find(id="content") or sopa.find("main") or sopa.find("article") or sopa.body or sopa
    if "planalto.gov.br" not in it["url"]:
        for tag in corpo.find_all(["nav", "header", "footer", "aside"]):
            tag.decompose()
    md = markdownify(str(corpo), heading_style="ATX", strip=["img"])
    md = re.sub(r"\n{3,}", "\n\n", md).strip()
    destino.write_text(
        f"<!-- fonte: {it['url']} | convertido de HTML por tools/baixar_referencias.py (data em _catalogo.yaml) -->\n\n{md}\n",
        encoding="utf-8",
    )
    preencher_arquivo(r, destino, antigos.get(it["id"]))
    r["arquivo_html"] = rel(bruto)
    r["sha256_html"] = sha256(bruto)
    return []


def m_local(rede: Rede, it: dict, r: dict, antigos: dict, forcar: bool) -> list[dict]:
    """Arquivo fornecido pelo usuario, ja copiado em referencias/<pasta>/<arquivo>: nao baixa nada.
    Presente -> sha256 + paginas + status ok (ou o status pedido em 'status_local', ex.: pendente_ocr);
    ausente -> manual_needed."""
    destino = destino_de(it)
    if not destino.exists():
        r["status"] = "manual_needed"
        r["obs"] = juntar_obs(it.get("obs"), "arquivo local nao encontrado em " + rel(destino))
        return []
    preencher_arquivo(r, destino, antigos.get(it["id"]))
    r["url"] = r.get("url") or None
    esperado = it.get("sha256")
    if esperado and esperado != r["sha256"]:
        r["obs"] = juntar_obs(it.get("obs"), f"ATENCAO: sha256 difere do informado no manifesto ({esperado})")
    else:
        r["obs"] = it.get("obs")
    if it.get("status_local"):
        r["status"] = it["status_local"]
    return []


METODOS = {
    "local": m_local,
    "http": m_http,
    "http_pagina_tcu": m_pagina_tcu,
    "tcu_acordao": m_tcu_acordao,
    "tcu_sumula": m_tcu_sumula,
    "html_md": m_html_md,
}


# ------------------------------------------------------------------ duplicatas
def marcar_duplicatas(regs: list[dict]) -> None:
    visto: dict[str, str] = {}
    for r in sorted(regs, key=lambda x: x["id"]):
        r.pop("duplicata_de", None)
        h = r.get("sha256")
        if not h or r.get("status") != "ok":
            continue
        if h in visto:
            r["duplicata_de"] = visto[h]
        else:
            visto[h] = r["id"]


def gravar(regs: list[dict]) -> None:
    marcar_duplicatas(regs)
    regs.sort(key=lambda x: x["id"])
    cab = {
        "gerado_em": dt.datetime.now().isoformat(timespec="seconds"),
        "gerado_por": "tools/baixar_referencias.py",
        "total": len(regs),
        "por_status": {s: sum(1 for r in regs if r.get("status") == s) for s in ("ok", "failed", "manual_needed", "link_only", "pendente_ocr")},
    }
    CATALOGO.parent.mkdir(parents=True, exist_ok=True)
    CATALOGO.write_text(
        "# Catalogo do corpus de referencias -- gerado automaticamente; nao editar a mao.\n"
        + yaml.safe_dump({"metadados": cab, "documentos": regs}, allow_unicode=True, sort_keys=False, width=200),
        encoding="utf-8",
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ids", nargs="*", help="prefixos de id a processar (padrao: todos)")
    ap.add_argument("--forcar", action="store_true", help="rebaixa mesmo se o sha256 conferir")
    a = ap.parse_args()

    itens = yaml.safe_load(MANIFESTO.read_text(encoding="utf-8"))
    antigos: dict[str, dict] = {}
    if CATALOGO.exists():
        for r in (yaml.safe_load(CATALOGO.read_text(encoding="utf-8")) or {}).get("documentos", []):
            antigos[r["id"]] = r
    novos: dict[str, dict] = dict(antigos)
    ids_manifesto = {it["id"] for it in itens}
    # remove registros cujo pai/entrada saiu do manifesto
    for k in list(novos):
        if k not in novos:  # ja removido como descendente de outra entrada
            continue
        if not novos[k].get("contido_em") and k not in ids_manifesto:
            for d in descendentes(novos, k):
                novos.pop(d["id"], None)
            novos.pop(k)

    rede = Rede()
    alvo = [it for it in itens if not a.ids or any(it["id"].startswith(p) for p in a.ids)]
    for n, it in enumerate(alvo, start=1):
        r = registro_base(it)
        forcado = it.get("status")
        try:
            if forcado in ("link_only", "manual_needed"):
                r["status"] = forcado
                filhos: list[dict] = []
            else:
                filhos = METODOS[it.get("metodo", "http")](rede, it, r, antigos, a.forcar)
        except Exception as ex:  # noqa: BLE001
            r["status"] = "failed"
            r["obs"] = juntar_obs(it.get("obs"), f"erro: {ex}"[:500])
            filhos = []
        ant = antigos.get(it["id"])
        if (r["status"] != "ok" and not forcado and ant and ant.get("status") == "ok" and ant.get("arquivo")
                and (REF / ant["arquivo"]).exists() and sha256(REF / ant["arquivo"]) == ant.get("sha256")):
            # falha transitoria/anti-robo: mantem a copia boa anterior e seus filhos
            motivo = (r.get("obs") or r["status"])[:200]
            base_obs = re.sub(r"\s*\|?\s*ATUALIZACAO FALHOU.*$", "", ant.get("obs") or "")
            r = dict(ant)
            r["obs"] = juntar_obs(base_obs or None, f"ATUALIZACAO FALHOU em {HOJE} ({motivo}); mantida a copia anterior")
            filhos = [dict(v) for v in descendentes(antigos, it["id"])]
        # substitui filhos antigos deste item
        for d in descendentes(novos, it["id"]):
            novos.pop(d["id"], None)
        novos[it["id"]] = r
        for f in filhos:
            novos[f["id"]] = f
        log(f"{n}/{len(alvo)} {it['id']}: {r['status']}" + (f" (+{len(filhos)} extraidos)" if filhos else "")
            + (f" -- {r['obs'][:160]}" if r["status"] != "ok" and r.get("obs") else ""))
        if n % 10 == 0:
            gravar(list(novos.values()))
    gravar(list(novos.values()))
    log(f"catalogo: {CATALOGO}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
