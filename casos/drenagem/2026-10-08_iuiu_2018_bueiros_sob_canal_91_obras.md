# Vale do Iuiu (anteprojeto 2018) — 91 bueiros sob canal de irrigação, tubulares e celulares, Racional / Modificado / HUT, TR 25
tipo: positivo (catálogo de vazões e seções; capacidade não reprodutível com o que foi publicado) com divergências internas e com a versão de 2002
qualidade: B quanto a Q, tipo e geometria da bacia; C quanto à capacidade do bueiro (declividade, comprimento, C, IDF e Tc não informados nas páginas lidas)
fonte: doc 1069, "Alternativas de Obras de Engenharia" (Vol. 1, Tomo V, 2018 - Leilão Ecoinvest), pp. 124-127 (Quadros 4-89 e 4-90). Distinto do caso `iuiu_2002_drenagem_superficial_drenos_bueiros` (doc 1051, projeto básico 2002, que tem 7 bueiros sob canal).
disciplinas: [bueiros-e-travessias, hidrologia-de-projeto-para-drenagem]
nivel: anteprojeto
legenda de marcas: `✓` ancorado; `✓*` magnitude não provada; `·` sem testemunha; `!` divergente/valor não achado na camada de texto; `~` só OCR; `✓h` conferido por humano (nenhum). "texto" = lido na página com `ler`. As pp. 126 não têm linhas extraídas (marca "texto"); p. 127 tem 102 linhas `✓`; p. 124 tem 1 linha `!`.

## Pergunta de engenharia
Como um projeto de 3 etapas dimensionou as travessias de drenagem sob 91 pontos de canal (CP1, CP2, CP3, CS, CT), com que método de vazão por faixa de área e com que critério de seção (tubular × celular, nº de linhas)?

