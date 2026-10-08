# Velocidade, folga e TR de canal de drenagem: fontes lado a lado

Páginas = página física do PDF (marcador `<!-- p. N -->`). Conversão: 1 fps = 0,3048 m/s; 1 ft = 0,3048 m. IDs do Hidráulico
(HEC-15, NEH 650, EM-1601, DNIT-DREN, CDV-MANUAL-IRRIG, SRHCE-*, EMBRAPA-DREN-SUP) citados pelo ID dele (D1). Tab. 31 do DNIT
completa, Tab. 34 (n por revestimento) e tensão admissível do HEC-15 já estão em
`../../bueiros-e-travessias/references/velocidades-admissiveis-e-revestimentos.md` (arquivo compartilhado): não repetidas aqui.
Nada abaixo é decisão do pacote: o parecer declara a fonte escolhida e mostra a alternativa.

## 1. Velocidade máxima, tabelas de norma (m/s)

| Material | DNIT Tab. 31 [DNIT-DREN p. 131] | EM-1601 Tab. 2-5 [USACE-EM1601 p. 25] |
|---|---|---|
| Areia fina | 0,30 a 0,40 | 0,61 (2,0 fps) |
| Areia média / grossa | 0,35 a 0,45 | grossa 1,22 (4,0 fps) |
| Cascalho fino | 0,50 a 0,80 | 1,83 (6,0 fps; nota 1: pedra maior que ~20 mm, ver Plates 29-30) |
| Silte | 0,70 a 1,20 | terra silte arenoso 0,61; silte argiloso 1,07 |
| Argila | 0,80 a 1,30 (coloidal 1,30 a 1,80) | 1,83 (6,0 fps) |
| Grama | comum firme 1,50 a 1,80; com solo exposto 0,60 a 1,20 | Bermuda: silte arenoso 1,83, silte argiloso 2,44; Kentucky: 1,52 e 2,13 (talude < 5 %) |
| Concreto de cimento | 4,50 | não tabelado |
| Rocha | não tabelado | má 3,05; arenito mole 2,44; xisto mole 1,07; boa 6,10 |
| Rip-rap, gabião | **sem linha** (a calculadora avisa) | **sem linha** (ver Plates 29-30 do EM-1601; tensão no HEC-15) |

EM-1601 Tab. 2-5 nota 2: manter V < 5,0 fps (1,52 m/s) em canal gramado sem boa cobertura e manutenção [USACE-EM1601 p. 25]. O texto
da p. 25 manda tratar desvio da tabela por experiência de campo ou ensaio e pavimentar o canal cuja V ou tensão excede o admissível.
As duas tabelas divergem até 2 vezes (areia fina 0,30 x 0,61): o padrão do código é a Tab. 31 com o critério "min" (conservador); a
escolha é de critério e vai rotulada (`velocidade_admissivel(fonte="dnit"|"em1601", criterio="min"|"max")`).
`../../bueiros-e-travessias/references/` traz ainda a tabela do DAEE-IT-DPO11 p. 4 (terra 1,5; gabião 2,5; pedra argamassada 3,0;
concreto 4,0), com âmbito SP.

## 2. Velocidade máxima, outras fontes e projetos

| Fonte | Valor | Uso |
|---|---|---|
| PISF Trecho II [SRHCE-GED-030 p. 20, §6.2.3] | terra sem revestimento 0,70; concreto ou rocha alterada 3,00; rocha sã 4,50; até 5,00 em declividade alta com deflúvio crítico, TR 100 | drenos do PISF |
| PISF [SRHCE-GED-018 p. 27, Quadro 4.2] | solos arenosos 0,8; argilosos compactos 1,0; argilosos duros 1,2; cascalho grosso 1,5; rochas brandas 1,8; grama 1,5 (erodível) e 2,1 (resistente); colchão Reno e = 0,17/0,23/0,30 m: 1,8/3,5/4,5; concreto e aço 5,0 | canais; no mesmo documento, canal revestido de concreto limitado a 1,8 (p. 27) |
| Embrapa/CPATSA [EMBRAPA-DREN-SUP p. 7, §3.5] | V máxima não erosiva 0,5 para solo franco-arenoso e argilo-arenoso; o projeto calculou 0,42 a 2,3 m/s (descarga máxima) e aceitou a ultrapassagem eventual, com Fr máximo 0,89 | drenos de pivô central, Petrolina 1984 |
| USBR, Manual de Irrigação [CDV-MANUAL-IRRIG p. 515, §11.3.4] | tabela por tipo de solo para dreno em vala aberta; **valores ilegíveis na extração** (dígitos embaralhados): conferir no PDF antes de citar número. Silte não plástico exige análise especial, até tensão trativa | drenos de projeto de irrigação |
| Salitre Etapa 2 | memorial 0,30 a 1,2; planilha 0,3 a 1,5 [1584:105; 1585:97-123] | os dois limites coexistem; `verificar_limites_alternativos` |
| Iuiu 2002 | V <= 0,80 (até 1,00 em trechos) em dreno de terra [1051:321, 334] | critério de projeto |
| Canais de adução (irrigação) | `canais-abertos` do Hidráulico, `references/velocidades-admissiveis.md` (Fortier-Scobey, Kennedy, concreto 1,8 a 2,4) | **não aplicar a dreno**; aqui só como contraste |

## 3. Velocidade mínima (anti-sedimentação)

- NRCS CPS 608: "sem informação local, V mínima de projeto = 1,4 fps" = **0,43 m/s**; máxima ou tensão "com base nas condições locais"; V de canal novo com área > 1 mi² (2,59 km²)
  atende o CPS 582, não aberto [NRCS-CPS608-2023 p. 2]. Aplica-se a dreno principal e lateral de terra agrícola.
