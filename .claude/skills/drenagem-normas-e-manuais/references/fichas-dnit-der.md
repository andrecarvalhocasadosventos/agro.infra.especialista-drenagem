# Fichas por fonte: DNIT (IPR-724, 715, 736, 726, ES) e DER/PR

Convenção: `[ID p. N]` = página física do PDF (marcador `<!-- p. N -->`). **conf.** = lido no `_texto` na F6; **mapa** = vem
do MAPA (F3/H12-H15), não relido. Licença: publicação oficial de uso livre (citar). Corpus: IPR-724, 715, 736 e
ES 015-017/019/022-030/086/096 estão no corpus do Hidráulico (`../Especialista Hidraulica/referencias/`, D1; cite pelo ID
dele); IPR-726, ES 018/020/021, DER/PR e o Álbum com OCR (`LOC-DNIT-ALBUM-2018`) estão no corpus próprio.

## IPR-724, Manual de Drenagem de Rodovias (`DNIT-DREN`)

Edição 2ª ed. 2006 (1ª ed. DNER 1990); sem revisão posterior no corpus. 337 p.; **impressa = física − 4**. É a "norma de fato"
brasileira de bueiro e de dispositivo superficial. Nomogramas (Figs. 13-32) só em imagem.

| O que pede / traz | Página | Status |
|---|---|---|
| Bueiro funciona como canal, vertedor ou orifício; capacidade "como canal" = regime crítico com energia específica igual à altura | 36 | conf. |
| Bueiro tubular no crítico: Qc = 1,538·D^2,5 (m³/s); Vc = 2,56·√D; Ic = 32,82·n²/D^(1/3). Celular: Qc = 1,705·B·H^1,5 | 47-48 (tubular); celular mapa p. 47-50 | conf. (tubular) |
| Orifício se HW ≥ 1,2 D (ou 1,2 H); c = 0,63 | 89; 92 | conf. |
| Circular nº 5 do BPR (equivale ao HDS-5 antigo): controle de entrada por HW/D e de saída por H = (1 + Ke + 2g·n²·L/R^1,33)·V²/2g | 95-126 (HW/D p. 102-103; Ke citado na p. 96) | conf. (p. 96, 102-103); resto mapa |
| **Tab. 30** Ke por tipo de entrada (0,2 a 0,9); **muros de ala paralelos, geratriz reta = 0,2** | 130 (impr. 126) | conf. |
| **Tab. 31** V máxima admissível: grama 1,50-1,80; argila 0,80-1,30; areia fina 0,30-0,40; concreto 4,50; betuminoso 3,00-4,00 m/s | 131 (impr. 127) | conf. |
| Tab. 32-33 n de curso d'água natural; Tab. 34 n de condutos e canais (concreto 0,011-0,017 por acabamento) | 131-134 | conf. |
| Valeta de proteção de corte e de aterro; altura crítica retangular hc = 0,467·(Q/B)^(2/3) | 158-166; 161 | conf. (161) |
| **Sarjeta de corte**: racional **por metro** com TR 10 anos e duração de 5 min; Q = c·i·A/(36·10⁴), i em **cm/h**, A em m²/m | 166-175; 171 | conf. |
| Sarjeta de aterro p. 179-188; canteiro central p. 188-190; descidas d'água p. 186-195 (altura crítica p. 191); saídas; caixas coletoras; bueiro de greide | 179-205 | mapa (191 conf.) |
| Dissipadores (bacia de amortecimento, rip-rap): **só localizar** (D3, Hidráulico) | 203-209 | mapa |
| Drenagem do pavimento (camada drenante, drenos rasos) | 225-247 | conf. (início 225/227) |
| Drenagem subterrânea ou profunda (impr. 243) | 247 em diante | conf. |
| Travessia urbana (fora de escopo do Drenagem; D1 do núcleo) | 283 em diante | conf. |
| Geotêxtil como filtro (impr. 311) | 315 em diante | conf. |

