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

## 2026-10-07 — F1 · manifesto de fontes

- 1 Sonnet (`BRIEF_F1.md`): `tools/fontes_candidatas.yaml` com **28 itens abertos** (A=5, B=16, C=7) e **21 fontes locais** (12 A, 9 B; todas existem em `G:\Meu Drive\DRENAGEM`); YAML válido, sem IDs duplicados. `NAO_ABERTOS.md` (3,8 KB) e `PENDENTES_DOWNLOAD_MANUAL.md` (2,7 KB).
- URLs: todas as 28 com GET parcial 200/206 e `%PDF-`. Sem item no manifesto: FAO 38 (403), NRCS 606/607 (conexão reiniciada), USBR (conexão reiniciada) → pendentes. Espelhos marcados: USACE, HEC-11, CED, Snohomish.
- Fechados: NBR 8890:2020, DAEE Manual de Vazões 1994, NBR 15645 e 16085, Chow-Maidment-Mays, Tucci, AASHTO, ASCE MOP 77, TR de bueiros em perímetro irrigado.
- Download previsto: ~104 MB, ~2.500 páginas (abertos); fontes locais ~600 MB (251 MB só o Pfafstetter).
- Conferência: amostra de 3 URLs refeita por mim (3 PDF). Anos de HEC-13, EM 1110-2-2902, EM 1110-2-1413 e título da ES 018/2023 a conferir no download.
- Custo: ~US$ 1 estimado (243 mil tokens de subagente Sonnet, 93 chamadas). Sem testes novos (tests/hid inalterado).
- `verificar_instalacao.py` ainda não existe no pacote (entra na F11).

## 2026-10-08 — F2 · corpus

- Scripts em `tools/`: `montar_fontes.py` (gera `fontes.yaml` com 49 itens: 28 `http` + 21 `local`; `--copiar` copia só os 21 itens de `fontes_locais:`), `baixar_referencias.py` e `extrair_texto.py` (adaptados do Hidráulico; o de texto ganhou leitura de `.xlsx` e uso do OCR), `ocr_pdf.py` (RapidOCR local, página única, retomável), `catalogar.py` (acrescenta `tem_texto`, `ocr`, `paginas_ocr` ao catálogo), `indexar_fts.py`. Python 3.14 global; nenhum venv criado (PyMuPDF, RapidOCR, httpx já presentes). Nada alterado no pacote do Hidráulico.
- Abertos: **27 de 28 baixados** (assinatura `%PDF-` conferida, sha256 e páginas no catálogo); 1 falha: `FDOT-DRAINAGE-MANUAL-2016` (servidor entrega PDF truncado, igual em 2 tentativas) em `PENDENTES_DOWNLOAD_MANUAL.md`. Tamanho: 115,7 MB; 2.598 páginas; ~3 min.
- Locais: **21 de 21 copiados** de `G:\Meu Drive\DRENAGEM` (18 PDF + 3 `.xlsx`), 602,1 MB, 3.929 páginas; nada além da lista. Licença `uso-interno` em 19 itens (o álbum DNIT 2018 e o NEH Tc ficaram com `aberta` e `dominio-publico`, como no manifesto aprovado).
- Total no catálogo: 48 `ok` + 1 `manual_needed` = 49; 717,9 MB; 6.527 páginas. `referencias/**` segue ignorado pelo git (só `_catalogo.yaml` entra).
- Texto: 48 arquivos em `referencias/_texto/` (marcadores `<!-- p. N -->`; páginas de OCR levam também `<!-- ocr -->`; 3 planilhas como texto por aba). Escaneados pelo limiar (< 80 caracteres/página): 3 (`LOC-PFAFSTETTER-CHUVAS-INTENSAS`, `LOC-DNIT-ALBUM-2018`, `LOC-ROBSON-...-IV`). Slides do curso Robson I a III têm 69, 80 e 155 páginas só-imagem.
- OCR (RapidOCR/onnx, 200 dpi, 6 threads; sem tesseract/ocrmypdf no sistema): Pfafstetter 422 de 426 páginas em 38 min (confiança média 0,69; 106.479 caracteres); Álbum DNIT 2018 203 de 227 páginas em 43 min (confiança média 0,72; 285.886 caracteres; 18 páginas seguem sem texto). **Sem OCR:** Robson I a IV (521 páginas só-imagem, prioridade B; ~45 min se for necessário). Conferência do Pfafstetter (10 páginas): tabelas de β dos postos (p. 393 a 398) com ~97% dos números corretos e quadro de α correto; tabelas esparsas (células com traço, como os quadros de chuvas máximas por posto) perdem o alinhamento de colunas e têm erros isolados de dígito.
- Índice FTS5 por página fora do Drive: `C:\bibdren\db\corpus.sqlite` (48 documentos, 6.396 páginas com texto, 39,5 MB; tabelas `doc`, `pagina`, `busca_pagina`; tokenizer `unicode61 remove_diacritics 2`). Cobre só o corpus próprio do Drenagem; o do Hidráulico segue por caminho (D1). Reconstrói com `python tools/indexar_fts.py`.
- Conferências de manifesto: HEC-13 é a edição de 1972 (arquivada, superada pelo HDS-5); EM 1110-2-2902 é de 1997 com Change 1 de 1998; o arquivo `USACE-EM1110-2-1413` é a cópia do curso CED (C11-002); título da DNIT 018/2023-ES confirmado ("Drenagem – Sarjetas e valetas").
- Tempo de sessão: ~1 h 50 min (downloads 3 min, extração ~5 min, OCR 81 min em segundo plano). Custo: 0 de subagente.

