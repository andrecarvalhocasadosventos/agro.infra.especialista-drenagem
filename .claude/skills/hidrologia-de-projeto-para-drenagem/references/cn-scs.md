# SCS-CN: CN por grupo hidrológico e uso, S, Ia, umidade antecedente

Páginas = página física do PDF. Os CN valem para condição antecedente média (ARC II, AMC II) e Ia = 0,2·S. Tabelas resumidas: só as linhas úteis a perímetro irrigado; a tabela completa está no primário.

## 1. Equações

| Item | Forma (SI) | Fonte |
|---|---|---|
| Escoamento direto | Q = (P − Ia)²/(P − Ia + S), P > Ia, Q e P em mm | [NRCS-NEH630-CH10 p. 10, eq. 10-11]; DNIT: d = (P − 0,2S)²/(P + 0,8S) [DNIT-HIDRO p. 75] |
| Retenção | S[mm] = 25.400/CN − 254 (= 254·(100/CN − 1)) | [NRCS-NEH630-CH10 p. 10, eq. 10-13]; [DNIT-HIDRO p. 76] |
| Abstração inicial | Ia = 0,2·S. Os CN do NEH 630 cap. 9 foram obtidos com Ia = 0,2·S; **outra relação exige outro conjunto de CN** | [NRCS-NEH630-CH10 p. 10] |
| Faixa dos CN | Método não vale para CN < 40 ou > 98 no procedimento gráfico NRCS [NRCS-NEH650-CH02 p. 11]; CN < 30 usa-se 30 [NRCS-NEH630-CH09 p. 9, nota 6] | |
| Superfície impermeável e água | CN = 98 | [NRCS-NEH630-CH09 p. 7] |
| Origem dos CN | Bacias em geral < 1 mi² (2,6 km²), tempestades de até 1 dia, cheias anuais; "não recomendado para vazões baixas ou pequenas cheias" | [NRCS-NEH630-CH09 p. 7; NRCS-NEH630-CH10 p. 25] |
| Verificação do P < Ia | Q = 0; ARC e CN pequeno com chuva pequena: o método erra mais | [NRCS-NEH630-CH10 p. 25] |

Exemplo numérico (conferido com `chuva_efetiva`): P = 5,1 pol, CN 75 → Q = 2,53 pol; CN 69 → 2,03 pol [NRCS-NEH630-CH10 p. 19, ex. 10-3]; CN 74 → S = 3,51 pol [p. 12, Tab. 10-1].

## 2. Grupo hidrológico do solo (HSG)

Critério por condutividade hidráulica saturada da camada menos transmissiva, **quando não há camada impermeável nem lençol a menos de 1 m** [NRCS-NEH630-CH07 p. 12, Tab. 7-2]:

| Grupo | Ksat (µm/s) | Ksat (mm/h) |
|---|---|---|
| A | > 10 | > 36 |
| B | 4 a 10 | 14,4 a 36 |
| C | 0,4 a 4 | 1,44 a 14,4 |
| D | ≤ 0,4 | ≤ 1,44 |

Com camada impermeável entre 50 e 100 cm e lençol entre 60 e 100 cm, os limites de Ksat sobem para > 40, 10 a 40, 1 a 10 e ≤ 1 µm/s [NRCS-NEH630-CH07 p. 12, Tab. 7-1]; com camada impermeável a menos de 50 cm ou lençol a menos de 60 cm, o solo é D. DNIT: terreno plano com drenagem fraca e lençol que aflora após chuva prolongada vai para D [DNIT-HIDRO p. 78]. Em perímetro irrigado com lençol raso, esperar C e D. **O Ksat vem de Geotecnia** (ensaio Porchet no Iuiu, doc 1051): `[DELEGAR: geotecnia]`. A classe A a D do projeto é premissa até chegar o ensaio.

## 3. CN (ARC II) por grupo e uso

### 3.1 Terras agrícolas [NRCS-NEH630-CH09 p. 8-9, Tab. 9-1]

Condição: Poor = pouca cobertura/resíduo, aumenta o escoamento; Good = o contrário. SR = fileiras retas; C = em nível; T = terraceado.