Armadilhas próprias:
- **Ke × HDS-5**: a linha "muros de ala paralelos" dá 0,2 aqui e **0,7** no HDS-5 Tab. C.2 p. 216 e no HEC-13 Tab. 1 p. 100. O código usa 0,7 (`ke_entrada`, `fonte_ke="dnit"` para 0,2). Decisão F7: mostrar as duas.
- **Remissões internas erradas**: a p. 169 manda ver "tabela 26 do Apêndice B" para a velocidade do revestimento da sarjeta; a tabela de velocidades é a **31** (p. 131; as p. 159, 166, 174, 177 e 182 citam a 31). Citar a 31.
- **Vc da Tab. 1 (p. 55)**: usa Vc = 2,56·√D também para o círculo e A_c ≈ 0,60·D²; fica 7,7 % acima do crítico exato (`vazao_critica_legado_dnit` x `vazao_critica_exata`).
- Sarjeta com i em **cm/h** e A em m²/m: conferir a dimensão antes de comparar com HEC-12/22 (mm/h, ft).
- Método de bueiro do IPR-724 (crítico/orifício) **não** é controle de entrada e de saída do HDS-5; os projetos do acervo usam o primeiro. Apontar a divergência, não "corrigir" o projeto (núcleo, seção 9).

## IPR-715, Manual de Hidrologia Básica (`DNIT-HIDRO`)

2ª ed. 2005; 137 p.; **impressa = física − 4**. Base hidrológica oficial; a chuva vem do Pfafstetter (p. 15, 59, 106) e **não é entrega do Drenagem** (Clima).

| O que pede / traz | Página | Status |
|---|---|---|
| Risco J = 1 − (1 − 1/TR)^n; Fig. 1 (risco × TR × vida útil) | 24-25 | conf. |
| IS-203: dimensionar o bueiro com TR 10 anos para condição crítica e **verificar o nível a montante para 20 ou 25 anos**; ponte com folga mínima de 1,00 m | 24 | conf. |
| TR por tipo de obra (bueiro 10-20, ponte 50-100) | 23-24 | mapa |
| Estatística de máximos (Gumbel p. 35-39; Hazen p. 40-45; Log-Pearson III p. 46-52) | 35-53 | mapa |
| Hidrograma unitário sintético SCS (procedimentos A e B), CN, chuvas antecedentes | 57-82 | mapa |
| Tc: 14 fórmulas com velocidade média por fórmula; DNOS (p. 89); **Kirpich modificada com coeficiente 1,42** (p. 90; "×1,42 sobre a Kirpich" é leitura do MAPA H12); recomendação de Kirpich, DNOS, Kirpich modificada, George Ribeiro, Pasini e Ventura (p. 94); variação 1:3 a 1:5 entre métodos | 83-98 | conf. (89, 90, 94); resto mapa |
| Racional com coeficiente c calibrado por CN, fator de distribuição **n = A^−0,10 (A em km²)**; exemplo A = 10,5 km², c = 0,385, 96,1 mm/h → 107,9 m³/s (28 % acima das descargas específicas) | 127-133 (131) | conf. |

