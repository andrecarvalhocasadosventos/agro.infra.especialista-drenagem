"""Infraestrutura comum de CLI dos modulos tools.hid (apenas stdlib).

Uso:
    python -m tools.hid.perdas --json '{"funcao": "hf_darcy", "Q": 0.1, "L": 500, "D": 0.3, "eps": 1e-4}'
    python -m tools.hid.perdas --funcao hf_darcy --Q 0.1 --L 500 --D 0.3 --eps 1e-4

Saida (stdout, JSON UTF-8): entradas, saidas, metodo, avisos, versao.
"""
import argparse
import inspect
import json
import sys


def _converter(v):
    """Converte texto de argumento nomeado em numero/JSON quando possivel."""
    try:
        return json.loads(v)
    except (ValueError, TypeError):
        return v


def _serializavel(x):
    if isinstance(x, dict):
        return {str(k): _serializavel(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [_serializavel(v) for v in x]
    if hasattr(x, "descricao"):
        return x.descricao()
    if isinstance(x, float):
        return x
    return x


def executar(modulo_nome, versao, funcoes, argv=None):
    """Executa a CLI de um modulo. `funcoes` mapeia nome -> callable."""
    ap = argparse.ArgumentParser(prog="python -m " + modulo_nome,
                                 description="Calculadora hidraulica verificavel.")
    ap.add_argument("--json", help="entradas em JSON: {'funcao': nome, ...argumentos}")
    ap.add_argument("--funcao", help="nome da funcao")
    ap.add_argument("--listar", action="store_true", help="lista as funcoes")
    args, resto = ap.parse_known_args(argv)
    if args.listar:
        print(json.dumps({"funcoes": sorted(funcoes), "versao": versao}, ensure_ascii=False))
        return 0
    entradas = {}
    if args.json:
        entradas.update(json.loads(args.json))
    i = 0
    while i < len(resto):
        t = resto[i]
        if t.startswith("--") and i + 1 < len(resto):
            entradas[t[2:]] = _converter(resto[i + 1])
            i += 2
        else:
            ap.error("argumento nao reconhecido: " + t)
    nome = args.funcao or entradas.pop("funcao", None)
    entradas.pop("funcao", None)
    if nome not in funcoes:
        print(json.dumps({"erro": "funcao desconhecida: %r" % nome,
                          "funcoes": sorted(funcoes), "versao": versao},
                         ensure_ascii=False))
        return 2
    fn = funcoes[nome]
    avisos = []
    try:
        res = fn(**entradas)
    except (TypeError, ValueError) as e:
        print(json.dumps({"erro": str(e), "assinatura": nome + str(inspect.signature(fn)),
                          "versao": versao}, ensure_ascii=False))
        return 2
    if isinstance(res, dict):
        res = dict(res)
        avisos = list(res.pop("avisos", []))
        metodo = res.pop("metodo", None)
        saidas = res
    else:
        saidas = {"valor": res}
        metodo = None
    doc = (fn.__doc__ or "").strip().splitlines()
    saida = {
        "entradas": dict(entradas, funcao=nome),
        "saidas": _serializavel(saidas),
        "metodo": metodo or (doc[0] if doc else nome),
        "avisos": avisos,
        "versao": versao,
    }
    print(json.dumps(saida, ensure_ascii=False, indent=2))
    return 0


def principal(modulo_nome, versao, funcoes):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(executar(modulo_nome, versao, funcoes))