## 2026-10-08 — F4 · casos reais e F5a · migração

- F4: 3 Sonnet em paralelo (`tools/briefs/BRIEF_F4.md`), lotes L1 canais de drenagem, L2 estradas e hidrologia,
  L3 bueiros e subsuperficial. **16 casos novos** (10 positivos, 6 negativos) em `casos/drenagem/2026-10-08_*.md`;
  total 26. Documentos do acervo: 1069, 1122, 1128, 1131, 1139, 1182, 1390, 1419, 1492–1494, 1515, 1520, 1521,
  1584, 1585 + planilha local do gabião. Nenhum número com `✓h` (gabaritos candidatos). `casos/drenagem/_INDICE.md`
  consolidado. Sugestões numéricas em `evals/sugestoes_casos_numericos_F4.md`. Sem caso: Hooghoudt/Ernst calculado
  em projeto, sarjeta/descida com memória, D-56/D-85 específicos. Tokens de subagente: ~724 mil (Sonnet).
- F5a (D2): `tools/hid` → `tools/dren`, `tests/hid` → `tests/dren` (git mv, 9 arquivos + 21 com referências
  atualizadas). pytest antes e depois: 127 passed, 11 xfailed. `PACOTE.yaml`: calculadoras/testes/marcadores. ~69 mil tokens.

## 2026-10-08 — F3 · mapa de conhecimento

- 4 Sonnet em paralelo (`tools/briefs/BRIEF_F3.md`): G1 hidrologia (8 docs, ~155 p. lidas), G2 bueiros e tubos
  (11 docs, ~130 p.), G3 estradas (13 docs, ~200 p.), G4 canais e subsuperficial (12 docs, ~190 p.). 44 documentos
  mapeados, 0 ignorados (Robson I–IV e FDOT fora por não terem texto/arquivo).
- Localizados: ~54 gabaritos para calculadora (G1 17, G2 13, G3 13, G4 11), ~150 tabelas/ábacos com página.
  Divergências entre fontes: G1 7, G2 6, G3 13 (+4 anomalias), G4 7.
- `referencias/MAPA_DE_CONHECIMENTO.md` consolidado (99,7 KB). Tokens de subagente: ~1,01 milhão (Sonnet).
- Achados para a F5: A_c = 0,60 D² ganha fonte impressa (IME p. 151–152); Ke = 0,7 de alas paralelas confirmado no
  HEC-13 Tab. 1 p. 100; Picking com unidade conferida (IME p. 29); fator 1,16 de Glover-Dumm fecha em exemplo
  (Maniçoba p. 2–3); Ernst com exemplo (WATERLOG-ENDRAIN p. 10, divergência 3,5 %); Dooge, Giandotti, DNOS e o
  1,5× da Kirpich modificada não estão no corpus próprio.

## 2026-10-08 — F5 · calculadoras e F6 · skills

