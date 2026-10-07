# Lições aprendidas do Especialista em Drenagem

Caixa de entrada curada e versionada, na RAIZ do pacote (vale para toda instalação, Modo A ou B). Lição não mora
aqui para sempre: é **incorporada na skill** na avaliação periódica (`PLANO.md` §10) e sai da busca. Entradas não
substituem o corpus, as calculadoras nem as regras V1-V12: são calibragens de uso (correções do usuário,
armadilhas encontradas, critérios que valem reaproveitar).

## Como o agente usa este arquivo (sem ler inteiro)

- **Consulta:** Grep só das linhas `ativa` da skill carregada (ou `*`, que vale para todas), nunca Read do arquivo:
  `^\| L-\d{3} \|[^|]*\|[^|]*(<skill>|\*)[^|]*\| ativa \|`. Roteamentos: `^\| R-\d{3} \|.*\| ativa \|`.
- **Proposta:** ao fim de trabalho material, se houve correção do usuário, armadilha nova ou critério
  reaproveitável, propor a linha exata e gravar (Edit, no fim da tabela) só depois do "sim". Sem "sim", não grava.
  Não editar nem apagar linha existente sem confirmação.

## Regras de escrita

- **Uma linha por lição**, IDs sequenciais `L-001`, `L-002`... (nunca reaproveitar). Barra vertical dentro do texto
  vai escapada (`\|`).
- **Skills:** nomes exatos das skills afetadas, separados por vírgula; `*` só para o que vale em qualquer
  disciplina (forma do parecer, unidades). É esta coluna que decide quem enxerga a lição.
- **Status:** `ativa`, `revisar` (conflita com fonte nova ou com a calculadora), `obsoleta` (descartada) ou
  `incorporada` (já está na skill; coluna **Incorporada em** = `skill@commit`, ex.: `canais-abertos@b8e60f8`).
- **Base:** `[ID p. N]` do corpus, `doc:pág` do acervo com a marca de ancoragem, ou `sem base no corpus` (nunca
  citada como fonte). **Origem:** pasta do parecer, `conversa` ou `correção do usuário`.
- Lição que contradiz o corpus ou V1-V12 não entra; o corpus prevalece e o conflito vira `revisar`.
- Não registrar coeficiente, constante de ábaco, rugosidade, celeridade, número de página como fato nem número de
  projeto do acervo: isso vem do corpus, da calculadora ou do acervo. Só método, critério e armadilha.
- Não é lição: divergência calculadora × acervo acima de 5% -> `tools/hid/DIVERGENCIAS.md` (D11); erro numa skill
  ou calculadora -> pendência em `PLANO.md` (o agente não altera skills nem `tools/hid/`); decisão D-xx do CDV ->
  fica no CDV (aqui, no máximo, o método transferível, sem números).
- Não duplicar: antes de propor, Grep pelo tema e propor a atualização da linha existente.

## Lições

| ID | Data | Skills | Status | Lição | Base | Origem | Incorporada em |
|---|---|---|---|---|---|---|---|

## Roteamentos aprovados (D13)

Tipos de `[DELEGAR]` que o Gestor aprovou. Depois de aprovado, o mesmo tipo de pedido é roteado sem esperar nova
aprovação (o bloco continua sendo emitido). Mesma regra de gravação: só com o "sim". Roteamento não é incorporado
em skill; sai só por `obsoleta`.

| ID | Data | Destino | Status | Pedido-tipo | Aprovado por |
|---|---|---|---|---|---|
