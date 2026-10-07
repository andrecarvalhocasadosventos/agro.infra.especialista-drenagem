# Constantes de controle de entrada, Ke e rugosidade (HDS-5, 3ª ed. 2012)

Fonte primária: `[FHWA-HDS5]` (FHWA-HIF-12-026, abril de 2012; domínio público). Páginas = marcador `<!-- p. N -->` do
`_texto` (página física do PDF). Tudo conferido no `_texto` em 2026-10-01, exceto onde indicado.

## 1. Equações e unidades

| Item | Forma | Página |
|---|---|---|
| Forma 1 (não submersa) | HW/D = Hc/D + K X^M + Ks S | [HDS5 p. 190, eq. A.1] |
| Forma 2 (não submersa) | HW/D = K X^M | [HDS5 p. 191, eq. A.2] |
| Submersa | HW/D = c X² + Y + Ks S | [HDS5 p. 191, eq. A.3] |
| Fator de vazão | X = Ku Q/(A D^0,5) | [HDS5 p. 191] |
| Ku | 1,0 (pés, cfs) ou **1,811 (SI)** | [HDS5 p. 191] |
| Ks | −0,5 (entradas não mitradas); **+0,7 (mitrada)** | [HDS5 p. 191] |
| Hc | carga específica no calado crítico, dc + Vc²/2g (m) | [HDS5 p. 191] |
| Validade não submersa | até Q/(A D^0,5) ≈ 3,5 (1,93 em SI, sem Ku), ou seja X ≤ 3,5 | [HDS5 p. 190] |
| Validade submersa | a partir de Q/(A D^0,5) ≈ 4,0 (2,21 SI), ou seja X ≥ 4,0 | [HDS5 p. 191] |
| Transição | curva tangente às duas; só há informação limitada (NBS) | [HDS5 p. 190, 86] |
| Perda de atrito, controle de saída | Hf = (Ku n² L / R^1,33) V²/2g, **Ku = 19,63 (SI)** (29 em pés) | [HDS5 p. 92, eq. 3.4b] |

Notas de uso:
- A = área plena do barril; D = altura interna (diâmetro no circular, altura no celular). HW é medido acima da geratriz
  inferior (invert) da seção de controle de entrada.
- Os nomogramas do HDS-5 usam S = 2 %; isso baixa o HW em 0,01 D. A calculadora usa a declividade real [HDS5 p. 85].
  Para declividade nula, somar 0,01 ao HW/D (0,014 a subtrair no mitrado); adversa: somar também 0,5 S (mitrado: subtrair
  0,7 S). Não usar se a saída estiver mais de D/2 acima da entrada [HDS5 p. 107, §3.3.4].
- Coeficientes de caixa (retangular) não valem para formas não retangulares e vice-versa [HDS5 p. 191, §A.3].
- Forma sem constantes: usar as curvas adimensionais do Chart 51 (circular e elíptico) ou 52 (arcos longos) [HDS5 p. 194,
  §A.3.2]; na calculadora o `arco` usa elipse e avisa.
- Precisão do método: HW com ±10 % [HDS5 p. 83, §3.1.1]. Esse é o piso de incerteza de qualquer comparação.
- Conferência cruzada: HDS-5 Tabela A.1 impressa na p. 197 do PDF; a `bueiros.py` cita "p.197 do arquivo" em
  `DIVERGENCIAS_bueiros.md` (mesma página).

## 2. Tabela A.1: círculos, caixas e entradas afuniladas [HDS5 p. 197]

Forma da equação: 1 ou 2. Ke = coeficiente de perda de entrada da Tabela C.2 para a mesma configuração [HDS5 p. 216].
"Chave" = nome em `tools/hid/bueiros.py::ENTRADAS`; "—" = não implementada (usar a linha mais próxima, rotulada, ou HY-8).