Armadilhas próprias:
- **Divisor do racional**: o exemplo da p. 131 fecha com Q = c·i·A/**3,6** (0,385·96,1·10,5/3,6 = 107,9); o `_texto` traz "6,3" por embaralhamento. Conferir na imagem antes de codar.
- **Sem teto de área** para o racional (aplica-se a bacia maior com a correção A^−0,10); o teto vem de outras fontes (seção 8 do SKILL).
- Kirpich modificada ×1,42, DNOS e Dooge: as docstrings de `hidrologia.py` dizem "não conferida"; a p. 90 confirma o 1,42, a fórmula completa do DNOS (p. 89) segue a conferir na imagem.

## IPR-736, Álbum de Projetos-Tipo de Dispositivos de Drenagem (`DNIT-ALBUM` no Hidráulico; `LOC-DNIT-ALBUM-2018` com OCR)

**5ª ed. 2018** (folha de rosto; o catálogo do Hidráulico registra 2006, que é a 2ª ed.; edições 1988, 2006, 2010, 2011, 2018).
227 p. "Documento de caráter orientador e não normativo": o projetista faz o dimensionamento hidráulico [LOC-DNIT-ALBUM-2018 p. 23, conf.].
No Hidráulico só 6 de 227 páginas têm texto; **o OCR do corpus próprio cobre 203 p.** (24 sem OCR). Todo número de OCR: conferir na imagem.

- Cap. 1 superficial p. 25-49 (VPC valeta de corte, VPA de aterro, STC/STG/SZC/SCC sarjetas, MFC meios-fios, EDA entradas, DAR/DCD/DAD descidas, DES/DED dissipadores, CCS caixas); cap. 2 drenagem subterrânea (DPS p. 53, DPR p. 54, BSD p. 55); cap. 3 subsuperficial DSS p. 59; cap. 4 DSH p. 63; cap. 5 pluvial urbana p. 67-74; cap. 6 transposição de talvegues (bueiros tubulares p. 79-84, celulares p. 87-120, aduelas cap. 7 p. 125-203, minitúnel cap. 8 p. 205-210) [mapa].
- **Cap. 9 dispositivos lineares pré-fabricados** p. 213-227: dimensionamento por Manning e continuidade com **TR 10 anos (ou NBR 10844:1989) e Tc 6 min**; lâmina máxima ≥ 3 cm abaixo da grelha [conf. p. 214, OCR].
- Armadilha: o **Tc de 6 min** do Álbum diverge do 5 min (IPR-726 p. 258) e do 10 min (IPR-726 p. 463). Tabelas de armadura (p. 127-203) e quantitativos: ler no PDF.
- Quando o pedido é "qual dispositivo-tipo", a resposta é seleção no Álbum + **verificação hidráulica pelo projetista** (p. 23). Detalhe de dispositivo: skill `drenagem-de-estradas-e-plataformas`.

## IPR-726, Diretrizes Básicas para Estudos e Projetos Rodoviários (`DNIT-IPR726-2006`, corpus próprio)

3ª ed. 2006; 487 p.; na coletânea de manuais vigentes do IPR; **impressa = física − 3**. Escopos e Instruções de Serviço; **não dimensiona** sarjeta nem valeta.

| IS | Conteúdo | Página | Status |
|---|---|---|---|
| IS-203 Estudos Hidrológicos | tabela de **TR por espécie**: drenagem superficial 5-10; subsuperficial 10; **bueiro tubular 15 (como canal) e 25 (como orifício)**; **bueiro celular 25 (canal) e 50 (orifício)**; pontilhão 50; ponte 100. **Tc de drenagem superficial = 5 min** | 258 | conf. |
| IS-203 | método por área: tabela "< 10 km² racional e racional corrigido; > 10 km² hidrograma"; e, na mesma página, limites **≤ 4 km² racional; 4-10 km² racional corrigido; > 10 km² HUT** (duas regras na mesma página) | 259 | conf. |
| IS-203 | Tabela 1 "Classificação dos Problemas" (ERM, ERJ, ES, RE, AS, AL, ED) de bueiros existentes; planilha de descargas | 259-261 | mapa (início conf.) |
| IS-210 Projeto de Drenagem | classes de drenagem; drenagem do pavimento se precipitação anual > 1.500 mm e TMD > 500 veículos comerciais; memória de cálculo obrigatória | 305-311 | mapa |
| IS-239 Hidrologia, rodovias vicinais | mesma tabela de TR; **Tc de drenagem superficial = 10 min**; racional se A < 10 km², hidrograma acima | 463-464 | conf. |
| IS-242 Projeto de drenagem, vicinais | dispositivos de superfície e tipos de bueiro | 472-473 | mapa |

Aplicação a estrada de serviço de perímetro irrigado: a IS-239 (vicinais) é a mais próxima; mostrar a IS-203 como alternativa. **Padrão provisório, decisão F7.**

## DNIT ES 018/2023, 020/2006, 021/2023 (corpus próprio; especificações de serviço, sem dimensionamento)

| Norma | Edição e vigência | O que traz | Páginas | Status |
|---|---|---|---|---|
| **DNIT 018/2023-ES** Drenagem, sarjetas e valetas | jan/2023; vigente; revisão da 018/2006 (título conferido na p. 1) | sarjeta triangular com declividade transversal máxima adjacente ao acostamento **25 % (4H:1V)** por segurança (NBR 15486); concreto, execução, revestimento vegetal, sem revestimento; tolerância geométrica 1 % em pontos isolados; medição por metro | 2-6 | conf. (p. 2, 3 fck 20 MPa, 4 gabaritos a 3,0 m e junta a cada 12,0 m, 6); resto mapa |
| **DNIT 020/2006-ES** Meios-fios e guias | 2006; **sem revisão verificada** | definições, concreto de cimento e asfáltico, fôrmas a 3 m, junta a cada 1,00 m nas curvas; remete ao Álbum ENEMAX 1988 (anterior ao IPR-736 de 2018) | 2-3 | conf. |
| **DNIT 021/2023-ES** Entradas e descidas d'água | versão com errata 1 (11/2024); cancela a 021/2004 | argamassa de rejunte **1:3**; descidas > 10 m com juntas de dilatação (nota 3); tolerância 1 %; medição (entrada por unidade, descida por metro) | 3-5 | conf. |

Outras ES de drenagem (corpus do Hidráulico, só execução e aceitação): ES 015/016/017 (drenos), 019 (transposição de sarjetas), 022 (dissipadores), **023 e 025 (bueiros tubular e celular: folga de 0,30 m entre tubos, 0,40 m lateral em vala; celular 0,50 m por lado, `DIVERGENCIAS.md`)**, 026 (caixas e bocas), 027-030, 086, 096. **Armadilha**: citar a ES pelo ano da edição; as ES 018 e 021 de 2023 substituem as de 2006 e 2004.

## DER/PR ES-DR 01, 03, 05, 06, 07/23 (corpus próprio; espelho estadual de conferência)

Deliberação 111/2023; vigentes; licença aberta. Estrutura comum: objetivo, referências, definições, condições gerais, materiais e execução, manejo ambiental, controle, aceitação, medição. **Não é norma federal**: serve para conferir a DNIT e para detalhes (solo-cimento, gabaritos) que a ES do DNIT não traz.

| ES | Tema | Páginas-chave | Status |
|---|---|---|---|
| ES-DR 01/23 | sarjetas e valetas: concreto fck mín. 20 MPa e solo-cimento (IP ≤ 18 %, LL ≤ 40 %, #200 ≤ 40 %, cimento ≥ 10 %, 1,5 MPa) p. 4; gabaritos a **2,00 m no máximo** p. 5; **junta a cada 12 m** p. 6; **declividade longitudinal < 0,5 % implica demolição** p. 10; tolerância de dimensão ≤ 10 % p. 9 | 4-10 | conf. (5, 6, 10); resto mapa |
| ES-DR 03/23 | entradas e descidas d'água (degraus, rápido, caixa dissipadora); argamassa 1:4 (p. 5-6); tolerância 5 % (p. 7) | 3-8 | conf. (5-7); resto mapa |
| ES-DR 05/23 | bocas e caixas de bueiros tubulares; medição por DN e nº de linhas | 3-9 | mapa |
| ES-DR 06/23 | drenos longitudinais profundos; Quadro 1 areia filtrante p. 5; **Quadro 2 força mínima de ruptura de tubos de concreto DN 200-600** p. 6 (texto cita "Quadro 1" por engano); vala com declividade ≥ 1 % p. 7; geotêxtil: sobreposição de 20 cm com costura ou 50 cm sem | 3-12 | mapa |
| ES-DR 07/23 | drenos subsuperficiais; Quadro 1 granulometria (igual ao 06; texto diz "dreno profundo" por engano); vala ≥ 1 %; camadas ≤ 30 cm | 3-10 | mapa |

Divergências ES (registrar, não decidir): gabaritos 3,0 m (DNIT 018 p. 4, mapa) × 2,00 m (DER/PR 01 p. 5); tolerância 1 % × 5 % × 10 %; rejunte 1:3 (DNIT 021 p. 3-4) × 1:4 (DER/PR 03 p. 5); fck 20 MPa (DNIT 018, DER/PR 01) × 15 MPa (IPR-724, mapa p. 166-186).
