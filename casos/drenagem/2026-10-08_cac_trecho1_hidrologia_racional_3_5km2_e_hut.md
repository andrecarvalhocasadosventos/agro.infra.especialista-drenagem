# CAC Trecho 1 (Jati/Cariús) — Hidrologia da macro e média drenagem: Racional até 3,5 km², HUT acima, C 0,20 para 0,40 e CN 65 para 85
fonte: Relatório do Projeto Executivo, Vol. I Tomo I Memorial Descritivo (doc 1139) pp. 226-228, 239, 250; Tomo 1 Vol. 1 (doc 1128) p. 106 (Kirpich, para comparação)
disciplinas: [hidrologia-de-projeto-para-drenagem]
nivel: basico
tipo: positivo (limites e parâmetros) com 3 inconsistências de fórmula impressa
qualidade: B (sem exemplo numérico de vazão; 1139:229-237 sem texto, "ausente" no acervo)
marcas: `·` = lido por `ler` (doc híbrido, texto nativo nas páginas citadas); sem linhas em `parametros` nestas páginas. Nenhum `✓h`.

## Problema
Que método, limite de área, tc, C e CN o projeto do CAC usou para a vazão de pico de 448 bacias interceptadas pelo canal, e o que mudou do anteprojeto para o executivo?

## Dados de entrada
| item | valor | fonte | marca |
|---|---|---|---|
| Limite do racional | área < 3,5 km² (citando Manual de Hidrologia Básica, DNIT 2005) | 1139:227 | · |
| Bacias pelo racional / por HUT | 428 / 20 (total 448) | 1139:239 (Quadro 4.24) | · |
| Por lote, racional | 106; 91; 99; 132 | 1139:239 | · |
| Por lote, SCS (HUT) | 6; 4; 7; 3 | 1139:239 | · |
| C do racional: anteprojeto e projeto licitado | 0,20 | 1139:227 | · |
| C do racional: projeto executivo | 0,40 (visitas de campo, estudos da UFC) | 1139:227 | · |
| CN do HUT: anteprojeto e licitado / executivo | 65 / 85 | 1139:227 | · |
| TR das vazões de projeto dos bueiros | 100 anos (vazões para 2, 5, 10, 25, 50, 100 no Quadro 4.19) | 1139:228 | · |
| Tc (HUT): Kirpich modificada | tc = 85,5·(L³/h)^0,385, tc em min, L em km, h em m | 1139:228 | · |
| tp = d/2 + 0,6·tc; tb = (8/3)·tp | min | 1139:228 | · |
| Duração da chuva unitária d | "d = 7,5·tc" (impresso) | 1139:228 | · |
| Pe = (P − 0,2S)/(P − 0,8S) e S = 25400 − 254·CN / CN (impressos) | mm | 1139:227 | · |
| Qp = 2·A/Tb (impresso, sem constante de unidade) | — | 1139:227 | · |
| Estrada de serviço: 6,0 m de largura nas bermas de cada lado; 8,0 m nas adutoras de sifão; piçarra | m | 1139:253 | · |

## Método do projetista
Racional (Q = C·I·A) para < 3,5 km²; hidrograma unitário triangular com convolução de hidrogramas parciais para > 3,5 km² (Figura 4.54). Obras-padrão DNIT: bueiros tubulares (BSTC 0,8 e 1,0 m, BDTC, BTTC), celulares (BSCC), celulares especiais de múltiplas células 3×(3,0×3,0 m) (mais econômicos que sifão invertido), passagens molhadas (1139:239, 250, 255). Princípio: não concentrar vazões nem transpor bacias (1139:226).

## Resultado
Distribuição dos bueiros do Quadro 4.25 (1139:250): BSTC 0,8 m 271 (60,5 %); BSTC 1,0 m 51 (11,4 %); BDTC 1,0 m 40 (8,9 %); BTTC 1,0 m 24 (5,4 %); BSCC 1,0×1,0 m 2. Vazões por bacia: Quadros 4.20 a 4.23, não lidos.

## Gabarito candidato (pendente de ✓h)
Regra de seleção: A < 3,5 km² usa racional com C = 0,40; A ≥ 3,5 km² usa HUT com CN = 85, TR 100. Contagem: 106 + 91 + 99 + 132 = 428; 6 + 4 + 7 + 3 = 20; 428/448 = 95,5 % (conferido, B).

## Rastro
A: todos os valores da tabela. B: somas e percentuais acima. C: leitura de "d = 7,5·tc" como relação invertida (abaixo).

## Divergências
1. Limite do racional por projeto: Xingó 2 km² (1419:62), CAC 3,5 km², Baixio 100 ha, Iuiu 350 ha (casos já existentes). Nenhum dos limites é derivado de tc ou de C: é regra de prática. O agente deve citar o limite do projeto, não impor um.
2. C: 0,20 para 0,40 e CN: 65 para 85 em um só salto, justificados por "energia das lâminas" vistas em campo (1139:227). Sem série de vazões observadas para calibrar. Quem usar o CAC como referência deve tratar C 0,40 e CN 85 como calibração local do semiárido cearense, não como valor de livro (CN 85 é alto; conferir contra a tabela NRCS antes de generalizar).
3. "d = 7,5·tc" (1139:228): com tp = d/2 + 0,6·tc daria tp = 4,35·tc, absurdo. A relação padrão do SCS é D = tc/7,5 (= 0,133·tc), que dá tp ≈ 0,667·tc. Hipótese C: o texto inverteu a razão. Verificar no PDF.
4. "Pe = (P − 0,2S)/(P − 0,8S)" (1139:227): a forma correta é Pe = (P − 0,2S)²/(P + 0,8S). O texto extraído mostra sinal "−" no denominador e sem expoente 2; pode ser perda de formatação da extração. Verificar no PDF antes de afirmar erro do projeto.
5. "Qp = 2·A/Tb": sem a constante de conversão de unidades (A em km², P em mm, Tb em min); a fórmula não é executável como está. Unidade de Qp: "m³/s" sem "/mm".
6. Kirpich modificada 85,5 = 1,5 × 57 (Kirpich em minutos, L em km, H em m). A calculadora `hidrologia.py` deve ter o fator 1,5 (pendência já registrada em PENDENCIAS §2). Em 1128:106 (EE Castanhão) a Kirpich é a original (L/0,3048, pés).
7. Para comparação, o mesmo projeto usa tc mínimo de 5 min nas valas da EE (1128:106) e não informa tc mínimo no HUT.

## Fronteira (delegar)
IDF e chuva por TR: clima. Dimensionamento do bueiro (HW/D, controle de entrada): bueiros-e-travessias.

## Teste sugerido (evals)
(a) Entrada A = 2,0 km²: o agente deve dizer "racional no CAC (< 3,5 km²) mas HUT no Xingó (≥ 2 km²)". (b) Dado L = 3,0 km, h = 20 m: tc Kirpich modificada = 85,5·(27/20)^0,385 = 96 min (B, conferir).
