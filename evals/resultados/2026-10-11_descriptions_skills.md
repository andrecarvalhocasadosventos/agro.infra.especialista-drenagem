# Roteamento após encurtar descriptions de skills (2026-10-11, servidor; defeito M3 do Bloco 1)

- Mudança: só a `description` do frontmatter de 2 das 9 skills (as outras já tinham <= 1.024); o carregamento cortava o texto em 1.024 caracteres e o fim do "Não use para" se perdia. Corpos intactos; todas as fronteiras mantidas (conferido por script). `hidrologia-de-projeto-para-drenagem`: menos métodos de Tc listados e uma fronteira nova, "vigência de fonte e da IDF de Pfafstetter (drenagem-normas-e-manuais)". `drenagem-normas-e-manuais`: lista de fontes enxugada e gatilho novo "a IDF de Pfafstetter ainda vale?".

| skill | antes | depois |
|---|---|---|
| drenagem-normas-e-manuais | 1.065 | 1.018 |
| hidrologia-de-projeto-para-drenagem | 1.034 | 1.021 |

- Método: juízes Haiku (subagentes `general-purpose`) lendo só o perfil do agente, as descriptions das 9 skills e os prompts (sem `evals/`), 4 por rodada (blocos de 24), nos 95 casos; avaliador `avaliar_roteamento.py` (função `avaliar`, com delegação obrigatória ⊆ observada ⊆ obrigatória ∪ tolerável; `climatologia` lido como `clima`). A versão "antes" foi apresentada como o carregamento a entrega (cortada em 1.024 caracteres).

| rodada | juiz | acerto |
|---|---|---|
| última registrada (2026-10-09 v3; 2026-10-10 HEC-RAS 8/8) | Sonnet | 86/88 = 97,7 % |
| 2026-10-11 antes (cortada em 1.024) | Haiku | 80/95 = 84,2 % |
| 2026-10-11 depois, 1ª versão | Haiku | 80/95 = 84,2 % |
| 2026-10-11 depois, 2ª versão | Haiku | 82/95 = 86,3 % |

- O juiz Haiku é mais severo que o Sonnet da rodada de 2026-10-09 neste pacote: a maior parte das reprovações, iguais antes e depois, é delegação a mais (`[DELEGAR: hidraulica]`/`clima`/`geotecnia` não previstos: hid-02, bue-02, bue-06, del-04, del-05, hr-01) e bueiros-e-travessias em nao-07/nao-08, em skills e regras que esta mudança não tocou. Por isso a comparação vale entre as rodadas de hoje, com o mesmo juiz: não houve queda.
- Caso que piorou e foi ajustado: vig-04 ("a IDF de Pfafstetter ainda vale?", nao_esperado hidrologia) carregou hidrologia-de-projeto-para-drenagem nas duas primeiras versões. Ajustes acima (gatilho em normas, fronteira em hidrologia). Repetição x3 dos 8 casos sensíveis (vig-04, cdv-04, cdv-08, nao-10, dsub-02, par-06, par-11, del-08): antes 17/24, 2ª versão 16/24, versão final 17/24, com vig-04 1/3 -> **3/3**; a única oscilação restante (par-11, `pavimentacao` não emitida, 2/3 -> 1/3) é de delegação, já registrada como falha em 2026-10-09 e fora das skills alteradas.
- Critério D15 (>= 90 %): não atingido pelo juiz Haiku nem antes nem depois (84-86 %); com o juiz Sonnet do critério original a última rodada fica em 97,7 %. Recomendação: repetir a rodada completa com Sonnet na próxima revisão de descriptions do pacote (pendência já citada em 2026-10-10-roteamento-hecras.md).
- Respostas: `respostas_2026-10-11_descriptions_antes.yaml`, `..._depois1.yaml`, `..._depois2.yaml` (a versão final só mudou as duas descriptions e foi verificada nos 8 casos sensíveis).