| Chart/escala | Forma e material | Configuração de entrada | Eq. | K | M | c | Y | Ke | Chave |
|---|---|---|---|---|---|---|---|---|---|
| 1/1 | circular concreto | aresta viva com muro de testa | 1 | 0,0098 | 2,0 | 0,0398 | 0,67 | 0,5 | `circ_concreto_aresta_viva_muro` |
| 1/2 | circular concreto | ponta-e-bolsa (groove) com muro de testa | 1 | 0,0018 | 2,0 | 0,0292 | 0,74 | 0,2 | `circ_concreto_boca_sino_muro` |
| 1/3 | circular concreto | ponta-e-bolsa projetante | 1 | 0,0045 | 2,0 | 0,0317 | 0,69 | 0,2 | `circ_concreto_boca_sino_projetante` |
| 2/1 | circular metálico corrugado | muro de testa | 1 | 0,0078 | 2,0 | 0,0379 | 0,69 | 0,5 | `circ_corrugado_muro` |
| 2/2 | circular metálico corrugado | mitrada ao talude | 1 | 0,0210 | 1,33 | 0,0463 | 0,75 | 0,7 | `circ_corrugado_mitrado` (Ks = +0,7) |
| 2/3 | circular metálico corrugado | projetante | 1 | 0,0340 | 1,50 | 0,0553 | 0,54 | 0,9 | `circ_corrugado_projetante` |
| 3/A | circular | anel biselado 45° | 1 | 0,0018 | 2,50 | 0,0300 | 0,74 | 0,2 | `circ_bisel_45` |
| 3/B | circular | anel biselado 33,7° | 1 | 0,0018 | 2,50 | 0,0243 | 0,83 | 0,2 | `circ_bisel_33_7` |
| 8/1 | caixa de concreto | alas a 30° a 75° | 1 | 0,026 | 1,0 | 0,0347 | 0,81 | 0,4 (topo com aresta viva) | `ret_alas_30_75` |
| 8/2 | caixa de concreto | alas a 90° e 15° | 1 | 0,061 | 0,75 | 0,0400 | 0,80 | 0,5 | `ret_alas_90_15` |
| 8/3 | caixa de concreto | alas a 0° (paralelas) | 1 | 0,061 | 0,75 | 0,0423 | 0,82 | 0,7 | `ret_alas_0` |
| 9/1 | caixa de concreto | ala 45°, d = 0,043 D | 2 | 0,510 | 0,667 | 0,0309 | 0,80 | a confirmar (0,2 se topo biselado) | — |
| 9/2 | caixa de concreto | ala 18° a 33,7°, d = 0,083 D | 2 | 0,486 | 0,667 | 0,0249 | 0,83 | a confirmar (0,2 se topo biselado) | — |
| 10/1 | caixa de concreto | muro de testa 90° com chanfro de 3/4" | 2 | 0,515 | 0,667 | 0,0375 | 0,79 | 0,5 (adotado na calculadora: chanfro de 3/4" tratado como aresta viva) | `ret_muro_chanfro_3_4` |
| 10/2 | caixa de concreto | muro de testa 90° com bisel 45° | 2 | 0,495 | 0,667 | 0,0314 | 0,82 | 0,2 | `ret_muro_bisel_45` |
| 10/3 | caixa de concreto | muro de testa 90° com bisel 33,7° | 2 | 0,486 | 0,667 | 0,0252 | 0,865 | 0,2 (biselado em 3 lados) | — |
| 11/1 | caixa de concreto | chanfro 3/4", muro esconso 45° | 2 | 0,545 | 0,667 | 0,04505 | 0,73 | — | — |
| 11/2 | caixa de concreto | chanfro 3/4", muro esconso 30° | 2 | 0,533 | 0,667 | 0,0425 | 0,705 | — | — |
| 11/3 | caixa de concreto | chanfro 3/4", muro esconso 15° | 2 | 0,522 | 0,667 | 0,0402 | 0,68 | — | — |
| 11/4 | caixa de concreto | bisel 45°, muro esconso 10° a 45° | 2 | 0,498 | 0,667 | 0,0327 | 0,75 | — | — |
| 12/1 | caixa chanfro 3/4" | alas 45° sem offset | 2 | 0,497 | 0,667 | 0,0339 | 0,803 | — | — |
| 12/2 | caixa chanfro 3/4" | alas 18,4° sem offset | 2 | 0,493 | 0,667 | 0,0361 | 0,806 | — | — |
| 12/3 | caixa chanfro 3/4" | alas 18,4°, barril esconso 30° | 2 | 0,495 | 0,667 | 0,0386 | 0,71 | — | — |
| 13/1 | caixa, bisel no topo | alas 45° com offset | 2 | 0,497 | 0,667 | 0,0302 | 0,835 | — | — |
| 13/2 | caixa, bisel no topo | alas 33,7° com offset | 2 | 0,495 | 0,667 | 0,0252 | 0,881 | — | — |
| 13/3 | caixa, bisel no topo | alas 18,4° com offset | 2 | 0,493 | 0,667 | 0,0227 | 0,887 | — | — |
| 55/1 | circular | garganta afunilada lisa | 2 | 0,534 | 0,555 | 0,0196 | 0,90 | 0,2 | — |
| 55/2 | circular | garganta afunilada rugosa | 2 | 0,519 | 0,64 | 0,0210 | 0,90 | 0,2 | — |
| 56/1 | face elíptica | afunilada, arestas biseladas | 2 | 0,536 | 0,622 | 0,0368 | 0,83 | 0,2 | — |
| 56/2 | face elíptica | afunilada, arestas vivas | 2 | 0,5035 | 0,719 | 0,0478 | 0,80 | 0,2 | — |
| 56/3 | face elíptica | afunilada, aresta fina projetante | 2 | 0,547 | 0,80 | 0,0598 | 0,75 | 0,2 | — |
| 57/1 | retangular concreto | garganta afunilada | 2 | 0,475 | 0,667 | 0,0179 | 0,97 | 0,2 | — |
| 58/1 | retangular concreto | afunilamento lateral, bordas menos favoráveis | 2 | 0,56 | 0,667 | 0,0446 | 0,85 | 0,2 | — |
| 58/2 | retangular concreto | afunilamento lateral, bordas mais favoráveis | 2 | 0,56 | 0,667 | 0,0378 | 0,87 | 0,2 | — |
| 59/1 | retangular concreto | afunilamento de declividade, menos favoráveis | 2 | 0,50 | 0,667 | 0,0446 | 0,65 | 0,2 | — |
| 59/2 | retangular concreto | afunilamento de declividade, mais favoráveis | 2 | 0,50 | 0,667 | 0,0378 | 0,71 | 0,2 | — |

