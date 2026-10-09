# Caso HR-04 — Manchas de inundação dos riachos Recife e Ferreira, 2D não permanente (TPF)

**Tipo:** positivo. **Pergunta:** que lâmina e velocidade os riachos paralelos ao canal produzem para TR 2, 10, 25 e 100 anos, e o canal e o sifão ficam afetados?
`REL-FINAL` = Relatório Final (id 1709); `HR-RF` = `4. Relatórios\Outros\2026.09.29 - HECRAS\riachos recife e ferreira_HECRAS.zip` (id 1532; membros por caminho interno; só `.prj`, `.p01`, `.u01` e `Hidrograma travessia.txt` lidos). Marcas A, B; sem ✓h.

## Dados de entrada
| Item | Valor | Fonte | Marca |
|---|---|---|---|
| IDF (GAM IDF, Kappa) | i = 597,669·TR^0,172 / (9,206 + t)^0,706 (mm/h; t em min) | REL-FINAL:37 | A |
| Conferência da IDF (B) | i(TR 2, 5 min) = 103,42; i(TR 10, 60 min) = 44,60; i(TR 100, 1.440 min) = 7,74 — iguais à Tab. 1 | REL-FINAL:38 | B |
| Sub-bacias (área km², L km, S %, Tc h, CN) e picos SCS TR 2/10/25/100 | Tab. 8: 10 sub-bacias (6 do Ferreira, 4 do Recife); ex.: Recife-SB1: 932,21 km², 65,32 km, 0,42 %, Tc 13,66 h, CN 77, Q = 657,71 / 997,34 / 1.243,41 / 1.701,99 m³/s | REL-FINAL:56-57 | A |
| Pico no arquivo (hidrograma de entrada) | Recife_SB1 TR 100: 1.701,99; TR 2: 657,71; Ferreira_SB1 TR 100: 416,03 (todos iguais à Tab. 8) | HR-RF `riachos_recife_ferreira_TR100/riachos_recife_ferr.u01` e `..._TR2/...u01` | A |
| Software | HEC-RAS 6.5; 2D; simulação 24-set 01:00 a 29-set 23:00 (5 d 22 h), 10 s | HR-RF `.p01` | A |
| Rugosidade | Manning 0,040 | REL-FINAL:57 | A |
| Malha | 50 m (LIDAR + ANADEM) | REL-FINAL:57 | A |
| Contorno de jusante | declividade 0,012 % | REL-FINAL:57 | A (arquivo não conferido) |
| Declividade nos contornos de entrada | 0,002 | HR-RF `.u01` (`Flow Hydrograph Slope`) | A |

## Método do projetista
Chuva-vazão SCS por sub-bacia (Tc de Kirpich, hidrograma por TR; chuva da IDF acima) e entrada dos hidrogramas como contornos de vazão no 2D; mapas de lâmina (cor azul escura ≥ 1 m) e velocidade por TR (REL-FINAL:58-62). A vazão de pico que chega à travessia do sifão do riacho Recife para TR 100 é **589,69 m³/s** (HR-RF `riachos_recife_ferreira_TR100/resultados/Hidrograma travessia.txt`; origem do número no modelo não declarada).

## Resultado
Mapas e shapefiles de contorno de 0,5 m e de limite de inundação por TR (nomes em `resultados/SHP/`). Velocidade máxima mostrada na Fig. 53 (TR 100) com escala até 1,50 m/s (REL-FINAL:62, página com OCR 0,78: **conferir na imagem**). Números de lâmina e de área inundada: **não informados no texto**.

## Gabarito (candidato; sem ✓h)
Os picos de entrada devem coincidir com a Tab. 8 (conferido, 3 de 3 amostras). Conferência adicional de Tc de Kirpich com a fórmula do relatório, Tc = 0,0663·L^0,77·S^-0,385 (L em km, S em m/m; REL-FINAL:50) (B): Recife-SB1 13,62 h contra 13,66 h; Ferreira-SB1 12,77 h contra 12,89 h; Recife-SB4 8,86 h contra 8,97 h (Δ de −1,7 % a +3,9 % nas 10 sub-bacias; maior: Ferreira-SB6, +3,9 %).

## Divergências
- Tab. 8, Recife-SB4 perdeu a coluna de declividade na extração do texto (REL-FINAL:57); conferir no PDF.
- Origem e atenuação do 589,69 m³/s na travessia (ver acima) não explicadas.

## Teste que a skill deve passar
Exigir no parecer: hidrogramas de entrada rastreáveis (pico, tempo ao pico, volume) por sub-bacia e conferência arquivo × tabela; mapa com escala e limiar de lâmina.