| Uso e tratamento | Condição | A | B | C | D |
|---|---|---|---|---|---|
| Pousio, solo nu | — | 77 | 86 | 91 | 94 |
| Cultura em fileira, SR | Poor / Good | 72 / 67 | 81 / 78 | 88 / 85 | 91 / 89 |
| Cultura em fileira, em nível (C) | Poor / Good | 70 / 65 | 79 / 75 | 84 / 82 | 88 / 86 |
| Cultura em fileira, em nível e terraceada | Poor / Good | 66 / 62 | 74 / 71 | 80 / 78 | 82 / 81 |
| Grãos pequenos, SR | Poor / Good | 65 / 63 | 76 / 75 | 84 / 83 | 88 / 87 |
| Leguminosas ou prado em rotação, SR | Poor / Good | 66 / 58 | 77 / 72 | 85 / 81 | 89 / 85 |
| Pasto, pastagem ou campo | Poor / Fair / Good | 68 / 49 / 39 | 79 / 69 / 61 | 86 / 79 / 74 | 89 / 84 / 80 |
| Prado (capim protegido, ceifado) | Good | 30 | 58 | 71 | 78 |
| Arbustos e ervas (brush) | Poor / Fair / Good | 48 / 35 / 30 | 67 / 56 / 48 | 77 / 70 / 65 | 83 / 77 / 73 |
| Pomar (50 % árvores, 50 % capim) | Poor / Fair / Good | 57 / 43 / 32 | 73 / 65 / 58 | 82 / 76 / 72 | 86 / 82 / 79 |
| Mata | Poor / Fair / Good | 45 / 36 / 30 | 66 / 60 / 55 | 77 / 73 / 70 | 83 / 79 / 77 |
| Sede, edificações, pátios | — | 59 | 74 | 82 | 86 |
| Estrada de terra (com faixa de domínio) | — | 72 | 82 | 87 | 89 |
| Estrada de cascalho | — | 76 | 85 | 89 | 91 |

Notas da fonte: pasto "Poor" = menos de 50 % de cobertura ou muito pastejado; "Fair" = 50 a 75 %; "Good" = mais de 75 % [p. 9, nota 4]. Para pastagem em clima úmido usar esta tabela; em região árida e semiárida usar a 3.2 [p. 11, nota 1].

### 3.2 Pastagem e arbusto em região árida e semiárida [NRCS-NEH630-CH09 p. 11, Tab. 9-2]

Poor: menos de 30 % de cobertura (serrapilheira, capim, arbusto); Fair: 30 a 70 %; Good: mais de 70 %. CN de A só existe para "desert shrub".

| Cobertura | Condição | A | B | C | D |
|---|---|---|---|---|---|
| Herbáceas (capim, ervas, arbusto baixo, arbusto secundário) | Poor / Fair / Good | — | 80 / 71 / 62 | 87 / 81 / 74 | 93 / 89 / 85 |
| Sage-grass (artemísia com capim) | Poor / Fair / Good | — | 67 / 51 / 35 | 80 / 63 / 47 | 85 / 70 / 55 |
| Desert shrub (saltbush, mesquite, cactos, palo verde) | Poor / Fair / Good | 63 / 55 / 49 | 77 / 72 / 68 | 85 / 81 / 79 | 88 / 86 / 84 |

São tabelas do sudoeste dos EUA. **Não há CN validado para a caatinga no corpus.** "Desert shrub" e "herbáceas" são os análogos mais próximos; usar como premissa rotulada, e o NRCS avisa que o método concordou mal numa bacia do sudoeste semiárido [NRCS-NEH630-CH10 p. 25].

### 3.3 Tabela simplificada do DNIT [DNIT-HIDRO p. 77, Tab. 11]

Para projeto rodoviário; "retenção superficial" Pobre ou Boa. A extração da tabela está desalinhada: a atribuição abaixo segue a ordem do texto e deve ser conferida no PDF.

| Cobertura | Retenção | A | B | C | D |
|---|---|---|---|---|---|
| Terreno não cultivado, pouca vegetação | Pobre | 77 | 86 | 91 | 94 |
| Terreno cultivado | Pobre / Boa | 72 / 51 | 81 / 67 | 88 / 76 | 91 / 80 |
| Pasto | Pobre / Boa | 68 / 39 | 79 / 61 | 86 / 74 | 89 / 80 |
| Mata ou bosque | Pobre / Boa | 45 / 25 | 66 / 55 | 77 / 70 | 83 / 77 |
| Área urbana | Pobre / Boa | 74 / 70 | 80 / 76 | 87 / 83 | 90 / 86 |

