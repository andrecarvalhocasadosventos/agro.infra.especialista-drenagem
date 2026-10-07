# EXECUÇÃO — diário do Especialista Drenagem

Só fatos e contagens, datados. Nada de opinião nem de plano (isso é o `PLANO.md`). Uma seção por sessão de treinamento
ou de manutenção.

## 2026-10-02 — semente

- Separada do Especialista Hidráulica (D18-Hid). Registro em `LEIA-ME.md` e `PENDENCIAS_DE_TREINAMENTO.md`.

## 2026-10-07 — F0 · plano

- `PLANO.md` v0.1 escrito (Agent Builder, Opus, sem subagentes). Decisões D1–D8 aprovadas pelo André em 2026-10-07.
- Contagem de partida: 2 skills (24,4 + 24,3 KB; 6 + 6 references), 3 calculadoras (`hidrologia` 31,6 KB,
  `bueiros` 33,2 KB, `drenos` 23,0 KB) + `_cli.py`, 3 arquivos de teste; pytest `tests/hid`: **127 passed, 11 xfailed,
  1 warning** (5,1 s). Casos: 10 `.md` + `_INDICE_original_completo.md`. Evals: 11 de roteamento + 1 numérico.
- Pasta `G:\Meu Drive\DRENAGEM` inventariada (D8): 300 arquivos, 2.440 MB; 16 PDFs triados A/B em `PLANO.md` §5.1;
  nenhum duplicado no corpus do Hidráulico ou do Clima, exceto os manuais e álbuns do DNIT (IPR-724/736).
- `tools/BRIEF_F1.md` pronto (1 Sonnet, manifesto de lacunas + bloco de fontes locais).
- `.gitignore` copiado do padrão do Hidráulico (`referencias/**` fora do git, salvo catálogo e mapa).
- `verificar_squad.py`: Drenagem 1 PASS, 1 AVISO, 2 FALHA (agente e núcleo ausentes: esperado até F6/F8).
- Git: repositório `agro.infra.especialista-drenagem` vinculado, gitdir `C:\gitdirs\especialista-drenagem` (D7).
- Custo: subagentes 0; só a sessão do Agent Builder.
- Portão F0: aprovado por André em 2026-10-07.