- Salitre: piso 0,30 [1584:105]. Delmiro: o memorial cita "velocidade mínima" sem valor [1520:129]; 10 trechos da planilha têm V < 0,5, com mínimo 0,292 [1521:171, 156, 163, 177]. Embrapa: declividade
  adequada 0,2 a 0,5 % [EMBRAPA-DREN-SUP p. 7, §3.4].
- A calculadora não tem padrão de V mínima: `verificar_velocidade(V, V_max, V_min=None)` avisa que a verificação de sedimentação não foi feita. Pedir o valor ao projetista; se não houver, mostrar 0,43 m/s do CPS 608
  como alternativa rotulada (fonte americana de dreno agrícola, não é norma brasileira).

## 4. Folga e borda livre, alternativas com fonte (m)

O código usa **25 % do tirante** (padrão provisório, decisão F7), origem: memorial de Delmiro [1520:129], não é norma. Aplicado a três tirantes do acervo:

| Critério | Fórmula ou valor | DS-1.1/C Delmiro (y = 0,432; Q 0,518) | DS-4.1/A Salitre (y = 1,492; Q 113) |
|---|---|---|---|
| 25 % do tirante (provisório) | 0,25 y | 0,108 | 0,373 |
| NRCS CPS 608 | folga calculada ou **mínimo 0,5 ft = 0,15 m** acima do nível de projeto [NRCS-CPS608-2023 p. 2] | 0,15 | 0,15 |
| HEC-15 | canal permanente de beira de estrada ~0,15 m; transitório pode ser nulo; declive forte: folga = tirante [FHWA-HEC15 p. 34, §2.3.4] | 0,15 | 0,15 (declive suave) |
| NEH 650-9, Tab. 9-1 (desvio) | nenhuma / 0,3 ft (0,09 m) / 0,5 ft (0,15 m) conforme o uso protegido [NRCS-NEH650-CH09 p. 16] | 0 a 0,15 | 0 a 0,15 |
| EMBRAPA-DREN-SUP | 0,20 m acima da lâmina máxima [p. 7, §3.3] | 0,20 | 0,20 |
| PISF, USBR por vazão [SRHCE-GED-030 p. 20, §6.2.4]; log = log10 | Q <= 1: 0,15; 1 a 3: 0,12 log Q + 0,15; 3 a 10: 0,23 log Q + 0,10; 10 a 40: 0,34 log Q - 0,01; 40 a 600: 0,36 log Q - 0,05; depois arredondar a múltiplo de 25 cm de profundidade | 0,15 | 0,69 |
| EM-1601, canal de controle de cheia | 2 ft (0,61 m) em seção retangular e 2,5 ft (0,76 m) em trapezoidal de concreto; 2,5 ft em rip-rap; 3 ft em dique de terra; reduz se o topo está abaixo do terreno; "não há fórmula única" [USACE-EM1601 p. 23, §2-6a] | 0,76 (ordem de grandeza; escala de rio) | 0,76 |

Leitura: a folga adotada na planilha de Delmiro (0,02 m em DS-1.1/C, [1521:120]) fica abaixo de **todas** as alternativas; a de Salitre DS-4.1/A é 0,008 m (h = 1,50 m para y = 1,492; planilha não preenche a coluna de borda livre).
O 25 % não é o mais exigente nem o mais frouxo; o parecer lista as alternativas e o que muda na altura da seção. Para canal de adução a borda livre é de `canais-abertos` (USBR, Lencastre, Codevasf, CDV D-31).

## 5. TR de projeto de canal de drenagem, alternativas com fonte

| Fonte | TR | Aplicação |
|---|---|---|
| USBR, Manual de Irrigação [CDV-MANUAL-IRRIG p. 514-515, §11.3.3] | **5 anos** para a maioria dos sistemas de drenagem de irrigação; drenos de proteção e travessias de canal com TR maior, mesma freqüência para ambos; **25 anos** nos grandes sistemas de canais (inclusive borda livre do dique); estudo com 100 anos onde o transbordamento seria grave | dreno em perímetro irrigado |
| NRCS NEH 650-9, Tab. 9-1 [NRCS-NEH650-CH09 p. 16] | chuva de 24 h. Temporário: 2 anos (obra), 5 (canteiro), 10 (terra agrícola). Permanente: 10 (recreação, recuperação de mina), 25 (edificação agrícola, abatimento de poluição), 50 (área urbana, indústria) | desvio e interceptação |
| FHWA HEC-15 [FHWA-HEC15 p. 33-34, §2.3.1] | revestimento permanente de beira de estrada: 5 ou 10 anos; transitório: ~2 anos | canal lateral de estrada |
| FHWA HEC-11 [FHWA-HEC11 p. 37, §3.1] | 10 a 50 anos para rip-rap de obra viária; avaliar também vazões menores, que podem ser piores para a estabilidade | revestimento de pedra |
| Acervo | Salitre: crítica de 24 h TR 10, verifica cheia com TR 50 [1584:102]; Delmiro: TR 10 por igualdade de coeficientes da IDF, **não declarado** [1520:127; 1521:120]; Sertão Pernambucano: TR 100 nos drenos laterais ao adutor [1390:429]; PISF: TR 100 [SRHCE-GED-030 p. 20]; Xingó: TR 10 em valeta de proteção (caso `xingo_lote1_valetas_protecao_comprimento_critico`) | projetos |

TR de canal é decisão de critério (consequência da falha, tipo de obra), não de fórmula. Mostrar TR **e** risco `hidrologia.risco_hidrologico` (núcleo, seção 1). O ponto aberto da F7 é o TR de **bueiro**
(`bueiros-e-travessias`); a regra de TR de canal vem do projeto ou do cartão.