Observações:
- O subscrito "°" das alas em 8/1 (30 a 75) e 8/2 (90 e 15) é a notação do HDS-5; "alas a 90° e 15°" refere-se a duas
  famílias de alas, não a um único ângulo.
- Entrada afunilada (charts 55 a 59): Ke = 0,2 e as perdas do afunilado entram na seção de controle da garganta
  [HDS5 p. 110 e Tabela C.2 p. 216]. Projeto de afunilado: HDS-5 §3.4 (a calculadora não cobre; delegar à projetista).

## 3. Tabela A.2: formas descontinuadas, ainda usadas (arcos, elipses, caixas metálicas) [HDS5 p. 198]

(O título da tabela diz "Discontinued Charts (see 2005 HDS 5)"; a 3ª ed. mantém as constantes. Fonte original: FHWA 1974 e
Bossy 1963.)

| Chart/escala | Forma | Configuração | Eq. | K | M | c | Y | Chave |
|---|---|---|---|---|---|---|---|---|
| 16-19/2 | caixa metálica | muro de testa 90° | 1 | 0,0083 | 2,0 | 0,0379 | 0,69 | — |
| 16-19/3 | caixa metálica | parede espessa projetante | 1 | 0,0145 | 1,75 | 0,0419 | 0,64 | — |
| 16-19/5 | caixa metálica | parede fina projetante | 1 | 0,0340 | 1,5 | 0,0496 | 0,57 | — |
| 29/1 | elipse horizontal, concreto | aresta viva, muro | 1 | 0,0100 | 2,0 | 0,0398 | 0,67 | — |
| 29/2 | elipse horizontal, concreto | ponta-e-bolsa, muro | 1 | 0,0018 | 2,5 | 0,0292 | 0,74 | — |
| 29/3 | elipse horizontal, concreto | ponta-e-bolsa projetante | 1 | 0,0045 | 2,0 | 0,0317 | 0,69 | — |
| 30/1 | elipse vertical, concreto | aresta viva, muro | 1 | 0,0100 | 2,0 | 0,0398 | 0,67 | — |
| 30/2 | elipse vertical, concreto | ponta-e-bolsa, muro | 1 | 0,0018 | 2,5 | 0,0292 | 0,74 | — |
| 30/3 | elipse vertical, concreto | ponta-e-bolsa projetante | 1 | 0,0095 | 2,0 | 0,0317 | 0,69 | — |
| 34/1 | arco (pipe-arch) 18" CM | muro de testa 90° | 1 | 0,0083 | 2,0 | 0,0379 | 0,69 | `arco_corrugado_muro` |
| 34/2 | arco (pipe-arch) 18" CM | mitrada | 1 | 0,0300 | 1,0 | 0,0463 | 0,75 | — |
| 34/3 | arco (pipe-arch) 18" CM | projetante | 1 | 0,0340 | 1,5 | 0,0496 | 0,57 | `arco_corrugado_projetante` |
| 35/1 | arco 18" CM | projetante | 1 | 0,0300 | 1,5 | 0,0496 | 0,57 | — |
| 35/2 | arco 18" CM | sem bisel | 1 | 0,0088 | 2,0 | 0,0368 | 0,68 | — |
| 35/3 | arco 18" CM | bisel 33,7° | 1 | 0,0030 | 2,0 | 0,0269 | 0,77 | — |
| 36/1 a 36/3 | arco 31" CM | mesmas três linhas de 35 | 1 | 0,0300 / 0,0088 / 0,0030 | 1,5 / 2,0 / 2,0 | 0,0496 / 0,0368 / 0,0269 | 0,57 / 0,68 / 0,77 | — |
| 41-43/1 | arco CM | muro de testa 90° | 1 | 0,0083 | 2,0 | 0,0379 | 0,69 | `arco_corrugado_muro` |
| 41-43/2 | arco CM | mitrada | 1 | 0,0300 | 1,0 | 0,0473 | 0,75 | `arco_corrugado_mitrado` (Ks = +0,7) |
| 41-43/3 | arco CM | parede fina projetante | 1 | 0,0340 | 1,5 | 0,0496 | 0,57 | `arco_corrugado_projetante` |

