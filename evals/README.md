# Evals do agente engenheiro-de-drenagem

Arquivos de avaliação:

- `evals/roteamento.yaml`: casos escritos à mão que verificam se o agente `engenheiro-de-drenagem` carrega as skills
  certas para cada pedido (roteamento) e se emite `[DELEGAR]`, modo CDV e rótulos de vigência quando devido. Incorpora os
  11 casos herdados do Hidráulico (`roteamento_drenagem.yaml`, apagado), com os nomes de skill corrigidos.
- `evals/casos_numericos.yaml`: liga os gabaritos do acervo (`casos/drenagem/*.md`) às calculadoras (`tools/dren/`) e
  aos testes (`tests/dren/`). Incorpora o caso herdado (`casos_numericos_drenagem.yaml`, apagado).
- `evals/sugestoes_casos_numericos_F4.md`: insumo da F4, já absorvido em `casos_numericos.yaml`.
- `evals/casos_reais.yaml` (quando existir): **gerado** dos pareceres por `Agent Builder/tools/registro.py --resumir`;
  não editar à mão; os casos de lá não se copiam para o `roteamento.yaml`.

Resultados de cada rodada vão em `evals/resultados/<AAAA-MM-DD>.md`.

## Formato do `roteamento.yaml`

| Campo | Conteúdo |
|---|---|
| `id` | identificador único (`prefixo-NN`) |
| `prompt` | pedido do usuário, em português |
| `esperado` | skills que DEVEM ser carregadas (lista vazia = nenhuma skill) |
| `nao_esperado` | skills cuja carga seria erro claro |
| `nota` | justificativa e marcas: `PAR`, `DELEGACAO`, `NAO-GATILHO`, `CDV`, `VIGENCIA` |

Prefixos de id: `fund-` (núcleo, pedidos amplos); por skill: `hid-` (hidrologia-de-projeto-para-drenagem), `bue-`
(bueiros-e-travessias), `est-` (drenagem-de-estradas-e-plataformas), `can-` (canais-de-drenagem-e-macrodrenagem), `dsub-`
(drenagem-subsuperficial), `nrm-` (drenagem-normas-e-manuais), `cas-` (drenagem-casos-de-referencia); por categoria
`par-` (skills vizinhas), `del-` (delegação), `nao-` (não-gatilho), `mis-` (pedido misto), `cdv-` (modo CDV), `vig-`
(vigência/edição). O prefixo indica o foco do caso; um caso `par-` ou `mis-` conta para cada skill de `esperado`.

Só valem as 8 skills do pacote (`.claude/skills/`): `drenagem-fundamentos` (núcleo), `hidrologia-de-projeto-para-drenagem`,
`bueiros-e-travessias`, `drenagem-de-estradas-e-plataformas`, `canais-de-drenagem-e-macrodrenagem`,
`drenagem-subsuperficial`, `drenagem-normas-e-manuais`, `drenagem-casos-de-referencia`. Skills do Hidráulico e do Clima
(`canais-abertos`, `chuvas-intensas-e-idf` etc.) não existem aqui e não entram em `esperado` nem em `nao_esperado`.

O núcleo `drenagem-fundamentos` é pré-carregado (campo `skills` do agente). Ele só é cobrado em `esperado` em pedido
amplo (conceito, fluxo de trabalho, dados mínimos, formato do parecer, triagem de cartão sem enunciado) e entra em
`nao_esperado` nos não-gatilhos, onde nenhuma skill é carregada. Skills complementares toleráveis (podem aparecer sem
reprovar) ficam fora de `esperado` e de `nao_esperado`; a `nota` diz quais são.

### Marcas da `nota`

- `PAR`: par de skills vizinhas em que o gatilho pode colidir (um caso em cada sentido). Pares cobertos: hidrologia x
  bueiros, bueiros x estradas, bueiros x canais, estradas x canais, canais x subsuperficial, estradas x subsuperficial,
  hidrologia x estradas, hidrologia x canais, normas x disciplina, casos x disciplina.