O "cultivado, Boa" do DNIT (51, 67, 76, 80) é bem menor que "row crops, Good" do NRCS (67, 78, 85, 89) e coincide com leguminosas em nível e terraceadas. Para cultura irrigada em fileira, preferir a 3.1. O DNIT recomenda prudência: admitir o terreno sem vegetação por mais tempo que o cultivado [p. 78].

### 3.4 Pré-dimensionamento (Jabôr) [ABDER-APOSTILA p. 57]

CN estimado só por área e declividade da bacia (ex.: A < 30 km², CN de 68 (< 0,5 %) a 90 (> 10 %)). A própria ABDER o indica "como ponto de partida"; **não usar em projeto básico**.

### 3.5 CN do acervo (rastro)

Vale do Iuiu CN 78 (solo B, cultura em fileira, boa), igual ao da Tab. 9-1 (SR, Good, B = 78). Baixio de Irecê: 32, 58, 56,5, 71,2 (Quadro 7.4 do memorial; CN 62,04 ponderado na bacia de 323,4 ha). CSB: 66 (bacia 5, 386,5 km²). Xingó: 67,45 a 79,47.

## 4. Umidade antecedente (AMC / ARC)

- DNIT: a condição II é a "média das cheias anuais"; condição I = solo seco; III = solo quase saturado após cinco dias de chuva forte. Tab. 12 converte: CN II 60 → III 79; 70 → 87; 80 → 94 [DNIT-HIDRO p. 79].
- NRCS Tab. 10-1: CN II 74 → I 55, III 88 [NRCS-NEH630-CH10 p. 12].
- O NRCS não encontrou relação entre a chuva antecedente de 5 dias e S em bacias onde predomina o escoamento superficial (Treynor, Iowa) e propõe tratar CN como variável aleatória [NRCS-NEH630-CH10 p. 13].
- DNIT, procedimento B (o mais usado no Brasil): usa CN já elevado (74 no lugar de 60), sem chuvas antecedentes [DNIT-HIDRO p. 57-58, 108].
- Regra do agente: para obra de drenagem em solo de perímetro irrigado, a umidade do solo no dia da chuva é maior que a da bacia natural. Declarar ARC II ou III e mostrar a sensibilidade (Q com CN II e CN III). A escolha é do projetista (D2) e vai ao parecer como premissa.

**CN do CAC Trecho 1 (doc 1139:227):** 65 no anteprojeto e no licitado, **85 no executivo** (HUT acima de 3,5 km², TR 100), sem calibração com vazão observada. CN 85 é alto frente às tabelas do NRCS: tratar como calibração local do semiárido cearense, não como valor de livro, e mostrar a sensibilidade (CN 65, 75 e 85). Delmiro BHD1: CN 75,2 (planossolo B-C, sub-bacia 1), S = 83,77 mm, P bacia 112,40 mm → Pe 50,99 mm (`casos-l2-e-divergencias-f5.md` seção 1).

## 5. CN ponderado ou Q ponderado

Se os CN das partes são próximos, os dois métodos dão o mesmo Q. Se diferem muito, o CN ponderado erra para mais ou para menos conforme o tamanho da chuva; o Q ponderado é exato, com mais trabalho [NRCS-NEH630-CH10 p. 17-19, ex. 10-3 a 10-5]. Ponderar por área (CN) só com subáreas de CN próximo.
Função `escoamento_ponderado(P, CN, A)` pondera o **escoamento** (não o CN). McCuen Ex. 7-17/7-18 [LOC-MCCUEN-HYDROLOGIC-ANALYSIS p. 408-409 física]: P = 7 pol; CN 55, 70, 75 e 83 → Q = 2,12; 3,62; 4,15 e 5,03 pol; no Ex. 7-17 o CN médio dá 0,28 pol contra 0,385 pol do Q ponderado. Teste: `test_mccuen_scs_ex_7_15_a_7_18_e_ponderacao_do_escoamento`. Conversão de CN para Ia = 0,05·S: `cn_para_lambda_005` (a conversão por si não torna o CN tabelado válido; ver NRCS-NEH630-CH10 p. 10).
