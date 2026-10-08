# Delmiro Gouveia (CODEVASF 2016, Hydros) — NERC chamado "Kirpich", velocidade em km/h sob "m/s" e declividade BH4.5 incoerente
fonte: doc 1494 pp. 31, 64; doc 1492 pp. 141-142 (Quadro 3.50), 155
disciplinas: [hidrologia-de-projeto-para-drenagem]
nivel: basico
tipo: NEGATIVO (3 inconsistências verificáveis; nenhuma muda a vazão adotada do BHD1, uma invalida o teste de aceitação do Tc)
qualidade: A (as três reproduzidas por cálculo independente)
marcas: `·` = lido por `ler`, texto nativo; sem linhas em `parametros`. Nenhum `✓h`.

## Problema
Os Tc e as declividades do HUT de Delmiro Gouveia servem de gabarito? Onde o memorial se contradiz?

## Dados (BHD1 TR 50, 1494:64)
L = 13,21 km; A = 36,34 km²; desnível 32,00 m. Planilha: "Kyrpich" tc = 7,65 h, vel 1,73; "Bransby Williams" tc = 7,53 h, vel 1,75; adotado 7,53 h, vel 0,49.
Texto: 1494:31 chama a primeira fórmula de Kirpich; 1492:155 chama o mesmo par de "NERC (1975, apud Watkins e Fiddes, 1984)" e "Bransby-Williams". Critério de aceitação: velocidade de translação entre 0,5 e 2,00 m/s (1492:155).
Quadro 3.50 (1492:141-142): 58 sub-bacias do sistema viário com área, comprimento, cotas, declividade e CN.

## Erro 1: rótulo do Tc (B)
Kirpich (0,0663·L^0,77·S^−0,385, L em km, S em m/m) dá 4,92 h para L 13,21 km e S = 32/13210 = 0,00242. O valor impresso 7,65 h é reproduzido por `tc = 2,8·(L/√(H/L))^0,47` = 7,650 h (L em km, H/L em m/km), a forma do NERC. O rótulo "Kirpich" de 1494:31 está errado; o Memorial (1492:155) está certo. O Vol. 3 também diz "H é a declividade em m", ambíguo. Quem implementar o "Kirpich do Delmiro Gouveia" com a fórmula de livro obtém 4,92 h, não 7,65 h.

## Erro 2: velocidade em km/h sob rótulo m/s (B)
13,21 km / 7,65 h = 1,727 km/h e 13,21 / 7,53 = 1,754 km/h: são os 1,73 e 1,75 impressos, em km/h. Em m/s: 0,480 (NERC) e 0,487 (B-W); a linha "adotado" imprime 0,49 m/s (confere). Pelo critério 0,5 a 2,0 m/s do próprio memorial, os dois Tc ficam abaixo de 0,5 m/s e só passariam se a coluna fosse lida (erradamente) como 1,73 e 1,75 m/s. O critério foi aplicado com o número na unidade errada. Efeito na vazão do BHD1: pequeno; efeito no processo: o teste de aceitação não funciona como descrito.

## Erro 3: declividade de BH4.5 (B)
Quadro 3.50, ordem 40 (1492:142): BH4.5, A 3,143 km², L 3252,5 m, cota montante 250,00 m, cota jusante 236,00 m, declividade impressa 0,0618 m/m. As cotas e o comprimento dão (250 − 236)/3252,5 = 0,0043 m/m (razão 14,4). As outras 57 linhas conferem dentro de 5 % entre (cota montante − cota jusante)/L e a declividade impressa. Se 0,0618 alimentou o Tc de BH4.5, o Tc saiu curto demais e a vazão ficou superestimada (a favor da segurança); não rastreado, porque a planilha de BH4.5 não foi lida.
Teste que revela: recalcular S = ΔH/L para cada linha do Quadro 3.50 e sinalizar |razão − 1| > 5 %.

## Gabarito
Nenhum para vazão. Números para testes negativos: (a) NERC(13,21 km; 32 m) = 7,65 h, diferente do Kirpich 4,92 h; (b) v = L/tc = 0,49 m/s, abaixo do mínimo de 0,5 m/s; (c) S(BH4.5) = 0,0043 m/m, não 0,0618.

## Rastro
A: valores impressos (1494:64; 1492:141-142). B: todos os recálculos acima. C: a hipótese de que 0,0618 alimentou o Tc de BH4.5.

## Fronteira
Chuva e IDF: clima. Fórmulas de Tc de literatura (Kirpich, NERC, B-W): hidrologia-de-projeto-para-drenagem; a pendência da `hidrologia.py` sobre Kirpich continua aberta (PENDENCIAS §2).