- F5: 5 Sonnet em paralelo (`tools/briefs/BRIEF_F5.md`): hidrologia 0.3.0, bueiros 0.3.0, drenos 0.2.0, novos
  `tubos.py` 0.1.0, `estradas.py` 0.1.1, `canais_drenagem.py` 0.1.1. pytest `tests/dren`: **269 passed, 14 xfailed**
  (partida 127/11). Revisão de fórmula por 1 Opus: 19 itens amostrados, 16 conferidos no primário, 2 avisos corrigidos
  (grelha HEC-12 p. 87; seção composta EM-1601 p. 60), 3 pendentes F7; nenhuma fórmula alterada. Registro em
  `tools/dren/DIVERGENCIAS.md` (seções F5 e "Revisão de fórmula F5"). Tokens: Sonnet ~1,0 milhão; Opus ~208 mil.
- F6: 8 Sonnet (núcleo primeiro, depois 7 em paralelo; `tools/briefs/BRIEF_F6.md`). Skills: `drenagem-fundamentos`
  (25,6 KB), `hidrologia-de-projeto-para-drenagem` (25,2), `bueiros-e-travessias` (25,5; renomeada de
  `bueiros-e-drenagem-superficial`, D4), `drenagem-de-estradas-e-plataformas` (17,8), `canais-de-drenagem-e-macrodrenagem`
  (19,5), `drenagem-subsuperficial` (22,4), `drenagem-normas-e-manuais` (21,1), `drenagem-casos-de-referencia` (16,4);
  35 references. Conferente de forma (script): 8/8 com `name` = pasta, description ≤ 1.024 com "Use quando" e
  "Não use", SKILL.md ≤ 25,6 KB. Tokens ~1,8 milhão (Sonnet).

## 2026-10-08/09 — F7 · revisão técnica (parte automática), F8 · agente, F9 · redação dos evals

- F7: 2 Opus (lote A direto; lote B com 4 sub-revisores, um por skill; `tools/briefs/BRIEF_F7.md`). Amostradas
  ~151 afirmações nas 8 skills (A: 59; B: 21 + 15 + 24 + 16 ≈ 76; mais ~16 do fundamentos/casos); correções de
  página, unidade e texto nas skills; nenhum erro numérico de calculadora. Seção `## Revisão técnica` no fim dos 8
  SKILL.md. Achados em `tools/dren/DIVERGENCIAS.md` (Lote A; Lote B reconstituído em 2026-10-09 porque a gravação
  concorrente do lote A o sobrescreveu). pytest inalterado: 269 passed, 14 xfailed. Tokens Opus ~0,8 milhão.
- F8: 1 Sonnet. `.claude/agents/engenheiro-de-drenagem.md` (20,5 KB; description 1.066 caracteres; 18 V-regras;
  8 linhas de roteamento; 12 pontos abertos com padrão provisório), `memoria/MEMORIA.md` em 4 camadas, `LICOES.md`,
  `pareceres/parecer_cabecalho.md`.
- F9 (redação): 1 Sonnet. `evals/roteamento.yaml` 88 casos (PAR 30, DELEGACAO 39, NAO-GATILHO 10, CDV 9,
  VIGENCIA 6, mistos 5; ≥ 4 por skill), `evals/casos_numericos.yaml` 40 casos (21 reproduz, 9 divergência > 5 %,
  10 sem gabarito), `evals/README.md`; herdados incorporados e apagados. `evals/avaliar_roteamento.py` adaptado do
  Clima (delegação lida da `nota`). Uma sessão `/treinar squad` escreveu por engano em `evals/` entre 19:35 e 19:41;
  o redator conferiu e regravou os arquivos.
- Processos: registro órfão da F2 encerrado em 2026-10-09 (sem processo ativo).

## 2026-10-09 — F9 · medição de roteamento

- Simulação Sonnet em 3 rodadas (`evals/resultados/2026-10-09-roteamento-simulado.md`): 65,9 % → 81,8 % (gabarito com
  delegação explícita) → 94,3 % → **97,7 %** (86/88; del 9/9; nao 10/10). Ajustes só no perfil do agente (7 regras de
  desempate) e em 1 linha de gabarito (del-09); descriptions de skill inalteradas. Perfil do agente 20,45 KB (tabela
  de pontos abertos movida para `drenagem-fundamentos/references/pontos-abertos.md`).
- `PARA_O_ANDRE_F7.md`: 20 decisões de critério, 3 pedidos de informação, veredito proposto para os 14 xfail.
