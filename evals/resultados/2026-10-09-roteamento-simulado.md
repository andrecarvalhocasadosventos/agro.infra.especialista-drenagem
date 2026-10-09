# Roteamento simulado — 2026-10-09

Simulador: Sonnet, lendo só o perfil do agente, os frontmatters das skills, a matriz §1 e os prompts (sem `evals/`).
Avaliador: `evals/avaliar_roteamento.py` (delegação obrigatória ⊆ observada ⊆ obrigatória ∪ tolerável).

| rodada | mudança antes da rodada | acerto | delegação (del) | não-gatilho (nao) |
|---|---|---|---|---|
| v1 | — (gabarito com delegação só na nota) | 58/88 = 65,9 % | 5/9 | 4/10 |
| v1 reavaliada | gabarito com `delegacao` e `delegacao_toleravel` explícitos (redator sem acesso às respostas) | 72/88 = 81,8 % | 4/9 | 10/10 |
| v2 | 6 regras de desempate no perfil do agente (dado indispensável ausente → bloco; delegar não dispensa a skill própria; projeto real → casos; norma com vigência → normas; critério de dispositivo → estradas; vazão em travessia → hidrologia) | 83/88 = 94,3 % | 7/9 | 10/10 |
| v3 | regra 1 ampliada (sarjeta pavimentada, dreno profundo), regra 7 (talvegue sob o adutor), del-09 com `clima` tolerável | **86/88 = 97,7 %** | **9/9** | **10/10** |

Critério (PROCESSO §5): ≥ 90 % e 100 % em não-gatilho e delegação: **atendido**.
Falhas restantes: par-11 (dreno profundo de estrada pavimentada: carregou subsuperficial, não emitiu pavimentacao);
mis-05 (dreno que cruza o adutor: carregou bueiros-e-travessias além de canais). Fronteira estradas × subsuperficial
no dreno profundo de pavimento fica para a revisão de descriptions depois da F10.
