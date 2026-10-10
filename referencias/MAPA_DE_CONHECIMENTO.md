# MAPA DE CONHECIMENTO — corpus próprio do Especialista Drenagem

Consolidado em 2026-10-08 a partir de `_mapa_parcial/` (F3; 4 subagentes Sonnet, ~740 páginas lidas no total, leitura
pelo `_texto/`; página = página física do PDF; números de OCR marcados para conferência na imagem). Cobre só os 48
itens do corpus próprio (`_catalogo.yaml`). O corpus do Hidráulico (HDS-5, HEC-14/15/22, IPR-715/724/736, NEH 630/624/650,
ILRI 16, DAEE, FAO 26) segue mapeado em `../Especialista Hidraulica/referencias/MAPA_DE_CONHECIMENTO.md`, seções
H12–H15 (D1). Fora do mapa: slides Robson I–IV (sem OCR) e FDOT (não baixado).

Grupos: G1 hidrologia · G2 bueiros e tubos · G3 estradas e plataformas · G4 canais de drenagem e subsuperficial.
Cada grupo termina com "Gabaritos para calculadora" e "Pendências para a F5/F7".


---

# Mapa parcial F3 — grupo G1-hidrologia (Especialista Drenagem)

Convenção de páginas: "p. N" = página física do PDF (marcador `<!-- p. N -->` do `_texto`), salvo dito. Conversões úteis:
McCuen impressa = física − 19; Eslamian impressa = física − 17; NEH-630 cap. 15 "15-N" = física − 6; WSP 1849 impressa = física − 6;
Pfafstetter "pág." do livro = física − 6; EM 1110-2-1413 (cópia CED) impressa "9-n" = física − 99 no cap. 9.
Aviso geral sobre o OCR/extração: nos livros (McCuen, Eslamian) as **equações, os números de várias tabelas e as figuras** saíram do texto
(células de tabela sem valores, expoentes ilegíveis). O que está marcado "(legível)" foi lido no `_texto`; o resto é "(conferir na imagem)".
Nenhuma fórmula ou coeficiente abaixo substitui a fonte; são índices de localização.

## LOC-MCCUEN-HYDROLOGIC-ANALYSIS — McCuen, Hydrologic Analysis and Design (2ª ed., 1998)
Vigência: livro-texto (sem edição de norma); licença: uso-interno; 833 p. (camada de texto nativa, sem OCR).
Temas e onde estão (física):
- Cap. 3 Características da bacia p. 116–190: n de Manning (Tab. 3-3 p. 133 e Tab. 3-4 p. 149–151, valores de células ilegíveis), Cowan (Tab. 3-10 p. 154), grupos de solo (Tab. 3-17 p. 174), **CN** (Tab. 3-18 p. 176–178, legível; ajuste de umidade AMC I/III, Tab. 3-19 p. 179).
- **Tempo de concentração**, seção 3.6, p. 158–173: definições p. 159; classificação (Tab. 3-13) p. 160; método da velocidade (Tab. 3-14, Fig. 3-19) p. 161–163; escoamento laminar por onda cinemática e limites de comprimento p. 164–165; nove fórmulas empíricas p. 170–173 (Carter, Eagleson, Espey-Winslow, **FAA** com C, Kerby-Hathaway, **Kirpich** Pensilvânia e Tennessee com multiplicadores 0,4 e 0,2 para superfície/canal de concreto ou asfalto p. 172, **lag do SCS** com tc = 1,67·lag p. 172–173, Van Sickle). Dooge, Giandotti e Picking: **não existem** como fórmula de Tc no livro.
- Cap. 4 Precipitação p. 191–245: IDF e ajuste matemático p. 197–202 (Ex. 4-1 a 4-3; Tab. 4-2 p. 202; Fig. 4-4 IDF de Baltimore p. 200), redução por área (Fig. 4-7 p. 205), dupla massa (Fig. 4-9 a 4-11 p. 213–216), tormentas de projeto SCS (Tab. 4-10 p. 224, Fig. 4-15 p. 225, Tab. 4-11 p. 226).
- Cap. 5 Análise de frequência p. 246–335: posições de plotagem (Weibull) p. 256–258; normal p. 255; log-normal (Ex. 5-2, Tab. 5-2 p. 262–264); **Log-Pearson III** (procedimento e Ex. 5-5 Back Creek p. 273–275, Tab. 5-5/5-6, Fig. 5-11); vazão baixa (Ex. 5-4 a 5-6 p. 276–278); assimetria ponderada (Fig. 5-14 p. 282), IC (Tab. 5-9 p. 285), cheias históricas (Tab. 5-10 p. 289), outliers (Tab. 5-11 p. 293), urbanização (Tab. 5-12 p. 298, Fig. 5-19 a 5-22 p. 298–302), risco binomial (Tab. 5-22 p. 322), série parcial (Tab. 5-24 p. 325–327). Tabela de K do LP3 ("Apêndice 5-1"): não localizada por busca de texto (a confirmar).
- Cap. 7 Vazão de pico p. 378–440: regressões USGS urbanas p. 386–389; **método racional** p. 394–401 (Tab. 7-9 C por grupo de solo e declividade p. 395; Tab. 7-10 C por uso p. 396; C ponderado p. 397; sub-bacias, Ex. 7-11 p. 398–399; Ex. 7-12 e Tab. 7-12 p. 400–401); **SCS runoff** p. 404–409 (S = 1000/CN − 10 e Ia = 0,2·S p. 405; Fig. 7-7 p. 406; Tab. 7-13 Q×CN×P p. 407); **método gráfico SCS** p. 409–417 (Ia/P Tab. 7-14 p. 411; Fig. 7-9a–d qu p. 413–414; lagoas Tab. 7-16 p. 412; limitações p. 415); envoltórias p. 421–423.
- Cap. 8 Métodos de projeto (calhas e inlets, **bueiro** 8.7, detenção) a partir de p. 436: fora do foco do G1, não lido; registrar para o G2.
- Cap. 9 Hidrograma a partir de p. 496: perdas (phi, Horton, Green-Ampt), **HU** (convolução p. 524–, S-hydrograph Ex. 9-16/9-17 p. 536–539, Tab. 9-11 p. 539), **HU adimensional SCS e triangular** p. 553–561 (Tab. 9-17 p. 556; Ex. 9-23/9-24 p. 557–559), hidrograma do racional (Ex. 9-22, Tab. 9-16 p. 553–554), Snyder.
- Cap. 10–11 (Muskingum-Cunge, Puls, p. 603–671): só localizado.
Exemplos resolvidos (física): Tc — Ex. 3-12 p. 165; Ex. 3-13 p. 165–166; Ex. 3-14 p. 166–170; Ex. 3-15 p. 170. IDF — Ex. 4-1/4-2 p. 199–202. Frequência — Ex. 5-1 p. 260; 5-2 p. 264; 5-5 p. 273–275. Racional — Ex. 7-9 p. 397; 7-10 p. 397–398; 7-11 p. 398–399; 7-12 p. 400–401. SCS — Ex. 7-15 p. 405–406; 7-16 a 7-18 p. 406–409; 7-19 p. 415–416; 7-20 p. 417. HU — Ex. 9-16/9-17 p. 537–538; 9-22 p. 553; 9-23/9-24 p. 557–559.
Lacunas: equações de Tc (3-47, 3-48 e 3-49 a 3-57) ilegíveis no `_texto`: ler na imagem antes de calibrar `hidrologia.py`; sem IDF brasileira.
Páginas lidas: ≈ 60 (índice p. 4–14; 159–173; 394–401; 405–412; 415–417; 273–276; 264; 202; 133, 176, 179; 537–539; 553–561 parcial).

## LOC-ESLAMIAN-HANDBOOK-HYDROLOGY — Eslamian, Handbook of Engineering Hydrology, Livro III (2014)
Vigência: livro de capítulos de autores diversos; licença: uso-interno; 594 p. (nativo). Só o **cap. 16 "Stormwater Modeling and Management" (p. 346–363; impressa 329–346)** serve a drenagem; os outros 28 capítulos (aquíferos, nanotecnologia, esgoto, governança) não têm relação (não abertos). Cap. 17 (p. 364–381) só varrido por palavra-chave: sem Tc, racional ou CN.
- TR e probabilidade (Eq. 16.2 p. 350); IDF ilustrativa (Fig. 16.2 p. 349); **C do racional** Tab. 16.1 p. 350 (faixas, fonte TR-55); **CN urbano** Tab. 16.2 p. 351 (A/B/C/D, legível, igual à Tab. 3-18 do McCuen); **racional em SI** Q = fa·C·I·A/360 (m³/s; ha; mm/h), fa = 1,0 (2–10 anos), 1,1, 1,2 e 1,25 (25, 50, 100 anos), "área menor que 80 ha" p. 352; **SCS** Eq. 16.4–16.7 (Qd; Sr = 25,4·(1000/CN − 10); qu em m³/s/km²/mm) p. 352; racional probabilístico Eq. 16.8 p. 353; HU p. 353; Manning (Eq. 16.9) p. 357.
- Sem fórmula de Tc (só definição p. 351), sem Kirpich, sem exemplo numérico de vazão. Gumbel só na p. 474 (cap. 23, sem relação direta).
Exemplos resolvidos: 0. Tabelas: 2 (16.1, 16.2). Ábacos: 0.
Páginas lidas: ≈ 6 (350–353 em detalhe; 346–363 e 366–372 por filtro).

## LOC-PFAFSTETTER-CHUVAS-INTENSAS — Pfafstetter, Chuvas Intensas no Brasil (DNOS, 1957)
Vigência: referência histórica brasileira (98 postos, dados até ~1950); licença: uso-interno; 426 p., **quase todo em OCR** (números de OCR: "OCR, conferir na imagem"). Papel no Drenagem: só localizar e citar (o Clima entrega a IDF).
- Introdução, método (coleta, análise de frequência, gráficos, ajuste): p. 7–21. Formulação: P = K·[a·t + b·log(1 + c·t)], K = T^(α + β/T^γ) com γ = 0,25 (p. 13–17; OCR da expressão incompleto, conferir na imagem); TR pelo "método californiano" T = n/m (p. 10); validade 5 min a 6 dias e 0,2 a 100 anos ou mais (p. 21).
- **Exemplos numéricos** p. 22–23 (impressos 16–17): Campos 40 min/5 anos; Belo Horizonte 6 h/50 anos; Porto Alegre 2 h com TR inverso. Conferi os dois últimos recalculando a fórmula (fecham em ≤ 1 %).
- Quadros I–III (folhas de coleta, exemplo Vassouras) p. 24–26; **Quadro IV** (lista dos 98 postos, coordenadas, anos) p. 27–33; **Salvador (Ondina), posto nº 69, é o único posto da Bahia**: lista p. 31, gráficos P×T p. 278–280, coeficiente β p. 397. Gráficos P×T×duração por posto: p. 33–386 (Fortaleza p. 139); estação-ano p. 387–392; **Quadro V** (α por duração, 0,108 a 0,176) p. 393; **Quadro VI** (β por posto, 1 h a 6 d) p. 393–398; curvas K p. 399–400; P(T = 1 ano) × duração com a, b, c por posto p. 401–425 (média dos 98 postos p. 425).
- Lacunas: nada de Sento Sé/Sobradinho; nenhum posto do semiárido baiano além de Salvador; sem IDF no formato i = a·T^b/(t+c)^d.
Páginas lidas: ≈ 45 (1–33 e amostras de 381–397 e 424–426).

## LOC-NEH-TC-ESCOAMENTO-PLANO — NRCS NEH Parte 630, cap. 15 Time of Concentration (maio/2010)
Vigência: edição final de 2010 (rodapé "210-VI-NEH, May 2010"; o mapa do Hidráulico registra NRCS-NEH630-CH15 como rascunho de out/2008); licença: domínio público; 29 p.
- Tipos de escoamento e Tt = ℓ/(3600·V) p. 7–8; lag e relação **L = 0,6·Tc** (Eq. 15-3) p. 9–10; **método do lag** (Eq. 15-4a/b; comprimento Eq. 15-5, ℓ = 209·A^0,6; declividade Y por contornos) p. 11; **método da velocidade** (Eq. 15-7) p. 11–15; **Tab. 15-1** n de escoamento laminar (liso 0,011; relvas etc.) p. 12; **Eq. 15-8** laminar, Tt = 0,007·(n·ℓ)^0,8/(P2^0,5·S^0,4) em h, limite ℓ ≤ 100 ft p. 12–13; **Tab. 15-2** comprimentos máximos (McCuen-Spiess) p. 13; escoamento raso concentrado **Fig. 15-4 e Tab. 15-3** (V = k·S^0,5; k = 20,328 pavimento e ravinas, 16,135 canal gramado, 9,965, 8,762, 6,962 pastagem curta, 5,032, 2,516) p. 14; canal/Manning (Eq. 15-10) p. 14–15; variação do lag, Tab. 15-4 p. 16; **exemplos** p. 18–21; Anexo 15A (Kirpich Eq. 15A-1 p. 25, coeficiente "0,007" na leitura do OCR; Kerby 15A-2; Simas 15A-5/6; equações de área Tab. 15A-1; Folmar-Miller p. 26); Anexo 15B, curvas de escoamento raso de Cerrelli-Humpal p. 27–29.
- Exemplos resolvidos: (a) método do lag, Mawney Brook p. 18; (b) método da velocidade, três trechos p. 18–21 (Tab. 15-5 e 15-6 p. 20).
Lacunas: sem Giandotti, Dooge, Picking; sem Kirpich "modificada".
Páginas lidas: ≈ 14 (7–14 e 18–22 em detalhe; 23–29 por filtro).

## LOC-PLANILHA-ESCOAMENTO-PLANO-001 e -REDENCAO — planilhas internas de tempo de escoamento plano (14/04/2022)
Vigência: planilhas de trabalho (sem versão normativa); licença: uso-interno; aba útil "FAA" em ambas.
- **001**: n, L (m), i (mm/h), S → L(ft) = L·3,28084; i(in/h) = i/25,4; Tti(min) = 0,933/i^0,4·(n·L/√S)^0,6 (E1); Vti = L/Tti/60 (E2).
- **Redenção**: mesma célula FAA (n = 0,011) mais IDF i = a·(t + c)^b (a = 73,4068; b = −0,7893; c = 0,5892; t em h) e conversão para t em min (B15–B17: a = 1858,79; c = 35,352); p = i·t; **tanque**: V = 13 500 m²·p/1000·0,9, h = 2 m, largura 6 m, comprimento; IDF de T = 5 anos i = K·T^a·(t + b)^−c (K = 8460,202; a = 0,177; b = 41,05; c = 1,092). Célula M19 sem rótulo.
- Atenção: a aba chama-se "FAA", mas a fórmula é a da **onda cinemática** (divergências 2 e 5).

## USGS-WSP1849 — Barnes, Roughness Characteristics of Natural Channels (1967; reimpressão 1987)
Vigência: clássico sem substituta; licença: domínio público; 219 p. (nativo).
- Fórmulas e procedimento de cálculo do n (Eq. 1–6, condutividade) p. 11–13; aplicação dos coeficientes p. 13–14; **50 canais** (4 páginas cada: dados, croquis e seções, fotos), ordenados por n de 0,024 (Columbia R. em Vernita, p. 16–19) a 0,075 (Rock Creek, p. 212–215); índices p. 9–11 e 217–219.
- Cada canal: Q de pico, A, largura, profundidade, R, V, comprimento e queda; d50 e d84 do leito. Exemplo legível: Vernita (p. 16).
Lacunas: sem tabela-resumo de n por tipo de canal; as fotos não têm texto.
Páginas lidas: ≈ 8 (3–5, 11–14, 16).

## USACE-EM1110-2-1413 — Hydrologic Analysis of Interior Areas (versão CED C11-002)
Vigência: **o catálogo diz 1987 "a conferir"; o texto traz série até 2010, risco residual, costeiro e HEC-RAS: é revisão posterior** (provável 2018), em cópia de curso PDH (paginação própria). Licença: domínio público; 125 p.
- Cap. 2 conceitos p. 9; cap. 3 estudos hidrológicos p. 14; **cap. 4 áreas ribeirinhas** p. 27–61 (período de registro, eventos discretos, **frequência coincidente**, Eq. 4-1 de probabilidade total p. 48; Tab. 4-1 coincidência; **Tab. 4-4 grau de correlação R**, forte 0,7–1,0, moderada 0,4–0,7, fraca < 0,4, p. ≈ 55–56); cap. 5 costeiro p. 62; cap. 6 medidas (bombas, comportas) p. 74; cap. 7 risco residual p. 85; cap. 8 exemplo de período de registro p. 93; **cap. 9 exemplo de frequência coincidente** p. 100–110 (Tab. 9-1 a 9-6); cap. 10 galgamento p. 111.
- Aderência ao Drenagem: baixa (planície com dique); sem Tc, racional, CN ou HU para dimensionar bueiros.
Páginas lidas: ≈ 18 (3–6, 48–49, 55–56, 100–110).

## Divergências entre fontes do grupo (7) e nota de catálogo (1)
1. Posição de plotagem e TR: Pfafstetter T = n/m "californiano" (p. 10) × McCuen Weibull, T = (n+1)/m (Eq. 5-5a; p. 257–258 e 273–274).
2. Coeficiente da onda cinemática do escoamento laminar: McCuen 0,938 (Ex. 3-12 usa 34,28 = 0,938·(n·L/√S)^0,6; p. 164–165) × planilhas 0,933 (E1 das duas; ≈ 0,5 % menor).
3. Comprimento máximo do escoamento laminar: McCuen cita TR-55 com 300 ft, "muitos" com 100 ft, e critério n·L/√S ≈ 100 (p. 165; OCR a conferir) × NEH-630 cap. 15, limite de 100 ft e Tab. 15-2 (p. 12–13). A planilha-001 (L = 492 ft) viola os dois.
4. C do racional e período de retorno: McCuen separa as colunas "< 25 anos" e "≥ 25 anos" na Tab. 7-9 e manda usar a média da faixa (p. 395) × Eslamian "C igual para qualquer recorrência", com fa de 1,0 a 1,25 e limite de 80 ha (p. 352).
5. A fórmula "FAA": McCuen Eq. 3-52 depende do C do racional (p. 172) × aba "FAA" das planilhas (onda cinemática com i e n, sem C). Rótulo trocado ou fórmula diferente.
6. Kirpich: NEH-630 Eq. 15A-1 lê "0,007" (p. 25) × McCuen Tennessee "0,0078" (p. 172); ambos de OCR (conferir na imagem). O McCuen só traz multiplicadores 0,4 e 0,2; não há "1,5×".
7. Edição do NEH-630 cap. 15: este arquivo (maio/2010; Eq. 15-4a/b; exemplos p. 18–21) × entrada NRCS-NEH630-CH15 do mapa do Hidráulico (rascunho out/2008; Eq. 15-3a/b; exemplos p. 16–19). Conferir qual é o padrão do agente.
8. (catálogo) EM 1110-2-1413: ano 1987 no catálogo × conteúdo de revisão recente.
Sem divergência: CN urbano (McCuen Tab. 3-18 p. 176 × Eslamian Tab. 16.2 p. 351); lag = 0,6·Tc (NEH p. 9) × Tc = 1,67·lag (McCuen p. 172–173).

## Gabaritos para calculadora
Unidade original da fonte. "calc." = conferi aritmeticamente; "derivado" = não legível/impresso, calculei.
1. McCuen Ex. 3-12, p. 165: onda cinemática (Eq. 3-47), n = 0,15, L = 120 ft, S = 0,002. Com i = 8 in/h: Tt = 14,9 min; iterando (i = 4,6 in/h): 18,6 min. Versão SCS (Eq. 3-48), P2 = 3,12 in: 28,8 min (calc. 28,8). O resultado final depende da IDF da Fig. 4-4: testar só o passo com i dado.
2. McCuen Ex. 3-13, p. 165–166 (velocidade): antes = 140/0,25 + 260/1,40 + 480/2,1 = 560 + 186 + 229 s = 975 s = 16,2 min; depois = 238 + 24 + 214 + 71 s = 547 s = 9,1 min (tubo 15 in, n = 0,011, S = 0,009, V a seção plena 5,9 ft/s, calc.).
3. McCuen Ex. 3-14, p. 166–170: existente 12,6 + 19,1 + 12,6 = 44,3 min; desenvolvido 1,1 + 1,6 + 2,3 + 5,1 + 5,7 = 15,8 min.
4. McCuen Ex. 9-23, p. 557–558 (lag do SCS, Eq. 3-56): A = 300 ac, L = 6500 ft, S = 1,3 %, CN = 92 → tc = 1,34 h (calc. 1,342); qp = 726·300/(640·1,34) = 254 ft³/s; tp = 0,893 h; base 2,381 h (valores das legendas da Fig. 9-27).
5. NEH-630 cap. 15, p. 18 (lag): A = 0,17 mi², ℓ = 3865 ft, Y = 4,79 %, CN = 63 (S = 5,87 in) → **Tc = 1,14 h** (calc. 1,143).
6. NEH-630 cap. 15, p. 18–21 (velocidade): laminar 100 ft, n = 0,15, P2 = 3,6 in, S = 0,08 → 0,09 h (calc. 0,089); R-1 = 0,09 + 0,11 + 0,39 + 0,20 + 0,21 = 1,00 h; R-2 = 6000 ft/5,2 ft/s = 0,32 h; R-3 = 0,43 h (Tab. 15-6); **Tc = 1,75 h**.
7. McCuen Ex. 7-9, p. 397 (racional): A = 2,4 ac, C = 0,95, i = 8,6 in/h → 19,6 ft³/s (derivado); com tc mínimo de 15 min, i = 6,5 → 15 ft³/s (impresso).
8. McCuen Ex. 7-11, p. 398–399: sub-áreas 5,3, 7,2 e 6,4 ac; C = 0,2, 0,4, 0,6; i(15 min) = 5,4 in/h → 5,7 e 15,6 ft³/s; total 18,9 ac, C ponderado 0,412, i = 4,8 → **37,4 ft³/s** (soma simples 41,8; hidrograma do racional, Ex. 9-22, p. 553: 28,1 ft³/s).
9. McCuen Ex. 7-15, p. 405–406 (SCS-CN): P = 7 in, CN = 75 → S = 3,333 in; Ia = 0,667 in; **Q = 4,15 in**. Ex. 7-18, p. 408–409, P = 7 in: CN 55 → 2,12; 70 → 3,62; 75 → 4,15; 83 → 5,03 in; Q ponderado = 3,62 in. Ex. 7-17, p. 408: Q com CN ponderado 0,28 in × Q ponderado 0,385 in (ponderar Q, não CN).
10. McCuen Ex. 7-19, p. 415–416 (método gráfico): tc = 2960 s = 0,82 h; CN = 66; P = 4,8 in; Q = 1,59 in; Ia/P = 0,21; qu = 370 ft³/s/mi²/in (Fig. 7-9c); A = 23 ac → qp ≈ 21,1 ft³/s (derivado: 370·23/640·1,59; o valor impresso está ilegível).
11. McCuen Ex. 5-5, p. 273–274 (LP3): 38 anos; média dos logs 3,722; desvio 0,2804; assimetria −0,731 (usar −0,7); **Q100 = 16 992 ft³/s (log 4,2285)**; 10 000 ft³/s → p ≈ 0,155 (≈ 6 anos).
12. McCuen Tab. 9-17, p. 556 (HU adimensional SCS, legível): t/tp = 0,5 → q/qp 0,470 e Qa/Q 0,065; 1,0 → 1,000 e 0,375; 1,5 → 0,680 e 0,700.
13. Pfafstetter, p. 22–23: BH 6 h/50 anos: α = 0,174 e 0,176 (média 0,175), β = 0,04, K = 2,10, P(T = 1) = 58 mm → **122 mm**; Porto Alegre 2 h: P = 102,2 mm, P(T = 1) = 36 mm, α = 0,166, β = 0,08 → K = 2,84, **T = 290 anos** (calc.: K(290) = 2,86); Campos 40 min/5 anos: 44 mm (30 min) e 50 mm (1 h) → 46 mm (OCR, conferir na imagem).
14. Planilha-001 (aba FAA): n = 0,13; L = 150 m; i = 186 mm/h; S = 0,15 → **Tti = 9,0114 min; Vti = 0,27743 m/s**.
15. Planilha-Redenção (aba FAA): n = 0,011; L = 141,86 m; i = 186 mm/h; S = 0,0097 → **Tti = 4,5032 min; Vti = 0,52503 m/s**; IDF a/b/c com t = 0,12539 h → i = 95,704 mm/h, p = 12,000 mm; T = 5 anos, t = 7 min → i = 163,94 mm/h; tanque (13 500 m²) V = 281,46 m³, área 140,73 m² (h = 2 m), comprimento 23,455 m (largura 6 m).
16. EM 1110-2-1413, Tab. 9-1 e 9-5, p. 103 e 109 (probabilidade total, Eq. 4-1): pesos 40, 20, 15, 10, 5, 4, 3, 2, 1 % (B9 a B1); na cota 471,55 ft P(Zc|Bi) = 0,102; 0,103; 0,104; 0,107; 0,111; 0,118; 0,136; 0,176; 0,467 → **P = 0,110** (calc. 0,1106); cota 491,32 ft → 0,002. Tab. 9-6: P = 0,01 → 481,1 ft; P = 0,50 → 466,8 ft.
17. WSP 1849, Vernita, p. 16: Q = 406 000 ft³/s; A = 47 100 ft²; R = 26,16 ft; V = 8,65 ft/s; **n = 0,024** (S não legível no `_texto`; calc.: Q/A = 8,62).