Observação sobre `ENTRADAS`: as chaves `arco_*` da calculadora reproduzem as linhas 41-43 (e 34 para o muro de testa).
O exemplo do HDS-5 §A.3.1 usa c = 0,0496 com Y = 0,53 para a elipse de chapa estrutural projetante [HDS5 p. 191], enquanto a
Tabela A.2 traz Y = 0,57 para a mesma linha (34/3): divergência interna do manual. A calculadora segue a tabela (Y = 0,57).

## 4. Outras tabelas de constantes (resumo)

| Tabela | Conteúdo | Página |
|---|---|---|
| A.3 | Caixa de concreto de Dakota do Sul (RCB), 13 croquis (K 0,44 a 0,69; M 0,49 a 0,74; c 0,023 a 0,047; Y 0,48 a 1,02), forma 2 | [HDS5 p. 199] |
| A.4 | Arco de concreto de fundo aberto (relação vão/altura 2:1 e 4:1; usar 2:1 até 3:1 e 4:1 acima de 3:1) | [HDS5 p. 200] |
| A.5, A.6 | Formas circulares e elípticas **embutidas** (NCHRP 15-24), com 0,2 D, 0,4 D, 0,5 D de embutimento | [HDS5 p. 200] |

Não implementadas na calculadora. Em irrigação só entram se o projeto usar caixa de DOT americano ou fundo embutido;
nesses casos pedir HY-8 à consultoria.

## 5. Tabela C.2: coeficientes de perda de entrada Ke (controle de saída) [HDS5 p. 216]

Perda de entrada He = Ke V²/2g (V no barril) [HDS5 p. 91, eq. 3.4a].

| Estrutura e entrada | Ke |
|---|---|
| **Tubo de concreto**: ponta-e-bolsa projetante | 0,2 |
| tubo de concreto: ponta (corte reto) projetante | 0,5 |
| tubo de concreto: muro de testa ou muro e alas, ponta-e-bolsa | 0,2 |
| tubo de concreto: muro de testa ou alas, aresta viva | 0,5 |
| tubo de concreto: muro de testa, arredondado (raio D/12) | 0,2 |
| tubo de concreto: mitrado ao talude | 0,7 |
| tubo de concreto: seção terminal conforme o talude (end-section) | 0,5 |
| tubo de concreto: bisel 33,7° ou 45° | 0,2 |
| tubo de concreto: afunilado lateral ou de declividade | 0,2 |
| **Tubo ou arco metálico corrugado**: projetante, sem muro | 0,9 |
| metálico: muro de testa ou alas, aresta viva | 0,5 |
| metálico: mitrado ao talude (pavimentado ou não) | 0,7 |
| metálico: seção terminal conforme o talude | 0,5 |
| metálico: bisel 33,7° ou 45° | 0,2 |
| metálico: afunilado | 0,2 |
| **Caixa de concreto armado**: muro de testa paralelo ao aterro, sem alas, aresta viva em 3 bordas | 0,5 |
| caixa: idem, arredondada (D/12 ou B/12) ou biselada em 3 lados | 0,2 |
| caixa: alas a 30° a 75°, aresta viva no topo | 0,4 |
| caixa: alas a 30° a 75°, topo arredondado (D/12) ou biselado | 0,2 |
| caixa: alas a 10° a 25°, aresta viva no topo | 0,5 |
| caixa: **alas paralelas** (prolongamento das paredes), aresta viva no topo | **0,7** |
| caixa: afunilada lateral ou de declividade | 0,2 |

