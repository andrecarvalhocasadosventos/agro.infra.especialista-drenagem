# Roteamento da skill modelagem-hidraulica-hec-ras - 2026-10-10

Juiz: 1 subagente Haiku, lendo só o perfil do agente, os frontmatters das 9 skills e a MATRIZ §1-2 (sem `evals/`).
Casos: hr-01 a hr-07 (novos) e nao-10 (reescrito: HEC-RAS deixou de ser não-gatilho, D9 e MATRIZ §2).
Respostas: `respostas_hr_2026-10-10.yaml`. Avaliador: `avaliar_roteamento.py` (função `avaliar`).

Resultado: 7/8 na primeira leitura. Falha: hr-07 emitiu `[DELEGAR: hidraulica]` (aqueduto, D18), não previsto no gabarito;
o gabarito foi corrigido para `delegacao_toleravel: [hidraulica]` (defeito do gabarito, não do roteamento). Reavaliado: 8/8.
Não foi rodada a simulação dos 95 casos completos (só os 8 do escopo HEC-RAS); a rodada completa fica para a revisão de descriptions.
