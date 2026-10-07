# Pendências para o treinamento do Especialista em Drenagem

Estado em 2026-10-02, no momento da separação (D18 do pacote hidráulico).

## 1. O que falta construir

| Item | Situação | Observação |
|---|---|---|
| Agente `engenheiro-de-drenagem.md` | não existe | espelhar `../Especialista Hidraulica/.claude/agents/engenheiro-hidraulico.md` (roteamento, delegação, parecer replicável, modo CDV, regras V) |
| Skill núcleo `drenagem-fundamentos` | não existe | convenções, dados mínimos, fluxo, fronteiras (Hidráulica, Climatologia, Geotecnia, Terraplenagem, Orçamento), protocolo de consulta |
| Skill `drenagem-subsuperficial` | não existe | calculadora `drenos.py` já existe; primários: NRCS NEH 624, USBR Drainage Manual, FAO 62, Embrapa; faltam ILRI Pub. 16 e FAO 38 (ver §3) |
| Skill `dissipacao-na-saida-de-bueiros` ou uso da `vertedouros-e-dissipadores` do hidráulico | decidir | rip-rap e bacia de impacto (HEC-14 cap. 9-10) estão em `dissipadores.py` do pacote hidráulico |
| Skill de drenagem de estradas de serviço e plataformas (sarjetas, descidas, drenagem profunda de pavimento) | parcial | hoje é uma seção de `bueiros-e-drenagem-superficial` e `references/valetas-sarjetas-descidas.md` |
| Evals | 11 casos herdados | completar para ~50; não-gatilhos; delegação para Hidráulica e Climatologia; critério D15 (≥ 90%) |
| Casos de aceitação do CDV | nenhum formal | P-134, P-265 a P-268 (bueiros fora do McMath, 77 a 346 m³/s), D-56/D-85 (macrodrenagem), P-42/P-115 a P-118 e D-86 (tubo dreno de 300 mm) |

## 2. Divergências e correções pendentes nas calculadoras

- `hidrologia.py`: Dooge (unidade de S), Giandotti (faixa de área), Picking (unidade), Kirpich modificada (1,5×) e
  DNOS conferidos só parcialmente no primário; tabela de K do DNOS por terreno a confirmar (DNIT-HIDRO p. 89).
- `bueiros.py`: A_c = 0,60 D² do tubular é ajuste à Tab. 1 do DNIT, não fórmula impressa; velocidade de saída do
  exemplo HDS-5 p. 280 (6,47 m/s) não testada; Ke de alas paralelas 0,2 (DNIT) × 0,7 (HDS-5): padrão HDS-5, decidir.
- `drenos.py`: Ernst sem exemplo de livro; fator 1,16 de Glover-Dumm e tabelas indicativas "a confirmar" (faltam
  ILRI 16 e FAO 38); fórmula legada do Xingó (33,5·D^2,67·i^0,5) equivale a n ≈ 0,0093.
- xfail (divergência > 5% com o acervo, para sessão com o André): Baixio folga ao TN (erro aritmético do gabarito?),
  Baixio legado × HDS-5 (6 a 18%), CSB BTCC-17 (Manning dá 28,6 × 39,18 m³/s), Xingó BU-01/06/24 (lâmina por energia,
  não normal), Iuiu DP11 McMath (unidade de S), Baixio HUT TR25 (hietograma não recuperável), CSB 2DN150 (vazão por tubo).

## 3. Fontes que faltam (ver `../Especialista Hidraulica/NAO_ABERTOS.md` e `PENDENTES_DOWNLOAD_MANUAL.md`)

- ILRI Publication 16 *Drainage Principles and Applications* (Ritzema 1994): download falhou (403); tentar edepot.wur.nl.
- FAO Irrigation & Drainage Paper 38 *Drainage design factors* e 26 *Small hydraulic structures*: só HTML por capítulo.
- DAEE-SP *Guia Prático para Projetos de Pequenas Obras Hidráulicas* (2005) e *Manual de Cálculo das Vazões* (1994).
- DNIT ES 018 e 021 (citadas pelo IPR-724); OCR do Álbum IPR-736 (escaneado).
- NBR 8890:2020 (tubos de concreto; substitui 9793/9794): não aberta.
- **IDF e regionalização de chuvas intensas para o norte da Bahia** (Sento Sé/Sobradinho): nada aberto encontrado;
  é o pedido nº 1 ao futuro Especialista em Climatologia.
- TR normativo para bueiros de perímetro irrigado: só USBR (5 a 15 anos) e a prática do acervo (25/50).

## 4. Lições do acervo a preservar como casos negativos

- Projetos do acervo verificam bueiros por Manning plena ou orifício, nunca por HDS-5; o legado subestima HW em 6 a 18%.
- Salitre BTCC 7 e BTCC 1 dariam HW/D ≈ 2,25 e 1,78 pelo controle de entrada; o memorial só mostra Manning.
- Cada projeto usa um limite diferente para o racional (50 ha, 100 ha, 350 ha, 2 km²) e uma fórmula de Tc diferente.
- Coluna "OK" em planilha com folga negativa (Baixio); declividade "5%" onde o contexto indica 0,5% (Iuiu).
- Froude com profundidade geométrica em seção trapezoidal (Baixio) — vale também para canais de drenagem.