## Dados de entrada
| grandeza | valor | un. | fonte doc:pág | marca |
|---|---|---|---|---|
| Nº de bueiros sob canal | 91 (19 Etapa 1, 33 Etapa 2, 39 Etapa 3); BU1 a BU93, sem BU53 (aqueduto Olho d'Água) e BU59 (excluído) | un. | 1069:124 | texto |
| Tubulares / celulares | 65 / 26 | un. | 1069:124-125 | texto; ✓ (soma em 1069:127) |
| Bueiros tubulares de Ø1,50 m | 7 (1 duplo + 6 triplos) | un. | 1069:124 | `!` (o valor está por extenso no texto: "sete") |
| TR do bueiro | 25 | anos | 1069:125 | texto |
| Manning n | 0,0165 | adim. | 1069:125 | texto |
| Declividade mínima do bueiro | "5 %" | — | 1069:125 | texto (suspeito: ver divergências) |
| Ø mínimo tubular | 0,80 | m | 1069:124 | texto |
| Altura máxima das células | 1,50 | m | 1069:124 | texto |
| Distância geratriz superior do tubo ao fundo do canal | ≥ 0,50 | m | 1069:124 | texto |
| Berço de areia | 0,20 | m | 1069:124 | texto |
| Equações | D = √(4Q/(π·Vmáx)); Q = (1/n)·A·R^(2/3)·I^(1/2) | — | 1069:125 | texto (forma de D lida do PDF, garbled) |
| Colunas do Quadro 4-89/4-90 | A (km²), L (km), H (m), s (%), Método (RAC/MOD/HUT), Q15, Q25, Q50 (m³/s), tipo | — | 1069:125-127 | ✓ |

Exemplos de linhas (todas de 1069:125-127, marca ✓):
| bueiro | local | A (km²) | L (km) | H (m) | s (%) | método | Q15 / Q25 / Q50 (m³/s) | tipo |
|---|---|---|---|---|---|---|---|---|
| BU5 | CS12 8+840 | 2,15 | 2,071 | 21 | 1,014 | MOD | 9,28 / 10,10 / 11,22 | BTTC Ø1,50 |
| BU6 | CS12 9+450 | 0,24 | 1,109 | 11 | 0,992 | RAC | 1,73 / 2,17 / — | BSTC Ø1,00 |
| BU13 | CT123 3+560 | 3,20 | 3,954 | 37 | 0,936 | MOD | 11,15 / 12,13 / 13,47 | BTTC Ø1,50 |
| BU2 (celular) | CS12 2+640 | 6,18 | 3,941 | 19 | 0,482 | MOD | 14,59 / 15,88 / 17,63 | BDCC 2,00x2,00 |
| BU3 (celular) | CS12 5+100 | 25,32 | 13,968 | 156 | 1,117 | HUT | — / — / 76,99 | 2 × BDCC 3,00x3,00 |
| BU61 (celular) | CP2 30+050 | 33,97 | 10,620 | 61 | 0,574 | HUT | — / — / 93,04 | 2 × BDCC 3,00x3,00 |
| BU88 (celular) | CS31 1+880 | 12,97 | 7,892 | 11 | 0,139 | HUT | — / — / 34,71 | BTCC 2,50x2,50 |

## Método do projetista
- Vazão por faixa de área (inferido da tabela; o texto diz só "mesmos critérios dos drenos", 1069:125): RAC para A ≤ ≈ 1,0 km² (maior RAC: BU26, 0,99 km²); MOD (método modificado, não definido nas páginas lidas) de ≈ 1,0 a ≈ 8,7 km² (maior MOD: BU64, 8,72 km²); HUT (hidrograma unitário triangular) a partir de ≈ 10,2 km² (menor HUT: BU34, 10,15 km²). Rastro C (limites lidos da tabela, não escritos).
- Seção: Manning + continuidade; tubular com mínimo Ø0,80 (manutenção) e até triplo; celular com altura limitada a 1,50 m no texto.
- Sem HW/D, sem controle de entrada, sem verificação de saída, sem velocidade de saída: nada disso é publicado.

## Resultado
- 65 tubulares e 26 celulares, 14 linhas HUT (todas celulares, só com Q50 publicada), 6 linhas tubulares sem Q publicada (BU1, BU24, BU58, BU87 sem bacia; BU52 e BU75 com bacia mas sem Q).
- Maior bueiro: 2 × BDCC 3,00x3,00 (BU61, Q50 = 93,04 m³/s; BU43, Q50 = 84,49; BU3, 76,99).

## Gabarito para a calculadora (propostas; nenhuma promovida a gabarito sem `✓h`)
- Classificação de método por área: aplicar RAC se A ≤ 1,0 km² etc. reproduz a coluna "Método" nas 91 linhas (contagem manual por faixas; confirmar o limite exato de 1,0 km² e de ≈ 10 km² com o texto de 1069:123, não lido).
- Soma de unidades: 65 tubulares (13 Ø0,80, 20 Ø1,00, 25 Ø1,20, 7 Ø1,50) e 26 celulares (texto, 1069:124-125).
- Não há gabarito de capacidade: a declividade e o comprimento de cada bueiro não estão nas páginas lidas (só `s` da bacia). Sugestão de eval: dado Q25 e tipo, verificar por HDS-5 se a escolha cabe (ex.: BU5, 3 × Ø1,50, Q25 = 10,10 m³/s, 3,37 m³/s por linha) com S e L declarados pelo avaliador.

## Rastro
- A: números do Quadro 4-89/4-90 (uma linha por bueiro) lidos do texto nativo; contagens 65 e 26 conferidas por contagem manual (65 tubulares na tabela; células 1 + 10 + 9 + 6 = 26 batem com o texto).
- B: faixas de área por método (derivadas da tabela).
- C: significado de "MOD" e "Q15" (TR 15 ou "15 min"? o cabeçalho diz Q15/Q25/Q50; não informado).

## Divergências
1. TR: 2018 (1069:125) usa TR 25 para bueiros sob canal; o caso de 2002 (doc 1051:316, 331) usa TR 50 sob canal e 25 sob estrada. Mesmo perímetro, duas premissas.
2. Q usada no dimensionamento: o texto diz TR 25, mas as 14 linhas HUT publicam só Q50 (sem Q25) e as linhas RAC só Q15 e Q25 (sem Q50). Não está dito para qual TR cada seção foi dimensionada.
3. Altura das células: texto "limite de altura de 1,50 m" (1069:124) × quadro 4-90 com células de 2,00 a 3,00 m (25 das 26 passam de 1,50 m; só BU37, BTCC 1,50x1,50, respeita). O limite parece remanescente da versão de 2002 (1051: células 2,0x1,5).
4. Declividade mínima "5 %" (1069:125): idêntica ao caso de 2002; 5 % em bueiro de travessia de canal é implausível (0,5 % mais provável). Não informado; conferir `s` no desenho 807-CDVF-IUI-DR-OH-07/08 (Vol. 3).
5. Distribuição do tubular Ø: o texto dá Ø0,80 com 9 simples e 4 duplos e Ø1,20 com 5 simples, 8 duplos e 12 triplos (1069:124); a tabela (contagem minha) dá 8 simples de Ø0,80 e 6 simples de Ø1,20. Um BSTC aparece como Ø0,80 no texto e Ø1,20 na tabela. Total 65 coincide.
6. Linhas incompletas: BU1, BU24, BU58, BU87 (sem bacia nem Q) e BU52, BU75 (bacia sem Q); BU73 e BU74 têm os mesmos dados (A = 0,35, L = 0,718, H = 13), com "BH33b" e "Bh33b" (duplicação provável de bacia).

## Fronteira
Chuva por TR e Tc: Clima/Drenagem-hidrologia. Estrutura da aduela e do berço: Estruturas. Cota e greide do canal: Hidráulica.