Nota da tabela: a seção terminal pré-fabricada que acompanha o talude equivale a um muro de testa; seções com afunilamento
fechado têm desempenho melhor e se projetam como entrada biselada [HDS5 p. 216].

### Divergência com o DNIT (Tabela 30 do IPR-724)

`[DNIT-DREN p. 130]` (impressa 126; conferida na imagem do PDF) traz os mesmos valores, **exceto**: para caixa com
muros de ala **paralelos**, geratriz reta, o DNIT dá Ke = **0,2** e o HDS-5 dá **0,7**. A linha "muro de testa paralelo ao
aterro (sem alas), borda reta ou arredondada (R = D/12)" do DNIT funde duas linhas do HDS-5 (0,5 e 0,2) num só valor, 0,5.
Regra: usar o HDS-5 (mais conservador) e registrar a divergência no parecer; Ke não é calibração local. O DNIT aplica a
tabela a "bueiro metálico corrugado e bueiro celular de concreto" na mesma seção.

Chaves Ke usadas pela calculadora: ver coluna "Ke" da seção 2 (campo `Ke` de `ENTRADAS`); para valor diferente passar
`Ke` em `dimensionar_bueiro` ou em `controle_de_saida`.

## 6. Rugosidade de Manning do barril

| Material | n | Fonte |
|---|---|---|
| Tubo de concreto liso | 0,010 a 0,011 (laboratório); 0,011 a 0,013 em campo, após instalação e envelhecimento | [HDS5 p. 208, Tabela B.1; p. 204 §B.2] |
| Caixa de concreto (moldada in loco) | 0,012 a 0,015 (tabela B.1); in loco 0,012 a 0,022 | [HDS5 p. 208; p. 204 §B.3] |
| Corrugado metálico, helicoidal 2-2/3" x 1/2" (68 x 13 mm) | 0,011 a 0,023 (varia com o diâmetro) | [HDS5 p. 208] |
| Corrugado metálico anular 2-2/3" x 1/2" ou arco e caixa | 0,022 a 0,027 | [HDS5 p. 208] |
| Corrugado 5" x 1" / 3" x 1" | 0,025 a 0,026 / 0,027 a 0,028 | [HDS5 p. 208] |
| Chapa estrutural 6" x 2" / 9" x 2-1/2" | 0,033 a 0,035 / 0,033 a 0,037 | [HDS5 p. 208] |
| PEAD corrugado liso por dentro / corrugado | 0,009 a 0,015 / 0,018 a 0,025 | [HDS5 p. 208] |
| PVC | 0,009 a 0,011 | [HDS5 p. 208] |
| Valores típicos para o nomograma de saída | 0,012 (liso) e 0,024 (corrugado) | [HDS5 p. 90] |
| DNIT: tubos e células de concreto | **0,015** | [DNIT-DREN p. 114, Tabela 26] |
| DNIT: metálicos corrugados 68 x 12,7 / 76 x 25,4 / 152 x 51 mm; "não destrutivo" | 0,019 / 0,021 / 0,024; 0,024 | [DNIT-DREN p. 114, Tabela 27] |
| DNIT (Tabela 34): faixa mín.-máx. para condutos metálicos e outros | 0,019 a 0,028 (68 x 13 a 152 x 51) | [DNIT-DREN p. 132-134] (rótulos das duas colunas não impressos; conferir) |
| DAEE (SP): concreto 0,018; aço corrugado 0,024 | — | [DAEE-IT-DPO11 p. 4, Tabela 5] |

Observação importante: o n de 0,015 do DNIT e dos casos do acervo (Baixio, CSB, Salitre, Xingó) é mais alto que o 0,012 do
nomograma do HDS-5 para concreto. Em controle de entrada o n não entra; em controle de saída o HW sobe com n. Declarar qual n foi
usado e por quê (n de projeto DNIT = conservador).

Rugosidade composta (parte do perímetro com outro material): n_c = [Σ(p_i n_i^1,5)/p]^(2/3), verificada em modelo físico
[HDS5 p. 96, eq. 3.8]; exemplo do manual: CMP 6 ft com 40 % do perímetro revestido a 0,013 dá n_c = 0,021. O DNIT usa a
ponderação de Azevedo Netto, forma equivalente de ponderar por n² [DNIT-DREN p. 114].
