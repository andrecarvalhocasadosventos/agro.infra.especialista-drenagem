# Brief F3 — mapa de conhecimento do corpus próprio do Drenagem (2026-10-08)

Base: `../Agent Builder/modelos/BRIEF_MAPA.md` (leia; vale integralmente, inclusive o teto de 80 p./documento e 300 p.
no total). RAIZ = `08. AI Squad/Especialista Drenagem`. Só os itens novos do corpus próprio (`referencias/`); o corpus
do Hidráulico já tem mapa (`../Especialista Hidraulica/referencias/MAPA_DE_CONHECIMENTO.md`, seções H12–H15 são de
drenagem — use Grep nelas só para registrar divergência ou complemento com o que você mapeou, sem refazer).
Texto: `referencias/_texto/<ID>.*` com `<!-- p. N -->` (páginas de OCR marcadas `<!-- ocr -->`: números de OCR
saem "(OCR, conferir na imagem)"). Índice FTS opcional: `C:\bibdren\db\corpus.sqlite`.
Escreva só `referencias/_mapa_parcial/<grupo>.md`. Ignore os slides Robson I–IV (sem OCR) e o FDOT (não baixado).

Grupos:
- **G1-hidrologia**: LOC-MCCUEN-HYDROLOGIC-ANALYSIS, LOC-ESLAMIAN-HANDBOOK-HYDROLOGY, LOC-PFAFSTETTER-CHUVAS-INTENSAS,
  LOC-NEH-TC-ESCOAMENTO-PLANO, LOC-PLANILHA-ESCOAMENTO-PLANO-001, LOC-PLANILHA-ESCOAMENTO-PLANO-REDENCAO,
  USGS-WSP1849, USACE-EM1110-2-1413. Prioridade: exemplos resolvidos de Tc (Kirpich, NRCS lâmina/concentrado,
  Dooge, Giandotti, Picking), racional, SCS-CN, HU, frequência — que sirvam de teste de calculadora (1 %).
  Pfafstetter: só localizar (o Clima entrega IDF; o Drenagem cita).
- **G2-bueiros-tubos**: LOC-ABTC-* (6), FHWA-HDS3, FHWA-HEC13, FHWA-HY8-V770-NRCS, USACE-EM1110-2-2902,
  LOC-SISCCOH-MANUAL-V11. Prioridade: classes de tubo NBR 8890 (PA/PS, recobrimento), n de tubos, exemplos de bueiro.
- **G3-estradas**: DNIT-ES018-2023, DNIT-ES020-2006, DNIT-ES021-2023, DNIT-IPR726-2006, DERPR-ES-DR-01/03/05/06/07-23,
  FHWA-HEC12, LOC-IME-DRENAGEM-URBANA-RODOVIAS, LOC-DNIT-ALBUM-2018, WSDOT-HYDRAULICS-M2303-12. Prioridade:
  sarjeta, valeta, descida, caixa, dispositivos-tipo, drenagem profunda; exemplos numéricos de sarjeta/valeta.
- **G4-canais-subsuperficial**: USACE-EM1110-2-1601, FHWA-HEC11, NRCS-CPS608-2023, EMBRAPA-* (4), ILRI-56-ENVELOPE,
  LOC-COMAER-EDMIR-DREN-SUBSUPERFICIAL, WATERLOG-DRAINAGE-EQUATION, WATERLOG-ENDRAIN, LOC-RETROANALISE-CANAL-GABIAO.
  Prioridade: velocidade admissível e revestimento, rip-rap de canal (localizar; dissipação é do Hidráulico, D3),
  Hooghoudt/Ernst/Glover-Dumm com exemplo resolvido (faltam para `drenos.py`), critério de envoltório, fator 1,16.

Além do formato base, termine o arquivo com a seção `## Gabaritos para calculadora` (exemplo resolvido: fonte e
página, entradas, resultado, unidade) e `## Pendências para a F5/F7` (fórmula conferida/divergente do que o
`PENDENCIAS_DE_TREINAMENTO.md` §2 lista).
