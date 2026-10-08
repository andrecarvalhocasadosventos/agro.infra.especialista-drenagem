# Retroanálise canal retangular em gabião x tubo circular (planilha local do André, Manning com faixa de n)
fonte: `G:\Meu Drive\DRENAGEM\01. ESTUDOS\RETROANÁLISE CANAL GABIÃO.xlsx` (fonte local D8, não é projeto de terceiros nem do acervo), aba Planilha1, lida com openpyxl (fórmulas e valores em cache), arquivo de 04/2023
disciplinas: [canais-de-drenagem-e-macrodrenagem, hidraulica-de-canais-de-drenagem]
nivel: estudo interno (sem projeto de origem identificado)
tipo: positivo (cálculo reproduzível); com ressalvas de rótulo e de critério listadas abaixo
qualidade: B (a planilha é limpa e reproduz, mas não diz de que obra vem, qual a vazão a escoar nem a conclusão)

## Problema
Comparar a capacidade de um canal retangular revestido em gabião (1,59 m de largura, 1,00 m de altura) com a de um tubo circular de DN 1000 mm, para ver em que parte da incerteza do coeficiente de Manning o tubo escoa mais que o canal. Objetivo da retroanálise e local da obra: não informado no arquivo.

## Dados de entrada (célula, valor)
| grandeza | valor | célula | anc. |
|---|---|---|---|
| largura do canal | 1,59 m | B2 | A |
| altura do canal | 1,00 m | B3 | A |
| lâmina d'água no canal | 80 % da altura (0,80 m) | B4, B5 | A |
| declividade | 0,003 (rótulo "declividade (%)", usada como m/m na fórmula) | B6, B17 | A |
| n do canal | 0,035 no caso-base; faixa 0,02 a 0,035 (Gabião) | B7, D6:D8 | A |
| diâmetro do tubo | 1,00 m | B11 | A |
| lâmina no tubo | 85 % de D | B12 | A |
| n do tubo | 0,010 no caso-base; faixa PEAD 0,009 a 0,011; concreto 0,011 a 0,015 | B18, D17:E19 | A |

## Método
Manning para canal retangular: Q = A·R^(2/3)·√I / n, com A = B·y e R = A/(B + 2y) (função nomeada VAZAO_CANAL). Para o tubo parcialmente cheio: α = asin(2·y/D − 1); A = (π + 2α)·D²/8 + D²·cosα·sinα/4; P = (π + 2α)·D/2; R = A/P; Q = A·R^(2/3)·√I / n (VAZAO_TUBO). Duas grades de 21 x 21 (n do canal de 0,02 a 0,035 em 21 passos; n do tubo em 21 passos de 0,009 a 0,011 para PEAD e de 0,011 a 0,015 para concreto) avaliam a condição "Q do canal < Q do tubo" em cada célula e contam a fração verdadeira (H23 e H48).

## Resultado e gabarito (valores em cache; reconferidos em B por Manning)
- Canal, caso-base (B8): Q = 1,0784 m³/s (A 1,272 m²; P 3,19 m; R 0,3988 m; V 0,848 m/s em B).
- Tubo, caso-base: α = 0,7754 rad (B13); P = 2,3462 m (B14); A = 0,7115 m² (B15); R = 0,3033 m (B16); Q = 1,7591 m³/s (B19); V 2,47 m/s em B.
- Fração das combinações de n em que o tubo de PEAD escoa mais que o canal: 0,8844 = 390/441 (H23).
- Fração com tubo de concreto: 0,4762 = 210/441 (H48).
Gabarito para a calculadora: com os dados da tabela de entrada, `manning_retangular` deve devolver 1,0784 m³/s e `manning_circular_parcial` 1,7591 m³/s (tolerância 0,5 %); a fração da grade deve voltar 390/441 e 210/441 para as mesmas faixas.

## Rastro
A: dados de entrada, fórmulas e valores em cache. B: reprodução de Manning e das contagens. C: propósito da planilha (inferido pelo nome e pela estrutura).

## Divergências e armadilhas
1. Rótulo "declividade (%)" com valor 0,003, usado como m/m (0,3 %): quem lê o rótulo erra por 100. Mesmo tipo de erro já registrado no Iuiu (0,5 % x 5 %); vale como caso de teste de unidade.
2. Lâminas diferentes nos dois lados (80 % da altura contra 85 % de D): a comparação favorece o tubo. Com lâmina igual, o resultado das frações muda; a planilha não mostra isso.
3. Caso-base com n do tubo 0,010, que fica fora da faixa do concreto (0,011 a 0,015) e dentro da faixa do PEAD, e n do canal 0,035, extremo superior da faixa, que é o mais desfavorável ao canal.
4. As frações 88 % e 48 % são proporção da grade uniforme, não probabilidade de o tubo ser melhor.
5. Faltam verificações que o parecer precisa: velocidade (canal 0,85 m/s, tubo 2,47 m/s), Froude, folga/borda livre, capacidade a seção plena do tubo, controle de entrada e vazão de projeto a escoar.

## Marcas de ancoragem
Fonte local D8, não passa pelo catálogo do acervo; sem marcas `!`/`~`/`✓*`. Nenhum `✓h`. Os valores em cache dependem de o Excel ter recalculado a última vez (as funções são LAMBDA nomeadas; confirmei por Manning independente).

## Fronteira
Escolha de gabião x tubo e custo são de Orçamento/Hidráulica; a estabilidade do gabião e da escavação é de Geotecnia.
