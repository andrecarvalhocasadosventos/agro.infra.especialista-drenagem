# Coeficiente de escoamento C (método racional): uso do solo, declividade e TR

Páginas = página física do PDF. Os valores são das fontes; a escolha dentro da faixa e a correção por TR são decisões do projetista e vão para o parecer como premissa. Nenhuma tabela aberta no corpus dá C rural **por TR com números**; ver seção 4.

## 1. Rural e terrenos naturais

### 1.1 Peltier / Bonnenfant, por área e declividade [ABDER-APOSTILA p. 53]

Área de contribuição de 0 a 10 ha e de 10 a 400 ha; colunas = declividade < 5 %, 5 a 10 %, 10 a 30 %, > 30 %. A tabela é indicada para A ≤ 4 km².

| Cobertura | 0 a 10 ha | 10 a 400 ha |
|---|---|---|
| Plataformas e pavimentos de estrada | 0,95 / 0,95 / 0,95 / 0,95 | 0,95 / 0,95 / 0,95 / 0,95 |
| Terrenos desnudos ou erodidos | 0,55 / 0,65 / 0,70 / 0,75 | 0,55 / 0,60 / 0,65 / 0,70 |
| Culturas correntes e pequenos bosques (região montanhosa com rocha) | 0,50 / 0,55 / 0,60 / 0,65 | 0,42 (a confirmar) / 0,55 / 0,60 / 0,65 |
| Matas e cerrados (região montanhosa) | 0,45 / 0,50 / 0,55 / 0,60 | 0,30 / 0,36 / 0,42 / 0,50 |
| Floresta comum (região plana) | 0,30 / 0,40 / 0,50 / 0,60 | 0,18 / 0,20 / 0,25 / 0,30 |
| Floresta densa (plana com alagadiço) | 0,20 / 0,25 / 0,30 / 0,40 | 0,15 / 0,18 / 0,22 / 0,25 |

O 0,42 da cultura em 10 a 400 ha com declividade < 5 % fica abaixo do vizinho (0,55) numa tabela que cresce com a declividade; pode ser erro de impressão ou de extração. Conferir no PDF antes de usar.

### 1.2 Gariglio e Ferrari, por solo, permeabilidade e cobertura [ABDER-APOSTILA p. 54]

| Solo, permeabilidade, cobertura | C |
|---|---|
| Rochoso, baixa permeabilidade, vegetação rala / densa | 0,70 a 0,85 / 0,65 a 0,80 |
| Rochoso, média permeabilidade, vegetação rala / densa | 0,60 a 0,75 / 0,55 a 0,70 |
| Argiloso, baixa permeabilidade, vegetação rala / densa / floresta | 0,50 a 0,65 / 0,45 a 0,60 / 0,40 a 0,55 |
| Argilo-arenoso, média permeabilidade, vegetação rala / densa / floresta | 0,35 a 0,50 / 0,30 a 0,45 / 0,25 a 0,40 |
| Argilo-arenoso, alta permeabilidade, vegetação rala (linha 11, valor extraído sem rótulo) | 0,20 a 0,35 (a confirmar a linha) |
| Argilo-arenoso, alta permeabilidade, vegetação densa / floresta | 0,15 a 0,30 / 0,10 a 0,25 |

### 1.3 DNIT, superfícies de rodovia e terrenos [DNIT-DREN p. 224, Tab. 39]

| Superfície | C |
|---|---|
| Revestimento de concreto de cimento | 0,70 a 0,90 |
| Revestimento betuminoso | 0,80 a 0,95 |
| Revestimento primário | 0,40 a 0,60 |
| Solo sem revestimento, baixa permeabilidade / permeabilidade moderada | 0,40 a 0,65 / 0,10 a 0,30 |
| Taludes gramados | 0,50 a 0,70 |
| Prados e campinas | 0,10 a 0,40 |
| Áreas florestais | 0,10 a 0,25 |
| Terrenos cultivados em zonas altas / em vales | 0,15 a 0,40 / 0,10 a 0,30 |

### 1.4 ASCE 1960, via HDS-2 e HEC-22 (valores para TR de 5 a 10 anos no DNIT)

[FHWA-HDS2 p. 182, Tab. 6.5; FHWA-HEC22 p. 58, Tab. 4.1; DNIT-HIDRO p. 132-133, Tab. 24 e 25]

| Tipo | C |
|---|---|
| Terrenos baldios ("unimproved") | 0,10 a 0,30 |
| Parques, cemitérios | 0,10 a 0,25 |
| Playgrounds | 0,20 a 0,40 (HDS-2) / 0,20 a 0,35 (DNIT) |
| Pátio de ferrovia | 0,20 a 0,40 |
| Gramado, solo arenoso: plano < 2 % / médio 2 a 7 % / íngreme > 7 % | 0,05 a 0,10 / 0,10 a 0,15 / 0,15 a 0,20 |
| Gramado, solo compacto: plano / médio / íngreme | 0,13 a 0,17 / 0,18 a 0,22 / 0,25 a 0,35 (HDS-2); 0,15 a 0,35 (DNIT, íngreme) |
| Asfalto, concreto, telhado | 0,70 a 0,95; 0,80 a 0,95; 0,75 a 0,95 |

Nota: as duas fontes diferem no "íngreme, solo compacto" (0,25 a 0,35 no HDS-2; 0,15 a 0,35 no DNIT) e no playground. Citar a fonte usada. Os usos urbanos (comércio, residencial, industrial) estão nas mesmas tabelas e não se aplicam ao perímetro.

### 1.5 Outras

