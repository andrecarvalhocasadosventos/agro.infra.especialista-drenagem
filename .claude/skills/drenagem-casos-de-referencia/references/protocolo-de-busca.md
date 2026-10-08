# Protocolo de busca no acervo e no corpus (drenagem)

Somente leitura. Scripts em `../../03. Infraestrutura/Projetos de Referência/_BIBLIOTECA_TECNICA/02_PIPELINE/`
(relativo à raiz do pacote). Working set do acervo: `C:\bibtec`.

## 0. Antes de tudo

```
$env:PYTHONIOENCODING="utf-8"; $env:ACERVO_RAIZ="C:\bibtec"
python verificar_acervo.py        # deve terminar em OK; catálogo degradado: dizer ao usuário antes de responder
```

## 1. Ordem (parar no primeiro passo que responde)

| Passo | Comando | Para quê |
|---|---|---|
| 1 | ler `casos/drenagem/_INDICE.md` e o caso | o projeto já foi lido? |
| 2 | `MAPA.md` do acervo | quais documentos existem sobre drenagem |
| 3 | `python consultar.py buscar "<termos>" --disciplina HID --limite 20` | achar documento e página |
| 4 | `python consultar.py buscar "<termos>" --doc <n>` | a página dentro do volume |
| 5 | `python consultar.py doc <n>` | ficha: rota (texto, imagem), extração, tamanho |
| 6 | `python consultar.py parametros --doc <n> --so-ancorados` | número já extraído, com marca |
| 7 | `python consultar.py ler <n> --pagina <p>` | página literal (teto: 8 por chamada) |

FTS5: espaço = AND, `OR`, `"frase"`, `prefixo*`; acento indiferente. Termos úteis de drenagem: `bueiro`, `celular`,
`BSTC`, `BTCC`, `tempo de concentracao`, `racional`, `hidrograma unitario`, `Kirpich`, `curva numero`, `valeta`,
`dreno de fundo`, `Manning`, `folga`, `deságue`. Filtros: `--projeto`, `--tipo memoria_calculo`.

## 2. Armadilhas da busca

- **Ausência não é ausência**: tentar sinônimo, radical com `*`, sem filtro. Rota `imagem` (321 documentos) não é
  alcançável por texto: dizer "página em imagem, não lida".
- **Duplicatas**: Delmiro 1520 = 1492 e 1521 = 1493; SRHCE-EI-* do corpus do Hidráulico = documentos do acervo. Uma
  fonte, não duas confirmações.
- **Tabela extraída**: coluna deslocada é comum (Xingó Quadro 3.39, 40 colunas do Iuiu). Para tabela, `ler` a página e
  não confiar em `parametros`.
- **Planilha/docx**: o "número de página" é bloco de texto (12.000 caracteres), não página do PDF.
- **Estudo citado e ausente**: HARZA 2001 (CAC), Vol. 3 do Iuiu 2018. Dizer que não está no acervo.

## 3. Marcas de ancoragem

`✓` ancorado na camada de texto; `✓*` ancorado com candidato alternativo (dar os dois e a nota); `~` aproximado; `!`
diverge entre campos (dar o campo); `·` lido por `ler` sem linha em `parametros`; `✓h` conferido por pessoa; `✗h`
rejeitado por pessoa. Tabela oficial: skill `consultar-acervo`. **Nenhum caso de drenagem tem `✓h`**: número `✓`,
`✓*`, `~`, `!` ou `·` vai ao usuário como "valor do projeto, não conferido" e nunca entra em teste como gabarito sem
conferência. Para promover: `python 89_app_revisao.py --ids parametro:<id>` (conferência pontual) e esperar o
veredito do André.

## 4. Corpus (livros e manuais)

Para "o que o manual diz" (não para "o que o projeto fez"): `drenagem-fundamentos` §7. Corpus próprio
`referencias/MAPA_DE_CONHECIMENTO.md` (G1 a G4) → `_catalogo.yaml` → `_texto/<ID>.md` (marcador `<!-- p. N -->`);
corpus do Hidráulico por caminho (D1), citando pelos IDs dele; índice FTS5 em `C:\bibdren\db\corpus.sqlite` e
`C:\bibhid`. PDF original só para figura, ábaco ou fórmula ilegível.

## 5. Como citar

`Nome do documento.pdf:176` ou `1131:65` com a marca; `[ID p. N]` no corpus; `tools/dren/<módulo>.<função>` com as
entradas. Nunca "o acervo diz" sem página. Valor lido na página sem linha no catálogo é dito assim.