## Pendências para a F5/F7
(§2 de `PENDENCIAS_DE_TREINAMENTO.md`, só o que o G1 consegue conferir)
- `hidrologia.py`, **Dooge**: não conferível no G1 (aparece só como citação de roteamento, p. 380, 625, 632; não é fórmula de Tc). **Giandotti** e **Picking**: ausentes do grupo inteiro; manter "a confirmar" ou buscar em DNIT/DAEE. **Kirpich**: Tennessee e Pensilvânia no McCuen p. 172 (equações ilegíveis) e Eq. 15A-1 no NEH p. 25; os multiplicadores 0,4 e 0,2 existem; **o "1,5×" da Kirpich modificada não aparece** no G1 (não conferido). **DNOS e tabela K por terreno**: o Pfafstetter só traz chuva, sem K nem Tc.
- Tc laminar: decidir entre 0,938 (McCuen) e 0,933 (planilhas), e entre a Eq. 3-47 (usa i) e a NEH Eq. 15-8 (usa P2 de 2 anos/24 h, 0,007 em h); adotar o limite de 100 ft do NEH. Conferir na imagem o 0,007 do NEH e o 0,0078 do McCuen.
- Racional: o limite de área não aparece no trecho lido do McCuen (p. 394–395, a confirmar); o Eslamian dá 80 ha. Continua valendo a lição de que cada projeto usa um limite.
- SCS-CN: Q, S, Ia = 0,2·S e a regra P < 0,2·S → Q = 0 estão no McCuen p. 405 e no Eslamian p. 352; os gabaritos 9 e 10 servem de teste de 1 %.
- HU: Tab. 9-17 (p. 556) e a constante 726 (triangular) × 484 (curvilíneo) do McCuen p. 557 precisam ser escolhidas e documentadas (ler na imagem).
- Frequência e TR: o Clima entrega a IDF; o Drenagem deve citar Pfafstetter (Salvador é o único posto baiano) com o aviso do TR californiano (divergência 1).
- Fora do G1 (ficam para G2 e G4): bueiros (McCuen cap. 8, p. 452 em diante, não lido), classes de tubo, drenos (Hooghoudt, Ernst, Glover-Dumm, fator 1,16) e envoltórios.
- Catálogo: corrigir o ano do EM 1110-2-1413 (divergência 8) e registrar que o NEH cap. 15 do corpus próprio é a edição de maio/2010 (divergência 7).

---

# Mapa parcial F3 — G2-bueiros-tubos

Convenções: `[ID p. N]` = página física do PDF (marcador `<!-- p. N -->` do `_texto`). Nenhuma página destes documentos está marcada `<!-- ocr -->`. O mapa localiza; valores de norma não são transcritos, exceto os usados como índice. Os documentos FHWA/USACE são em unidades inglesas (cfs, ft, fps) salvo indicação.
Gabaritos marcados "(conferido)" foram recalculados por Manning/Marston; diferença entre parênteses.

## Resumo do grupo
| ID | Mapeado | Páginas lidas |
|---|---|---|
| LOC-ABTC-ALTERACOES-NBR8890 | sim | 1–5 |
| LOC-ABTC-ESPEC-TUBOS-LICITACOES | sim | 1–7 |
| LOC-ABTC-HISTORIA-MANNING | sim | 1–12 |
| LOC-ABTC-COMPARACAO-CONCRETO-POLIMERO | sim | 1–11 |
| LOC-ABTC-PROJETO-ESTRUTURAL-TUBOS | sim | ~22 (2–5, 15–17, 21, 29–31, 33–34, 36–37, 43, 45–49, 54) |
| LOC-ABTC-PROJETO-ESTRUTURAL-ADUELAS | parcial (estrutural: só localizado) | ~12 (1–11, 38, 57) |
| FHWA-HDS3 | sim | ~14 (7–8, 15–16, 53–55, 108–109) |
| FHWA-HEC13 | sim | ~22 (1, 7–12, 100, 111, 119, 121, 127, 135, 139, 141, 147, 152) |
| FHWA-HY8-V770-NRCS | sim (sem conteúdo técnico) | 1–2 |
| USACE-EM1110-2-2902 | sim | ~14 (1, 4–5, 25, 27, 66–72) |
| LOC-SISCCOH-MANUAL-V11 | sim | ~8 (16, 22, 25, 37, 39–42) |
Total lido ≈ 130 p. (teto 300; nenhum documento acima de 80).

---

## LOC-ABTC-ALTERACOES-NBR8890 — Alterações da NBR 8890 (versão 2020)
- Ano: n/d no catálogo; trata a NBR 8890:2020 [p. 1]. Vigência: não informada no catálogo (reflete a norma vigente de 2020). Licença: uso-interno. 5 p.
- **Temas:** 14 mudanças da NBR 8890:2020 [p. 1–5]: cimento resistente a sulfatos em rede contaminada por esgoto (item 1, p. 1); tubos com reforço secundário de fibras (RSF) e só fibras (RF), RF até DN 1000 (itens 2, 3, 12; p. 1, 4); macho-e-fêmea só a partir de DN 500, abaixo disso ponta-e-bolsa (item 4, p. 1); DN > 600 obrigatoriamente armado/RF/RSF (item 10, p. 4); classe acima de PA4/EA4 → galeria celular NBR 15396 (item 11, p. 4); "carga de fissura" vira "força mínima isenta de fissura" (item 6, p. 4); itens de aquisição que o comprador informa (item 14, p. 5).
- **Tabelas (espessura mínima de parede, mm, por classe):** Tab. 1 ponta e bolsa, água pluvial, PS1/PS2/PA1–PA4, DN 200–2000 [p. 2]; Tab. 2 macho e fêmea, DN 500–2000 [p. 3]; Tab. 3 junta elástica, esgoto/água pluvial, ES/EA2–EA4 [p. 3]. Traz também comprimento útil mínimo (L) e da bolsa (B) e folga máxima do encaixe (Ca).
- Exemplos resolvidos: nenhum. Ábacos: nenhum.
- Lacuna: não há valores de força de ruptura/fissura (estão em ESPEC p. 3–4 e TUBOS p. 46) nem recobrimento de terra.

## LOC-ABTC-ESPEC-TUBOS-LICITACOES — Como especificar tubos de concreto em licitação (8 passos)
- Ano: n/d (cita NBR 8890 vigente, ≥ 2020 pelo conteúdo). Vigência: n/d. Licença: uso-interno. 7 p.
- **Temas:** unidade de compra em metro linear (passo 1, p. 2); DN = diâmetro interno, 200–2000 mm (passo 2, p. 2); água pluvial (P) × esgoto (E) (passo 3, p. 2); armado (A) × simples (S), DN > 600 sempre armado (passo 4, p. 3); classe 1–4 e influência de berço, carga móvel, tipo de assentamento e altura de aterro (passo 5, p. 3); encaixe PB × MF (passo 6, p. 4–5); junta JE × JR (passo 7, p. 5); norma (passo 8, p. 5).
- **Tabelas:** Tab. 1 compressão diametral de tubos simples PS1/PS2/ES, DN 200–600, kN/m [p. 3]; **Tab. 2 força mínima isenta de fissura e de ruptura por classe PA1–PA4 / EA2–EA4, DN 300–2000, kN/m** (e Qd = força por unidade de DN) [p. 4]; nota b: ruptura = 1,5 × isenta de fissura [p. 4]. É a tabela de classes a usar para "classe de tubo" (idêntica à Tab. 5.1 de TUBOS p. 46).
- **Exemplos de especificação (3):** Ex. 1 DN1200, 65 kN/m, MF, JR → "DN1200 PA2 MF JR"; Ex. 2 DN800 esgoto, 85 kN/m, PB → "DN800 EA4 PB JE"; Ex. 3 DN400, 37 kN/m → "DN400 PA4 PB JR" (abaixo de DN 500 só PB) [p. 6].
- Lacuna: não explica como obter a força de ensaio (ver TUBOS p. 45 e o software ABTC citado na p. 3).

## LOC-ABTC-HISTORIA-MANNING — História do coeficiente de Manning (ACPA 2004, trad. ABTC)
- Ano: tradução jul/2004 [p. 3]. Vigência: n/d (histórica). Licença: uso-interno. 12 p.
- **Temas:** valores de laboratório × valores de projeto (fator de 20–30 %) [p. 5]; Kutter × Manning [p. 5]; testes Iowa 1926 [p. 6], Minnesota 1950 [p. 7], Alberta/Canadá 1962 [p. 6–7], Flórida/St. Anthony Falls (efeito de juntas, ~1,9 %) [p. 8–9], Alberta e Utah 1986 concreto × PVC [p. 9], lodo e biofilme em esgoto, n ≈ 0,013 após operação [p. 10].
- **Tabelas (n):** Tab. 1 n de laboratório × projeto (drenagem/esgoto) por material (concreto, plástico, cimento-amianto, ferro, metal corrugado) [p. 5]; Tab. 2 Iowa 1926 (Kutter e Manning, DN 300–750) [p. 6]; Tab. 3 e 4 Minnesota 1950 [p. 7] (texto da Tab. 4 aparece com colunas trocadas na extração: conferir na imagem); Tab. 5 Alberta 1986 [p. 9]; Tab. 6 Utah 1986 [p. 9].
- Exemplos resolvidos: nenhum. Ábacos: nenhum.
- Uso: respalda o n de tubo de concreto (lab ≈ 0,010; projeto 0,012 em drenagem e 0,013 em esgoto) e a leitura do legado Xingó (ver Divergências).

## LOC-ABTC-COMPARACAO-CONCRETO-POLIMERO — Concreto (NBR 8890) × PEAD/PVC/PP (NBR ISO 21138)
- Ano: ≥ 2018 (bibliografia com acesso 2018, p. 11). Vigência: n/d. Licença: uso-interno. 11 p. Documento de posição do fabricante (parcial).
- **Temas:** normas aplicáveis [p. 2–3]; manuseio e equipamento [p. 3–4]; assentamento (vala, aterro, cravação × só vala) [p. 4]; **dimensionamento hidráulico: n = 0,013 recomendado pela norma de esgoto independente do material; ovalização e sedimento anulam a vantagem de rugosidade** [p. 4–5]; resistência e fluência [p. 6]; fogo e sol [p. 7–8]; execução e reaterro [p. 8]; ocorrências e custo final [p. 9–10].
- Tabelas/ábacos/exemplos: nenhum. Sem números hidráulicos próprios. Uso: apenas argumento para escolha de material; tratar como fonte interessada.

## LOC-ABTC-PROJETO-ESTRUTURAL-TUBOS — Projeto estrutural de tubos circulares de concreto armado (El Debs, ABTC/IBTS)
- Ano: 2003, 1ª ed. [p. 2]; baseado na NBR 8890/2003 [p. 4]. Vigência: anterior à NBR 8890:2020 (ver Divergências). Licença: uso-interno. 69 p.
- **Temas e localização:** Cap. 1 comportamento, tipos de instalação e solos [p. 8–16]; Cap. 2 cargas do solo (vala Cv, aterro projeção positiva Cap, projeção negativa Can) [p. 16–24] — equações: k = tg²(45°−φ/2) (1.1) [p. 15]; q = Cv·γ·b² (vala) [p. 17]; q = Cap·γ·d² (aterro, projeção positiva) [p. 19]; q para projeção negativa [p. 22]; Cap. 3 sobrecargas (propagação, veículos-tipo, ferrovia, aeroporto) [p. 25–36]; Cap. 4 fatores de equivalência (vala, aterro, bases) [p. 37–44]; Cap. 5 classe do tubo (Fens = γ(q+qm)/α) [p. 45–46]; Cap. 6 armadura em telas soldadas [p. 47–62]; Cap. 7 fabricação/transporte [p. 62–66].
- **Recobrimento de terra mínimo:** hs ≥ 0,6 m para tráfego normal; tráfego pesado exige recomendação específica [p. 29]. Coeficiente de impacto por cobrimento: ≤0,30 m → 1,3; ≤0,60 → 1,2; ≤0,90 → 1,1; > 0,90 → 1,0 (Tab. 3.3) [p. 33].
- **Tabelas:** Tab. 1.1 solos (kμ e γ, 5 tipos) [p. 16]; Tab. 2.1 razão de recalque [p. 21]; Tab. 3.1–3.2 pesos e características dos veículos-tipo [p. 30–31]; Tab. 3.4 trens-tipo [p. 34]; Tab. 3.5 aeroviária [p. 36]; **Tab. 4.1 fatores de equivalência em vala (classes A–D)** [p. 37]; Tab. 4.2 η e Tab. 4.3 χ [p. 43]; **Tab. 5.1 classes PA1–PA4 e EA2–EA4 por DN (fissura/ruptura, kN/m) e coeficientes de segurança γ = 1,0 (fissura) e 1,5 (ruptura)** [p. 45–46]; Tab. 6.1 cobrimento da armadura [p. 48]; Tab. 6.2–6.4 esforços e armadura [p. 49, 54].
- **Exemplos resolvidos:** nenhum cálculo numérico completo (as ocorrências de "exemplo" no texto são ilustrativas). Ábacos: Fig. 3.1 pressão vertical × altura de terra [p. 24].
- Lacuna: não há tabela de altura de aterro máxima/mínima por classe e DN (a ABTC remete ao software, ESPEC p. 3).

## LOC-ABTC-PROJETO-ESTRUTURAL-ADUELAS — Galerias e canais com aduelas (NBR 15396:2017)
- Ano: ≥ 2017 (cita NBR 15396:2017 e NBR 6118:2014, p. 8–10). Vigência: n/d. Licença: uso-interno. 85 p. Pertence ao domínio de estruturas (PLANO §1.2); aqui só localização.
- **Temas:** Cap. 1 galerias de seção fechada, aberturas de 1,0×1,0 a 4,0×4,0 m [p. 8–56] (comportamento, p. 9–10: efeito de arqueamento só quando hs > largura externa); Cap. 2 canais em U [p. 57–85] (estrutura análoga). Cargas e sobrecargas: Tab. 3.1–3.5 [p. 20–30]; módulo de reação do solo Tab. 4.1 [p. 32]; coeficientes Tab. 5.1 [p. 35]; cobrimento NBR 15396 [p. 38]; dimensionamento Tab. 6.1–6.2 [p. 42–43]. Cap. 2 repete as tabelas [p. 64–76].
- Exemplos resolvidos: não localizados. Ábacos: nenhum.
- Uso para o Drenagem: apenas aduela como alternativa a tubo quando a classe passa de PA4 (ALTERACOES p. 4).

## FHWA-HDS3 — Design Charts for Open-Channel Flow (FHWA-EPD-86-102; 1961)
- Ano: 1961. Vigência (catálogo): arquivada, sem substituta direta. Licença: domínio público. 116 p. **Numeração**: página impressa + 8 = página do PDF (ex.: "Chart 55, p. 68" impresso = p. 76 do PDF).
- **Temas:** princípios [p. 11–14 a confirmar]; Cap. 3 canais retangulares, trapezoidais (2:1) e triangulares [p. 15–45]; Cap. 4 canais gramados [p. 46–52]; **Cap. 5 tubos circulares [p. 53–81]**; Cap. 6 tubo-arco [p. 82–96]; Cap. 7 tubos ovais [p. 97–107]; Apêndices A (tabelas) [p. 108–110], B (construção dos ábacos) [p. 110–111], C (nomograma de Manning) [p. 112].
- **Ábacos (83 charts; unidades inglesas):** 1–14 retangular (n = 0,015; larguras 2–20 ft); 15–28 trapezoidal 2:1 (n = 0,03); 29 triangular; 30–34 gramado; **35–51 tubo circular 12–96 in (n = 0,015, escalas auxiliares 0,012 e 0,024) [p. 53–64 do índice impresso → PDF ~p. 45–72]**; 52–54 circular a seção plena; **55 relações parciais Q/Qfull, V/Vfull, S/Sfull por d/D [PDF p. 76]**; 56–57 profundidade crítica e carga específica; 58–60 declividade crítica; 61–73 tubo-arco; 74–82 oval; 83 nomograma Manning [PDF p. 112]. Índice dos charts: [p. 8].
- **Tabelas:** Tab. 1 n de Manning (tubo de concreto 0,011–0,013; corrugado; vitrificado; revestimentos; gramados) [p. 108]; Tab. 2 e 3 velocidades permissíveis (solo erodível e gramado) [p. 109]; Tab. 4 fator de vazão para caixa fechada [p. 109]; Tab. 5 guia de retardância [p. 109].
- **Exemplos resolvidos (25, leitura de gráfico):** 1–5 retangular/trapezoidal/caixa [p. 15–16]; 6–9 gramado [p. 46–47]; **10–17 tubo circular [p. 53–55]**; 18–21 tubo-arco [p. 83]; 22–25 oval [p. 98].
- Lacuna: tubo parcialmente cheio em unidade SI não existe; leitura de gráfico limita a conferência a ~1 % (ver Gabaritos).

## FHWA-HEC13 — Hydraulic Design of Improved Inlets for Culverts (Circular nº 13, agosto/1972)
- Ano: 1972 [p. 1]. Vigência: carimbo "Archival… superseded… HDS-5 3rd edition 2012" em todas as páginas; arquivada. Licença: domínio público. 185 p.
- **Temas:** entradas melhoradas (biseladas, cônicas lateral e de fundo, anel biselado) [p. 33–52]; procedimento de projeto [p. 53–60 a confirmar]; considerações gerais (hidrologia, HW admissível, detritos, sedimento, velocidade de saída, comprimento) [p. 41–44 do índice impresso]; Apêndice A exemplos [p. 109–152]; B desenvolvimento dos ábacos [p. 153–163 a confirmar]; C levantamento de campo [p. 164 em diante, a confirmar]; D formulários de cálculo [p. 167+ impresso].
- **Ábacos (19 charts, unidades inglesas):** 1–4 carga a seção plena (caixa, concreto, CMP padrão, CMP chapa estrutural) [p. 79–82]; 5–6 profundidade crítica retangular e circular [p. 83–84]; 7 HW de caixa em controle de entrada [p. 85]; 8–10 HW de caixa (90°, esconsa, alas 18–45°) [p. 86–88]; 11–12 HW de tubo de concreto e CMP em controle de entrada [p. 89–90; Chart 12 em p. 90]; 13 anel biselado [p. 91]; 14–19 gargalo e face de entradas cônicas [p. 92–97, a confirmar]. Índice: [p. 7–8].
- **Tabelas:** **Tab. 1 coeficiente de perda de entrada ke por tipo de estrutura (concreto, CMP, caixa)** [p. 100]; Tab. 2 n de Manning de canais naturais [p. 101]; Tab. 3–8 valores auxiliares BD^3/2, D^3/2, D^5/2, áreas de elipse e de segmento circular [p. 102–105].
- **Exemplos resolvidos (6):** Ex. 1 caixa, Q = 1000 cfs (TR 50), S0 = 0,05, AHW 200, cota de saída 172,5, L = 350 ft, canal a jusante trapezoidal 8 ft, 2:1, n = 0,03 → caixa simples 7×6 ft [p. 111, 119]; Ex. 2a mesmos dados, tubo de concreto n = 0,012 → D = 7 ft com entrada cônica [p. 121, 127]; Ex. 2b CMP [p. 129–134]; Ex. 3 caixa com S0 = 0,005 → caixa 10×9 ft biselada, FALL 0,8 ft [p. 135, 139]; Ex. 4 tubo, Q = 150 cfs, AHW 100, saída 75, L = 350, S0 = 0,05 [p. 141]; Ex. 5 mesmos com AHW 96 → CMP 48 in [p. 147, 152].
- Lacuna: só unidades inglesas; sem exemplos com n/ke do Brasil.

## FHWA-HY8-V770-NRCS — HY-8 v7.70 (UG 210-22-3, NRCS, 08/12/2021)
- Ano: 2021 (catálogo 2023). Vigência: HY-8 vigente é a 8.0 (2024). Licença: domínio público. 2 p.
- Conteúdo: comunicado de disponibilidade do programa e referência às bases HDS-5 (2012) e HEC-14 (2006) [p. 1]. **Sem ábaco, tabela ou exemplo.** Serve só para registrar que o programa implementa HDS-5/HEC-14 e como cópia de conferência cruzada (catálogo). Nada a mapear além disso.

## USACE-EM1110-2-2902 — Conduits, Culverts, and Pipes (edição antiga)
- Ano: 31/out/1997, Change 1 em 31/mar/1998 [p. 1] (catálogo diz 1998). Vigência: substituída pela edição de 2020 (catálogo). Licença: domínio público. 87 p. Cabeçalho da p. 1 imprime "EM 1110-2-2909" (erro tipográfico do original).
- **Temas:** Cap. 2 conduto moldado no local [p. 12–21 aprox.]; Cap. 3 tubo circular de concreto armado para pequenas barragens e diques (instalação, cargas, análise D-load) [p. 21–29]; Cap. 4 tubo metálico corrugado [p. 30–35]; Cap. 5 bueiros de concreto (cargas, Fig. 5-2 cargas rodoferroviárias, Fig. 5-5 coeficiente Cc de projeção positiva) [p. 36–44]; Cap. 6 tubo plástico, recobrimento e compactação (p. 46 tabela de compactação do berço) [p. 45–53]; Cap. 8 cravação [p. 54–57]; Apêndices A (referências) [p. 58–64], B (exemplos) [p. 65–80]. Conteúdo é carregamento e estrutura; **não traz hidráulica de bueiro (HW, controle de entrada/saída)**.
- **Tabelas:** Tab. 3-1 fator de berço Bf em vala (comum 1,5; primeira classe 1,9; berço de concreto 2,5) [p. 27] e repetida [p. 71]; Tab. 3-2 constantes χ (Xa) por taxa de projeção e tipo de berço, e η (Xp) [p. 27]; Eq. 3-1 (Bf em aterro) e Eq. 3-2 (D0,01 = Hf·WT/(Si·Bf), Hf = 1,3) [p. 25]; Tab. 4-1 normas ASTM [p. 32]; classes ASTM C76 e D0,01 [p. 71].
- **Exemplos resolvidos (Apêndice B):** Cap. 2 cargas prisma, trincheira e aterro [p. 66–70] (**Cd, W de vala: ver Gabaritos**); Cap. 3 D-load de tubo de concreto, Classe ASTM C76M III [p. 71–72]; Cap. 4 CMP pela ASTM A 796, carga de terra e viva [p. 73–74]; método de elementos finitos [p. 75+ a confirmar].
- Atenção: na p. 71–72 o Bf impresso (6,098) não reproduz o D0,01 = 57 N/m/mm (exigiria Bf ≈ 3,33 com W = 175 130 N/m, Hf = 1,3, Si = 1200 mm); página sem OCR mas a fórmula está truncada. Não usar como gabarito sem conferir na imagem.