- `DELEGACAO`: o agente resolve até a fronteira e emite `[DELEGAR: <id-destino>]`; `esperado` traz a skill própria que
  ainda assim se aplica; a nota diz o bloco esperado, com o id da `MATRIZ_DE_INTERFACES.md` §1 (`clima`, `hidraulica`,
  `geotecnia`, `terraplenagem`, `pavimentacao`, `irrigacao`, `orcamento`; `estruturas` é destinatário que ainda não
  existe: o bloco vira pendência humana). "Tolerável" na nota = bloco que pode aparecer sem reprovar.
- `NAO-GATILHO`: pedido fora de escopo, `esperado: []`, e a nota diz para quem vai. Também cobre o que o perfil declara
  não coberto (drenagem urbana em rede) e consultoria (HEC-RAS 2D).
- `CDV`: modo CDV (cartão CT-xx, D-xx, P-xx). Os enunciados completos vêm do Gestor da Visão CDV e não estão no pacote:
  os prompts usam só o que o `PLANO.md` e as `PENDENCIAS_DE_TREINAMENTO.md` dizem de cada pendência (P-42, P-108, P-115,
  P-116, P-134, P-265 a P-268, P-272, D-56, D-85, D-86). P-108 e P-272 não têm tema registrado no pacote.
- `VIGENCIA`: edição, vigência ou licença (HDS-5 3ª ed. 2012; NBR 8890:2020, ES 018/021 e FAO-38 não abertos: citar,
  nunca transcrever; âmbito do DAEE; Pfafstetter só localizar).

## Como rodar

Estático (sem LLM): o YAML carrega, `id` único, `prompt` e `nota` não vazios, todo nome em `esperado` e `nao_esperado`
é uma pasta de `.claude/skills/`, cada skill de disciplina aparece em `esperado` em pelo menos 3 casos.

Roteamento (manual, um caso por conversa nova):

1. Abrir o projeto no Claude Code na RAIZ (a pasta com `PACOTE.yaml`).
2. Invocar `Use o agente engenheiro-de-drenagem: <prompt>`.
3. Anotar as skills carregadas (arquivos `SKILL.md` lidos, visíveis nas chamadas de ferramenta) e a delegação emitida.
4. Gravar num YAML `id -> {skills: [...], delegacao: [ids]}` e rodar o avaliador de roteamento
   (`python evals/avaliar_roteamento.py <respostas.yaml>`; modelo: `../Especialista Clima/evals/avaliar_roteamento.py`,
   que deve ser copiado para esta pasta, apontando para o `roteamento.yaml` daqui).

