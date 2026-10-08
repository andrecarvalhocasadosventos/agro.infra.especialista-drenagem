# Canal do Sertão Pernambucano — 204 canais de drenagem laterais ao adutor (TR 100, concreto simples, seções-padrão ST)
fonte: Relatório final, anteprojeto 2014, Tomo I Texto (doc 1390):429-440 (Quadros 8.12 e 8.13) — Projeto Sertão Pernambucano
disciplinas: [canais-de-drenagem-e-macrodrenagem, interceptacao-de-talvegues]
nivel: anteprojeto
tipo: positivo (inventário e critério; sem memória hidráulica no trecho lido)
qualidade: B (totais e padrões reproduzem; vazão, declividade e velocidade por dreno não aparecem no trecho lido)

## Problema
Interceptar e conduzir as águas de chuva paralelamente ao eixo do sistema adutor (canais CP-I a CP-XVIII, EB-1 a reservatório Volta), lançando-as em bueiros sob o canal, talvegues naturais, cursos d'água ou reservatórios, e fixar as seções-padrão e o afastamento em relação ao canal. É a referência para o problema "talvegues interceptados pela faixa do canal de adução".

## Dados de entrada
| grandeza | valor | un. | fonte | anc. |
|---|---|---|---|---|
| vazão de projeto | deflúvio crítico de TR 100 anos, de curvas área x vazão do Estudo de Viabilidade e do Projeto Básico do Trecho Inicial | anos | 1390:429 | A |
| quantidade | 204 canais, 162,464 km; 87 drenos iniciais (EB-1 a reservatório Rajada) vindos do Projeto Básico do Trecho Inicial | — | 1390:431 | A |
| revestimento | concreto simples em todos os drenos (manutenção, erosão) | — | 1390:430 | A |
| geometria | trapezoidal, talude 1V:1H; 13 seções-padrão ST (base x altura): 40x50, 60x50, 60x80, 60x100, 60x120, 60x150, 80x80, 80x100, 80x120, 80x150, 100x80, 100x150, 100x200 (cm) | cm | 1390:430 (Quadro 8.12) | A |
| afastamento | mínimo de 6,00 m entre a borda do dreno e o offset do canal adutor | m | 1390:430 | A |
| transições | diedro, ângulo de convergência/divergência de 30° | — | 1390:431 | A |
| velocidade | "velocidade crítica" citada como critério, sem valor | — | 1390:431 | A (não informado) |

## Método do projetista
Padrões de seção pré-definidos e aplicados caso a caso: escolhe-se o padrão de capacidade compatível com a vazão de projeto e ajusta-se a declividade e a profundidade da linha de fundo para respeitar o critério hidráulico (velocidade crítica) (1390:431). Em pequenos vales previu-se aterro para evitar obra de travessia. Deságue em talvegue natural, curso d'água, reservatório ou a montante/jusante de bueiro BU-nn (Quadro 8.13, 1390:431-440).

## Resultado e gabarito
Quadro 8.13: cada dreno tem canal, margem, estaca inicial e final, extensão, base, altura e local de deságue. Leitura do quadro (B; 311 trechos, porque os drenos são divididos em a, b, c quando a seção muda):
- soma das extensões = 162.464,0 m, igual ao "162,464 km" do texto (1390:431);
- 204 drenos numerados de D-001 a D-204, sem lacunas nem repetições; 107 trechos intermediários sem deságue e 204 com deságue (135 a montante de BU, 15 a jusante de BU, 26 em talvegue natural, 23 em reservatório ou outro, 5 em curso d'água);
- uso das seções (trechos): 60x50 157; 40x50 69; 60x80 37; 60x100 20; 80x120 9; 100x150 4; 60x120 3; 60x150 3; 80x100 3; 80x150 2; 80x80 2; 100x80 1; 100x200 1; todas pertencem ao Quadro 8.12;
- exemplos: D-056 (CP-V, margem direita, 24+310 a 24+008, 292,0 m, 0,60 x 0,50, deságue a montante de BU-17); D-085 (CP-VIII, margem esquerda, 40+810 a 41+130, 325,0 m, 0,60 x 0,50, deságue em reservatório Baixa/Lago); D-108a/b/c (CP-XIV, 945, 670 e 1.425 m, seções 60x50, 60x100 e 80x120, deságue a montante de BU-33).
Gabarito para a calculadora: validação cruzada, não vazão. Dado Q e declividade, a calculadora escolhe a menor seção ST do Quadro 8.12 que escoa Q com V ≤ V_crítica informada pelo usuário; não há Q nem declividade no trecho lido para reproduzir o padrão escolhido (não informado).

## Rastro
A: critérios, padrões, totais declarados e quadros. B: somas, contagens e uso por seção. C: extensão do dreno difere do desnível de estaca em alguns trechos (p. ex. D-001: 192 m para 85 m de estaca; D-037c: 264 m para 128 m; 8 trechos com diferença acima de 60 m e 15 %), plausível por desvio em planta, mas não explicado.

## Divergências
Nenhuma divergência de total. O texto não traz a velocidade crítica nem as declividades; o Quadro 8.13 não traz vazão. A planta 787-CDVF-CSP-SD-010 (seções típicas) e as plantas SD-001 a 009 (layout) não foram abertas.

## Marcas de ancoragem
Valores lidos direto das páginas (texto nativo, sem marca `!`, `~` ou `✓*`). Nenhum `✓h`. Na extração, canal, margem e estacas aparecem coladas numa só linha em parte das linhas (sobretudo CP-XIII a CP-XVII); a leitura por expressão regular fechou todas as 311 linhas, mas confira a página aberta antes de citar um trecho.

## Fronteira
Bueiros BU-01 a BU-69 deste anteprojeto (tabela 1390:428-429, com 66,751 m³/s no BU-19, valor fora da faixa dos demais) são do lote L3; vazão por curva área x vazão TR 100 é de Hidrologia.