## LOC-SISCCOH-MANUAL-V11 — Manual técnico do SisCCoH v1.1
- Ano: n/d no catálogo. Vigência: n/d. Licença: uso-interno. 87 p. Numeração: seção/página impressa = página do PDF − 1.
- **Temas:** condutos simples (Hazen-Williams e Universal) [p. 15–17]; canais regulares (máxima eficiência, uniforme, crítico, variado, ressalto, enrocamento) [p. 18–38]; **4.1 Bueiros [p. 39–42]**; degraus (nappe e skimming) [p. 43–63]; bacias de dissipação por ressalto e em enrocamento [p. 64–71]; confluência e curvas [p. 73–83]. Dissipação é do Hidráulico (D3): só registrada.
- **Bueiros (p. 39–41):** três regimes (canal livre, orifício, conduto forçado); declividade crítica, Qadm e U para tubular e celular em regime sub e supercrítico (Eq. 4.1–4.10); orifício (Eq. 4.11–4.15); afogado por energia com Ce e Cs (Eq. 4.16); **redução de capacidade de 5 % por linha adicional (duplo = 95 %, triplo = 90 %)** [p. 41]. É método por Manning/orifício, não por HDS-5 (controle de entrada não existe).
- **Tabelas:** Tab. 3.1 geometria/profundidade normal de seções [p. 18]; Tab. 3.3 curvas de remanso [p. 27]; Tab. 3.4 classificação do ressalto por Froude [p. 30]; Tab. 4.1 canal em trechos [p. 60]; Tab. 5.1 coeficientes de Boussinesq [p. 74].
- **Exemplos (resultados em figuras de tela, não em texto, salvo onde indicado):** 2.1 conduto simples DN 400, 1 km, 100 L/s, concreto [p. 16]; 3.1 [p. 19]; 3.2 retangular uniforme [p. 22]; **3.3 profundidade crítica, trapezoidal 1:1, b = 1 m, Q = 14 m³/s → yc = 1,661 m (texto)** [p. 25]; 3.4 [p. 28, 35]; 3.5 canal em enrocamento (Q = 2,5 m³/s, 2:1, b = 1,5 m, S = 2 %, Cu = 2,12) [p. 37]; **3.6 bueiro tubular duplo de concreto, Q = 16 m³/s, n = 0,015, S = 2 %, D = 1,80 m, L = 4,20 m, aterro 3 m** [p. 41] (sem resultado em texto); 4.1–4.7 degraus e bacias [p. 46–70]; 5.1–5.2 [p. 77, 82].
- Uso: conferência cruzada, **não é fonte primária**; os coeficientes impressos nas equações estão truncados no `_texto` (conferir no PDF).

---

## Divergências entre fontes do grupo (6)
1. **Fator de berço em vala:** TUBOS Tab. 4.1 [p. 37] usa classes A–D (A 2,25–3,4; B 1,9; C 1,5; D 1,1) × EM 2902 Tab. 3-1 [p. 27, 71] usa comum 1,5, primeira classe 1,9, berço de concreto 2,5, sem "D" (aparece só como "impermissible", η = 1,31). Valores coincidem onde há correspondência (1,5; 1,9; 2,5 dentro de 2,25–3,4). **χ e η iguais** em TUBOS Tab. 4.3/4.2 [p. 43] e EM 2902 Tab. 3-2 [p. 27].
2. **Edição da norma NBR 8890:** TUBOS [p. 4, 46] reflete 2003 ("carga de fissura/trinca", γ de ruptura 1,5, cobrimento Tab. 6.1 p. 48) × ALTERACOES [p. 4] versão 2020 ("força mínima isenta de fissura", RSF/RF, DN > 600 armado, MF só ≥ DN 500). A tabela de classes é igual nas duas ([TUBOS p. 46] = [ESPEC p. 4]); o que muda é terminologia, tipos de reforço e proibição de MF < DN 500. Cobrimento da armadura pela NBR 8890:2020 não está no grupo.
3. **n de Manning do tubo de concreto:** ABTC HISTORIA Tab. 1 [p. 5]: laboratório 0,009–0,011, projeto 0,012 (drenagem) e 0,013 (esgoto); medições Minnesota ≈ 0,010–0,011 [p. 7], Alberta/Utah ≈ 0,010 [p. 9], Iowa 0,012–0,013 [p. 6] × HDS-3 Tab. 1 concreto 0,011–0,013 [p. 108] e charts-base 0,015 (circular) [p. 53] × SisCCoH Ex. 3.6 usa 0,015 [p. 41] × COMPARACAO n = 0,013 [p. 5].
4. **Coeficiente de entrada:** HEC-13 Tab. 1 [p. 100] varia por tipo de entrada (0,2 a 0,9; caixa com alas paralelas 0,7; tubo de concreto com muro e alas, ponta de macho 0,2 e aresta viva 0,5) × SisCCoH [p. 41] cita Ce de 0,2 a 0,7 (e saída 0,3–1,0) e, no mesmo trecho, orienta Cs = 0,2 e Ce = 1,0 "respectivamente" (ordem trocada/inconsistente dentro da própria página).
5. **Redução por linhas múltiplas:** SisCCoH [p. 41] impõe −5 % de capacidade por linha adicional; HEC-13 e EM 2902 não trazem regra equivalente (EM 2902 trata apenas carga de tubos múltiplos em vala, p. 27). Sem divergência numérica, mas é regra sem primária no corpus.
6. **Método hidráulico de bueiro:** SisCCoH [p. 39–41] verifica por Manning/orifício/conduto forçado; HEC-13 [p. 33–52, 79–91] e HDS-5 usam controle de entrada e saída. Coincide com a lição "projetos do acervo usam Manning/orifício, nunca HDS-5" (PENDENCIAS §4).
Complemento ao Hidráulico: HEC-13 Tab. 1 [p. 100] confirma os valores de ke da Tab. C.2 do HDS-5 listada em H13/H20 (sem divergência); não refeito.

## Ábacos, tabelas e exemplos localizados (resumo)
- Ábacos: 102 (HDS-3: 83; HEC-13: 19). Tabelas relevantes: ≈ 60 (ABTC ≈ 35; HDS-3 5; HEC-13 8; EM 2902 4; SisCCoH 5). Exemplos resolvidos: ≈ 65 (HDS-3 25; HEC-13 6; EM 2902 3+; SisCCoH ≈ 16; ABTC-ESPEC 3 de especificação; ABTC-ALT/HIST/COMP/TUBOS/ADUELAS 0 numéricos).

## Lacunas do grupo
- Nenhum documento traz a **tabela de altura de aterro mínima/máxima por classe e DN** da NBR 8890:2020 (só o software ABTC); só hs ≥ 0,6 m (TUBOS p. 29) e fatores de impacto (p. 33).
- Sem hidráulica de bueiro em SI nem exemplo de HW pelo Brasil; HDS-5 (Hidráulico) é a primária. HEC-13 e HDS-3 só em unidades inglesas.
- HY-8 7.70: só nota de disponibilidade; sem manual.
- EM 2902: edição antiga; sem hidráulica; D-load do exemplo com Bf inconsistente.
- SisCCoH: resultados dos exemplos em figuras (sem número em texto, exceto Ex. 3.3).
- ADUELAS: estrutural; exemplos não localizados.

## Gabaritos para calculadora
Tolerância alvo 1 %. "Recalculo" = conferência independente feita aqui por Manning/Marston.

| # | Fonte e página | Entradas | Resultado impresso | Recálculo / observação |
|---|---|---|---|---|
| 1 | SisCCoH Ex. 3.3 [p. 25] | canal trapezoidal 1:1, b = 1 m, Q = 14 m³/s | yc = 1,661 m | 1,6610 m (0,0 %). **Usável (1 %)** |
| 2 | EM 2902 App. B Cap. 2 [p. 67–68] | Kμ' = 0,15, H = 2,44 m, Bd = 1,52 m, γ = 18 850 N/m³ | Cd = 1,274; We1 = 55 483 N/m | Cd = 1,2740; We = 55 483 N/m (0,0 %). **Usável**. We2 = γ·Bc·H com Bc = 1,22 m = 56 113 N/m (confere) |
| 3 | HDS-3 Ex. 10 [p. 53] | circular 30 in, n = 0,015, S = 0,005, Q = 25 cfs | dn = 2,05 ft; Vn = 5,8 fps; dc = 1,7 ft; Vc = 6,9 fps | dn = 2,037 ft (0,6 %); V = 5,84 fps (0,7 %). Usável com tolerância 1 % |
| 4 | HDS-3 Ex. 12 [p. 54] | circular 72 in, n = 0,030, S = 0,003, d = 3,0 ft | Q = 50 cfs; V = 3,5 fps (via escala n = 0,015 ÷ 2) | Q = 50,26 cfs (0,5 %) |
| 5 | HDS-3 Ex. 14 [p. 55] | 48 in, n = 0,011, S = 0,005, d = 3,0 ft | Qfull = 120; Q/Qfull = 0,91; Q = 109 cfs | Qfull = 120,1; Q = 109,5 (0,4 %) |
| 6 | HDS-3 Ex. 15 [p. 55] | 10 ft, n = 0,012, S = 0,0006, Q = 315 cfs | d/D = 0,63; dn = 6,3 ft; V = 6,0 fps | d = 6,27 ft (0,5 %); V = 6,08 fps (1,3 %: leitura de gráfico) |
| 7 | HDS-3 Ex. 16 [p. 55] | 10 ft, n = 0,025, Q = 600 cfs, d = 7,5 ft | Sf = 0,0058 | 0,00585 (0,9 %) |
| 8 | HDS-3 Ex. 17 [p. 55] | 10 ft, n = 0,012, Q = 600 cfs | dc = 5,9 ft; Sc = 0,0026; Hc = 8,4 ft | dc = 5,87; Sc = 0,00266; Hc = 8,30 ft (1,2 %). Hc fora de 1 % |
| 9 | HDS-3 Ex. 1 e 3 [p. 15–16] | Ex. 1: retangular 5 ft, n = 0,015, S = 0,01, Q = 200; Ex. 3: trapezoidal b = 6 ft, 2:1, d = 4 ft, n = 0,03, S = 0,005 | Ex. 1: dn = 3,2 ft, V = 12,5 fps, dc = 3,7 ft; Ex. 3: Q = 350 cfs, V = 6,1 fps | Ex. 1: 3,216 ft; Ex. 3: Q = 346,1 cfs (1,1 %: leitura de gráfico). Não usar como teste de 1 % |
| 10 | HDS-3 Ex. 5 [p. 16] | caixa 6×4 ft, Q = 150 cfs, S = 0,001; fator de Tab. 4 | D/B = 0,667 → fator 1,27; Q ajustado 190 cfs; Sf = 0,0031 | fator de Tab. 4 [p. 109] (a conferir); Sf lido de chart |
| 11 | ABTC-ESPEC Ex. 1–3 [p. 6] | DN1200/65 kN/m; DN800 esgoto/85; DN400/37 | PA2; EA4; PA4 | seleção por "menor classe com força isenta de fissura ≥ F" na Tab. 2 [p. 4]: PA2 = 72 ≥ 65; EA4 = 96 ≥ 85; PA4 = 48 ≥ 37 (PA3 = 36 < 37). **Usável (seleção exata)** |
| 12 | HEC-13 Ex. 1, 2a, 3, 5 [p. 111, 121, 135, 147] | Q = 1000 cfs, AHW, L etc. (acima) | caixa 7×6 ft; D = 7 ft; caixa 10×9 ft; CMP 48 in | Resultados de seleção (arredondados a dimensões comerciais); HW intermediário em gráfico. Teste só de ordem de grandeza |
| 13 | EM 2902 Tab. 3-1/3-2, Eq. 3-2 [p. 25, 27] | berço e taxa de projeção | Bf trench 1,5/1,9/2,5; χ; η | tabelas conferidas contra TUBOS Tab. 4.1–4.3; **Eq. 3-1 truncada**, não testar |

## Pendências para a F5/F7
Referente a `PENDENCIAS_DE_TREINAMENTO.md` §2 (itens deste grupo):
- **`bueiros.py` — Ke de alas paralelas 0,2 (DNIT) × 0,7 (HDS-5):** HEC-13 Tab. 1 [p. 100] **confirma 0,7 para caixa de concreto com alas paralelas e aresta viva no topo** (0,2 se a aresta do topo for arredondada/chanfrada). Para tubo de concreto com muro de testa e alas: 0,2 (ponta de macho/bolsa) e 0,5 (aresta viva). O 0,2 do DNIT pode corresponder à entrada com aresta tratada; verificar no DNIT (fora do grupo). Padrão HDS-5/HEC-13 mantido.
- **`bueiros.py` — A_c = 0,60 D² do tubular (ajuste à Tab. 1 do DNIT) e V de saída do HDS-5 p. 280:** não cobertos por este grupo (sem fonte aqui). Para tubo circular parcialmente cheio, HDS-3 Chart 55 [p. 76] e a geometria exata do segmento reproduzem os exemplos 10–17 em 0,4–1,3 %; sugerir usar geometria exata e não 0,60 D² nos testes.
- **`drenos.py` — fator 1,16 de Glover-Dumm, Ernst:** nada neste grupo.
- **Fórmula legada do Xingó (33,5·D^2,67·i^0,5) ≈ n = 0,0093:** abaixo do n de projeto 0,012–0,013 e ao nível do mínimo de laboratório do tubo liso (0,009–0,010) [HISTORIA p. 5, 7, 9]; reforça que o legado usa n de laboratório sem fator de 20–30 % e subestima a perda. Registrar como caso negativo (D-lição PENDENCIAS §4).
- **Classe de tubo (indicativa) — o que a F5 pode implementar:** Fens = γ(q + qm)/α [TUBOS p. 45], γ = 1,0 fissura e 1,5 ruptura, α = fator de berço (TUBOS Tab. 4.1 p. 37; EM 2902 Tab. 3-1 p. 27), classe = menor com força isenta de fissura ≥ Fens (ESPEC Tab. 2 p. 4). Cv/Cap exigem as figuras/equações das p. 17–22 (conferir imagens). hs mínimo 0,6 m [TUBOS p. 29]. Falta tabela de altura máxima de aterro por classe.
- **Escolha de n de tubo:** decidir uma regra única (ABTC 0,012 drenagem; 0,013 esgoto/misto; 0,015 do HDS-3 como base de gráfico) antes de comparar com SisCCoH Ex. 3.6 (n = 0,015).
- **xfail do CSB BTCC-17 e Baixio (Manning × acervo):** nada resolvido aqui; este grupo só reforça que Manning pleno ≠ controle de entrada (divergência 6).
- Para o consolidador: duplicidade provável de HY-8 7.70 (2 p.) sem valor técnico; considerar excluir da lista de skills.

---

# Mapa parcial F3 - grupo G3-estradas (drenagem de estradas e plataformas)

Convenções: `p. N` = página física do PDF (marcador `<!-- p. N -->` do `_texto`). Onde há página impressa diferente, vai dita.
Páginas marcadas `<!-- ocr -->` (só o LOC-DNIT-ALBUM-2018): números lidos por OCR saem "(OCR, conferir na imagem)".
O mapa localiza; não substitui a fonte. Valores só como índice de localização, com página conferida no `_texto`.
Complemento do mapa do Hidráulico: seção H14 (`../Especialista Hidraulica/referencias/MAPA_DE_CONHECIMENTO.md`) cobre DNIT-DREN
(IPR-724) p. 158-186 (valetas, sarjetas), HEC-15, HEC-22; este grupo traz os documentos que lá não aparecem.

Taxonomia (PLANO.md): tudo aqui alimenta `drenagem-de-estradas-e-plataformas` (sarjeta, valeta, descida, caixa, dispositivos-tipo,
drenagem profunda); IPR-726, IME e WSDOT tocam também hidrologia de projeto e bueiros; DERPR-ES-DR-06/07 tocam drenagem subsuperficial.

---

## 1. Normas DNIT de serviço (especificações; sem dimensionamento hidráulico)

### DNIT-ES018-2023 - DNIT 018/2023-ES Drenagem - Sarjetas e valetas
Ano 2023 | vigente (substitui 018/2006) | licença aberta | 7 p. | lido: p. 1-7 (inteiro).
- Temas: objeto e referências p. 1-2; definições de sarjeta (triangular, trapezoidal, retangular, semicircular) e valeta p. 2
  (triangular: declividade transversal máxima junto ao acostamento 25 % = 4H:1V, p. 2; segurança lateral pela NBR 15486, p. 2);
  materiais (concreto fck mín. 20 MPa aos 28 dias, revestimento vegetal) p. 3; execução convencional e com extrusora p. 3-4;
  revestimento vegetal p. 4-5; sem revestimento (uso restrito a chuva moderada, solo resistente, declividade moderada) p. 5;
  condicionantes ambientais p. 5; inspeção, controle geométrico (tolerância 1 %) p. 5-6; medição (por metro) p. 6; índice remissivo p. 7.
- Ábacos, tabelas e exemplos: nenhum (norma de serviço). Dimensões vêm do projeto ou do Álbum IPR-736 (p. 2-3).
- Anomalia interna: numeração de "Sarjeta Triangular" é 3.2 no corpo (p. 2) e 3.1.1 no índice (p. 7).

### DNIT-ES020-2006 - DNIT 020/2006-ES Drenagem - Meios-fios e guias
Ano 2006 | edição de 2006, revisão posterior não verificada | aberta | 6 p. | lido: p. 2, 3, 5 e varredura de seções.
- Temas: definições de meio-fio e guia p. 2; concreto de cimento e concreto asfáltico p. 2-3; execução (fôrmas a 3 m, junta a cada
  1,00 m nas curvas, juntas de dilatação) p. 3-4; inspeção p. 4-5; fck estimado × fck p. 5; medição p. 5.
- Ábacos, tabelas, exemplos: nenhum. Referencia o Álbum do DNER/ENEMAX de 1988 (p. 2), anterior ao IPR-736 de 2018.

### DNIT-ES021-2023 - DNIT 021/2023-ES Entradas e descidas d'água (com errata 1)
Ano 2023 | vigente, versão corrigida 11/2024 | aberta | 7 p. | lido: p. 2-5.
- Temas: definições de descida e entrada d'água p. 2; materiais (concreto fck mín. 20 MPa, aço CA-50) p. 2; execução in loco
  p. 3, pré-moldada semicircular (meia-cana) p. 4; juntas de dilatação em descidas > 10 m (nota 3) p. 4; inspeção e tolerância
  geométrica 1 % p. 5; medição: entrada por unidade, descida por metro, p. 5.
- Ábacos, tabelas, exemplos: nenhum.

## 2. Instrução de projeto DNIT

### DNIT-IPR726-2006 - Diretrizes básicas para estudos e projetos rodoviários (Escopos Básicos / Instruções de Serviço, 3ª ed.)
Ano 2006 | edição na coletânea vigente do IPR | aberta | 487 p. | lido: p. 1-8, 257-262, 305-309, 462-465, 472-475 (27 p.).
Observação: o livro é de escopos; nenhuma sarjeta ou valeta é dimensionada nele. Paginação impressa = PDF − 3.
- IS-203 Estudos Hidrológicos (impressa 252-258): p. 255-261. TR usuais por espécie de obra (superficial 5-10 anos; ponte 100; pontilhão 50; valores de
  subsuperficial e bueiros com colunas misturadas na extração, conferir na imagem) p. 258; Tc de drenagem superficial = 5 min,
  p. 258; método por faixa de área p. 259; Tabela 1 "Classificação dos Problemas" de bueiros existentes (ERM, ERJ, ES, RE, AS, AL, ED)
  p. 259-260; planilha de descargas por bacia (colunas Nº, estaca, A, L, desnível, i%, Tc, C, I, Q para 10/15/25/50 anos, h/D) p. 261.
- IS-210 Projeto de Drenagem (impressa 302-308): p. 305-311. Classes de drenagem (transposição de talvegues; superficial: valetas de
  proteção de corte e de aterro, sarjetas, valeta de canteiro central, descida, saída, caixa coletora, bueiro de greide, dissipadores,
  escalonamento, corta-rios; subsuperficial: camada drenante, drenos rasos; profunda: drenos profundos, espinha de peixe, colchão,
  sub-horizontais, valetões, verticais; travessia urbana) p. 307-308; drenagem do pavimento necessária se precipitação anual
  > 1500 mm e TMD > 500 veículos comerciais p. 307; memória de cálculo obrigatória p. 308; planilha de bueiros de grota p. 309.
- IS-239 Estudos hidrológicos, rodovias vicinais (impressa 459-461): p. 462-464: mesma tabela de TR (p. 463), Tc de drenagem
  superficial = 10 min (p. 463), racional < 10 km² e hidrograma > 10 km² (p. 464).
- IS-242 Projeto de drenagem, rodovias vicinais (impressa 469-471): p. 472-473; lista dispositivos de superfície (valeta, sarjeta de
  corte, banqueta de aterro, entrada, descida, caixa coletora, caixa de amortecimento, escalonamento) e tipos de bueiro.
- Ábacos/exemplos: nenhum ábaco; 2 tabelas úteis (TR, p. 258; classificação de problemas, p. 259-260); 1 planilha-modelo (p. 261).
- Não lidos: os demais escopos (EB/IS de geometria, pavimento, OAE etc.), fora do tema.

## 3. Normas estaduais DER/PR 2023 (espelho de conferência da DNIT)

Todas: ano 2023, vigentes (Deliberação 111/2023), aberta. Estrutura comum: 1 objetivo, 2 referências, 3 definições, 4 condições gerais
(proibido em dia de chuva), 5 materiais/equipamento/execução, 6 manejo ambiental, 7-8 controle, 9 aceitação, 10 medição, 11 pagamento.