Juiz: **Haiku**, só para o que o script não decide (forma do bloco `[DELEGAR]`, formato CDV, rótulo de edição, "valor
inventado"). Quem rodou não é quem escreveu os casos. Entregar ao juiz: o `prompt`, o `esperado`, o `nao_esperado`, a
`nota` e a resposta completa do agente; pedir veredito S/N por item da lista abaixo e a frase da resposta que o sustenta.
O juiz não calcula engenharia e não decide D-xx.

Conferir por categoria:

- `DELEGACAO`: bloco `[DELEGAR: <id>]` completo (pedido, entrego, preciso de, premissa provisória, impacto se mudar,
  urgência) e do id da nota; o agente não chamou outro agente (`disallowedTools` bloqueia `Agent`) nem resolveu a parte alheia.
- `NAO-GATILHO`: nenhuma skill carregada, nenhum valor inventado, destino indicado.
- `CDV`: formato Situação / Preciso de você / Próximo passo / Detalhes; nenhuma D-xx decidida; dúvida vira P-nova com a
  hipótese; nada escrito fora da linha `escreve:` do cartão (só `pareceres/`, `memoria/` e `LICOES.md` do pacote).
- `VIGENCIA`: edição rotulada (HDS-5 3ª ed. 2012); norma não aberta citada como referência, sem transcrição.
- `PAR`: as duas skills do par, no sentido do caso (a nota diz quem ganha).
- Misto (`mis-`): skill própria carregada **e** bloco para a parte alheia.

## Critério de instalável (`PADRAO_DO_PACOTE.md` §8)

- roteamento >= 90 % dos casos com todas as skills de `esperado` carregadas e nenhuma de `nao_esperado`;
- 100 % dos `NAO-GATILHO` sem skill e sem valor inventado;
- 100 % das `DELEGACAO` com o bloco do id certo;
- 100 % dos `CDV` sem decisão de D-xx e sem escrita fora do cartão;
- 100 % dos `VIGENCIA` com a edição rotulada e sem transcrição de norma não aberta;
- calculadoras dentro da tolerância nos casos `reproduz`; os `divergencia_>5%` registrados em `tools/dren/DIVERGENCIAS.md`;
- zero respostas sem fonte numa amostra de 20.

Falha de roteamento se corrige na `description` da skill (gatilhos e não-gatilhos), não no corpo; repetir os casos `PAR`
das skills vizinhas. Esta redação não ajusta `description` nem o agente.

## Como registrar o resultado

`evals/resultados/<AAAA-MM-DD>.md`: (1) cabeçalho (data, modelo, versão do agente, quem rodou, modelo do juiz); (2) tabela
`id | skills carregadas | esperado ok | nao_esperado violado | aprovado (S/N) | observação`; (3) contagem por categoria
(skill, `PAR`, `DELEGACAO`, `NAO-GATILHO`, `CDV`, `VIGENCIA`) e percentual global; (4) veredito e casos reprovados com a
causa provável; (5) ajustes de `description` feitos e a nova rodada dos casos afetados.

## Casos numéricos (`casos_numericos.yaml`)

Campos: `id` (`num-NN`; `cdv-NN` para aceitação CDV), `caso` (gabarito em `casos/drenagem/*.md`, ou `livro`), `modulo` e
`funcao` (`tools/dren/`), `entradas`, `esperado` (valor do projetista ou do livro, com fonte `doc:pág`, nunca o da
calculadora), `tolerancia`, `status` e `nota` (teste real de `tests/dren/`, valor calculado e linha de
`tools/dren/DIVERGENCIAS.md`).

`status`:

- `reproduz`: a calculadora devolve o número do documento dentro da tolerância. Não significa que o documento esteja certo.
- `divergencia_>5%`: diferença acima de 5 %. Regra D11: não se ajusta a fórmula; o teste fica `xfail` (`strict=True` nos casos
  de Delmiro BHD1 e do tubo de dreno, para falhar se alguém ajustar sem registrar) e o caso vai para sessão interativa.
- `sem_gabarito`: há caso, mas sem número ancorado reproduzível, sem teste dedicado, ou o item é só consistência do próprio
  documento (Salitre, extensão total) ou pendência CDV sem enunciado no pacote.

**Nenhum caso de `casos/drenagem/` tem check-h (`✓h`).** Todos os números do acervo são candidatos (marcas `!`, `~`, `✓*`)
até a conferência humana da F7 (D17): "reproduz" só mede a calculadora contra o documento. Exceções: exemplos de livro
(`caso: livro`: HDS-5, HDS-3, ILRI-16, NEH 624, USBR), que são exemplos impressos e não gabarito de projeto. Lacuna
conhecida: o acervo não tem dreno agrícola calculado (Hooghoudt, Ernst, Glover-Dumm só têm gabarito de livro, num-36),
nem sarjeta e descida d'água com memória de cálculo.

Os casos `cdv-01` a `cdv-04` ligam as 13 pendências da aceitação F10 (D6) às calculadoras; todos `sem_gabarito`, porque
o enunciado vem do cartão e nenhum número do CDV é gabarito (só o André decide D-xx; nenhuma escrita no CDV).

Para conferir: `python -m pytest tests/dren -q` (os `xfail strict` falham se alguém ajustar a fórmula sem registrar).