- PMSP, TR = 10 anos: matas, parques e campos de esporte 0,05 a 0,20; subúrbios com pouca edificação 0,10 a 0,25 [PMSP-DRENURB-V2 p. 55, Tab. 1.14].
- Bacias de 4 a 10 km² com coeficiente de retardo (Burkli-Ziegler): campos de cultura em região plana 0,20 a 0,30; parques e jardins planos com alagadiço 0,15 a 0,25 [ABDER-APOSTILA p. 54].
- McMath (USBR): C é a soma de três parcelas, vegetação (0,08 a 0,30), solo (0,08 a 0,30) e topografia (0,04 a 0,15), de "baixo" a "extremo"; C total de 0,20 a 0,75 [USBR-DRAINAGE p. 57-58, Tab. 2-3]. Valem só para a fórmula de McMath.

## 2. Valores adotados em projetos do acervo (rastro, não norma)

| Projeto | C | TR | Observação |
|---|---|---|---|
| CSB GEOHIDRO (doc 1341:47, 74, 145) | C10 rural 0,05 a 0,30; adotado 0,20; valetas 0,10 | C_T = 0,8·T^0,1·C10 (TR 100: 0,25) | Mais coeficiente de distribuição Cd = A^-0,10 |
| Vale do Iuiu (doc 1051:316) | 0,3 | 10 | Racional até 50 ha |
| Baixio de Irecê (doc 670:116) | 0,10 a 0,40 conforme textura e declividade (Quadro 7.4 do memorial) | 25 | Racional até 100 ha, k de área 1 / 0,95 / 0,9 |
| **CAC Trecho 1** (doc 1139:227) | 0,20 no anteprojeto e no licitado; **0,40 no executivo** (visitas de campo, estudos da UFC); racional < 3,5 km², TR 100 | 100 | Calibração local sem vazão observada: rotular, não generalizar |
| **Delmiro Gouveia** (lotes, docs 1520-1521) | 0,15; racional com IDF TR 10, Tc Kirpich + viagem; n 0,025 | 10 | Caso `delmiro_gouveia_drenos_lotes_racional_manning` |
| **CAC Castanhão** (doc 1128:107) | 0,8 (semi-impermeável, J > 50 %) e 0,6 (demais), tc 5 min | não informado | Caso negativo: P (mm) usada como mm/h |
| Exemplo ABDER (p. 66, 69) | 0,30 a 0,36 (região montanhosa), 0,35 em 8,5 km² | 25 | Gariglio/Ferrari |

## 3. Piso e condição futura

DAEE-SP: C e C2 mínimos de 0,25 e CN mínimo de 60; os coeficientes devem refletir a condição atual e, se houver projeção de uso, a futura [DAEE-IT-DPO11 p. 2, Tab. 3]. É exigência paulista; citar como referência, não como regra do perímetro. DNIT: o tipo de cobertura dificilmente se mantém na vida útil, admitir mais tempo o terreno sem vegetação do que o cultivado [DNIT-HIDRO p. 78] (o texto é sobre CN, mas a lógica vale para C). Em perímetro irrigado, a mudança de uso é certa (a obra existe para isso): usar o uso **final** da bacia e a compactação de estradas e acessos.

## 4. Correção do C por TR

- HDS-2: "algumas tabelas de C variam com a AEP"; sem valores [FHWA-HDS2 p. 183].
- HEC-22: o fator de correção por frequência existe em algumas agências, mas a FHWA **não o endossa** [FHWA-HEC22 p. 56-57].
- PMSP: C_T a partir de C10 (Eq. 1.25, em imagem; a confirmar no PDF) [PMSP-DRENURB-V2 p. 55].
- Acervo (CSB): C_T = 0,8·T^0,1·C10, limitado a 1,0. Função `coef_c_para_tr`. Fatores derivados: TR 2 = 0,86; 5 = 0,94; 10 = 1,01; 25 = 1,10; 50 = 1,18; 100 = 1,27; 200 = 1,36.
- McCuen Tab. 7-9: duas colunas, "< 25 anos" e "≥ 25 anos"; usar a média da faixa [LOC-MCCUEN-HYDROLOGIC-ANALYSIS p. 395 física]. Eslamian Tab. 16.1: C igual para qualquer TR, com fator fa = 1,0 (2 a 10 anos), 1,1 (25), 1,2 (50) e 1,25 (100) e limite de 80 ha [LOC-ESLAMIAN-HANDBOOK-HYDROLOGY p. 350-352]. Divergência de fontes: declarar qual.
- DNIT: sem correção por TR no racional; usa o "fator de precipitação" FP e tabelas de c em função de tc, A, CN e FP (tabelas não reproduzidas no `_texto`) [DNIT-HIDRO p. 129-131].

Regra do agente: C_T com a forma do CSB só em anteprojeto, rotulada "forma do acervo, equação-fonte a confirmar". No projeto básico, ou se C10·f(TR) > 0,6, comparar com o SCS-CN do mesmo TR: o CN já tem a dependência com a chuva.

## 5. Média ponderada

C = Σ C_i·A_i / A [FHWA-HDS2 p. 183, eq. 6.11; FHWA-HEC22 p. 57, eq. 4.2]. Para plataforma e talude, o peso é a largura do implúvio [DNIT-DREN p. 171]. Função `c_ponderado(C, A)`; McCuen Ex. 7-11 (p. 398-399 física; C 0,2/0,4/0,6 em 5,3/7,2/6,4 ac → 0,412; Q 37,4 ft³/s com i = 4,8 pol/h; soma simples das sub-bacias 41,8; hidrograma do racional 28,1) e Ex. 7-9 (C 0,95, 2,4 ac, i 8,6 → 19,6 ft³/s; com tc mínimo de 15 min, i 6,5 → 15 ft³/s). Testes: `test_mccuen_racional_ex_7_9_e_7_11`.