### DERPR-ES-DR-01-23 - Sarjetas e valetas (10 p.) | lido p. 3-7, 9, 10
- Definições p. 3; concreto fck mín. 20 MPa e solo-cimento (IP ≤ 18 %, LL ≤ 40 %, #200 ≤ 40 %, cimento ≥ 10 %, 1,5 MPa) p. 4;
  execução com gabaritos a 2,00 m, juntas a cada 12 m, saída de sarjeta de corte prolongada ≈ 10 m ("bigodes") p. 5-6;
  vegetal e solo-cimento p. 6; sem revestimento p. 7; aceitação (dimensões ≤ 10 %, espessura ±10 %) p. 9; declividade longitudinal
  mínima 0,5 % com demolição se menor, e rejeição se maior que a máxima de projeto p. 10; medição p. 10.
- Ábacos/exemplos: nenhum.

### DERPR-ES-DR-03-23 - Entradas e descidas d'água (8 p.) | lido p. 3-5, 7, 8
- Definições (descidas de corte retangulares em degraus que descarregam em caixa; descidas de aterro tipo rápido ou em degraus com
  caixa dissipadora; entradas) p. 3; concreto 20 MPa, armadura ES-OA 03 p. 4; execução rápida/trapezoidal p. 4-5, em degraus p. 5;
  tolerância geométrica 5 % p. 7; medição p. 8. Exemplos: nenhum.

### DERPR-ES-DR-05-23 - Bocas e caixas para bueiros tubulares (9 p.) | lido p. 3-5, 8, 9
- Caixas coletoras × bocas p. 3; concreto 20 MPa, ciclópico (pedra de mão 10-15 cm), alvenaria p. 3-4; execução p. 4-5;
  tolerância 5 % p. 8; medição (caixa por volume, boca normal por unidade, discriminando DN e nº de linhas) p. 8-9. Cruza com G2.

### DERPR-ES-DR-06-23 - Drenos longitudinais profundos (12 p.) | lido p. 3-12
- Definições (contínuo × descontínuo; cego × com tubo) p. 3; tubos (concreto perfurado/poroso, PVC, PEAD, PRFV, cerâmico) p. 3-4;
  material drenante e filtrante, critérios (não colmatar, permeabilidade, compatível com furos) p. 4-5;
  Quadro 1 granulometria da areia filtrante (peneiras 3/8" a nº 100) p. 5; Quadro 2 resistência à ruptura de tubos de concreto
  DN 200-600 (comprimento útil, espessura, bolsa, força mín. 24-36 kN/m) p. 6; rejunte 1:4 p. 6; boca de saída fck 15 MPa p. 7;
  vala com declividade de fundo ≥ 1 % p. 7 e p. 11; camada de fundo 10 cm, camadas de 20 cm, sobreposição de geotêxtil 20 cm com
  costura ou 50 cm sem costura p. 8; saída defletida ≈ 45°, raio ≈ 5 m, ≥ 1 m além do offset p. 8; controle e aceitação p. 9-11.
- Ábacos/tabelas: 2 quadros (p. 5, p. 6). Exemplos: nenhum. Anomalia: texto de tubos porosos cita "Quadro 1" (p. 6) onde deveria ser o Quadro 2.

### DERPR-ES-DR-07-23 - Drenos subsuperficiais (10 p.) | lido p. 3-10
- Definições (transversais e longitudinais rasos, no subleito) p. 3; filtrante/drenante p. 4; Quadro 1 granulometria (igual ao DR-06) p. 4;
  tubos p. 5; execução (vala ≥ 1 %, camadas ≤ 30 cm, bocas de saída em aterro) p. 5-6; contínuo e descontínuo com tubo, cego p. 6-7;
  controle (granulometria a cada 1000 m, 5 tubos por km) p. 8; medição p. 10. Anomalia: texto do Quadro 1 diz "dreno profundo" (p. 4).
- Ábacos/exemplos: 1 quadro (p. 4); nenhum exemplo. Cruza com G4 (subsuperficial).

## 4. Dispositivos-tipo

### LOC-DNIT-ALBUM-2018 - Álbum de Projetos-Tipo de Dispositivos de Drenagem, IPR-736, 5ª ed. 2018
Ano 2018 | vigência não registrada no catálogo (5ª edição) | licença aberta | 227 p. | camada de texto: OCR local em 203 p. (parcial) |
lido: p. 8, 23-27, 213-214 + varredura do título de cada página. Todos os números abaixo: (OCR, conferir na imagem).
- Natureza: "documento orientador e não normativo"; o projetista faz o dimensionamento hidráulico (p. 23). Só desenhos, quantitativos e tabelas
  de armadura; sem memória hidráulica de sarjeta ou valeta.
- Sumário p. 9-11. Capítulo 1 Drenagem superficial p. 25-49: valetas de proteção de corte VPC-01 a 04 (p. 27; consumos médios por metro
  de escavação, apiloamento, grama, concreto fck ≥ 20 MPa, argamassa asfáltica; guias de madeira a cada 2 m e junta asfáltica a cada 12 m
  nas notas) e de aterro VPA (p. 28); sarjetas triangulares de concreto STC (p. 29-30), de grama STG (p. 31), trapezoidais SZC (p. 32),
  de canteiro central SCC (p. 33); transposição de sarjetas (p. 34-35); meios-fios MFC (p. 36-37); entradas EDA (p. 38-39); descidas
  tipo rápido DAR (p. 40-42), em degraus de corte DCD (p. 43) e de aterro DAD (p. 44); dissipadores DES/DED (p. 45-47); caixas
  coletoras de sarjeta CCS com grelha de concreto ou ferro (p. 48-49).
- Capítulo 2 Drenagem subterrânea: drenos profundos em solo DPS (p. 53), em rocha DPR (p. 54), bocas de saída BSD (p. 55), camada
  drenante em rocha (p. 56). Cap. 3 subsuperficial DSS (p. 59). Cap. 4 taludes e encostas, drenos sub-horizontais DSH (p. 63).
  Cap. 5 pluvial urbana: bocas de lobo (p. 67-70), caixas de ligação CLP (p. 71), poços de visita (p. 72-74).
- Capítulo 6 transposição de talvegues (cruza com G2): berços (p. 77), tubos de concreto armado e armaduras (p. 78), bueiros tubulares
  simples, duplo e triplo (p. 79-84), caixa coletora de talvegue CCT (p. 86); bueiros celulares (p. 87-120); Cap. 7 aduelas
  (p. 125-203); Cap. 8 minitúnel (p. 205-210; tabela de vazão a 1 % na p. 207, a confirmar).
- Capítulo 9 dispositivos lineares pré-fabricados (p. 213-227): critérios de dimensionamento (Manning + continuidade, TR 10 anos,
  Tc 6 min, lâmina ≥ 3 cm abaixo da grelha) p. 214; Tabela 1 classes de carga (NBR 10160) p. 215; vazão de canal com grelha (a 0,6 %) p. 217;
  Tabela 4 (concreto polímero) p. 219; Tabela 6 (polietileno/polipropileno) p. 221.
- Lacuna: p. 24 e 26 em branco, p. 8 sem texto; 24 p. sem OCR (catálogo "parcial"); tabelas de armadura de galerias (p. 127-203) não lidas.

## 5. Manual de drenagem de pavimentos dos EUA

### FHWA-HEC12 - HEC-12 Drainage of Highway Pavements (FHWA-TS-84-202), 1984
Ano 1984 | arquivada, absorvida pelo HEC-22 (marca d'água "Archival/Superceded" no texto) | domínio público | 155 p. | camada de texto
completa (só p. 55 vazia); paginação impressa = PDF − 17 (p. 1 impressa = p. 18 PDF) | lido: p. 5-14, 19-22, 29-32, 34-36, 38-43, 46, 48-49, 110, 113.
- Índice p. 5-8; símbolos p. 12-14. Geometria: greide mínimo de sarjeta 0,3 % (0,2 % em terreno muito plano) e 0,3 % a 50 ft de ponto
  baixo, L/A ≤ 167, p. 19; Tabela 1 declividades transversais p. 21; valetas laterais e de canteiro p. 21-22.
- Hidrologia: racional, Tabela 2 de C p. 29, C ponderado p. 30, IDF p. 30-31, Tc = escoamento superficial por onda cinemática
  (eq. 2 em imagem; K = 56 em unidades inglesas) p. 31, Chart 1 p. 33, tempo de sarjeta e Tabela 3 p. 34-35, Chart 2 p. 35; outros métodos (TRRL, SCS TR-55) p. 38.
- Fluxo em sarjetas (eq. 4, K = 0,56 inglês) p. 39; Chart 3 p. 40; Chart 4 p. 42; composta p. 41-43, Chart 5 p. 44; seção circular
  (Chart 6) p. 48; sag p. 46; relação de capacidades p. 49.
- Bocas de lobo: p. 53 em diante (Charts 7-15, p. 72-98); localização e espaçamento Cap. 9; valeta de canteiro e talude Cap. 10, Charts 16-17 p. 111-112;
  Apêndice A IDF p. 124-137; Apêndice B velocidade média em canal triangular p. 140; Apêndices C, D (composta, parabólica) p. 143+.
- Exemplos resolvidos (30): Ex. 1 p. 32; 2 p. 34; 3 p. 36; 4-5 p. 41 (5 conclui p. 43); 6-7 p. 46; 8 p. 49; 9 p. 73; 10 p. 75; 11 p. 80;
  12-13 p. 83-85; 14 p. 87; 15 p. 93; 16 p. 97; 17 p. 99; 18-20 p. 102-103; 21 p. 104; 22 p. 106; 23 p. 110; 24-25 p. 113; 26-28 p. 124-137;
  29 p. 143; 30 p. 150. Unidade original: pés, ft³/s, in/h. Úteis para sarjeta e valeta de estrada de serviço: 1, 2, 4, 5, 6, 8, 23-25.
- Cobertura para G3: sarjeta triangular com meio-fio (equivalente à sarjeta de aterro/pé de corte), valeta trapezoidal de canteiro,
  swale circular. Não cobre valeta de proteção de corte, descida d'água nem caixa de dissipação.

## 6. Apostila brasileira de drenagem de rodovias

### LOC-IME-DRENAGEM-URBANA-RODOVIAS - IME, Curso de Drenagem Urbana e Meio Ambiente (apostila, Cel P. R. D. Morales)
Ano não registrado | vigência não registrada | licença uso-interno | 176 p. | texto nativo (sem OCR), slides com equações em imagem;
paginação impressa ≈ PDF − 9/10 | lido: p. 4-6, 28-36, 42-60, 82-87, 142-160 (56 p.).
- Índice p. 4-6. Hidrologia p. 28-34: Tc por California Culverts, George Ribeiro, Ven Te Chow, Picking (p. 28-29), IDF p. 30,
  fórmulas empíricas de vazão (Iszkowski, tabelas de m e k; Burkli-Ziegler; Aguiar-DNOCS TR 100; racional e Tabela 3.4 de C) p. 31-34.
- Drenagem superficial: elementos p. 42-43; sarjeta pé-de-corte e de aterro p. 44-45; disposições construtivas p. 47; valeta de proteção
  de corte p. 48-50, de aterro p. 51, de derivação p. 52; dimensionamento de canais, valetas e sarjetas (racional, sequência de cálculo
  com Manning, altura crítica, folga) p. 53-55; sarjeta de corte (L1, L2, C1, C2) p. 55; sarjeta de aterro p. 55; vala lateral,
  corta-rios, bacia de captação p. 57-59; descida d'água p. 60.
- Drenagem profunda: dimensionamento (Darcy, K = 100 d10², Scobey, Hazen-Williams) p. 82-83; dreno cego p. 84; comprimento crítico
  p. 84; espaçamento E = 2h·√(K/q) p. 85; muros de arrimo p. 86-87. Bueiros p. 89-118 (cruza com G2); conservação p. 118-119.
- Anexo I: trechos das Diretrizes IPR (IS-210/IS-242) p. 137-143; Anexo II cálculos (energia específica, regime crítico de bueiros
  tubular e celular) p. 145-155; Anexo III exercícios p. 157-160 (enunciados, sem respostas); Anexo IV orçamento p. 165-166 (TD-04-7, TH-04-9; a confirmar).
- Tabelas: Tab. 3.1 IDF de 3 cidades p. 30; Tab. 3.2/3.3 de Iszkowski p. 32; Tab. 3.4 de C p. 34; Tab. 4.2 folga em canais de concreto p. 55.
- Exemplos resolvidos: Tc (p. 29); energia específica (p. 145); derivação do regime crítico (p. 150-153). Nenhum exemplo numérico resolvido de sarjeta
  ou valeta; os 5 exercícios de superfície (p. 157-158) não trazem resposta.

## 7. Manual estadual dos EUA

### WSDOT-HYDRAULICS-M2303-12 - WSDOT Hydraulics Manual M 23-03.12
Ano 2025 no catálogo, mas o rodapé de todas as páginas diz "April 2026" | referência de prática, não norma brasileira | aberta | 325 p. |
texto nativo; PDF = impressa + 14 (cap. 1), +36 (cap. 2), +86 (cap. 4), +100 (cap. 5) | lido: p. 3-15, 63, 92-93, 102-111, 128-130.
- Índice p. 3-8; listas de figuras e tabelas p. 9-14. Cap. 2 hidrologia (racional, Tabela 2-2 de C p. 45, Tabela 2-3 p. 47, Tabelas de
  chuva p. 49-50; exemplos do racional só como figuras sem texto p. 63). Cap. 4 canais p. 87-100: critical depth p. 92-93, Tabela 4-1
  (referências de n) p. 93. Cap. 5 pavimentos p. 101-120: racional com Tc = 5 min p. 102; ranhuras e inlets de dreno proibidos p. 103;
  Tabela 5-1 TR × espaçamento permitido p. 104-105; inlets em greide e em sag, eqs. 5-1 a 5-6 (imagens) p. 105-109; valeta lateral
  (TR 10 anos, folga 0,5 ft, talude ≤ 2H:1V, grama só < 6 % e < 5 fps) p. 109; tipos de inlet p. 111-117; Tabela 5-2 grelhas p. 118.
  Cap. 6 coletores e subdrenos: espaçamento p. 124, n = 0,013 p. 128, drain pipe e underdrain p. 128-129 (≥ 6 in, limpeza a cada 150 ft).
- Exemplos resolvidos com números: nenhum extraído (equações e figuras do cap. 2 e 5 estão como imagem).
- Não lidos: cap. 3 (bueiros, G2), 7-10.

---

## Divergências entre fontes (cada uma com as duas ou mais páginas)

1. Resistência do concreto de sarjeta: 20 MPa [DNIT-ES018-2023 p. 3; DERPR-ES-DR-01-23 p. 4; Álbum p. 27 (OCR, fck ≥ 20 MPa)] × 11 MPa (110 kgf/cm²)
   [LOC-IME p. 47]. Complemento ao Hidráulico: DNIT-DREN p. 166-186 registra 15 MPa (H14).
2. Juntas de dilatação de sarjeta e valeta: a cada 12 m [DNIT-ES018 p. 4; DERPR-01 p. 6; Álbum p. 27 (OCR)] × corte 30 m e aterro 6 m [IME p. 47].
3. Espaçamento dos gabaritos de execução: 3,0 m [DNIT-ES018 p. 4] × 2,00 m [DERPR-01 p. 5; Álbum p. 27 (OCR)].
4. Tolerância de dimensão da seção: 1 % em pontos isolados [DNIT-ES018 p. 6; DNIT-ES021 p. 5] × 5 % [DERPR-03 p. 7; DERPR-05 p. 8] × 10 % [DERPR-01 p. 9].
5. Argamassa de rejunte/preenchimento de juntas de descida: 1:3 [DNIT-ES021 p. 3 e p. 4] × 1:4 [DERPR-03 p. 5].
6. Declividade longitudinal mínima do dispositivo: 0,5 % [DERPR-01 p. 10, vale para sarjeta e valeta, revestida ou não] × 0,3 % (0,2 % em
   terreno plano) para gutter com meio-fio [FHWA-HEC12 p. 19]. Contextos distintos; a norma brasileira federal (DNIT-ES018) não fixa o valor.
7. Tc de projeto para drenagem superficial: 5 min [IPR726 p. 258; WSDOT p. 102; IME p. 53 "5 min ou conforme o Tc"] × 6 min [Álbum p. 214, OCR]
   × 10 min [IPR726 p. 463, IS-239]. Divergência já dentro do IPR-726 (p. 258 × p. 463).
8. TR da drenagem superficial: 5 a 10 anos [IPR726 p. 258; p. 463] × 10 anos DNER e 25 anos ENGEFER [IME p. 53] × 10 anos (sag 50) [WSDOT p. 104] × 10 anos [Álbum p. 214, OCR].
9. Faixas de área do método racional: racional até 4 km², racional corrigido de 4 a 10 km², HUT acima de 10 km² [IPR726 p. 259, limites c-e] ×
   racional abaixo de 10 km² e hidrograma acima [IPR726 p. 259, tabela da mesma página; p. 464; IME p. 34].
10. Vazão do dreno de tubo em seção plena × "meia seção": o texto diz "fluxo a meia seção" e as fórmulas de Scobey (Q = 0,2113·C·D^2,625·I^0,5)
    e Hazen-Williams (Q = 0,2785·C·D^2,63·I^0,54) correspondem a tubo cheio (0,2113 = 0,269·π/4, recalculado) [IME p. 83].
11. Folga de valeta: f = 0,2 h até 0,3 m³/s, fórmula para 0,3 a 10 m³/s ilegível (EQ 4.7) e 10 a 18 cm em canal de concreto por faixa de vazão [IME p. 54-55]
    × 0,5 ft (≈ 0,15 m) fixos com TR 10 anos [WSDOT p. 109].
12. Tabelas de coeficiente de deflúvio com estrutura diferente (declividade × cobertura, faixas amplas) [IME p. 34] × tipologia de superfície
    [FHWA-HEC12 p. 29; WSDOT p. 45]; não usar uma como substituta da outra sem registrar.
13. Vigência do WSDOT: catálogo "abril de 2025" × rodapé "April 2026" em todas as páginas [p. 5, 102].

Anomalias internas (não contam como divergência entre fontes): numeração da sarjeta triangular [DNIT-ES018 p. 2 × p. 7]; "Quadro 1" no lugar do
Quadro 2 [DERPR-06 p. 6]; "dreno profundo" copiado no texto de subsuperficial [DERPR-07 p. 4]; EQ. 4.1/4.2 do IME com I em "m/h" e "cm/h" misturados [p. 53].

Divergência com o mapa do Hidráulico (H12 e H14): H14 registra para o IPR-724 Tc = 5 min e TR 10 anos de sarjeta (DNIT-DREN p. 166-186); isso concorda
com IPR726 p. 258 e WSDOT p. 102, mas não com IS-239 (p. 463, 10 min) nem com o Álbum (p. 214, 6 min).

## Lacunas do grupo
- Nenhum exemplo numérico resolvido de sarjeta triangular, de valeta de proteção ou de espaçamento entre descidas d'água em fonte brasileira
  do grupo (o IPR-724, p. 158-186, está no corpus do Hidráulico, fora deste grupo). Os exercícios do IME (p. 157-158) não têm resposta.
- Não há tabela de velocidade máxima admissível por revestimento, nem de n de Manning por revestimento, nos documentos do grupo (IME p. 53
  remete às tabelas 27-28 do IPR-724).
- Dimensionamento hidráulico da descida d'água e do dissipador-tipo: só desenhos no Álbum (p. 40-47, OCR); sem verificação de Froude ou comprimento.
- Dimensionamento de dreno profundo: só Darcy/Scobey/Hazen-Williams (IME p. 82-85), sem exemplo numérico; DER-PR-06/07 só especificam materiais.
- Os slides Robson I-IV e o FDOT estão fora do escopo; DNIT ES 019, 030 e 086 não estão no corpus próprio.
- Álbum: 24 p. sem OCR, números de OCR a conferir na imagem antes de usar em quantitativo.

## Gabaritos para calculadora

Todos recalculados e comparados com o impresso. Tolerância sugerida 1 % salvo onde dito (leitura de nomograma).

1. Tc California Culverts (Kirpich): [LOC-IME p. 29]. Entradas: L = 5 km, H = 300 m. Fórmula tc = 57·(L³/H)^0,385 (p. 28). Resultado impresso 41 min; recalculado 40,69 min. Unidade: min.
2. Tc Ven Te Chow: [LOC-IME p. 29]. Entradas: L = 5 km, I = 6 %. Impresso 39,8 min; recalculado 39,79 min com tc = 25,2·(L/√I)^0,64 (I em %). O texto extraído perdeu a raiz de I (a forma sem raiz dá 22,4 min): conferir na imagem antes de codar. Unidade: min.
3. Tc Picking: [LOC-IME p. 29]. Entradas: L = 5 km, I = 0,06 m/m. tc = 5,3·(L²/I)^(1/3). Impresso 40 min; recalculado 39,59 min (diferença de arredondamento de 1 %). Unidade: min.
4. Gutter triangular, equação 4: [FHWA-HEC12 p. 39 (equação) e p. 41 (Exemplo 4)]. T = 8 ft, Sx = 0,025, S = 0,01, n = 0,015. Impresso Q = 2,0 ft³/s (Chart 3, Qn = 0,03); recalculado 2,04 ft³/s com K = 0,56. Unidade: ft³/s (K = 0,376 em SI).
5. Gutter triangular, exemplo do próprio nomograma: [FHWA-HEC12 p. 40]. n = 0,016, Sx = 0,03, S = 0,04, T = 6 ft. Impresso Q = 2,4 ft³/s (Qn = 0,038); recalculado 2,41. Unidade: ft³/s.
6. Largura de espalhamento: [FHWA-HEC12 p. 46 (Exemplo 6)]. Q = 3,0 ft³/s, n = 0,015, Sx = 0,025, S = 0,003. Impresso T = 12 ft (Chart 3); recalculado 11,6 ft (3 % por leitura do nomograma; usar tolerância 5 %). Unidade: ft.
7. Gutter composto: [FHWA-HEC12 p. 41 e p. 43 (Exemplo 5)]. T = 8 ft, Sx = 0,025, depressão 2 in em w = 2 ft (Sw = 0,108), S = 0,01, n = 0,015. Impresso Eo = 0,69 (Chart 4), Q = 3,0 ft³/s e Qw = 2,1 ft³/s. Reproduz-se Q = 3,06 ft³/s com Eo = 0,69. Unidade: ft³/s.
8. Swale circular: [FHWA-HEC12 p. 49 (Exemplo 8)]. D = 5 ft, S = 0,01, n = 0,016, Q = 1,5 ft³/s. Impresso d = 0,30 ft e T = 2,4 ft; Manning em seção circular parcial com d = 0,30 ft dá 1,50 ft³/s e T = 2,37 ft. Unidade: ft, ft³/s.
9. Tc por onda cinemática: [FHWA-HEC12 p. 32 (Exemplo 1)]. L = 150 ft, S = 0,02, n = 0,4, i ≈ 3,6 in/h (TR 10, Colorado Springs). Impresso tc = 20 min (Chart 1, iterando i). A equação 2 não foi extraída (imagem, p. 31); uma reconstrução tc = 56·(nL)^0,6/(i^0,4·S^0,3) em segundos dá 21 min. Só como teste de ordem de grandeza (5 %).
10. Valeta trapezoidal de canteiro com grelha: [FHWA-HEC12 p. 110 e p. 113 (Exemplos 23-25)]. B = 4 ft, n = 0,03, z = 6, S = 0,02, Q = 10 ft³/s: d/B = 0,11 (d = 0,44 ft), V = 3,4 ft/s, E = 0,32, Qi = 3,2 ft³/s. Depende de Charts 7, 8, 16, 17 (leitura gráfica); usar só os dois primeiros resultados (d e V), que seguem de Manning.
11. Energia específica em canal retangular: [LOC-IME p. 145]. Q = 4,5 m³/s, B = 3 m. h = 0,30 m: V = 5,00 m/s e E = 1,57 m; h = 0,40 m: V = 3,75 m/s e E = 1,11 m. Recalculado 1,574 e 1,117. Unidade: m.
12. Regime crítico de bueiro tubular (Ec = D): [LOC-IME p. 151-152]. θc = 4,0335 rad (231,1°), dc = 0,716 D, Vc = 2,56·√D m/s, Ic = 32,82·n²/D^(1/3) (impresso). Área crítica A = 0,601·D² (recalculada). Qc impresso 1,533·D^2,5 m³/s (texto extraído); recalculado 1,538·D^2,5: conferir na imagem. Celular: Qc = 1,705·B·H^1,5, Vc = 2,56·√H (p. 152), recalculado 1,705.
13. Hazen-Williams e Scobey de dreno cego com tubo: [LOC-IME p. 83]. Fórmulas p. 83, sem exemplo numérico; só teste de forma (V·área plena), vide divergência 10.

Não há gabarito numérico no WSDOT (equações em imagem), nas normas DNIT/DER-PR nem no Álbum (OCR).

## Pendências para a F5/F7

Cruzamento com `PENDENCIAS_DE_TREINAMENTO.md` §2.
- `hidrologia.py`, Picking (unidade): conferida. IME p. 29 dá L em km, I em m/m, tc em min, com exemplo (gabarito 3).
- `hidrologia.py`, Kirpich modificada (1,5×): divergente. IME p. 28 traz a fórmula California Culverts com fatores 2,0 (gramada), 0,4 (concreto ou asfalto) e 0,2
  (canais de concreto), não 1,5×; a origem do 1,5× continua sem fonte neste grupo.
- Ven Te Chow no IME: forma e unidade de I (%) a conferir na imagem (gabarito 2); George Ribeiro p. 28 só tem a fórmula, sem exemplo.
- Dooge, Giandotti, DNOS e tabela de K do DNOS (DNIT-HIDRO p. 89): não cobertos neste grupo; seguem pendentes.
- `bueiros.py`, A_c = 0,60 D²: o IME deriva esse valor, A = D²·(θ − sen θ)/8 em θc = 4,0335 rad dá 0,601 D² (p. 151-152, gabarito 12). Passa a ser fórmula impressa (não ajuste à Tab. 1 do DNIT), com a condição Ec = D.
- `bueiros.py`, Ke de alas e exemplo HDS-5 p. 280: sem relação com este grupo (G2).
- `drenos.py`: o IME só traz Darcy, K = 100·d10², Scobey, Hazen-Williams e E = 2h·√(K/q) (p. 82-85); nenhum Hooghoudt, Ernst ou Glover-Dumm, nenhum exemplo; a nota de "meia seção" é incompatível com as fórmulas (divergência 10).
- Módulo de sarjeta e valeta (F5): fontes localizadas: eq. 4 do HEC-12 (K = 0,56) com 5 gabaritos; folga e sequência de cálculo do IME p. 53-55; critérios de projeto (TR, Tc) divergem (itens 7 e 8). Decisão pendente para o André: fixar Tc = 5 min e TR 10 anos (IPR726 p. 258, WSDOT p. 102 e H14 concordam) e registrar 6 min (Álbum) e 10 min (IS-239) como divergência.
- F7 (evals): casos de aceitação possíveis a partir dos gabaritos 1 a 8 e 11; para dispositivo-tipo, o roteamento é "seleção no IPR-736 (Álbum) e verificação hidráulica pelo projetista" (Álbum p. 23).

## Páginas lidas (por documento)
DNIT-ES018 7; DNIT-ES020 3 (+ varredura); DNIT-ES021 4 (+ varredura); DNIT-IPR726 27; DERPR-01 7; DERPR-03 5; DERPR-05 5; DERPR-06 10; DERPR-07 8;
HEC-12 ≈ 32; IME 56; Álbum ≈ 8 (+ varredura de títulos); WSDOT ≈ 25. Total ≈ 200 p. (teto 300).

---

# Mapa parcial — G4-canais-subsuperficial (F3, 2026-10-08)

Páginas = página física do PDF (marcador `<!-- p. N -->` de `_texto/`); nenhum documento do grupo tem página de OCR.
"Impr." = página impressa. Valores numéricos só aparecem quando são gabarito ou índice de localização; a fonte manda.
Fontes lidas por trechos (Grep e leitura de intervalos); teto de 80 p. por documento respeitado.
Skills de destino (PLANO §2): `drenagem-canais` (canais e revestimento), `drenagem-subsuperficial` (drenos, envoltório).

## 1. Canais, velocidade admissível, revestimento

### USACE-EM1110-2-1601 — EM 1110-2-1601 Hydraulic Design of Flood Control Channels (Change 1, 30/06/1994)
1991 (Change 1 1994) · vigência: no catálogo USACE em 2026 (conferir; host oficial 403) · licença: domínio público · 183 p. · unidades US (ft, fps, pcf).
Lidas: p. 7, 12, 16, 24–25, 29–31, 178–181 (+ varredura por Grep).
- **Temas e onde estão**
  - Sumário: p. 6–7. Elementos físicos e hidráulica: p. 10–25 (Manning/Chezy/Darcy e k equivalente p. 11–12; classificação de escoamento p. 12; borda livre p. 18, 21, 23).
  - **Velocidade máxima admissível e canal estável**: p. 24–25 (§2-7), **Tab. 2-5 "Suggested Maximum Permissible Mean Channel Velocities"** p. 25 (areia, argila, terra gramada < 5 %, rocha; nota: partículas > cascalho fino, ver Plates 29 e 30 do Apêndice B; manter V < 5,0 fps em canal gramado sem manutenção).
  - **Rip-rap de canal** (localizar; dissipação é D3 do Hidráulico): Cap. 3, p. 26–39. Características/graduação p. 26–28 (**Tab. 3-1** graduações p. 28); n de rip-rap por Strickler, **Eq. 3-2** n = K·D90(min)^(1/6), K = 0,034/0,036/0,038, p. 29; talude, forma e espessura p. 29; velocidade local V_SS e relações com R/W p. 30; **Eq. 3-3** D30 = Sf·Cs·CV·CT·d·[…]^2,5 p. 30–31 (definições de Sf, Cs, CV, CT p. 31); proteção de pé e **Tab. 3-2** (acréscimo de espessura) p. 35–36; gelo, detritos e vegetação p. 37.
  - Cap. 5 (Change 1): previsão de n de Manning, p. 47–62 (Tab. 5-1 leito e margens p. 49; Tab. 5-2 várzea p. 50; Tab. 5-5 Strickler e Keulegan p. 53; Tab. 5-8 p. 58; Tab. 5-9 alfa p. 61; Tab. 5-10 p. 60; rugosidade composta e método alfa p. 52–61).
  - Apêndice B (placas): Plates B-28/B-29 (graduação e velocidade permissível) p. 100–101; Plates B-30 a B-40 (V_SS, D30, correções C1/C2, **Plate 33** razão V_SS/V_AVG em curva) p. 102–112; Plates B-41 a B-46 (rip-rap em estruturas, pedra de ponta/derrick B-46) p. 113–122. Apêndice C (método alfa) p. 132–138; Apêndice D (curvas em regime rápido) p. 139–154; Apêndice F (padronização de graduações de rip-rap) a partir de p. 155 (até ≈ p. 170); Apêndice G (velocidade por campo) p. 176–177 (Plate G-1); Apêndice H (exemplos de pedra) p. 178–179; Apêndice I (notação) p. 180–181.
- **Exemplos resolvidos**: App. H Problema 1 (curva natural, V_SS = 1,48 × 7,1 = 10,5 fps, D30 = 0,62 ft → graduação 18 in) p. 178; **Problema 2** (trapezoidal, b = 140 ft, S = 0,0017, Q = 13 500 cfs, 1V:2H; **Tab. H-1** profundidade normal/V, **Tab. H-2** V_SS e D30) p. 178–179; Apêndice G exemplo p. 176; exemplos de curva em regime rápido p. 148–149 (Apêndice D) e Plate B-8 p. 71/84–85 (índice de plates).
- **Lacunas**: não há tabela de gramíneas por retardância (só Tab. 2-5 e referência ao SCS 1954 p. 25); concreto/gabião só como k equivalente (Tab. 2-1 p. 12); sem sistemática de canal de drenagem agrícola; unidades só US.

### FHWA-HEC11 — HEC-11 Design of Riprap Revetment (1989)
1989 · vigência: edição 1989 (link FHWA 404; usado cópia Snohomish County) · licença: domínio público · 182 p. · texto com ruído de OCR de origem (símbolos e expoentes às vezes corrompidos).
Lidas: p. 5–9, 37–42, 45, 47–52, 54–55, 69, 76–78, 101–102, 166–170 (+ varredura).
- **Temas e onde estão** (p. impressa = PDF − 18)
  - Sumário p. 7–8; tipos de revestimento (rip-rap, gabião, bloco pré-moldado, rocha injetada, revestimento pavimentado) p. 25–35.
  - Conceitos: vazão de projeto (TR 10–50 anos) p. 37; tipos de escoamento e faixa de Froude 0,89–1,13 p. 38; geometria da seção p. 39–41; superelevação em curva p. 41; resistência ao fluxo (n) p. 41; **extensão da proteção** (1,0 largura a montante e 1,5 largura a jusante de curva) p. 42; profundidade de pé p. 43–46.
  - **Dimensionamento de rip-rap**: Cap. 4, p. 47–62. **Eq. 6** D50 = 0,001·V³/(d^0,5·K1^1,5) (US) com K1 = [1 − sen²θ/sen²φ]^0,5 (**Eq. 7**) p. 48; correções C_sg (Eq. 8) e C_sf (Eq. 9) p. 49; fatores de estabilidade em curva (SF por R/W: > 30 → 1,2; 30–10 → 1,3–1,6; < 10 → 1,7), pilares e encontros p. 50–51; onda (Hudson, Eq. 11–13) p. 52; graduação **Tab. 2/Tab. 3** (seis classes AASHTO) p. 54–55; espessura p. 55; filtro (granular e geotêxtil) p. 55–62.
  - Gabiões: p. 97–105 (**Tab. 4** tamanhos padrão p. 101; **Tab. 5** critério de espessura p. 102); blocos e pavimento p. 106–118; Apêndice A especificações p. 127–137; Apêndice C gráficos (Chart 1 solução gráfica da Eq. 6 p. 144; Chart 2 correção C p. 145; Chart 3 ângulo de repouso p. 146, Chart 4 K1, Chart 7 onda p. 150) p. 143–153; Apêndice D derivação e comparação com outros métodos p. 159–170.
- **Exemplos resolvidos**: **Exemplo 1** (canal trapezoidal de rip-rap, Q = 5000 cfs, S = 0,0049, SG 2,65) p. 69–80, com Figs. 24–30 (formulários e Chart 1 p. 78; Chart 4 K1 p. 77; ângulo de repouso p. 76); **Exemplo 2** (proteção de margem) p. 81–96. Comparação gráfica de métodos de velocidade permissível: Figs. 61–63 p. 168–170.
- **Lacunas**: sem tabela de velocidade admissível por material de canal (só gráficos p. 168–170); sem dissipador (D3, Hidráulico); gabião tratado em nível de especificação.

### NRCS-CPS608-2023 — Conservation Practice Standard 608 Surface Drain, Main or Lateral (ft)
Agosto/2023 · vigente · domínio público · 4 p. (todas lidas, p. 1–3 em detalhe).
- Critérios de capacidade, linha de energia (folga mínima 0,5 ft sobre o nível de projeto), profundidade (fundo ≥ 1 ft abaixo do invert de drenos subsuperficiais que descarregam no canal), seção, taludes (remete NEH 650 §650.1412 e NEH 654 cap. 10 para seção em dois estágios) e **velocidade** (sem valor numérico; "baseada nas condições locais") p. 1–2; bermas e depósito de material escavado **Tab. 1** (largura mínima de berma × profundidade) p. 3; considerações e plano p. 3–4.
- Lacunas: sem fórmula nem exemplo; nenhum limite numérico de velocidade, de talude ou de K; normas 606 e 607 ausentes (PENDENTES).

### EMBRAPA-DOC237-VARZEA — Drenagem superficial para cultivos rotacionados em solos de várzea (Documentos 237, 2008)
2008 · vigência: método qualitativo, várzea do Sul do Brasil · licença: Embrapa (aberta) · 24 p. no PDF (22 p. de texto).
Lidas: p. 3–4, 8, 13–14, 17.
- Sumário p. 8; drenagem superficial natural, locação e construção de drenos (valetamento) p. 13–15 (Figs. 1–2); adequação da superfície (aplainamento, sistematização, camalhões, sulco/camalhão) p. 17–22 (Figs. 3–6).
- Sem tabela, sem exemplo numérico, sem Manning, velocidade, vazão ou coeficiente de drenagem. Serve de apoio qualitativo em português para drenagem superficial de lavoura.

### LOC-RETROANALISE-CANAL-GABIAO — Retroanálise de canal em gabião (planilha .xlsx)
Estudo interno · sem ano · uso-interno · planilha (sem paginação; fonte por célula, aba `Planilha1`). Registrada e mapeada por célula (texto das células, não OCR).
- Bloco "Canal retangular" (A1:B8): b = 1,59 m, altura 1 m, lâmina 0,8 (80 %), declividade 0,003 (rótulo "%", valor decimal m/m, a confirmar), n = 0,035 (gabião), **Q = 1,0784 m³/s** (B8). Varredura de n de 0,02 a 0,035 (linha 1, H1:AB1) e de declividade (coluna G, G2…) com matriz lógica (H2:AB…) por fórmula matricial não exportada.
- Bloco "Canal circular" (A10:B19): D = 1 m, lâmina 85 %, alfa 0,7754 rad, P = 2,3462 m, A = 0,7115 m², R = 0,3033 m, S = 0,003, n = 0,01 (PEAD) → **Q = 1,7591 m³/s** (B19); n tabelados: PEAD 0,009/0,010, concreto 0,011/0,015, gabião 0,020/0,035 (D6:E19).
- Lacuna: fórmulas matriciais (retroanálise de n por Q observada) não legíveis; o objetivo da retroanálise (Q observada) não aparece nas células lidas.

## 2. Drenagem subsuperficial agrícola

### EMBRAPA-ESPACAMENTO-1990 — Validade de algumas equações de drenagem para espaçamento de drenos cobertos, I. Regime permanente (PAB 25(3):353–363)
1990 · vigência: parte I de série de dois artigos; modelo físico de laboratório (várzea) · licença: aberta · 11 p. (todas lidas).
- Revisão (Nwa & Twocock: Hooghoudt superestima S em até 302 %; Wesseling: Hooghoudt × Kirkham < 5 %) p. 2–3; modelo físico (caixa 149 cm, 56 piezômetros) p. 3–4 (Fig. 1); **fórmulas de Donnan-Hooghoudt** (S² = 8·K·d·H/q + 4·K·H²/q), Hooghoudt e **Kirkham (série)** p. 5–6; ensaios: **Tab. 1** granulometria p. 5; **Tab. 2 e 3** (K0, q, H0 por d; solo orgânico e mineral) p. 7–8; **Tab. 4 e 5** desvios % de S estimado × 149 cm por d, d/H, K0/q p. 9; **Tab. 6** S médio, DP e CV por teoria p. 10; **Tab. 7** % das estimativas por faixa de desvio p. 10; conclusões p. 10.
- Resultado-chave: Donnan-Hooghoudt, d ≠ 0, S médio 154,5 cm contra 149 cm (CV 9,5 %); com o tubo sobre a camada impermeável (d = 0) as teorias falham (p. 1, 10).
- Lacunas: sem Ernst nem Glover-Dumm; sem K de campo; só laboratório.

### EMBRAPA-MANICOBA-1988 — Drenagem subterrânea no Perímetro Irrigado de Maniçoba (PAB 23(4):405–413)
1988 · vigência: dados de campo, Juazeiro-BA, solo arenoso classe 3 · licença: aberta · 9 p. (todas as seções lidas, p. 1–3, 7–8 em detalhe).
- Resumo e resultado (Hooghoudt superestima L em 24 %; Glover-Dumm subestima em 30 %; μ = 7,8 % e 24 %; fator de intensidade de drenagem 0,15 e 0,21) p. 1; fórmulas de Hooghoudt (L² = 4·K·h·(2d + h)/q, camada equivalente d de Beers 1965) e **Glover-Dumm** com o **fator 1,16** L = π·[K·D·t/(μ·ln(1,16·h0/ht))]^(1/2) p. 2; parâmetros e **exemplo de cálculo do espaçamento** p. 3; regime de umidade e perfil do lençol p. 3–5 (Figs. 1–6); K por furo de trado (2,03 e 2,53 m/d) p. 5; transmissividade KD (Kraijenhoff van de Leur) e recálculo a posteriori p. 7; **Tab. 2** (água de drenagem, envoltório) e resistência de entrada p. 8; conclusões p. 8.
- Lacunas: Ernst ausente; só um solo.

### EMBRAPA-BEBEDOURO-1986 — Parâmetros de drenagem subterrânea nos latossolos do Perímetro Irrigado de Bebedouro (Anais do VII CONIRD)
1986 · vigência: trecho de 4 p. dentro do PDF dos anais; texto com ruído de OCR de origem (números e expoentes corrompidos) · licença: aberta · 7 p. (todas lidas).
- Sistema de drenos (1,53 m, 30 m, 93 m); fórmula de Hooghoudt com d de Beers (1965) e Manning para o diâmetro p. 2–3; custos (**Tab. 1**, 92,42 OTN/ha) p. 4 e 6; K e transmissividade pela relação q/h × h p. 4; **Glover-Dumm com 1,16** e KD = 0,99 m²/d, L = 29 m p. 5; **Tab. 2 e 3** (vazões por dreno, q, h, q/h e KD) p. 7; conclusões (descarga normativa média 3,6 mm/d, picos de 13,6 mm/d; K = 1,98 m/d) p. 5.
- Os números impressos estão degradados: usar só como localização; não usar como gabarito sem a imagem.

### WATERLOG-DRAINAGE-EQUATION — Drainage equation (Oosterbaan, waterlog.info)
Sem ano no PDF · vigência: nota de aula; conferência de Hooghoudt/Ernst com ILRI-16 · licença: aberta · 9 p. (todas lidas).
- Equação de Hooghoudt e parâmetros p. 2; regime permanente e derivação p. 3; **profundidade equivalente em forma fechada (van der Molen & Wesseling)** p. 4; terreno inclinado e resistência de entrada p. 5–6; uso estendido (camadas, anisotropia, EnDrain) p. 6–8; referências p. 9. Sem exemplo numérico.

### WATERLOG-ENDRAIN — EnDrain, balanço de energia do escoamento subterrâneo (Oosterbaan, maio/2021)
2021 · vigência: método alternativo, fora do padrão do pacote · licença: aberta (domínio público declarado) · 19 p.
Lidas: p. 1, 5–13.
- Menu e opções p. 5–6 (Figs. 3–6); **Exemplos 1 a 4 (dados de Ritzema, ILRI-16 cap. 8)** p. 7–10; conclusões p. 11; referências p. 11–12; apêndice (HydrCond) p. 13.
- Exemplo 1 (dreno de tubo): q = 0,001 m/d, h = 1,0 m, r = 0,1 m, K = 0,14 m/d, D = 4,8 m → De = 3,22 m, **S = 65 m** (Ritzema); EnDrain 67 m (Darcy) p. 7. Exemplo 2 (vala, perímetro molhado 1,91 m): 72 m (Ritzema), 77 m (EnDrain) p. 8–9. Exemplo 3 (duas camadas, Ka = 0,06 e Kb = 0,30 m/d, interface na cota do dreno): 95 m (Ritzema), 98 m (EnDrain) p. 9–10. **Exemplo 4 (equação de Ernst)**: Q = 0,007 m/d, Hn = 0,7 m, r = 0,05 m, Ka = 0,5, Kb = 2,0 m/d, Dw = 2,0, D1 = 3,0, D2 = 7,0 m → 0,014·L² + 1,18·L − 98,6 = 0, **L = 51,8 m** (EnDrain Darcy 50,5; balanço de energia 56,9) p. 10.
- Lacunas: Glover-Dumm ausente; Ernst só no Exemplo 4 e com equação mal diagramada no texto (p. 10).

### ILRI-56-ENVELOPE — Envelope Design for Subsurface Drains (ILRI 56; Vlotman, Willardson, Dierickx, 2000)
2000 · vigência: edição única; fronteira com geotecnia (D-86 do CDV) · licença: aberta · 380 p. · PDF = impr. + 20 (Parte 1, cap. 1–4); capítulos 5–6 seguem o mesmo deslocamento.
Lidas: p. 1–14, 40–47, 62–73, 173–176 (≈ 38 p.).
- **Sumário** p. 9–14 (Partes 1 Guidelines e 2 Resource).
- **Necessidade de envoltório e discrepâncias entre critérios**: cap. 2, p. 27–47; faixas de largura de granulometria do solo-base (Fig. 4) p. 39–40; **coeficiente de drenagem e profundidade típicos (valores de referência por clima)** p. 42; K médio geométrico para projeto p. 43; sensibilidade do espaçamento a h, K e q (Box 5) p. 45; capacidade do tubo cheio por Manning p. 46; **fluxograma de necessidade (Fig. 7)** com HFG = exp(0,332 − 0,132·K + 1,07·ln PI) p. 47 (e p. 167–169).
- **Critério hidráulico e de retenção (granular)**: cap. 3, p. 53–72. Método e critérios generalizados p. 62–64 (Boxes 10 e 11); **pontos de controle da faixa granulométrica** (1 a 7, limites grosso e fino: retenção D15c × d85f, guia D50c, segregação D100c, hidráulico D15f × d15c, D5f, banda D60f) p. 66–68; critérios diversos (cobertura ≥ 75 mm) e material britado p. 69; **critérios de ponte (bridging)** p. 70; observações finais e **exemplos Paquistão (Fig. 11) e Reino Unido (Fig. 12)** p. 71–72; ASTM C33 e D1073 como alternativa (Fig. 10) p. 71.
- Orgânico p. 73–75; sintético (geotêxtil: retenção, hidráulica, anti-colmatação) p. 76–88 (retenção p. 81).
- Cap. 5 (teoria): resistência de entrada p. 144–149; ponte p. 160–164; **HFG** p. 165–171; **K por granulometria** p. 173–176 (**Tab. 14** faixas de K por textura p. 175; **Eq. 39** K × D15, correlação de Sherard e comparação com Hazen, que dá K ≈ 3 vezes maior, p. 175–176); **Tab. 15** conjunto de 21 peneiras US p. 65; ensaios p. 181–246.
- Cap. 6 critérios existentes: necessidade (EUA, Alemanha, Holanda, França, Egito, Índia, Canadá, Paquistão) p. 269–283; granulares p. 286–301; **exemplos Califórnia e Paquistão** p. 318–319.
- **Fator 1,16 não está neste documento** (é de Glover-Dumm; ver Embrapa, p. 2). Sem Hooghoudt/Ernst/Glover-Dumm resolvidos.
- Lacunas: sem exemplo numérico completo de dimensionamento de envoltório (só faixas desenhadas, Figs. 11–12); critérios do Brasil e do SCS (1994) citados, não tabulados aqui.

### LOC-COMAER-EDMIR-DREN-SUBSUPERFICIAL — Estudo da drenagem subsuperficial e subterrânea de sítios aeroportuários (TCC ITA, 2013)
2013 · vigência: trabalho de graduação; segue FAA AC 150/5320-5C, Apêndice G (FAA 2009) · licença: uso-interno · 93 p. (impr. = PDF; sumário p. 14–17).
Lidas: p. 1–16, 47–50, 65, 68, 82–90.
- **Escopo**: drenagem de pavimento (camada drenante e coletores), não drenagem agrícola; não traz Hooghoudt, Ernst nem Glover-Dumm (Grep sem ocorrência). Útil à `drenagem-subsuperficial` só como camada drenante e dreno coletor de pavimento.
- Temas: danos da água no pavimento p. 18–27; Darcy e permeabilidade p. 34–45; ensaios de permeabilidade (carga constante/variável, tubo aberto) p. 36–43 (**Tab. 2** K de areia e cascalho p. 43); **capacidade da camada drenante** (Eqs. 35–38) p. 47–48; **tempo de drenagem T50 e T85** (Eqs. 39–41, Fig. 10) p. 48–49; comprimento e inclinação do caminho (Eqs. 42–43) p. 49–50; filtros, camada de separação e geotêxtil (Tabs. 6 e 7) p. 51–52, 63–64; critérios de projeto (espessura, Eqs. 44–49) p. 57–59; materiais (Tabs. 3 a 5) p. 61–63; **drenos coletores profundos** (vazão da camada Q = H·i·k Eq. 51 p. 65; rebaixamento do lençol, Fig. 11 p. 65–66; **Manning a seção plena Eq. 55 e Tab. 8** de n p. 68; D mín. 150 mm, declividade mín. 0,15 %) p. 64–68; valas e geotêxtil (Tab. 9) p. 69–72; saída e headwall p. 73–75.
- **Estudo de caso** (Aeroporto Salgado Filho): L = 21 m, F = 0,5, R = 30,30 mm/h, t = 1 h, camada de 10 a 20 cm: **Tab. 15 (n_e necessário × espessura)** p. 87; solos RADAM Tabs. 10–14 p. 85–86; verificação de T85 p. 87–88.
- Lacunas: nenhuma equação de espaçamento de drenos; envoltório só por critério FAA.

## 3. Divergências entre fontes e dentro de fontes do grupo

| # | Tema | Fonte A | Fonte B | Observação |
|---|---|---|---|---|
| 1 | Equação de Hooghoudt: termo extra | WATERLOG-DRAINAGE-EQUATION p. 2 (`Q·L² = 8·Kb·De·(Di−Dd)·(Dd−Dw) + 4·Ka·(Dd−Dw)²`) | EMBRAPA-ESPACAMENTO-1990 p. 5 (S² = 8·K·d·H/q + 4·K·H²/q) e EMBRAPA-MANICOBA p. 2 | O fator (Di−Dd) do primeiro é dimensionalmente inconsistente; reproduzi Ritzema com a forma sem ele (ver Gabarito 5) |
| 2 | De em forma fechada: operador | WATERLOG-DRAINAGE-EQUATION p. 4 (texto achatado: `De = πL/8 {ln(L/πr)+F(x)}`) | cálculo do mapeador | O ajuste a Ritzema só funciona com o denominador `[ln(L/πr)+F(x)]`; o ano de van der Molen & Wesseling é 1991 em p. 4 e 9, mas 1981 em WATERLOG-ENDRAIN p. 12 |
| 3 | Hooghoudt: sentido do viés | EMBRAPA-MANICOBA p. 1 e 8 (superestima L em 13,5–35 %) | EMBRAPA-ESPACAMENTO-1990 p. 10, Tab. 6 (S médio 117,4 cm contra 149 cm real: subestima, −21 %) | Campo (solo arenoso, d ≈ 0) × laboratório (várzea); Maniçoba resumo (24 %, 30 %) × conclusões 8 (13,5–35 %, 22–39 %) p. 1 e 8 |
| 4 | Exemplo de camada drenante: i e unidade de T85 | LOC-COMAER p. 82 (i = 0,01 m/m) | LOC-COMAER p. 87–88 (i = 0,001; k = 300 m/dia; "T85 = 17,5 horas") | Com os dados da p. 88 o resultado é 17,5 dias; com i = 0,01 dá 1,75 dia (42 h). Não usar como gabarito |
| 5 | Manning de rip-rap | USACE-EM1110-2-1601 p. 29 (Eq. 3-2: n = K·D90(min)^(1/6), K = 0,034–0,038) | FHWA-HEC11 p. 166 (Eq. 20: n = 0,0395·D50^(1/6)) | Diâmetro representativo diferente (D90 mínimo × D50); ambos Strickler |
| 6 | Estabilidade de rip-rap | USACE-EM1110-2-1601 p. 30–31 (D30 por velocidade local V_SS, Sf, CV, K1; 1V:1,5H ou mais suave) | FHWA-HEC11 p. 48–50 (D50 por V médio do canal principal, SF por R/W, K1 de talude) | Métodos distintos: não comparar D30 com D50 sem a graduação; HEC-11 p. 49 e p. 166 grafam o expoente de C_sf de forma diferente (OCR; conferir na imagem) |
| 7 | Ernst: coeficientes impressos | WATERLOG-ENDRAIN p. 10 (0,014·L² + 1,18·L − 98,6 = 0 → 51,8 m) | forma padrão reconstituída pelo mapeador (ΣKD = 8) → 50,0 m | 3,5 %; a equação impressa na p. 10 está truncada; conferir em ILRI-16 (corpus Hidráulico) |

Complementos com o mapa do Hidráulico (`MAPA_DE_CONHECIMENTO.md`, H14 e H15), sem refazê-lo: a linha USACE-EM1601 pág. 26–39 do H14 confere com Cap. 3 aqui; o H15 já lista Hooghoudt, elipse e Ernst com **exemplos resolvidos em NRCS-NEH624-CH04 (p. 63–79; Exemplos 1 e 2: S = 202 ft e 196 ft), NRCS-NEH624-CH10 (Exemplos 10-1 a 10-4), EMBRAPA-DREN-SUBT (exemplo L = 35 m) e FAO-IDP62 (p. 193–212)**, que são a fonte natural de gabarito de Hooghoudt/Ernst; o H15 não traz Glover-Dumm com 1,16 (este grupo traz). Velocidade não erosiva do H14 (EMBRAPA-DREN-SUP: 0,5 m/s; SRHCE-GED-030: 0,70/3,00/4,50 m/s) não está neste grupo; aqui o único quadro de velocidade é a Tab. 2-5 do EM-1601 (p. 25).

## Gabaritos para calculadora

1. **Glover-Dumm com fator 1,16** (EMBRAPA-MANICOBA-1988 p. 3, confirmado pelo mapeador): K = 2,3 m/d; μ = 0,15; h0 = 0,8 m; ht = 0,4 m; t = 3 d; D = D0 + (h0 + ht)/4 com D0 = 0, logo D = 0,3 m. Resultado **L = 12,72 m** (fonte). Recálculo: π·[2,3·0,3·3/(0,15·ln(1,16·2))]^0,5 = 12,72 m.
2. **Hooghoudt, camada impermeável sob o dreno (d = 0)** (EMBRAPA-MANICOBA-1988 p. 3): q = 4·K·h²/L², K = 2,3 m/d, h = 1,60 − 1,10 = 0,50 m, q = 8,0 mm/d. **L = 16,96 m** (fonte; recálculo 16,96 m). Média dos dois métodos 14,84 m, adotado 15 m (p. 3).
3. **Recálculo a posteriori com L real de 15 m** (EMBRAPA-MANICOBA p. 7): Hooghoudt 20,3 m e Glover-Dumm 9,18 m (parâmetros da p. 7, KD = 0,36 m²/d e K1·D1 = 0,63 m²/d; não tenho todos os dados do ajuste; usar só como ordem de grandeza).
4. **Hooghoudt tubo, camada única** (WATERLOG-ENDRAIN-2021 p. 7, dados de Ritzema/ILRI-16): q = 0,001 m/d, h = 1,0 m, r = 0,1 m, K = 0,14 m/d, D = 4,8 m → De = 3,22 m, **S = 65 m** (m). Recálculo do mapeador com a forma fechada (De = (πL/8)/[ln(L/πr) + F(x)], x = 2πD/L): De ≈ 3,16 m, S ≈ 64,0 m (1,5 %).
5. **Hooghoudt, duas camadas com interface na cota do dreno** (WATERLOG-ENDRAIN-2021 p. 9–10, Ritzema): mesmos q, h, r, D; Ka = 0,06 e Kb = 0,30 m/d → **S = 95 m**; recálculo com Q·L² = 8·Kb·De·h + 4·Ka·h²: 93,4 m (1,6 %).
6. **Ernst, dreno dentro da camada superior** (WATERLOG-ENDRAIN-2021 p. 10): Q = 0,007 m/d, Hn = 0,7 m, r = 0,05 m (W = 0,1 m), Ka = 0,5, Kb = 2,0 m/d, Dw = 2,0 m, D1 = 3,0 m, D2 = 7,0 m. Quadrática impressa 0,014·L² + 1,18·L − 98,6 = 0 → **L = 51,8 m** (fonte; a quadrática impressa reproduz 51,8). Reconstituição do mapeador da forma padrão dá 50,0 m; tratar como tolerância 5 % e conferir na ILRI-16.
7. **Donnan-Hooghoudt de laboratório** (EMBRAPA-ESPACAMENTO-1990 p. 10, Tab. 6): espaçamento real do modelo 149,0 cm; Donnan-Hooghoudt com d ≠ 0, média 154,5 cm (CV 9,5 %); Hooghoudt 119,4; Kirkham (d = 0 incluído) 92,6. Linha a linha: Tabs. 2–5 p. 7–9 (conferir a coluna de d e o sinal do desvio na imagem antes de usar).
8. **Rip-rap, Eq. 6 de HEC-11** (FHWA-HEC11 p. 78): V = 9,7 ft/s, d_avg = 11,8 ft, K1 = 0,73 (talude 2:1, φ ≈ 41°; recálculo da Eq. 7: 0,73), SG 2,65, SF 1,2 → **D50 = 0,43 ft** (fonte; recálculo 0,426 ft). Dados do canal: Q = 5000 cfs, S = 0,0049 (p. 69).
9. **Rip-rap, Manning e profundidade normal** (USACE-EM1110-2-1601 App. H Tab. H-1 p. 179): b = 140 ft, 1V:2H, S = 0,0017, Q = 13 500 cfs. n = 0,034/0,036/0,038 → y_n = 10,6/11,0/11,3 ft e V = 7,9/7,6/7,3 fps (recálculo n = 0,036: y = 11 ft, V = 7,59 fps, Q = 13 527 cfs, 0,2 %). Resultado de pedra (Tab. H-2): D30(min) das graduações 12/18/24 in = 0,48/0,73/0,97 ft contra D30 requerido 0,59/0,53/0,48 ft; 18 in é a menor adequada (p. 179). A Eq. 3-3 não foi reproduzida pelo mapeador (Sf, Cs, φ de entrada não ficam todos impressos).
10. **Canal retangular com n de gabião** (LOC-RETROANALISE-CANAL-GABIAO, células B2:B8): b = 1,59 m, y = 0,8 m, S = 0,003 m/m, n = 0,035 → **Q = 1,0784 m³/s** (recálculo igual). **Circular** (B11:B19): D = 1 m, y/D = 0,85, S = 0,003, n = 0,01 → A = 0,7115 m², P = 2,3462 m, R = 0,3033 m, **Q = 1,7591 m³/s**.
11. **Camada drenante de pavimento** (LOC-COMAER p. 82 e 87, Tab. 15): F = 0,5, R = 0,0303 m/h, t = 1 h; espessura h = F·R·t/(0,85·n_e): n_e = 0,178 → h = 0,10 m; 0,119 → 0,15 m; 0,089 → 0,20 m (recálculo 0,100/0,150/0,200 m). Só a verificação de T85 não serve (divergência 4).

## Pendências para a F5/F7 (contra `PENDENCIAS_DE_TREINAMENTO.md` §2, linha `drenos.py`)

- **Fator 1,16 de Glover-Dumm**: **conferido** na forma impressa L = π·[K·D·t/(μ·ln(1,16·h0/ht))]^(1/2), com D = D0 + (h0 + ht)/4 e exemplo numérico que fecha em 12,72 m (EMBRAPA-MANICOBA p. 2–3; EMBRAPA-BEBEDOURO p. 5 confirma o 1,16 mas com números degradados). Falta a página de ILRI-16 / FAO-38 que o PENDENCIAS pede, que não está neste grupo (ILRI-56 não traz o fator).
- **Ernst sem exemplo de livro**: agora há um exemplo (WATERLOG-ENDRAIN p. 10, dados de Ritzema; L = 51,8 m). Divergência de 3,5 % entre a quadrática impressa e a forma padrão reconstituída; resolver contra ILRI-16 (corpus Hidráulico) antes de gravar teste.
- **Hooghoudt**: dois exemplos de Ritzema (65 m e 95 m) e um de campo (16,96 m), todos reproduzidos a menos de 2 %; vale testar a calculadora de `De` em forma fechada (denominador, divergência 2). O termo extra (Di−Dd) de WATERLOG-DRAINAGE-EQUATION não deve ser copiado (divergência 1).
- **Tabelas indicativas "a confirmar"**: parcialmente cobertas aqui por ILRI-56 **Tab. 14** (K por textura, p. 175) e valores típicos de coeficiente de drenagem e profundidade (p. 42); a FAO-38 segue sem página neste grupo.
- **Envoltório**: critérios (pontos de controle 1–7, HFG) localizados em ILRI-56 p. 47, 66–72, 167–169; falta exemplo numérico completo com resposta para teste (só figuras).
- **Viés Hooghoudt**: campo (Maniçoba) superestima L, laboratório (Embrapa 1990) subestima (divergência 3); relevante para o aviso de incerteza do `drenos.py`.
- **Canais**: Strickler com dois diâmetros representativos (divergência 5) e dois métodos de rip-rap (divergência 6) para a F7; nada do grupo toca `hidrologia.py` ou `bueiros.py` (os pontos Dooge, Giandotti, Picking, A_c = 0,60 D² e Ke de alas ficam para G1 e G2).


# Mapa parcial F3 — grupo G5-hec-ras (modelagem hidráulica HEC-RAS, D9)

Os arquivos de origem ficam ao lado. Convenção: p. N = página física do PDF = número impresso.


## Conciliação feita pela sessão HEC-RAS (2026-10-10), após conferir no `_texto`
1. **Sensibilidade de n "±20 %"** (divergência 1 do grupo B): a regra está em [USACE-HECRAS-HRM-66 p. 389] ("uncertainty analyses ... varying all values ... by plus or minus 20%", no contexto de ruptura de barragem); [USACE-HECRAS-UM-66 p. 328] pede só uma "faixa realista" (exemplo 0,035 → 0,03 a 0,045). A skill adota ±20 % como padrão do treinamento, com a origem dita (dam break) e a faixa realista como alternativa. Faixas de n do HRM nessa página: canal de 0,025 a 0,075 e planície de 0,05 a 0,15 [USACE-HECRAS-HRM-66 p. 389].
2. **Equação padrão 2D** (divergência 1 do grupo A): [USACE-HECRAS-2DUM-66 p. 196, 211] diz difusão como padrão do programa; o PLANO §11.2 item 1 ("SWE-ELM por padrão") foi lido como padrão do ESPECIALISTA e fica corrigido na skill: difusão para desenvolvimento, SWE-ELM nas 8 situações de p. 196–197 e na versão final de cheia dinâmica.
3. **Courant**: p. 200–201 do 2DUM (1,0 alvo; até 3,0 SWE e 5,0 difusão; 1,0 em onda rápida ou partida a seco); o método do programa usa a velocidade da face e a distância entre centros [USACE-HECRAS-2DUM-66 p. 203–204]. `tools/dren/hecras_hdf.py` estima com sqrt(área).
4. Estabilização (ΔNA ≤ 0,01 m em 2 h) e limiar de erro de volume: **sem critério numérico nos manuais** (só o exemplo de ganho de volume de 0,02017 % em [USACE-HECRAS-2DUM-66 p. 208]); são critérios do treinamento (casos HR-02).

---

## Mapa parcial F3 — grupo HECRAS_A (Especialista Drenagem): HRM-66 e 2DUM-66

Convenção de páginas: "p. N" = página física do PDF (marcador `<!-- p. N -->` do `_texto`; coincide com o número impresso "Manual – N" e com os bookmarks do sumário nos dois manuais). Todas as páginas citadas abaixo foram conferidas no `_texto`, salvo onde está escrito "(localizado por busca, não lido)" ou "(a confirmar)".
Aviso sobre a extração: nos dois manuais **as equações numeradas e várias células de tabela saíram do texto** (só o título "n)" e a lista de símbolos restam). Onde a fórmula é o que importa, o item diz "(equação na imagem)". Unidades originais: sistema inglês (ft, cfs, acre-ft) com equivalentes SI esparsos. Nenhum valor abaixo substitui a fonte; valor numérico é só localizador, com página.
Versão: HEC-RAS 6.6 (HRM exportado 2024; o texto ainda traz rótulos "v6.4" e "Beta Dec 2020" no front matter, p. 15). O modelo da TPF foi 6.5 (ver catálogo).

### USACE-HECRAS-HRM-66 — HEC-RAS Hydraulic Reference Manual, v6.6 (USACE HEC, 2024)
Vigência: v6.6 na página oficial em 2026-10-09 (só a versão corrente em PDF); licença: domínio público; 482 p. (camada de texto nativa, sem OCR).
Capítulos pelo sumário (conferido): 4 Teoria 1D/2D p. 24–112; 5 Dados básicos p. 113–135; 6 Opcionais p. 136–172; 7 Pontes p. 173–208; 8 Bueiros p. 209–246; Pontes/bueiros múltiplos p. 247–252; Estruturas em linha e laterais p. 253–273; Encroachment p. 274–280; Redes de tubos p. 281; Erosão em pontes p. 282–294; Gelo p. 295–301; Canal estável e sedimentos p. 302–344; Ruptura de barragem p. 345–406; Referências p. 407; Apêndices p. 418–482.

### 1D permanente (Standard Step, energia, momentum)
- Equação de energia e perda (atrito + contração/expansão), comprimento ponderado por vazão p. 24–25; subdivisão da seção para condutividade (Manning por segmento; método alternativo estilo HEC-2 e comparação em 97 conjuntos do estudo HEC) p. 26–27; **n composto do canal principal**, aplicado só se o talude do canal for mais íngreme que 5H:1V e houver mais de um n (equação 6 "Chow 6-17", na imagem) p. 27–29; coeficiente de energia cinética α p. 29–30.
- Declividade de atrito: equação de Manning e as quatro formas (condutividade média = padrão, atrito médio, média geométrica, média harmônica) p. 30–31; critério de escolha por regime/perfil (Tab. 4-1) p. 137.
- Procedimento iterativo (tolerância 0,01 ft; 70 % do erro na 2ª tentativa; secante; máximo 20 iterações; "minimum error water surface" e limite 0,3 ft; critério de Froude 0,94 para checar regime) p. 31–33; profundidade crítica (parabólico × secante, até 3 mínimos) p. 33–35.
- **Momentum**: quando a energia deixa de valer (passagem por crítica), aplicações (ressalto, ponte baixa vazão, junção) p. 36; derivação eq. 20–37 p. 36–39; arraste de ar para Froude > 1,6 p. 39–40; **limitações do 1D permanente** (permanente, gradualmente variado, 1D, declividade < 1:10; tabela cos θ por declividade) p. 40–41.
- Seções transversais: espaçamento p. 117 (e critérios por equação de atrito); comprimentos de trecho p. 123; interpolação de seções p. 137–139; regime misto p. 139–141; junções por energia e por momentum p. 141–151; distribuição de vazão p. 151; tubo pressurizado e tampas ("lids") p. 154–160.

### 1D não permanente (Saint-Venant)
- Continuidade p. 41–43; momentum e as forças de pressão, gravidade e atrito (eq. 40–67) p. 43–46; uso no HEC-RAS (canal + planície, Barkau) p. 46–48; **esquema implícito de 4 pontos**: estável para 0,5 < θ ≤ 1,0, condicionalmente para θ = 0,5, instável para θ < 0,5; recomenda estudo de sensibilidade p. 48; Tab. 1–4 de diferenças finitas e coeficientes p. 55–56; condições de contorno 1D (montante: hidrograma de vazão; jusante: hidrograma de nível, de vazão, **curva-chave de valor único**, **normal depth** com declividade informada, com aviso de que a profundidade normal raramente existe e o contorno deve ficar longe da área de estudo) p. 58–62; tolerância numérica e iterações (máx. 20 por padrão; usa a melhor tentativa e avisa) p. 66–67; esquema volume-finito semi-implícito p. 67–74.
- Dados de escoamento não permanente e condições iniciais p. 134–135.

### 2D (SWE, difusão, numérica)
- Introdução (SW × difusão; sub-malha) p. 74–75; continuidade com porosidade p. 76; momentum SWE (termos: aceleração, Coriolis, pressão, difusão, atrito, vento, onda, arrasto) p. 77; atrito de fundo por Manning p. 78; Coriolis e arrasto p. 79; **turbulência/viscosidade turbulenta (Smagorinsky 0,05–0,2) e Tab. 1 e 2 de coeficientes de mistura longitudinal e transversal** p. 79–80; vento (4 fórmulas de Cd) p. 80–83; forçamento de onda p. 83–84; **aproximação de onda difusa (DSW)** a partir de p. 84, equação final p. 86; contornos 2D (nível, normal depth com declividade de atrito, vazão) p. 86.
- Malha e malha dual: **máximo 8 lados, células convexas, malha não precisa ser ortogonal mas a precisão é maior se for** p. 86; batimetria de sub-malha p. 89–92.
- Métodos numéricos: três solvers (DWE, SWE-ELM, SWE-EM), face-normal gradient p. 92; algoritmo de solução (laço de iteração tipo Newton) p. 74, 97, 99; ELM-SWE semi-Lagrangiano, "sub-passos com Courant ≤ 1 permitem passo grande sem perder estabilidade" p. 99–100; **SWE-EM: exige malha estritamente ortogonal e passo limitado pela condição CFL (eq. 209–210 na imagem)** p. 108–109; solvers de matriz (PARDISO direto; SOR/ASOR; FGMRES-SOR), critérios de parada e **Tab. 1 status do solver (Iterating/Converged/Stalled/Max Iterations/Divergent)** p. 109–112.

### Rugosidade de Manning e n composto
- Fatores que afetam n, calibrar com NA observado quando houver p. 124; **Tab. 3-1 n de Manning (Chow: canais naturais, planícies, concreto, etc.)** p. 124–126 (continua até p. 128, não lido); **Tab. 3-2 rugosidade equivalente k** p. 130; conversão k→n (eq. 215–217) p. 129–130; variação horizontal de n p. 129; n para condutos (Tab. 6-1 p. 232–233; **Tab. 6-2 corrugado** p. 233–234).
- n na ruptura de barragem: sensibilidade de n ±20 % p. 388–389; n subestimado em rios íngremes (Jarrett) p. 390–391, 399.

### Coeficientes de contração/expansão
- **Tab. 3-3** (sem perda 0/0; transição gradual 0,1/0,3; seção de ponte típica 0,3/0,5; abrupta 0,6/0,8; máximo 1,0) p. 131 e idêntica **Tab. 5-2** p. 180; supercrítico: gradual 0,01/0,03 e abrupto 0,05/0,2 p. 131; ponte classe C 0,03/0,05 (abrupto 0,05/0,1) p. 181; estudo RD-42 e recomendações no Apêndice p. 418–428.

### Pontes
- Quatro seções (1, 2, 3, 4) e duas internas; distância de expansão Le por **Tab. 5-1 razões de expansão** p. 173–174; seção 2 e 3 junto ao pé do aterro, nunca "1 ft" da face p. 175; seção 4 a ~1× comprimento médio da constrição p. 175; áreas inefetivas p. 176–179; perdas de contração/expansão p. 179–181.
- **Baixa vazão** (classes A, B, C por momentum crítico): métodos energia (standard step), **momentum**, **Yarnell** (só trapezoidal com pilares; Tab. K por forma do pilar p. 187), **WSPRO** (só subcrítico) p. 181–189; classe B e C p. 189; **vazão alta**: energia ou pressão+vertedor; pressão com comporta/orifício (C típico 0,8; faixa 0,7–0,9) p. 190–193; vertedor (coeficientes de descarga) p. 194–195; combinação p. 196. **Escolha do método** (quando usar energia, momentum, Yarnell, WSPRO) p. 196–198.
- Casos especiais: ponte suspensa, de baixa lâmina, esconsa, paralela, múltiplas aberturas, detritos de pilar p. 198–204; **pontes em 2D** (simplificado 1D/2D e detalhado) p. 204–208. Apêndice: transições no remanso de ponte p. 418–428; coeficiente de descarga e comprimento efetivo do WSPRO p. 434–438.
- Pontes/bueiros múltiplos: pontos de estagnação, abordagem de abertura múltipla e de fluxo dividido p. 247–252. Erosão (contração, pilar CSU e Froehlich, encontros HIRE) p. 282–294; Tab. 10-1 a 10-4 p. 287–291.

### Bueiros
- Tipos e até 25 barris idênticos p. 210–211; **quatro seções (1:1 contração, 1,5:1 expansão)** p. 211–214; limitação: forma, vazão e declividade constantes p. 215; **controle de entrada × saída** (conceito e verificação do controle de entrada com ressalto) p. 218–219; **carga a montante com controle de entrada** (equações FHWA 279–281, sub e não submerso; precisão dos nomogramas ~10 %, calculados para 2 % de declividade) p. 219–220; controle de saída p. 220–222; perfil por passo direto, profundidade normal e crítica, declividade horizontal/adversa, vertedor, regime supercrítico/misto, n múltiplos, bueiro parcialmente cheio ou enterrado p. 222–228; **comparação com os exemplos do USGS (Ex. 6, 7, 8; Ex. 8 questionado)** p. 228–229.
- Coeficientes: forma e dimensão p. 230–231; comprimento e barris p. 232; n p. 232–234; **perda de entrada** (equação 288 e Tab. 6-3 tubos, 6-4 caixa, 6-5 ConSpan; borda viva 0,5 e bem arredondada 0,2) p. 234–235; perda de saída p. 236; **Tab. 6-6 números de carta e escala FHWA** p. 237–245; cotas de fundo e coeficiente de vertedor p. 245. (Tab. 6-3 a 6-5 e 6-6 localizadas por busca; conteúdo de 6-3 a 6-6 não lido.)
- Observação: o texto de p. 214 remete os coeficientes de contração/expansão a "table 3-2", mas a tabela correta é a 3-3 (p. 131).

### Estruturas em linha e laterais, canal estável, ruptura
- Comportas (radial, plana, sobre-fluxo; exemplo de comporta radial em baixa vazão p. 262) p. 258–264; **Tab. 8-1 coeficientes típicos de vertedor** p. 265; submergência p. 265; estruturas laterais (Hager) p. 266–270; quedas p. 270–273.
- Canal estável: rugosidade de fundo, Tab. 12-1 a 12-8 (grama p. 311, preditores p. 312, Copeland p. 318, força trativa p. 328, velocidade de queda p. 333, granulometria p. 335, funções de transporte p. 339).
- **Ruptura de barragem** (aqui por causa dos critérios de passo de tempo e estabilidade): roteamento no reservatório p. 345–349; parâmetros de brecha (Tab. 13-1 a 13-5 p. 351–369; abordagem recomendada p. 373; **exemplo resolvido fictício** p. 375–380); espaçamento de seções (equações de Samuels e de Fread) p. 381–383; **passo de tempo e Courant** p. 384–387; n e sensibilidade p. 387–391; planície e diques p. 391–395; pontes e bueiros p. 396–398; rios íngremes p. 399–400; quedas no perfil p. 400; **condições iniciais e vazão base (1 % do pico, nunca acima de 10 %), canal piloto, contorno de jusante** p. 401–403; uso de áreas 2D p. 404–406.

### Precipitação e infiltração no 1D e opções
- Déficit-constante, **CN (abstração inicial Ia = razão 0,05–0,2 × S, p. 165; Tab. 4-2 grupos de solo p. 165; Tab. 3 CN p. 166)**, Green-Ampt (Tab. 4 parâmetros por textura p. 171) p. 164–172. Vazão de áreas sem posto (otimização) p. 160–164.

### Estabilidade e instabilidades (HRM)
Causas e remédios localizados: espaçamento de seções grande demais (Courant ≫ 1, p. 382) ou curto demais (p. 384–385); passo grande demais (atenua o pico em cerca de 10 % no exemplo 10 min × 1 min, p. 384–385) ou pequeno demais (< 0,1 s, arredondamento, p. 386); n subestimado ou mudança abrupta de n p. 390; pontes e bueiros (curvas que não sobem o bastante) p. 396; rios íngremes (rodar em regime misto) p. 399; quedas que forçam crítica p. 400; condição inicial inconsistente (vazão de comporta e níveis de áreas de armazenamento) p. 401–402; baixa vazão e poços/corredeiras p. 403; contorno de jusante p. 403; coeficientes de contração/expansão de subcrítico usados em supercrítico geram oscilações p. 131; tubo pressurizado na transição aberto/fechado p. 160.

### Tabelas, ábacos e exemplos do HRM (para citação)
Tabelas (≈ 40): 3-1 n p. 124–126; 3-2 k p. 130; 3-3 contração/expansão p. 131; 4-1 equação de atrito p. 137; 4-2 grupos de solo p. 165; Tab. 3 CN p. 166; Tab. 4 Green-Ampt p. 171; 5-1 razão de expansão p. 174; 5-2 p. 180; K de Yarnell p. 187; 6-1 a 6-6 p. 232–237; 8-1 p. 265; 10-1 a 10-4 p. 287–291; 11-1 n sob gelo p. 296; 12-1 a 12-8 p. 311–339; 13-1 a 13-5 p. 351–369; mistura 2D (Tab. 1–2) p. 80; solver (Tab. 1) p. 111; diferenças finitas (Tab. 1–4) p. 55–56. Exemplos: bueiros × USGS p. 229; comporta radial p. 262; brecha de barragem p. 375; instabilidade por espaçamento p. 384–385; ponte com pressão e vertedor (figura) p. 194; amostras de transporte de sedimento p. 466 (apêndice, não lido). Ábacos: nenhum de projeto; os de bueiro FHWA são referenciados (cartas) p. 236–245.
Páginas lidas (inteiras ou em parte): ≈ 95 (24–49, 74–92, 99–100, 108–112, 123–137, 173–181, 196–197, 211–215, 218–221, 229–234, 384–387, 402–404; mais ≈ 60 por busca dirigida com leitura de linhas). Observação: passou o teto de 80 páginas do brief por ~15, por causa das leituras parciais de equações perdidas na extração.

### USACE-HECRAS-2DUM-66 — HEC-RAS 2D Modeling User's Manual, v6.6 (USACE HEC, exportado set/2024)
Vigência: v6.6, mesma edição; licença: domínio público; 286 p. (nativo). Capítulos pelo sumário: Intro p. 10–14; Terreno e camadas (n, solo, infiltração, porosidade) p. 15–50; Malha e 1D/2D p. 51–140; Contornos e condições iniciais p. 141–195; Rodar o modelo p. 196–227; Saída no Mapper p. 228–269; **1D × 2D, permanente × não permanente p. 270–273**; hardware p. 274; referências p. 276.

### Fluxo de trabalho e limitações
Passos 1 a 16 de um modelo 2D ou 1D/2D (projeção, terreno, n, polígono, breaklines, malha, estruturas, pré-processador, conexões, contornos, opções, rodar, revisar) p. 13–14; limitações atuais (sem qualidade de água em 2D etc.) p. 14–15 (a lista foi lida só em parte); conjuntos de exemplo Muncie e BaldEagle p. 24 (citados, não lidos).

### Equações 2D: SWE-ELM, SWE-EM e difusão — quando usar cada
- **Difusão é o padrão** do programa (p. 196 e 211); rodar com difusão durante o desenvolvimento e depois criar um 2º plano em SWE e comparar; havendo diferença significativa, considerar a SWE a mais precisa p. 196.
- **Situações em que a SWE deve ser usada** (lista numerada de 8): ondas muito dinâmicas (ruptura, cheia relâmpago), contrações/expansões abruptas, rios muito planos (declividade menor que 1 ft/mi), influência de maré, propagação de ondas por manobra de comportas, superelevação em curvas, velocidades e níveis detalhados em estruturas, regime misto p. 196–197.
- SWE-ELM = original e mais rápido; SWE-EM = mais conservativo em momentum, explícito, só necessário para o detalhe em pilares, encontros e contrações fortes p. 211; SWE também oferece Coriolis e turbulência p. 196, 210, 214–216. Restart pode mudar de equação (difusão → SWE) p. 187.
- Teoria dos três solvers: HRM p. 84–112 (ver acima).

### Malha 2D
- Polígono do 2D e **limite 1D/2D deve ser terreno alto** p. 51–52; criação da malha, tamanho nominal base, ajustes por breaklines e regiões de refinamento p. 53 e 56; parâmetros do gerador (Cell Minimum Area Fraction, Face Conveyance Tol Ratio) p. 55; **o tamanho da célula deve seguir a declividade da superfície da água e as barreiras ao fluxo; sub-malha permite células maiores que em modelos de elevação única** p. 56, 64, 198–199; transição gradual de tamanhos p. 199.
- **Breaklines**: em qualquer barreira (diques, estradas, terreno alto), "near spacing", "near repeats", "far spacing" p. 57–58; **regiões de refinamento** p. 60–62; **malha de canal** (região de refinamento ao longo do canal + breakline no eixo, 4 near repeats no exemplo) p. 62–63; refinar na margem alinha faces à crista da margem p. 199.
- **Problemas de malha e correções** (contorno côncavo agudo, mais de 8 lados, centros duplicados ou fora do polígono, faces colineares por breaklines paralelas próximas, "bleed over") p. 64–69.
- **Não há valor numérico recomendado de tamanho de célula** nas páginas lidas: o texto é qualitativo (p. 53, 56, 198–199). Teste de consistência: refinar a malha e reduzir o passo juntos, testar ΔX e ΔT p. 201.
- Tabelas hidráulicas e pré-processador 2D p. 69–77; **n por face: padrão = valor no centroide da face, v6.4+ permite n composto em função da cota (fórmula como no 1D, válida para n de 0,01 a 0,1); para edificações sugere n de 0,25 a 0,5** p. 74–76.

### Rugosidade e uso do solo
Camada de cobertura e tabela n × classe, impermeabilidade p. 27–28; polígonos de classificação do usuário (ex.: canal principal n 0,035, p. 28); regiões de calibração de n p. 29–32; **tabela de n por classe NLCD** (faixas, para profundidades apreciáveis, não para escoamento raso) p. 30–31; curvas de fator de rugosidade em regiões de calibração p. 135–141; porosidade e arrasto (edificações, enrocamento, vegetação) p. 44–50.

### Conexões 1D/2D e estruturas
Estrutura lateral rio → 2D (coeficiente de vertedor, tabelas de estaqueamento) p. 78–92; **Tab. 3-1 coeficientes de vertedor lateral** (levee ≥ 3 ft acima do terreno 1,5–2,6, padrão 2,0; elevação 1–3 ft 1,0–2,0; barreira natural 0,5–1,0; terreno não elevado 0,2–0,5; e equivalentes SI) p. 91–92, com o aviso de que o erro mais comum é coeficiente alto demais e o decaimento de submergência (expoente 3,0) p. 92; **reach 1D diretamente ligado a 2D a montante ou a jusante** (último XS alinhado ao contorno; n idêntico entre a seção e a zona 2D, senão "o modelo fica instável de imediato"; usar rampa de condição inicial) p. 92–97; 2D com área de armazenamento ou outro 2D p. 97–103; vários 2D em um arquivo p. 103; estruturas dentro do 2D (vertedor, comporta, bueiro, outlet RC/TS) p. 104–110; **pontes dentro do 2D** (centerline, dados, curvas pré-processadas; mesmos métodos de baixa vazão energia/momentum/Yarnell e de alta vazão, **exceto WSPRO**) p. 110–125; estações de bombeamento p. 126–135.

### Condições de contorno e iniciais (2D)
- **Quatro externos**: hidrograma de vazão, hidrograma de nível, normal depth, curva-chave; **normal depth e curva-chave só para saída**; vazão positiva entra; duas condições distintas não podem ficar na mesma face p. 141–142. Hidrograma de vazão exige declividade de energia e distribui por condutividade p. 144; hidrograma de nível (opção "Use Initial Stage") p. 144; **normal depth exige declividade de atrito, que pode vir da declividade do terreno junto ao contorno** p. 144–145; curva-chave p. 145; nível espacialmente variável (ADCIRC) p. 145–163.
- Internos: hidrograma de vazão interno (ligar o hidrograma de sub-bacia, cuidado com dupla propagação) p. 163–165; precipitação no 2D p. 165.
- **Condições iniciais**: seco (padrão), nível único, arquivo de restart, interpolação de resultados anteriores, **rampa de condição inicial** (fração 0,1 por padrão), pontos de condição inicial p. 187–195; um 2D ligado direto a um reach 1D não pode começar seco p. 187.

### Chuva na malha, infiltração e evapotranspiração
- Precipitação como contorno por área (mesma lâmina em todas as células, método antigo) p. 165; **chuva global distribuída**: em grade (DSS ou NetCDF/GRIB via GDAL) p. 165–169; por postos com interpolação (**Thiessen, inverso do quadrado da distância, restrito, "peak preservation"**; célula de rasterização padrão de 2 km) p. 177–181; razão e sobrescrita de unidades p. 168; evapotranspiração (potencial; não usada no CN) p. 181; vento p. 181–184; pressão atmosférica p. 184–187.
- Métodos de perdas na malha: **CN** (razão de abstração inicial 0,05–0,2, p. 39; **Tab. 2-2 CN** p. 40; **Tab. 2-3 CN urbano** p. 41), déficit-constante (**Tab. 2-4 grupos de solo** p. 42), Green-Ampt (**Tab. 2-5 por textura** p. 43–44; parte numérica da tabela na p. 44), estimativa de parâmetros p. 44; camadas de solo (SSURGO) e de infiltração p. 32–38. O manual 2D traz o mecanismo de chuva na malha; **não traz recomendação de tamanho de célula nem passo para chuva na malha** nas páginas lidas (a confirmar no Applications Guide).

### Passo de tempo, Courant e tolerâncias
- **Seleção de malha e passo** p. 198–201: passo depende de ΔX e da velocidade; guia de Courant para SWE-ELM, SWE-EM e difusão (as expressões estão na imagem, p. 200); **meta C = 1,0 para a SWE, mas "pode-se chegar a 3,0 nas SWE e 5,0 na difusão"; usar C ≈ 1 em zonas de alta velocidade, em ondas rápidas ou com o 2D começando seco** p. 200–201; difusão às vezes precisa de C ≤ 1 (hidrogramas muito rápidos, canal seco) p. 200; plotar o Courant no Mapper p. 201.
- **Passo variável** (v6.0): fixo; por Courant (máximo, mínimo menor que metade do máximo, número de passos abaixo do mínimo antes de dobrar de 5 a 10 típico, máximos de dobras e de metades; o passo é cortado ao meio quando se excede o máximo; o passo tem de bater com o intervalo de saída do Mapper); por série de divisores p. 201–205.
- **Parâmetros de plano 2D** p. 209–220: **θ (0,6–1,0; padrão 1,0)**, θ de aquecimento p. 210; **tolerância de nível 0,01 ft (máx. 0,2)** e **tolerância de volume 0,01 ft**; **iterações máximas 20 (0 a 40)** p. 210–211; conjunto de equações p. 211; rampa de condição inicial p. 211; fatias de tempo p. 212; **convergência avançada** (máx. 0,15 ft, RMS 0,002 ft, estagnação 1 %) p. 212–214; mistura turbulenta (padrão desligada; modelos Nenhum/Conservativo/Não conservativo; tabelas de DL e DT) p. 214–216; Smagorinsky, checagem de volume no contorno, latitude de Coriolis, núcleos p. 216–217; solvers de matriz (PARDISO padrão; SOR relaxação 1,3; FGMRES reinício 10) p. 218–220; **iteração 1D/2D** (desligada por padrão, 0–20; começar com 3 ou 4; tolerância de vazão 0,1 %; mínimo de 1 cfs) p. 220; novo 1D de volume-finito (rápidas subidas sem instabilidade; tampas "lids" instáveis ao tocar a corda inferior) p. 221–225; vento p. 225–227.
- **Acompanhamento, estabilidade e erro de volume**: mensagens por tolerância não atingida e **log com balanço de volume do modelo e de cada 2D (exemplo: ganho de 123,5 acre-ft = 0,02017 %, "muito baixo")** p. 207–208. Não há limiar de aceitação em % de erro de volume escrito no manual (só o exemplo).

### Saída, 1D × 2D
Mapa e velocidades p. 228–269 (não lido); arquivo HDF5 de saída p. 257; **1D × 2D e permanente × não permanente** (lista de fatores para decidir; **permanente não deve ser usado em maré, ondas rápidas, fluxo reverso, galgamento de dique, rios muito planos, bombas, comportas complexas**; depende de a hidrologia já ter roteado bem) p. 270–273; remete ao TD-41 (HEC) p. 270.

### Instabilidades (2D) e remédios localizados
n diferente entre a seção 1D e a zona 2D conectada p. 94 e 97; começo com vazão ou nível de contorno alto demais ou com 2D seco ligado a 1D (usar rampa) p. 190–191, 211; vazões de bombas variando rápido p. 131; coeficiente de vertedor lateral alto e submergência de 95–100 % p. 92; passos grandes demais para a SWE p. 199–201; faces colineares e malha defeituosa p. 67–68; mais iterações só como último recurso (tolerância e máximo) p. 211, 220; resultados mudam levemente se o solver itera muito e há instabilidades p. 217.

### Tabelas e exemplos do 2DUM
Tabelas: n NLCD p. 30–31; CN p. 40 e 41; grupos de solo p. 42; Green-Ampt p. 43–44; porosidade p. 48; Tab. 3-1 vertedor lateral p. 91–92; mistura p. 215. Exemplos: balanço de volume p. 208; canal principal com n 0,035 p. 28; malha de canal p. 62–63; conjuntos Muncie e BaldEagle p. 24; rampa de condição inicial p. 190–191 (valores de exemplo 1 000 cfs). Ábacos: nenhum.
Páginas lidas (inteiras ou em parte): ≈ 75 (13–15, 24–31, 53, 56, 64–69, 74–76, 91–92, 110–111, 141–147, 165–168, 181, 187–192, 196–221, 270–273; resto por busca).

## Divergências e pontos de atenção entre as fontes (e com o PLANO)
1. **Equação padrão e quando usar SWE.** [USACE-HECRAS-2DUM-66 p. 196 e 211]: difusão é o padrão e a SWE entra nos 8 casos listados (p. 196–197). O HRM descreve as duas famílias (p. 74–86, 92) sem indicar padrão. O PLANO §11.2 item 1 diz "SWE-ELM por padrão": conflita com o 2DUM p. 196 e 211; revisar antes de F6.
2. **Courant.** [USACE-HECRAS-HRM-66 p. 386–387] (1D em ruptura): Courant 1 e passo prático como limite superior, com a velocidade máxima corrigida por um fator para estimar a celeridade. Em outro manual, [USACE-HECRAS-2DUM-66 p. 201] diz que C pode chegar a 3 (SWE) e 5 (difusão), com 1 em ondas rápidas ou domínio seco; SWE-EM com CFL ≤ 1 [USACE-HECRAS-HRM-66 p. 108 e 2DUM p. 199, p. 211].
3. **n composto.** [USACE-HECRAS-HRM-66 p. 27–29]: no 1D o composto só vale com talude do canal mais íngreme que 5H:1V e mais de um n. [USACE-HECRAS-2DUM-66 p. 75]: no 2D o padrão é n do centroide da face; composto por cota só v6.4+ (n de 0,01–0,1; edificações 0,25–0,5). **Dentro do próprio 2DUM**: [p. 30] diz que na v6.0 só um n por face e que "versões futuras" permitirão vários, contra [p. 75] v6.4+ (texto não atualizado).
4. **Coeficientes de contração/expansão em supercrítico.** Ponte em classe C: 0,03/0,05 e abrupto 0,05/0,1 [USACE-HECRAS-HRM-66 p. 181]. Supercrítico geral: 0,01/0,03 (gradual) e 0,05/0,2 (abrupto) [USACE-HECRAS-HRM-66 p. 131]. Subcrítico idêntico em p. 131 e 180. Referência cruzada de p. 214 aponta "table 3-2" (a tabela é a 3-3, p. 131).
5. **Pontes no 2D.** [USACE-HECRAS-HRM-66 p. 204–208] descreve a abordagem simplificada 1D/2D e a detalhada; [USACE-HECRAS-2DUM-66 p. 110] acrescenta que o método WSPRO não existe para pontes dentro do 2D (os do HRM p. 181–198 incluem WSPRO no 1D).
6. **Coeficientes de vertedor.** [USACE-HECRAS-HRM-66 p. 265, Tab. 8-1] valores típicos de vertedor em linha; [USACE-HECRAS-2DUM-66 p. 91–92, Tab. 3-1] estruturas laterais com coeficientes bem menores e o aviso de que o erro frequente é usar coeficiente alto demais.
7. **θ e tolerâncias.** [USACE-HECRAS-HRM-66 p. 48] 1D implícito: estável para θ acima de meio até 1,0 [USACE-HECRAS-HRM-66 p. 48] e só condicionalmente em meio; [USACE-HECRAS-2DUM-66 p. 210] 2D: θ 0,6–1,0, padrão 1,0. Tolerâncias: 1D permanente 0,01 ft (mínimo-erro até 0,3 ft) [USACE-HECRAS-HRM-66 p. 32–33]; 2D nível 0,01 ft, volume 0,01 ft, máx. 20 iterações [USACE-HECRAS-2DUM-66 p. 210]. São solvers diferentes; não somar.
8. Consistentes (sem divergência): tabelas de mistura turbulenta [USACE-HECRAS-HRM-66 p. 80 × 2DUM p. 215]; razão de abstração inicial 0,05–0,2 [USACE-HECRAS-HRM-66 p. 165 × 2DUM p. 39]; contornos 2D de nível/normal depth/vazão [USACE-HECRAS-HRM-66 p. 86 × 2DUM p. 141].
Total: 7 divergências e pontos de atenção (3 entre os manuais, 3 dentro de um mesmo manual ou com o PLANO, 1 de escopo).

## Lacunas (o que este grupo não cobre)
- Sem **tamanho de célula numérico** e sem passo de tempo específico para chuva na malha (rain-on-grid) nos trechos lidos; as orientações são qualitativas (2DUM p. 53, 56, 198–201). Possível complemento: Applications Guide (link_only) e o UM-66.
- Sem critério numérico de aceitação para erro de volume (só o exemplo de 0,02 %, 2DUM p. 208) e sem critério de estabilização do NA; o PLANO §11.2 (item 7) é de autoria interna.
- Equações numeradas (energia, momentum, SWE, Courant, Yarnell, WSPRO, FHWA de entrada, Manning composto) ficaram **na imagem**: conferir no PDF antes de codificar a calculadora. Tabelas de bueiro 6-3 a 6-6 e cartas FHWA p. 235–245, tabelas de n p. 126–128 (parte), apêndice WSPRO p. 434–466 e capítulos de sedimentos, gelo, erosão e dam break (parâmetros de brecha) só foram localizados.
- Parâmetros de plano do 1D não permanente (θ do 1D, tolerâncias, passo) estão no UM-66, não mapeados aqui; as p. 58–67 do HRM só confirmam o esquema e as iterações.
- Referência do PLANO a "2DUM p. 11" (vantagens do 2D) não foi conferida; a do HRM p. 389 (±20 % de n) e as de p. 196–203, 144–145, 53, 180 e 218–220 foram conferidas.
- Sem dados brasileiros (n, CN, IDF); unidades em ft/cfs; tabelas de n são de Chow (1959).


---

## Mapa parcial F3 — grupo HECRAS_B (Especialista Drenagem, escopo HEC-RAS, PLANO.md seção 11)

Convenção de páginas: "p. N" = página física do PDF (marcador `<!-- p. N -->` do `_texto`). Nos dois manuais a página impressa
("HEC-RAS User's Manual– N", "HEC-RAS Mapper User's Manual – N") coincide com a física, e os marcadores do Sumário (bookmarks) também;
conferido por amostra (UM p. 32, 60, 180, 231, 311, 610; Mapper p. 22, 33, 59, 132, 152). Camada de texto nativa nos dois (sem OCR); as figuras
(telas do programa) não têm texto: valores só em figuras ficam "(conferir na imagem)". Nada abaixo substitui a fonte; valor numérico é só localizador.
Este mapa cobre o fluxo de trabalho, entrada de dados, n e calibração, contornos e condições iniciais, estabilidade, resultados, Mapper e mapas de
inundação. O motor 2D (SWE-ELM/difusão, malha, Courant 2D) está no `USACE-HECRAS-2DUM-66` e a teoria/n de tabela/pontes no `-HRM-66` (outros grupos).

### USACE-HECRAS-UM-66 — HEC-RAS User's Manual, v6.6 (USACE HEC, 2024)
Vigência: v6.6 (a mais recente; 6.6 = versão de uso do plano); licença: domínio público; 837 p. (nativo). Prioridade A.
O manual é de **operação do programa**: diz onde clicar, quais campos e quais opções existem. Não traz tabela de n de Manning por tipo de leito/uso
(ver lacunas) nem teoria (isso está no HRM).

### Fluxo de trabalho de um modelo
- **Cinco passos** (projeto, geometria, escoamento e contornos, cálculo, resultados): p. 32; detalhe p. 33–42 [USACE-HECRAS-UM-66 p. 32]. Arquivo `.prj`, escolha do sistema de unidades antes de entrar dados: p. 33.
- Dados mínimos de uma seção (estação-cota, comprimentos a jusante, n das margens e do canal, estacas das margens, coeficientes de contração/expansão 0,1 e 0,3 como padrão): p. 35, 60–62 [USACE-HECRAS-UM-66 p. 35, 62]. Seções ordenadas da maior estaca (montante) para a menor (jusante): p. 35, 61.
- Plano = geometria + escoamento; regime subcrítico/supercrítico/misto; opções de simulação: p. 38; arquivos do projeto (.prj, .g, .f/.u, .p, .r, .o) e HDF5 de saída/geometria que alimenta o Mapper: p. 43–48 (HDF p. 45) [USACE-HECRAS-UM-66 p. 44–45].
- Layout geoespacial (estaca do rio, seções, áreas 2D, estruturas) pode ser feito no Mapper; parametrização final volta ao editor de geometria: p. 33–34 [USACE-HECRAS-UM-66 p. 34].
- Seção e tabelas de edição em lote: dados de seção p. 60–70; **tabela de n (somar constante, multiplicar, fixar, reduzir canal a um n)** p. 167–168; comprimentos p. 168; coeficientes de contração/expansão p. 169–170; níveis de ineffective p. 175; ferramentas de geometria (filtro de pontos, ajuste de datum vertical, achar laços) p. 188–204.
- Interpolação de seções: Seção "Cross Section Interpolation" tem bookmark p. 155 (conteúdo de bombas termina nessa página; a interpolação em si fica nas p. ~156–161, a confirmar); uso como teste de espaçamento: p. 313, 328.
- Geometria 2D e áreas de armazenamento no editor: áreas de armazenamento p. 128–130 (volume-elevação a partir do terreno; ligação por estrutura lateral); malha 2D (DX, DY, breaklines, n padrão da área, tolerâncias de volume e de perfil de face, padrão 0,01 ft) p. 131–140 [USACE-HECRAS-UM-66 p. 133–134]; condições de contorno externas de área 2D/armazenamento p. 148.

### Estruturas (entrada)
- **Pontes e bueiros**: quatro seções (1 a jusante com expansão plena, 2 junto ao pé do aterro de jusante, 3 junto ao de montante, 4 a montante com contração) p. 73–75; **tabela de razões de expansão** (b/B, declividade, n_marg/n_canal; ft/mile) p. 74; contração 1:1 como primeira estimativa p. 75; perdas de contração/expansão p. 75–76; cálculo de baixa vazão, pressão e vertedor p. 76–; editor de ponte p. 77–90; projeto de ponte p. 90–91; **bueiro**: controle de entrada (equações FHWA) e de saída, nove formas, "chart#/scale#" FHWA, coeficientes de entrada/saída, n do topo e do fundo p. 92–97 [USACE-HECRAS-UM-66 p. 92, 95]; opções p. 97–99; pontes em áreas 2D p. 100; múltiplas aberturas p. 101–105.
- Estruturas internas, laterais, conexões SA/2D, bombas: p. 105–127, 140–155; roteamento linear `Q = K·(armazenamento)/hora` p. 128 [USACE-HECRAS-UM-66 p. 128].
- Junções (energia ou momento): p. 70–72; problemas de junção em escoamento forte p. 326–327.
- Em bueiro e ponte, o HEC-RAS confere cota de montante; o dimensionamento do bueiro segue `bueiros-e-travessias` (PLANO 11.2, item 6).

### n de Manning e calibração
- n na seção: mínimo 3 valores (margem esquerda, canal, direita); variação horizontal (até 20 por seção) e vertical: p. 62 [USACE-HECRAS-UM-66 p. 62]. Nova seção herda n da seção de montante: p. 63.
- **n por classificação do uso do solo (Land Classification)**: tabela na geometria p. 180–181; vale hoje só para áreas 2D; base override e polígonos de região de n ("2D Area Mann n Regions") p. 181 [USACE-HECRAS-UM-66 p. 180–181]. Ver Mapper p. 59–61 e 97–99.
- Compositagem do n do canal principal e opções de geometria: p. 205; "Set Channel to Single Value" p. 201.
- **n variável com a vazão/estação**: "Flow Roughness Factors" (tabela vazão × fator, por trecho; pode ficar na geometria ou no plano, e aplicar nos dois **duplica** o fator) p. 202–203; "Seasonal Roughness Factors" p. 203–204; no plano p. 277–278 [USACE-HECRAS-UM-66 p. 202–203, 277–278]. Regra geral: n cai com o aumento da vazão e da profundidade em rio livre; sobe se a margem é mais rugosa que o leito: p. 301.
- **Tabela de n por forma de fundo aluvial** (ondulações, dunas, dunas lavadas, leito plano, ondas estacionárias, antidunas; faixas de n; fonte Simons, Li & Associates): p. 305 [USACE-HECRAS-UM-66 p. 305].
- **Calibração do modelo não permanente**: definição p. 298; qualidade dos dados observados (cotas ±1 ft; vazão de curva-chave ±5 % do USGS, que equivale a ±1 ft; marcas de cheia, com ressalvas sobre pilar e várzea) p. 299–300; área não monitorada por razão de áreas (exemplo Red River of the North) p. 300–301; geometria e armazenamento p. 301, 306–307; curvas de vazão em laço p. 302–303; rios aluviais p. 303–306 [USACE-HECRAS-UM-66 p. 298–306].
- **Passos de calibração** (oito etapas: permanente por curva-chave e marcas de cheia; eventos; armazenamento e vertedores laterais para hidrograma; n para cotas; fatores vazão-rugosidade; fatores sazonais; verificação em eventos não usados; reajuste): p. 309 [USACE-HECRAS-UM-66 p. 309]. **Tendências ao subir n** (cota local sobe, pico atenua, tempo de percurso aumenta, laço alarga) p. 309; ao subir armazenamento p. 310. **Sugestões e avisos** (calibrar a cotas; não forçar n irreal; contorno por curva-chave afastado; DEM de 10 m não calibra bem; armazenamento fora do canal subestimado; eventos de baixa a alta) p. 310–311 [USACE-HECRAS-UM-66 p. 310–311].
- Dados observados no editor (séries, marcas de cheia, curva-chave de posto, perfis medidos para comparação em gráficos e tabelas): permanente p. 233–235 (Observed WS; Observed Rating Curves); não permanente p. 260–265 [USACE-HECRAS-UM-66 p. 233–235, 260].
- **Calibração automática de n (não permanente)**: otimização global ou sequencial por trechos e zonas de vazão; precisa de série de cotas observada; produz tabela vazão × fator de rugosidade: p. 725–734 [USACE-HECRAS-UM-66 p. 725–728]. Otimização de hidrograma p. 735–739. Comparador de modelos p. 780–793.
- **Sensibilidade**: numérica (passo, theta, fatores de vertedor) p. 327–328; **física**: n com faixa realista (exemplo n estimado em 0,035, faixa 0,03 a 0,045), espaçamento de seções (dobrar o número por interpolação), armazenamento em seção, coeficientes de vertedor lateral p. 328–329 [USACE-HECRAS-UM-66 p. 327–328]. Rodar eventos de TR (2, 5, 10, 25, 50, 100) como análise de incerteza p. 328.

### Condições de contorno e iniciais
- **Permanente**: subcrítico exige só contorno de jusante, supercrítico só de montante, misto os dois p. 36; vazão por trecho e por seção (mudanças de vazão), perfis múltiplos p. 231; opções "Set Changes in WS and EG" (Known WS, K Loss etc.) p. 232–233; aberturas de comporta p. 235; cotas de armazenamento p. 236. Tipos de contorno de jusante (cota conhecida, profundidade crítica, profundidade normal, curva-chave) na tela de contornos: tela p. 36 (texto dos tipos a confirmar em p. 231–236).
- **Não permanente** (editor p. 246–247): hidrograma de vazão (DSS ou tabela; "Critical Boundary Condition", vazão mínima, multiplicador) p. 248–250; hidrograma de cota p. 250; cota e vazão combinadas p. 251; **curva-chave (valor único, sem laço) e profundidade normal** (usar declividade de energia; colocar longe do trecho) p. 251–252; vazão lateral e lateral uniforme p. 253; interfluxo de água subterrânea (Darcy) p. 253; comportas p. 253–255; contorno interno de cota/vazão p. 255–257; regras do usuário p. 257; **precipitação e vento (meteorologia) p. 257–258** [USACE-HECRAS-UM-66 p. 248–258].
- **Condições iniciais**: vazão por trecho + remanso permanente (o método comum), cota inicial de armazenamento, partir de perfil de execução anterior (útil para oscilação): p. 258–259; cotas iniciais internas e razão/mínimo global de vazão p. 260 [USACE-HECRAS-UM-66 p. 258–260].
- Precaução: abrir e fechar comportas rápido instabiliza p. 254; transição abrupta de cota para vazão forçada gera "choque" p. 256–257.

### Perfil permanente e não permanente (parâmetros de cálculo)
- **Permanente**: método de conveyance (quebras de n × entre cada ponto) p. 239–240; cinco métodos de declividade de atrito p. 240; **tolerâncias** (cota 0,01; profundidade crítica 0,01; iterações máx. 20; diferença máxima 0,30; fator de vazão em ponte/bueiro 0,001; divisão de fluxo 30 e 2 %) p. 240–241; profundidade crítica (parabólico × busca múltipla) p. 241; invasão de várzea/floodway p. 239 e 424–457 [USACE-HECRAS-UM-66 p. 239–241].
- **Não permanente**: pré-processador de geometria, motor, pós-processador (o pós-processador recalcula as estruturas com as equações, o motor usa famílias de curvas → cota de montante pode diferir) p. 267–272 [USACE-HECRAS-UM-66 p. 272]; janela de simulação p. 272; **intervalo de cálculo** (regra Tr/20; condição de Courant; 1 a 5 min em estruturas) p. 273; intervalo de saída de hidrogramas, de perfis detalhados, **intervalo de saída de mapeamento** (gera o `.p01.hdf` que o Mapper lê) p. 273–274; saída de nível computacional p. 274; theta e theta de aquecimento p. 281–282; tolerâncias, iterações p. 286–288; **passo de tempo por Courant** (Courant máximo, divisor do passo, datas definidas pelo usuário) p. 291–294; controle de saída p. 295 [USACE-HECRAS-UM-66 p. 273–274, 281–282, 292–294].
- Mudanças vazão-rugosidade e sazonal no plano: p. 277–278. Floodway não permanente no plano: p. 280.
- **Estabilidade (o que mais pesa)**: lista de 13 fatores p. 312; espaçamento (rios íngremes a ~100 ft; rios largos e planos a ~5000 ft; testar interpolando seções) p. 312–313; **condição de Courant e fórmula Δx ≤ c·Tr/20, número de Courant ótimo 1,0, Tabela 7-2 (fatores para velocidade da onda a partir da velocidade média)** p. 314–315; passo prático Δt ≤ Tr/20 p. 316; theta (0,6 a 1,0; padrão 1,0) p. 317; tolerâncias e iterações p. 317; vertedores longos e planos, comportas, submergência p. 318–319; trechos íngremes e regime misto p. 319; **contorno de jusante ruim** (declividade excessiva, exemplo Fig. 7-45) p. 320; seção e tabelas de propriedades hidráulicas p. 321; pontes e bueiros (curvas de remanso pré-calculadas, Fig. 7-46) p. 321–322; condição inicial e vazão baixa p. 323; degraus no perfil de fundo p. 323–324; n baixo em trechos íngremes p. 324–325 (Fig. 7-49); canal principal faltando ou ruim (Fig. 7-50) p. 326; junções p. 326–327 [USACE-HECRAS-UM-66 p. 312–327].
- **Como achar e corrigir instabilidade**: p. 329–335 (janela de cálculo p. 329–330, erros crescentes p. 330, saída em nível computacional p. 331–332, log detalhado p. 332–335) [USACE-HECRAS-UM-66 p. 329–335]. Para o ruído de cálculo em modelos de chuva, ver HRM e 2DUM (outros grupos).

### Erros, avisos e notas (permanente e não permanente)
- Verificação de dados na entrada (faixas, ordem de estacas, consistência de margens, deck × terreno) p. 610; verificação antes de calcular (completude e consistência, regime misto exige os dois contornos) p. 611 [USACE-HECRAS-UM-66 p. 610–611].
- **Sistema de Erros, Avisos e Notas** (definições das três classes; causas comuns de aviso: seções muito espaçadas, estacas extremas baixas demais, cota inicial ruim, dado ruim de seção) p. 611–612; resumo em View > Summary Errors, Warnings, Notes p. 611–612 [USACE-HECRAS-UM-66 p. 611–612]. Catálogo individual das mensagens (texto de cada aviso): **não consta do UM** (ver lacunas).
- Log de cálculo permanente (níveis 0 a 10; 4 a 5 gera arquivo grande) p. 613–614; log não permanente p. 614–615; ocorrência de profundidade crítica (quatro causas: dado ruim, nível de leve/ineffective, seções espaçadas, regime errado) p. 616; "computações que não terminam" p. 616–617 [USACE-HECRAS-UM-66 p. 613–617].
- Verificações de razoabilidade da saída (perfil sem saltos de EGL, top width brusco sugere mais seções) p. 615–616.

### Visualização e saída de resultados
- Gráficos de seção, perfil, curva-chave, "General profile", velocidade distribuída p. 376–383; envio a impressora/clipboard p. 384; vistas 3D p. 385–399 (Tabelas 8-1 a 8-8, atalhos do visualizador 3D, só localizadas); hidrograma de brecha p. 399; hidrogramas de cota e vazão p. 401 [USACE-HECRAS-UM-66 p. 376–401].
- **Tabelas**: detalhadas por seção/ponte/bueiro/distribuição de fluxo (Figs. 8-21 a 8-24) p. 402–406; **Profile Summary (Std. Tables 1 e 2 etc., casas decimais, tabela do usuário)** p. 407–409; clipboard p. 410–411; resultados direto no esquema p. 411; nível computacional p. 412–413 [USACE-HECRAS-UM-66 p. 402–413].
- Exportar a HEC-DSS p. 417–421; volume-vazão para roteamento p. 422; **mapeamento de inundação com o Mapper**: só um parágrafo, remete ao manual do Mapper p. 422–423 [USACE-HECRAS-UM-66 p. 422].
- Arquivo HDF por plano (`.pNN.hdf`, resultados + cópia da geometria) usado pelo Mapper: UM p. 45, 274; Mapper p. 133 (o formato interno do HDF **não** é descrito no UM; ver `rashdf`/`h5py` no PLANO 11.4).

### Outros capítulos (só localizados, não lidos)
Brecha de barragem/dique p. 246, 336–368, 641–663; vazão lateral não monitorada p. 369–375; ferramentas de projeto hidráulico (erosão em pontes p. 459–470; enrocamento e escavação p. 471–538, Apêndice A exemplo p. 533–538; escoamento uniforme p. 539–544; canal estável p. 544–552; transporte de sedimento p. 552–609); modificação de canal p. 618–636; regime misto p. 637; estações de bombeamento p. 664; barragens de navegação p. 670; tubo pressurizado com tampa p. 680; regras de operação p. 683–724; **redes de tubos (beta) p. 740–779**; formato de troca de dados SDF e importação GIS p. 799–837 (Tabelas B-1 a B-10 p. 799 em diante); georreferenciamento com HEC-GeoRAS (exemplo p. 214–228); importação de geometria p. 181–188 (Tabelas 5-2 e 5-3 p. 185 e 187).

### Tabelas, ábacos e exemplos resolvidos do UM
Tabelas: razões de expansão em pontes p. 74; n por forma de fundo aluvial p. 305; Tabela 7-2 (velocidade da onda) p. 315; Tabelas 5-2 e 5-3 (campos de importação GIS) p. 185 e 187; Tabela 12.1 p. 469 (erosão); Tabelas B-1 a B-10 (SDF) p. 799–; Tabelas 8-1 a 8-8 (visualizador 3D) p. 387–398 (a confirmar página a página). Ábacos: nenhum do tipo nomograma; as figuras de curvas de remanso de ponte (Fig. 7-46 p. 322) e de n × vazão (Mississippi, p. 302) são ilustrativas. Exemplos: configuração de comportas p. 235; contorno interno de cota/vazão (108 ft, 1100 e 1125 cfs) p. 256; Red River of the North (área não monitorada) p. 301; n × vazão no Mississippi p. 302; cotas de pilar × EGL p. 299; georreferenciamento p. 214–228; Apêndice de enrocamento p. 533–538. (Todos qualitativos/ilustrativos; nenhum dá cota de projeto reaproveitável.)

### USACE-HECRAS-MAPPER-66 — HEC-RAS Mapper User's Manual, v6.6 (USACE HEC, setembro/2024)
Vigência: v6.6; licença: domínio público; 193 p. (nativo). Prioridade B.

### Projeção, datum e configurações
- **Projeção do projeto**: obrigatória para fundo de imagem e reprojeção; arquivo ESRI `.prj` (também wkt, proj4, epsg citados em p. 22; p. 30 diz que hoje só `.prj`) p. 22, 30–31; GDAL pode dar aviso falso com "Authority" p. 30; método alternativo de reprojeção raster p. 31 [USACE-HECRAS-MAPPER-66 p. 22, 30].
- Configurações de projeto: casas decimais do terreno, filtro de pontos (limite de 500 pontos por seção), modo de renderização, tolerância de plotagem, tolerâncias de malha p. 23–24 [USACE-HECRAS-MAPPER-66 p. 23]. Configurações globais p. 25–29.
- Datum vertical: o Mapper converte unidades verticais na criação do terreno (pés para metros, metros para pés, valor próprio ou nenhuma) p. 34; o ajuste de datum da geometria é no editor (UM p. 201). **Datum vertical (SIRGAS/EGM) e projeção brasileira não são tratados** (ver lacunas).

### Terreno (RAS Terrain)
- Conceito: o terreno é MDT de terra nua em raster; canal precisa de batimetria; incluir diques, muros e estradas; **não incluir pontes**; pilares e edifícios entram só em 2D detalhado; tamanho de célula deve captar o canal e feições abruptas p. 33 [USACE-HECRAS-MAPPER-66 p. 33].
- **Criação**: prioridade entre rasters (o de cima vale), arredondamento (padrão 1/32 da unidade, ±0,0156), conversão vertical, "Create Stitches", "Merge Inputs to Single Raster" para blocos LiDAR com mesma resolução p. 33–35; processamento em 6 passos (GeoTiff, projeção, arredondamento, estatística, pirâmide, VRT e HDF) p. 35; BigTIFF, sem limite de tamanho p. 36 [USACE-HECRAS-MAPPER-66 p. 34–36].
- Visualização (contornos, hillshade) p. 36–38; **associação do terreno à geometria e ao plano** (necessária para profundidade) p. 38–39, 135.
- **Reamostragem, recorte à geometria ou à vista** (muda resolução e extensão) p. 39–40.
- Download: só **USGS 3DEP/GRiD (EUA)** p. 41–48; sem equivalente brasileiro (ver lacunas). Modificação de terreno (clonar, linhas, polígonos, formas) p. 116–125; dados NLD (diques dos EUA) p. 126–131.

### Uso do solo e n no Mapper
- Camadas de classificação (cobertura, impermeabilização, solos, infiltração, leito de sedimento) e sub-camada de polígonos de classificação (para sobrescrever) p. 49–50; nomes não podem ter `/` nem `\` (NLCD) p. 49.
- **Camada de cobertura (Land Cover) como substituta do n**; fontes de exemplo NLCD e USGS (30 m, "não bastam para rugosidade hidráulica"; canal exige foto aérea e campo); células padrão 100 p. 50 [USACE-HECRAS-MAPPER-66 p. 50]. Padrões de nomes: NLCD 2016, Anderson nível II, NOAA C-CAP p. 51; extensão de importação p. 51.
- **Tabela de n por classe NLCD** (faixas de n por classe: água aberta, desenvolvido por intensidade, solo nu, florestas, pastagem, cultivo, banhados) p. 59–61 (nota p. 61: valores adaptados de Chow 1959, **para profundidades apreciáveis, não para escoamento laminar raso e possivelmente inadequados para chuva na malha**; n de escoamento raso é bem maior) [USACE-HECRAS-MAPPER-66 p. 60–61].
- Associar a camada à geometria p. 59; **uso do Land Cover para n** p. 61; **n no Mapper**: base, "Base Override" e **Calibration Regions** (polígonos únicos; coluna à direita tem prioridade: região de calibração > override > base), camada "Final n Values" (mostra o que o modelo usa; em modelo com seções, reflete também o n das seções) p. 97–99 [USACE-HECRAS-MAPPER-66 p. 97–99].
- Impermeabilização p. 100; parâmetros de infiltração (Deficit Constant, SCS Curve Number, Green and Ampt) a partir de cobertura + solos (interseção) ou de shapefile; solos gSSURGO (EUA) p. 54–58, 101; porosidade e arrasto (obstruções) p. 102–103.

### Geometria no Mapper (2D, estruturas, contornos)
- Rios, seções, linhas de margem, linhas de borda (edge lines), superfície de interpolação de seções p. 70–79; ineffective e obstruções p. 79–80; **áreas de armazenamento** (curva elevação-volume do terreno) p. 81; **áreas 2D**: perímetro, pontos de cálculo (espaçamento DX/DY), **breaklines** (tabela de propriedades p. 87), **regiões de refinamento** (tabela p. 89), ordem de construção da malha p. 81–89 [USACE-HECRAS-MAPPER-66 p. 81–83, 85–89]; mensagens e erros de malha p. 111; importar malha da versão 2025 p. 112–115; pontes/bueiros, estruturas p. 90–96; bombas p. 96–97.
- **Linhas de contorno 2D** (vazão, cota, curva-chave, profundidade normal; externos devem estar fora da área) p. 103–104; **locais de referência** (pontos, linhas, áreas: saída durante a simulação e comparação com dados observados) p. 104–111 [USACE-HECRAS-MAPPER-66 p. 104].

### Mapas de resultados (lâmina, profundidade, velocidade, tempo de chegada, duração)
- Resultados em `.pNN.hdf` por plano; mapas padrão **Profundidade, Cota da lâmina e Velocidade**; terreno associado necessário p. 133 [USACE-HECRAS-MAPPER-66 p. 133, 141].
- **Mapas dinâmicos × armazenados** (dinâmico: vista atual, interpolado, "não é a resposta exata"; armazenado: grade na resolução do terreno, para publicar) p. 133–134, 138–139 [USACE-HECRAS-MAPPER-66 p. 133, 138].
- **Tabela de tipos de mapa** (Depth, WSE, Velocity, Inundation Boundary, Flow 1D, Courant por velocidade e por tempo de residência, Froude, Shear Stress, Stream Power, Depth×Velocity, Depth×Velocity², Energia profundidade/cota, **Arrival Time**, Arrival Time (Max), **Duration**, **Recession**, Percent Time Inundated, Wet Cells) p. 135–137 (Arrival Time indisponível em permanente p. 135; Duration ignora picos múltiplos p. 137; parâmetros: limiar de profundidade, instante inicial, unidade de tempo) [USACE-HECRAS-MAPPER-66 p. 135–137]. Perfis: permanente por perfil, não permanente por mínimo, máximo ou instante (intervalo de mapeamento) p. 137.
- **Modo de saída**: Raster (grade do terreno), camada de pontos, polígono no valor (contorno de inundação, padrão para Inundation Boundary) p. 138; **vários mapas de uma vez** (Create Multiple Maps) p. 139; gerenciar mapas e calcular/atualizar armazenados p. 152.
- **Superfície de interpolação** (1D: entre seções por quatro regiões de margem e borda; 2D: triangulação entre pontos e faces; armazenamento e 2D têm precedência sobre seções) p. 141–142; **fronteira de inundação** (contorno de profundidade zero, edição de buracos e linhas de borda) p. 143–148; velocidade (setas, partículas) p. 149–151 (tabela de opções p. 151).
- **Modo de renderização 2D** (horizontal conserva volume e é indicado para mapas com volume; inclinado/vértices de célula é o padrão e pode "criar água" em terreno íngreme; com faces; ponderado por profundidade; raso reduz a horizontal) p. 152–154; plot de conectividade e gradiente de lâmina 2D (tabela de cores p. 156), valores no mapa, deficiências de borda do modelo, datas de chegada p. 155–160 [USACE-HECRAS-MAPPER-66 p. 152–153].
- **Exportação**: raster GeoTIFF (extensão, buffer, tamanho de célula, raster único), contornos (linhas, faixas "0,2; 4,10; 10,Max") p. 161–162 [USACE-HECRAS-MAPPER-66 p. 161–162]; KML e KML 3D, Google Earth p. 182–189; **servidor de tiles** p. 190–192; calculadora raster (RASter Calculator: variáveis, código, ajuda) p. 173–181.
- **Avaliação**: dica de mapa, lista de observação, séries temporais, **perfis em linha**, contornos interativos p. 163–172; melhor via locais de referência (calculados durante a simulação) p. 163.

### Tabelas, ábacos e exemplos do Mapper
Tabelas: tipos de mapa p. 135–137; modos de saída p. 138; **n por classe NLCD p. 59–61**; propriedades de breaklines p. 87 e de regiões de refinamento p. 89; opções de velocidade p. 151; cores de gradiente de lâmina p. 156. Ábacos: 0. Exemplos resolvidos numéricos: 0 (só telas ilustrativas, p. ex. comparação dinâmico × armazenado p. 139, e renderização horizontal × inclinada p. 154).

## Divergências e pontos de atenção
1. **Sensibilidade de n "±20 %" (PLANO 11.2, item 5, cita UM p. 328 e HRM p. 389)**: o UM p. 328 não fixa percentual; pede "faixa realista" ao n (exemplo 0,035 → 0,03 a 0,045, isto é, cerca de −14 % e +29 %). Verificar HRM p. 389 antes de manter "±20 %" como regra do especialista (UM p. 328).
2. **Modo padrão de renderização 2D**: Mapper p. 23 diz que o padrão é "Hybrid" (sloping ou horizontal conforme a variação da lâmina); Mapper p. 152–153 diz que o padrão é Sloping (Cell Corners). Conferir na versão usada; afeta mapa de profundidade e volume.
3. **Projeção**: Mapper p. 22 cita `.prj`, wkt, proj4 e epsg; Mapper p. 30 diz que "no momento só" arquivo `.prj`.
4. **Georreferenciamento**: UM p. 61 diz que modelo georreferenciado hoje exige HEC-GeoRAS/ArcGIS, enquanto UM p. 33–34 e 207 dizem que o layout pode ser feito no Mapper (texto de p. 61 desatualizado).
5. **Coeficientes de contração e expansão**: padrão 0,1 e 0,3 em permanente (UM p. 35, 63) × padrão 0,0 em não permanente (UM p. 170); não confundir ao trocar o tipo de escoamento do mesmo modelo.
6. **Tabela de n do Mapper (NLCD, p. 59–61) × n de rio de UM p. 305**: a primeira é de uso do solo dos EUA para profundidade apreciável (Chow), a segunda é de forma de fundo aluvial; não são intercambiáveis e nenhuma serve direto a chuva na malha (Mapper p. 61).
7. **Dinâmico × armazenado** podem diferir, sobretudo no contorno da mancha (Mapper p. 133–134, 138–139): publicar sempre o armazenado e dizer qual foi usado.
8. **Cota de montante em estruturas**: o pós-processador pode dar cota maior que a da seção a montante porque o motor usa curvas pré-calculadas (UM p. 272).

## Lacunas (o que este grupo não cobre)
- **Sem tabela de n por tipo de canal/várzea** (Chow, Cowan, USGS): o UM só tem n de forma de fundo aluvial (p. 305) e o Mapper tem n por classe NLCD (p. 59–61). Buscar no HRM (outro grupo) e em Chow/FHWA fora deste grupo; nenhuma classe da Caatinga, MapBiomas, nem n para chuva na malha (n raso).
- **Sem catálogo das mensagens de erro/aviso** pelo texto exato; o UM só define as três classes e causas gerais (p. 611–612). Mensagens de estabilidade 2D estão no 2DUM.
- **Sem formato interno do HDF** (grupos, nomes de dataset) nem descrição de `.p01`/`.u01` por linha de arquivo; UM p. 44–45 só lista extensões. O verificador (PLANO 11.4) depende de `rashdf`/`h5py` e de inspeção real.
- **Terrenos**: download só USGS 3DEP/GRiD (p. 41–48); nada sobre ANADEM, SRTM, LiDAR brasileiro, SIRGAS 2000/UTM, datum vertical (geoide/MDE), nem resolução recomendada em número (só "pequena o bastante", Mapper p. 33).
- Sem cálculo de TR, hidrologia, IDF, ARF; sem exemplo resolvido de rio brasileiro ou de semiárido; os exemplos são dos EUA (Mississippi, Red River).
- Sem critérios quantitativos de aceitação de calibração (limite de erro de cota, RMSE); só qualitativo (UM p. 309–310).
- Equações 2D, malha adaptativa, chuva na malha, Courant 2D: no `2DUM-66`. Teoria de pontes, bueiros, n composto: no `HRM-66`.
- Não lidos (apenas localizados): brechas, sedimentos, redes de tubos, bombas, navegação, regras do usuário, SDF.

## Páginas lidas
- UM-66: ≈ 85 p. (integral ou quase: 32–41, 60–63, 73–76, 92–96, 128–135, 167–170, 180–181, 201–204, 231–236, 239–241, 246–260, 272–274, 298–313, 327–329, 610–617, 725–728; por filtro de títulos: 155, 281–297, 314–336, 402–409, 422). Sumário (bookmarks) lido inteiro.
- MAPPER-66: ≈ 55 p. (22–24, 30–31, 33–43, 49–53, 56–61, 81–84, 97–99, 103–104, 132–143, 152–156, 161–163; filtro de títulos em 85–90, 143–151, 155–160, 164–172). Sumário lido inteiro.

