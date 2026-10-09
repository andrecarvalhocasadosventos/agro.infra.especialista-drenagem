"""Avalia o roteamento do engenheiro-de-drenagem.

Uso (da raiz do pacote):
    python evals/avaliar_roteamento.py evals/resultados/respostas_AAAA-MM-DD.yaml

O arquivo de respostas mapeia id -> skills observadas e delegacao observada:

    fon-01:
      skills: [fontes-de-dados-climaticos]
      delegacao: null
    del-02:
      skills: [evapotranspiracao-e-evaporacao]
      delegacao: irrigacao

Regras de acerto por caso:
  - todas as skills de `esperado` foram carregadas;
  - nenhuma skill de `nao_esperado` foi carregada;
  - a delegacao observada e igual a esperada (null = nenhuma [DELEGAR] emitida).
O nucleo drenagem-fundamentos e pre-carregado e e ignorado nas observadas, salvo se estiver em `esperado`.
Casos sem resposta contam como erro. Sai com codigo 1 se o total ficar abaixo do criterio (90 %).
"""
import sys
from collections import defaultdict
from pathlib import Path

import yaml

NUCLEO = "drenagem-fundamentos"
CRITERIO = 0.90
DELEGACOES = {"clima", "hidraulica", "geotecnia", "terraplenagem", "pavimentacao", "irrigacao", "orcamento", "estruturas"}
import re


def _deleg_esperada(caso):
    """Conjunto de ids [DELEGAR: id] citados na nota (adaptado ao formato do Drenagem)."""
    if caso.get("delegacao") is not None:
        d = caso["delegacao"]
        return set(d if isinstance(d, list) else [d])
    return set(re.findall(r"\[DELEGAR:\s*([a-z]+)\]", caso.get("nota") or "")) & DELEGACOES


def _deleg_obs(resp):
    d = (resp or {}).get("delegacao")
    if d is None:
        return set()
    return set(d if isinstance(d, list) else [d])


def avaliar(caso, resp):
    obs = set((resp or {}).get("skills") or [])
    esp = set(caso.get("esperado") or [])
    if NUCLEO not in esp:
        obs.discard(NUCLEO)
    nao = set(caso.get("nao_esperado") or [])
    d_esp = _deleg_esperada(caso)
    d_obs = _deleg_obs(resp)
    falhas = []
    if esp - obs:
        falhas.append("faltou skill: " + ", ".join(sorted(esp - obs)))
    if nao & obs:
        falhas.append("skill indevida: " + ", ".join(sorted(nao & obs)))
    if d_esp != d_obs:
        falhas.append(f"delegacao esperada={sorted(d_esp)} observada={sorted(d_obs)}")
    return falhas


def main():
    raiz = Path(__file__).resolve().parent
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    casos = yaml.safe_load((raiz / "roteamento.yaml").read_text(encoding="utf-8"))
    respostas = yaml.safe_load(Path(sys.argv[1]).read_text(encoding="utf-8")) or {}
    ids = [c["id"] for c in casos]
    if len(ids) != len(set(ids)):
        print("ERRO: ids duplicados em roteamento.yaml")
        return 2
    for c in casos:
        d = c.get("delegacao")
        if d is not None and not set(d if isinstance(d, list) else [d]) <= DELEGACOES:
            print(f"ERRO: {c['id']} com delegacao invalida: {d}")
            return 2

    por_tema = defaultdict(lambda: [0, 0])
    reprovados = []
    for c in casos:
        tema = c["id"].split("-")[0]
        resp = respostas.get(c["id"])
        falhas = ["sem resposta"] if resp is None else avaliar(c, resp)
        por_tema[tema][1] += 1
        if not falhas:
            por_tema[tema][0] += 1
        else:
            reprovados.append((c["id"], falhas))

    print(f"{'tema':<6}{'acertos':>8}{'casos':>7}{'%':>7}")
    ok = tot = 0
    for tema in sorted(por_tema):
        a, n = por_tema[tema]
        ok += a
        tot += n
        print(f"{tema:<6}{a:>8}{n:>7}{100 * a / n:>7.1f}")
    pct = ok / tot if tot else 0.0
    print(f"{'total':<6}{ok:>8}{tot:>7}{100 * pct:>7.1f}")
    for i, f in reprovados:
        print(f"REPROVADO {i}: " + "; ".join(f))
    extras = sorted(set(respostas) - set(ids))
    if extras:
        print("Aviso: respostas sem caso correspondente: " + ", ".join(extras))
    print("Criterio D15 (>= 90 %): " + ("APROVADO" if pct >= CRITERIO else "NAO APROVADO"))
    return 0 if pct >= CRITERIO else 1


if __name__ == "__main__":
    sys.exit(main())
