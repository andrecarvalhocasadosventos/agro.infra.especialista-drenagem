# Brief F6 — skills do Especialista Drenagem (2026-10-08)

Base: `../Agent Builder/modelos/BRIEF_SKILL.md` (leia; vale integralmente: `[ID p. N]` conferido, ≤ 25 KB,
description ≤ 1.024 caracteres com "Use quando"/"Não use para", estrutura, armadilhas, mapa fórmula → função → teste).
Modelos de forma: `../Agent Builder/modelos/SKILL_nucleo.md` (núcleo) e `SKILL_disciplina.md`; exemplos instalados:
`../Especialista Hidraulica/.claude/skills/hidraulica-fundamentos/SKILL.md`, `canais-abertos/SKILL.md`.
RAIZ = `08. AI Squad/Especialista Drenagem`. Agente ainda não existe (F8): use como perfil `PLANO.md` §1–§3,
`LEIA-ME.md` e a linha `drenagem` da `../Agent Builder/MATRIZ_DE_INTERFACES.md` (§3.3 e linhas recíprocas).
Agente: `engenheiro-de-drenagem`; núcleo: `drenagem-fundamentos`. Ids de delegação: clima, hidraulica, geotecnia,
terraplenagem, pavimentacao, irrigacao, orcamento, estruturas.

Insumos: `tools/dren/README.md`, `tools/dren/DIVERGENCIAS.md` e docstrings dos módulos (hidrologia, bueiros, tubos,
drenos, estradas, canais_drenagem); `casos/drenagem/_INDICE.md` e os casos da sua skill; `referencias/MAPA_DE_CONHECIMENTO.md`
(corpus próprio, `referencias/_texto/`) e o mapa do Hidráulico H12–H15 (`../Especialista Hidraulica/referencias/`,
corpus por caminho, D1: cite pelos IDs dele). Decisões em vigor: D1–D8 do `PLANO.md` (D3 dissipador de saída de
bueiro = Hidráulico; D5 drenagem agrícola = Drenagem). **Pontos abertos para a F7** (não decida; escreva "padrão
provisório, decisão F7" e mostre as alternativas com fonte): TR de bueiros de perímetro irrigado (USBR 5–15 × acervo
25/50); Ke de alas paralelas (DNIT 0,2 × HDS-5/HEC-13 0,7); limite de área do racional; Tc mínimo de drenagem
superficial (5/6/10 min).

Regra transversal obrigatória (risco nº 1 do plano): diante de projeto do acervo que diverge do método, a skill manda
**apontar a divergência com evidência e consequência**, nunca "corrigir" o projeto em silêncio.

Escreva só em `.claude/skills/<sua-skill>/`. Skills existentes a revisar (mantenha o que está conferido; ajuste
caminhos `tools/dren`, novas funções e casos novos; não perca conteúdo): `hidrologia-de-projeto-para-drenagem`,
`bueiros-e-drenagem-superficial` → **renomear a pasta para `bueiros-e-travessias`** (D4) e mover o conteúdo de sarjeta/
valeta/descida/dispositivos para `drenagem-de-estradas-e-plataformas` (coordenação: o agente de bueiros remove; o de
estradas lê os references `valetas-sarjetas-descidas.md` e `dispositivos-tipo-dnit.md` do original via git
`git show HEAD:.claude/skills/bueiros-e-drenagem-superficial/references/<arq>` e os recria na sua pasta).
Hidrologia: ajustar ao Clima (o Drenagem não ajusta IDF; consome a entrega de `chuvas-intensas-e-idf` e cita).
Resposta ≤ 15 linhas no formato do brief base.
