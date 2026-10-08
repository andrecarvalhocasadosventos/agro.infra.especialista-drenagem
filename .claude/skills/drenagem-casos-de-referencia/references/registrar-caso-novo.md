# Registrar um caso novo de drenagem

Escreve **só neste pacote** (`casos/drenagem/`, `tests/dren/`, `tools/dren/DIVERGENCIAS.md`). Caso de canal de adução,
sifão ou adutora vai ao Hidráulico. Pedir ao André antes de gravar (lição e caso são decisões do usuário).

## 1. O caso (`casos/drenagem/<AAAA-MM-DD>_<slug>.md`)

```
# <Projeto> — <tema> (caso NEGATIVO | positivo)
fonte: <documento> (doc <n>) pp. <a>-<b>
disciplinas: [<skill da disciplina>]
nivel: anteprojeto | basico | executivo
tipo: positivo | NEGATIVO (<o que é>)
qualidade: A | B | C (<por quê>)
marcas: `·` lido por `ler`; ... Nenhum `✓h`.

## Problema
## Dados de entrada        (tabela: grandeza | valor | unidade | fonte doc:pág | marca)
## Método do projetista    (ou "não informado")
## Resultado
## Gabarito para a calculadora   (candidato; "nenhum número promovido; ✓h pendente")
## Rastro                  (A: lido; B: recálculo meu; C: hipótese)
## Divergências
## Fronteira               (delegar: clima, hidraulica, ...)
```

Regras: cada número com `doc:pág` e marca; inferência rotulada (B ou C); caso negativo inclui **o teste que revela o
erro** e o número esperado; conferências aritméticas citam as entradas. Se o doc é duplicata (1520 = 1492), citar os dois.

## 2. O índice

Linha em `casos/drenagem/_INDICE.md`: `slug | projeto (doc) | o que resolve | qualidade | tipo`. Sem `✓h`, o cabeçalho do
índice continua valendo.

## 3. O teste (`tests/dren/test_<módulo>.py`)

- Reproduz dentro de 5 % (acervo) ou 1 % (livro): teste normal, rotulado "acervo, sem check-h" no docstring.
- Diverge > 5 %: `@pytest.mark.xfail(strict=True, reason="DIVERGENCIAS.md: ...")` e linha em
  `tools/dren/DIVERGENCIAS.md` (caso, valor do projeto, valor calculado, teste, hipótese). Não ajustar fórmula.
- Faltam entradas: não escrever teste numérico; registrar no caso como "sem gabarito" e propor o eval.
- Padrão provisório envolvido (TR, Ke, tc_min, y/D 75 %, folga 25 %): o teste declara o argumento; rótulo
  "padrão provisório, decisão F7".

## 4. Depois

1. `python -m pytest tests/dren -q` (os xfail contam como esperados).
2. Número que o parecer vai usar: conferência pontual (`89_app_revisao.py --ids ...`) e espera do `✓h`.
3. Lição reaproveitável: propor a linha de `LICOES.md` (texto exato, coluna `Skills`) e gravar só depois do "sim".
4. Se o caso mudar o mapa: atualizar a tabela de `drenagem-casos-de-referencia` (pedido ao responsável pela skill).
