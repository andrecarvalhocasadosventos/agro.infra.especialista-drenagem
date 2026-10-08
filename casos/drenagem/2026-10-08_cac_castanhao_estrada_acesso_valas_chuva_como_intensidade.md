# CAC Trecho 1 (Captação Castanhão) — Drenagem da estrada de acesso e da EE: vazão racional com altura de chuva usada como intensidade
fonte: Tomo 1 Vol. 1 Memória Descritiva (doc 1128) pp. 106-112 (Quadros 5.3 a 5.6, Figura 5.1)
disciplinas: [drenagem-de-estradas-e-plataformas, hidrologia-de-projeto-para-drenagem]
nivel: basico
tipo: NEGATIVO (indício forte de erro de unidade/base de tempo; falta o ✓h no PDF original)
qualidade: B (a regra de cálculo do projetista é inferida pela reprodução de 7 de 7 linhas; a fórmula da planilha não está impressa)
marcas: `·` = lido por `ler` (texto nativo, regime nativo, 145/146 páginas); sem linhas em `parametros` para estas páginas. Nenhum `✓h`.

## Problema
Vazão de projeto das valas de crista e coletores da estação de bombeamento e da estrada de acesso, pelo método racional com tc mínimo de 5 min, e dimensionamento hidráulico (Manning, Y/D < 0,5).

## Dados de entrada
| grandeza | valor | unidade | fonte |
|---|---|---|---|
| tc: Kirpich, mínimo adotado | 5 | min | 1128:106 |
| Kirpich impressa: tc = 0,0078·(L/0,3048)^0,77 / J^0,385 | L em m, J em m/m, tc em min | — | 1128:106 |
| Altura de chuva P = 0,959·tc + 18,04 (interpolação 6 min a 1 h, "tabela 3 do relatório hidrológico") | mm | — | 1128:106 (texto "18,.04") |
| P usada nas tabelas, tc = 5 min | 23,20 | mm | 1128:109, 110, 112 |
| C | 0,8 (semi-impermeável, J > 50 %) e 0,6 (demais) | — | 1128:107 |
| n de Manning | 0,015 | — | 1128:107 |
| Critérios: Y/D < 0,5; tensão de arraste > 2 kN/m²; D mínimo 200 mm | — | — | 1128:107 |
| Quadro 5.6 (valas de crista da estrada), C = 0,6, tc = 5 min, P = 23,20 mm | áreas 10200; 44110; 19840; 14000; 43200; 2000; 12250 m² | — | 1128:112 |
| Q impressa (m³/s) VC1; VC2; VC3.1; VC3.2; VC4; VC5; VC6 | 0,039; 0,171; 0,077; 0,054; 0,167; 0,008; 0,047 | m³/s | 1128:112 |
| TR da chuva P | não informado (remete ao relatório hidrológico, Vol. 2) | — | 1128:106 |

## Método do projetista
Racional com P (altura em mm para a duração tc) e área em m². Coletores e valas em meia-cana/tubo: Manning com Y/D < 0,5 (Figura 5.1), verificação de poder de transporte (tensão de arraste).

## Resultado (impresso)
Quadro 5.6: valas de crista da estrada com D 0,20 a 0,45 m, i adotada 0,007 a 0,088, Y/D 0,21 a 0,48 (1128:112). Capacidade a seção plena do trecho VC2: Qf = 0,372 m³/s com Q = 0,171 m³/s.

## O erro (derivado, B)
Para as 7 linhas legíveis do Quadro 5.6, Q_impressa = C·P·A/3,6e6, com P = 23,20 usado como se fosse mm/h:
| vala | C·P·A/3,6e6 (P como mm/h) | Q impressa |
|---|---|---|
| VC1 | 0,0394 | 0,039 |
| VC2 | 0,1706 | 0,171 |
| VC3.1 | 0,0767 | 0,077 |
| VC3.2 | 0,0541 | 0,054 |
| VC4 | 0,1670 | 0,167 |
| VC5 | 0,0077 | 0,008 |
| VC6 | 0,0474 | 0,047 |
(VC3.3: Q 0,075 coincide com a área acumulada 14000 + 5500 m²: 0,0754.)
P = 23,20 mm é altura em 5 min (equivale a 278,4 mm/h). A intensidade correta do racional seria I = P·60/tc = 278,4 mm/h, e Q seria 12 vezes maior (razão 12,0 em seis das sete linhas; 11,6 na VC5 por arredondamento): VC2 daria 2,05 m³/s contra 0,171 m³/s impresso, VC4 2,00 contra 0,167. A seção VC2 (D 0,45 m, i 0,023, Qf 0,372 m³/s) ficaria subdimensionada (Q/Qf ≈ 5,5).
Teste que revela o erro: recalcular Q = C·(P·60/tc)·A/3,6e6 e comparar com a Q impressa; razão = 60/tc = 12.
Ressalva: se o projetista tiver definido P como intensidade (mm/h) na planilha, o texto "altura da chuva (mm)" estaria errado em vez da conta. Em ambos os casos, 23,2 mm/h para tc de 5 min no semiárido é muito baixo e o documento é internamente ambíguo. Confirmar no PDF/planilha original (✓h).

## Outras divergências
1. Fórmula impressa P = 0,959·tc + 18,04 dá P(5) = 22,84 mm, mas as tabelas usam 23,20. A constante 18,40 reproduz 23,195 (hipótese C: dígitos transpostos no texto, "18,.04" tem também ponto duplicado).
2. Quadros 5.3 e 5.4 (estação de bombeamento): a linha Q não reproduz com as áreas da mesma coluna (ex.: VC9 2025 m², C 0,8 → 0,0104 contra 0,011 impressa, mas VC12 880 m² → 0,0045 contra 0,018). A leitura das colunas dessas tabelas pelo texto é incerta (células mescladas); não usar sem ver o PDF.
3. Kirpich em minutos com L/0,3048 (L em pés) é a forma original; coerente. Pelos valores L e J da página 112, Kirpich dá menos de 5 min em todos os trechos (VC2: 3,9 min; VC4: 2,4 min), então o mínimo de 5 min comanda, mas a ligação entre áreas de 4,4 ha (VC2) e tc de 5 min é discutível (Kirpich vale para bacias pequenas; a área de 44110 m² com L = 250 m é aceitável, porém o tc real do escoamento até a vala é maior).
4. TR da chuva e fonte da "tabela 3" não informados (Vol. 2, não lido).

## Gabarito
Nenhum número promovido a gabarito. Candidato para a calculadora: com I = P·60/tc, Q(VC2) = 2,05 m³/s (derivado); com a regra do projetista, 0,171 m³/s. A calculadora deve apontar a diferença, não reproduzir 0,171.

## Fronteira (delegar)
P (altura 6 min a 1 h) e TR: clima. Seção, dissipador de saída: hidráulica.

## Teste sugerido (evals)
Dado A = 44110 m², C = 0,6, P(5 min) = 23,2 mm: o agente deve calcular I = 278,4 mm/h e Q = 2,05 m³/s e reportar que 0,171 m³/s só sai com P tomado como mm/h.
