# Delmiro Gouveia — seção de dreno subdimensionada e folga abaixo do critério (caso NEGATIVO)
fonte: Memória de cálculo hidráulico (doc 1521, duplicata 1493):120-187 e Memorial descritivo (doc 1520, duplicata 1492):129-137 — Projeto de Irrigação Delmiro Gouveia, CODEVASF 2016, executivo (Hydros)
disciplinas: [canais-de-drenagem-e-macrodrenagem, conferencia-de-memorial]
nivel: projeto executivo
tipo: negativo (erro de seleção de seção que a própria planilha acusa; critério de folga contradito pelas linhas; erros de nomenclatura nos quadros)
qualidade: B (contagens sobre texto extraído das 194 linhas; os itens D1 e D3 são A)

## Problema
A conferência de um memorial deve cruzar, linha a linha, o tirante de Manning com a altura da seção escolhida e a folga adotada com o critério declarado. O caso mostra onde a planilha de Delmiro Gouveia reprova nessas duas conferências. Complementa `2026-10-08_delmiro_gouveia_drenos_lotes_racional_manning.md`.

## Itens

### D1 — seção ZTT01 menor que o tirante (A)
DT-2.23.1 (1521:165; Quadro 3.46 em 1520:134, linha 139): A = 2,83 ha, Q = 0,120 m³/s, seção ZTT01 (b 0,20 m, h 0,20 m, 1:1, área cheia 0,080 m²). Na planilha: Io 0,00352, tirante calculado 0,331 m, área molhada 0,176 m², V 0,684 m/s, folga recomendada 0,083 m e folga adotada −0,131 m. O tirante é 65 % maior que a altura do dreno: com Q 0,120 o dreno transborda no trecho, e a planilha imprime o sinal negativo sem tratamento. O ramo vizinho DS-2.23/A (1521:165), com a mesma área de 2,83 ha e Q 0,131, usa ZTT02 e passa (folga adotada 0,048 m). O Quadro 3.46 e o memorial repetem ZTT01 sem comentário.
Variante marginal: DS-3.1/A (1521:173), ZTT01, tirante 0,201 m contra altura 0,20 m, folga adotada −0,001 m (arredondamento, mas ainda negativa).
Teste: tirante ≤ altura da seção em todos os trechos. Em 194 trechos, só esses dois falham (B).

### D2 — folga adotada abaixo do critério em 43 % dos trechos (B)
Memorial (1520:129): "A folga mínima foi fixada em 25 % do tirante hidráulico. Entre as seções são admitidas folgas menores e, até transbordamentos localizados cuja permanência é estimada inferior a 4 horas". Também diz que a folga foi verificada só nas seções de montante e de jusante.
Planilha (1521:120-187): cada trecho tem um tirante e uma altura (a mesma na seção de montante e na de jusante), então a exceção "entre seções" não se aplica: em 84 de 194 trechos a folga adotada é menor que a recomendada (diferença maior que 5 mm). Exemplo: DS-1.1/C (1521:120) tirante 0,43, recomendada 0,11, adotada 0,02 m; DS-1.2/C (1521:122) 0,181 contra 0,026 m; DT-1.2.2/D 0,159 contra 0,113 m.
Interpretação (C): o projetista adotou a seção padrão do Quadro 3.45 imediatamente superior ao tirante, sem aumentá-la quando faltava folga. O texto admite isso como "folga menor", mas sem registrar quanto e onde. Teste: folga adotada ≥ 25 % do tirante, com contagem e lista dos trechos que falham e justificativa pedida.

### D3 — Quadro 3.47: nomes duplicados e trocados (A)
Em 1520:136-137: "DT-2.10.1" aparece duas vezes (333,00 m e 482,5 m; o Quadro 3.46 tem DT-2.10.1 A/B e DT-2.10.3 A/B/C, e o segundo item deveria ser o DT-2.10.3); 9 itens (53 a 55, 57, 58, 61, 63, 66 e 67) usam prefixos "DT-1.21.x", "DT-1.22.x", "DT-1.23.x", "DT-1.24.x", "DT-1.26.x" onde o Quadro 3.46 e a planilha usam "DT-2.21.x" a "DT-2.26.x". A soma dos 86 itens é 37.569,13 m e bate com o TOTAL do quadro (B): o erro é de nome, não de extensão.
Teste: chave única por dreno e conciliação entre quadros por nome.

### D4 — velocidade mínima citada sem valor (A)
O memorial (1520:129) fala em "velocidade mínima" como motivo de aprofundamento, mas não dá o valor. A planilha tem 10 trechos com V < 0,5 m/s (DT-2.26.2 0,292 m/s com Io 0,0004; DT-2.10.2 0,364; DT-2.22.1/A 0,361; DS-3.3/A 0,44; páginas 1521:171, 156, 163, 177) em solo arenoso. Critério "não informado": a calculadora deve pedir o valor, não presumir.

## Dados de entrada e marcas
Valores lidos direto das páginas (texto nativo, sem marca `!`, `~` ou `✓*`); contagens são B. Nenhum `✓h`. D1 e D3 devem ser conferidos nas páginas por uma pessoa antes de virar caso de teste.

## O que a calculadora e o parecer devem fazer
Para cada trecho: tirante de Manning na seção adotada, folga e comparação com 25 % do tirante; falhar quando a folga for negativa; reportar o percentual de trechos fora do critério em vez de aceitar a frase "folgas menores são admitidas".

## Fronteira
Hidrologia dos lotes (Racional, IDF) é do caso positivo; classe e enrocamento das quedas não foram lidos aqui.
