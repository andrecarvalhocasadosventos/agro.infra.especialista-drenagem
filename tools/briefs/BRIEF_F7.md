# Brief F7 — revisão técnica das skills (Opus, por amostra) — 2026-10-08

RAIZ = `08. AI Squad/Especialista Drenagem`. Processo: `../Agent Builder/PROCESSO_DE_TREINAMENTO.md` (F7) e
`../Agent Builder/POLITICA_DE_MODELOS.md` §4. Você é revisor técnico, não autor.

Para cada skill do seu lote (`.claude/skills/<skill>/SKILL.md` + references):
1. Amostre **≥ 8 afirmações numéricas** (fórmula, coeficiente, limite, tabela) e confira no primário
   (`referencias/_texto/` do corpus próprio ou `../Especialista Hidraulica/referencias/_texto/`; PDF renderizado
   quando o texto perdeu símbolo). Confira também que cada função citada existe em `tools/dren/` com aquele nome e
   assinatura, e que os testes citados existem em `tests/dren/`.
2. Confira fronteiras (delegação certa pela `../Agent Builder/MATRIZ_DE_INTERFACES.md`; D3, D5), colisão de
   description com skills vizinhas (do pacote e do Hidráulico/Clima), e a regra "apontar divergência, não corrigir o
   projeto".
3. Corrija **na skill** erro comprovado (com a página). Erro de calculadora: não corrija; registre em
   `tools/dren/DIVERGENCIAS.md`, seção `## Revisão técnica F7 (Opus)`, e diga na resposta.
4. Acrescente ao fim do SKILL.md a seção `## Revisão técnica` (data, revisor Opus, nº de itens amostrados,
   conferidos/corrigidos/pendentes, pendências para o André). Não estoure 25 KB: se precisar, mova tabela para
   `references/`.
5. Não decida D-n. Pontos de escolha entre fontes ou critério normativo: liste como **decisão do André** com
   alternativas (fonte e página), efeito numérico e sua recomendação.

Insumos de decisões já levantadas: `tools/dren/DIVERGENCIAS.md` (tabela de decisões da revisão F5) e o
`PLANO.md` §Decisões (pontos não decididos). Sem git. Resposta ≤ 25 linhas: por skill, amostrados/conferidos/
corrigidos; erros de calculadora achados; lista consolidada de decisões do André (sem repetir as já listadas na
revisão F5, só citar o número delas se você tiver dado novo).
