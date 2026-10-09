# Caso HR-01 — Captação no rio São Francisco: NA por vazão em modelo 2D (TPF)

**Tipo:** positivo. **Pergunta de engenharia:** qual o nível d'água no ponto de captação para Q95, Q98, Q50, Qméd, QTR100 e QTR500, e com que dados de entrada?
**Marcas:** A = lido no documento; B = derivado de valor lido; nenhum número tem ✓h (nada conferido por humano) → **nenhum vira gabarito de calculadora** até conferência.

Documentos: `REL-FINAL` = `CDV-VDT-REL-INF-GER-001-R00 - Relatório Final.pdf` (acervo id 1709; páginas do PDF); `HR-SF` = `4. Relatórios\Outros\2026.09.29 - HECRAS\sao francisco_HECRAS.zip` (id 1533), membros citados por caminho interno.

## Dados de entrada
| Item | Valor | Fonte | Marca |
|---|---|---|---|
| Vazões de referência no posto Morpará (m³/s): Q95, Q98, Q50, Qméd, QTR100, QTR500 | 633,41; 501,61; 1.533,19; 2.119,93; 13.263,56; 16.491,55 | REL-FINAL:40 (Tab. 2) | A |
| Regionalização Q = Q_posto · (A_capt/A_posto) · (P_capt/P_posto); A = 435.392 e 345.341 km²; P = 1.032 e 1.052 mm; fator "1,24" | REL-FINAL:41 (Tab. 3) | A |
| Vazões no ponto de captação (m³/s) | 783,77; 620,68; 1.897,14; 2.623,16; 16.412,05; 20.406,29 | REL-FINAL:41 (Tab. 4) | A |
| Séries de vazão no modelo (hidrograma constante, 100 valores horários) | 783,77 (Q95); 1.897,14 (Q50); 16.412,05 (QTR100) | HR-SF: `sao_francisco_Q95/sao_francisco.u01` etc. | A |
| Software e versão | HEC-RAS **6.5 (fev/2024)**, equações SWE-ELM, 2D, 20 núcleos | HR-SF: `.p01` e `.b01`; mensagem de cálculo no `.p01.hdf` | A |
| Rugosidade | Manning **0,035** em todas as 31.313 células | REL-FINAL:41; HR-SF `.g01.hdf` (`Cells Center Manning's n`: 1 valor único) | A |
| Malha | 10 m na área da batimetria, 50 m fora (relatório); no arquivo, área de célula mediana 99,93 m² | REL-FINAL:41; HR-SF `.g01.hdf` | A |
| Contorno de jusante | declividade média do rio **0,01 %** (relatório); arquivo: 0,000093 (ver HR-03) | REL-FINAL:41; HR-SF `.u01` | A |
| Terreno | batimetria (levantamento) + ANADEM 30 m recortado | REL-FINAL:41; HR-SF `Terrain/` | A |

## Método do projetista
Modelo hidrodinâmico 2D com vazão constante em cada cenário (simulação de 24 h a partir de 14-set-2026 01:00, passo de 10 s), tomando o NA ao final como nível de projeto da captação. Os TR de 100 e 500 anos vêm da distribuição lognormal de 2 parâmetros do posto, regionalizada (REL-FINAL:39-41).

## Resultado
| Vazão | Q (m³/s) | NA (m) | Fonte |
|---|---|---|---|
| Q95 | 783,77 | 390,80 | REL-FINAL:42 (Tab. 5); HR-SF `sao_francisco_Q95/Resultados/Resultados.txt` ("NA = 390,80m") |
| Q98 | 620,68 | 390,45 | REL-FINAL:42 |
| Q50 | 1.897,14 | 392,25 | REL-FINAL:42; HR-SF `Q50/Resultados/Resultados.txt` |
| Qméd | 2.623,16 | 392,97 | REL-FINAL:42 |
| QTR100 | 16.412,05 | 397,56 | REL-FINAL:42; HR-SF `QTR100/Resultados/Resultados.txt` |
| QTR500 | 20.406,29 | 398,34 | REL-FINAL:42 (arquivo QTR500 não aberto) |

Vazão que passa pelo "braço LD" (margem esquerda/direita, nome do projetista): 90,27 m³/s no Q95 e 405,41 m³/s no Q50 (HR-SF `Resultados.txt`; B: 11,5 % e 21,4 % da vazão afluente). Não consta do relatório.

## Gabarito (candidato; sem ✓h)
- NA de Q95 = 390,80 m e de QTR100 = 397,56 m, **no ponto de captação** (ponto exato não informado). Valores de malha lidos do `.p01.hdf` (B): no fim da simulação do Q95, 21.996 células molhadas com NA mediano 390,88 m, p5 390,66 m, p95 391,01 m, máx. 391,02 m; no QTR100, 28.882 células molhadas, mediana 397,67 m, p5 397,45 m, p95 397,84 m, máx. 398,24 m. O NA do relatório cai dentro da faixa da malha, mas o gradiente espacial é de ~0,3 a 0,8 m: **quem cita o NA precisa dizer onde**.

## Rastro
A: Tab. 2-5 e `Resultados.txt`. B: regionalização conferida (Q_capt/Q_posto = 1,2374 em todas as seis vazões; o fator pelas áreas e chuvas é 1,2368; "1,24" é arredondamento); NA estatístico da malha. C: o ponto de leitura do NA.

## Divergências
- Tab. 5 do relatório, cabeçalho da coluna Qméd: unidade "N.A. (m³/s)" — deveria ser m (REL-FINAL:42). Erro de digitação sem efeito no número.
- A vazão do "braço LD" não aparece no relatório.

## Fronteira
Dimensionar a captação e as bombas é do Hidráulico (`estacoes-elevatorias-e-bombas`); Q95/QTR100 do posto vêm do Clima/hidrologia; MDT/batimetria é do futuro Geoprocessamento. A Drenagem só conduz a modelagem de cheia/NA.

## Teste que a calculadora/skill deve passar
Dado o conjunto (Q, malha, n, BC), o parecer precisa pedir ou reproduzir a regionalização (fator 1,2374) e declarar que o NA é pontual dentro de uma superfície com gradiente.
