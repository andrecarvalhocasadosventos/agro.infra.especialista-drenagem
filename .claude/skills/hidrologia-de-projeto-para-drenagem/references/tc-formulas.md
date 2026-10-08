# Tempo de concentração: fórmulas, faixa de validade e fonte

Páginas = página física do PDF (`<!-- p. N -->` do `_texto`), salvo aviso. SI: L em m ou km (conforme a coluna), H em m, A em km² ou ha (conforme a coluna), S em m/m, I em %. "Forma conferida" = a forma impressa foi comparada com a forma de unidades iguais do próprio manual (DNIT-HIDRO p. 97) ou com um exemplo numérico.

## 1. Fórmulas globais (um número por bacia)

| Fórmula | Forma | Faixa e origem | Observações e fonte |
|---|---|---|---|
| **Kirpich** (1940) | tc[min] = 0,0195 · L^0,77 · S^-0,385 (L em m) | Bacias de TN e PA de 1 a 112 acres = 0,004 a 0,45 km² [FHWA-HDS2 p. 80]; "menores que 0,8 km²" [DNIT-HIDRO p. 88]; 7 bacias rurais, S de 3 a 10 %, A ≤ 0,5 km², subestima tc com L > 10 km [PMSP-DRENURB-V2 p. 56]; vale quando há ravinamento em mais de 10 % do curso principal [FHWA-HDS2 p. 80] | Forma DNIT: tc[h] = 0,95·(L³/H)^0,385, L em km, H em m [DNIT-HIDRO p. 88]. As duas formas dão o mesmo valor (74,9 e 74,8 min para L = 2,9 km, H = 12 m). A constante 0,0195 (SI) é de [FHWA-HDS2 p. 80]; os expoentes estão em imagem no HDS-2 e foram conferidos pela forma DNIT. Forma ABDER: tc[h] = (0,294·L/√i)^0,77, L em km, i em % [ABDER-APOSTILA p. 59, 67] (6,4 min para L = 0,49 km e i = 7 %). DNIT: a velocidade implícita fica acima da média das fórmulas, sobretudo em bacia média e grande [DNIT-HIDRO p. 88, 94] |
| **California Culverts Practice** (1942) | tc[h] = 0,95·(L³/H)^0,385 (L km, H m) | É a Kirpich com S = H/L [PMSP-DRENURB-V2 p. 56]; o DNIT a descreve como a Kirpich "publicada no California Culverts Practice" [DNIT-HIDRO p. 88] | No módulo, `california_culverts` = 57·(L³/H)^0,385 min (0,95 × 60). Não é uma terceira fórmula: tratar Kirpich e California como a mesma |
| **Kirpich modificada (DNIT)** | tc[h] = 1,42·(L³/H)^0,385 (L km, H m) | "Tempos 50 % maiores" que a Kirpich para o HU triangular reproduzir cheias observadas em bacias médias e grandes [DNIT-HIDRO p. 90]; faixa de velocidades: 4,0 km/h (bacias pequenas), 4,8 km/h (médias e grandes) | Forma conferida (V = 0,7020·L^-0,155·H^0,385, p. 97). DNIT a indica para "grande faixa de áreas" e a adota na falta de dados observados [DNIT-HIDRO p. 90, 94, 98]. 1,42 ≈ 1,5 × 0,95. Caso CSB usa esta forma (doc 1341:46) |
| **DNOS** | tc[min] = (10/K)·A^0,3·L^0,2 / I^0,4 (**A em ha, L em m, I em %**) | K = 2,0 (areno-argiloso, vegetação intensa); 3,0 (comum); 4,0 (argiloso, vegetação); 4,5; 5,0 (rocha, pouca vegetação); 5,5 (rochoso, vegetação rala). "Aceitável para qualquer tamanho de bacia" com K = 4 [DNIT-HIDRO p. 89] | Forma conferida (V = 0,6029·A^-0,3·L^0,4·H^0,4, p. 97). **K maior dá tc menor** (K divide). `tools.dren.hidrologia.dnos` usa outra forma (ver "Divergências com a calculadora") |
| **Kerby** | (DNIT) tc[min] = 37·(L·a/I)^0,47, L em km, I em %, a = 0,5; (HDS-2) tov[min] = 1,44·(L·N/√S)^0,467, L em m, N da Tab. 3.5 | DNIT: "não aplicável" a bacias maiores, a velocidade cresce rápido [DNIT-HIDRO p. 85-86]. HDS-2: escoamento sobre o terreno, L ≤ 1.200 ft = 365 m [FHWA-HDS2 p. 79] | Usar a forma HDS-2 só para o trecho de escoamento superficial. N (retardância): 0,02 pavimento; 0,10 solo nu compactado; 0,20 pasto ralo ou cultura em fileira; 0,40 pasto médio; 0,60 floresta caducifólia; 0,80 grama densa ou floresta com serrapilheira [FHWA-HDS2 p. 79, Tab. 3.5]. Os expoentes do HDS-2 estão em imagem; α = 1,44 em SI é do texto. A forma DNIT tem a unidade de L diferente: não misturar |
| **Giandotti** | tc[h] = (4·√A + 1,5·L)/(0,8·√H) (A km², L km) | H = "desnível máximo" no DNIT [DNIT-HIDRO p. 91-92]; o original usa altitude média menos a da seção. Velocidade 2,1 km/h em bacia pequena: "pouco recomendável" nelas; 5,0 km/h em maiores | Faixa original de 170 a 70.000 km² vem da docstring de `giandotti`, **não está no corpus** (página a confirmar). Não usar em bacia de drenagem de perímetro |
| **Dooge** (1956) | tc[min] = 21,88·A^0,41·S^-0,17 (forma da calculadora) | 10 bacias rurais da Irlanda, 140 a 930 km², canais predominantes [PMSP-DRENURB-V2 p. 57] | A equação está em imagem no PMSP; unidade de S **a confirmar** (a calculadora adota m/m). Bacia média e grande, não de drenagem local |
| **SCS lag** (Mockus 1961) | lag[h] = ℓ^0,8·(S+1)^0,7 / (1.900·Y^0,5), ℓ em ft, S em pol, Y em %; tc = lag/0,6 | Desenvolvida em 24 bacias, a maioria < 2.000 acres (≈ 810 ha); teto mais realista 5 a 19 mi² (13 a 49 km²); CN' entre 50 e 95 [NRCS-NEH630-CH15 p. 9-10]. PMSP: rural até 8 km², superestima tc frente a Kirpich e Dooge [PMSP-DRENURB-V2 p. 57] | Converter: ℓ[ft] = 3,281·ℓ[m]; S[pol] = S[mm]/25,4. lag = 0,6·tc [NRCS-NEH630-CH15 p. 8, eq. 15-2]. Não há função na calculadora |
| **Lag DNIT (Kn)** | tc[h] ≈ 16,0·Kn·L^0,833 / H^0,167 (L km, H m) | Kn de 0,030 a 0,150 (urbano 0,013 a 0,033); Kn = 0,07 para A > 10 km², onde se aproxima da Kirpich modificada [DNIT-HIDRO p. 92-94] | Sem função na calculadora |
| Ven Te Chow | tc[min] = 25,2·(L/√I)^0,64 (L km, I %) | Pequenas bacias; "não recomendada" para grandes [DNIT-HIDRO p. 89] | √I conferida pela forma unificada (p. 97); a raiz se perdeu na extração |
| Corps of Engineers (EUA) | tc[h] = 0,30·(L/I^0,25)^0,76 (L km, I %) | Idem [DNIT-HIDRO p. 88-89] | Forma conferida. Usada em média com Chow e Kirpich no Xingó (doc 1419:28) |
| Picking | tc[min] = 5,3·(L²/I)^(1/3) (I m/m) | Não indicada para bacias maiores [DNIT-HIDRO p. 88] | O DNIT imprime "horas"; só fecha com minutos (p. 97). Unidade a confirmar no PDF |
| George Ribeiro | tc[min] = 16·L / ((1,05 − 0,2·p)·(100·I)^0,04) (L km, I m/m, p = fração com vegetação) | "Qualquer tamanho"; velocidade quase constante (~3,7 km/h), pouca sensibilidade às características da bacia [DNIT-HIDRO p. 90, 97]. Silveira (2005): bom ajuste em bacias de 1 a 39 km² [PMSP-DRENURB-V2 p. 58] | Sem função |
| Pasini, Ventura | tc[h] = 0,107·(A·L)^(1/3)/√I; tc[h] = 0,127·√(A/I) (A km², I m/m) | Velocidades baixas, vazões menores, "contra a segurança" [DNIT-HIDRO p. 90-91, 94] | Evitar |
| Rossi, John Collins, fórmula do CN, Giandotti em bacia pequena | — | Contra-indicadas ou pouco recomendáveis [DNIT-HIDRO p. 91-94] | Não usar |

## 2. Método da velocidade (soma de trechos)

tc = Σ (L_i/V_i): escoamento em lâmina, concentrado raso, canal e tubo [FHWA-HDS2 p. 68-69; NRCS-NEH630-CH15 p. 10]. É a forma "mais correta" segundo o PMSP [PMSP-DRENURB-V2 p. 56]. Limites: lâmina até 100 ft (30 m) pela NRCS [NRCS-NEH630-CH15 p. 13], raramente mais de 300 ft e na maioria menos de 100 ft [FHWA-HDS2 p. 69]. A forma cinemática do HDS-2 (α = 6,9 em SI, eq. 3.6) depende da intensidade e se resolve por iteração com a IDF [FHWA-HDS2 p. 69-70]; a de Welle-Woodward usa P2 de 24 h e é do SCS [NRCS-NEH630-CH15 p. 10]. Em perímetro irrigado, o trecho em canal ou dreno de terra usa Manning e velocidade a seção cheia (declarar). Quando a bacia tem trechos de declividade muito diferente, somar tc por parte [DNIT-HIDRO p. 98].

## 3. Qual usar

| Situação | Primeira escolha | Conferir com | Fonte da escolha |
|---|---|---|---|
| A ≤ 0,5 a 0,8 km², cursos curtos | Método da velocidade, ou Kirpich/California dentro da faixa | Kirpich modificada (1,5×) | HDS-2 p. 80; DNIT p. 88 |
| Bacia agrícola ou de drenagem de perímetro, 0,8 a ~10 km² | Kirpich modificada ou DNOS (K declarado) | Kirpich e SCS lag; mostrar a razão entre elas | DNIT p. 94, 98 |
| 10 a ~50 km² | Kirpich modificada ou Lag com Kn = 0,07 | SCS lag | DNIT p. 94; NRCS-CH15 p. 10 |
| > 50 km², rio com leito definido | Método da velocidade com canal calibrado; média de três fórmulas no acervo (Xingó) | Dados fluviométricos, se existirem | DNIT p. 98; caso Xingó |
| Declividade média < 0,5 % (perímetro plano) | Método da velocidade com Manning; declarar fora de faixa | Kirpich modificada como limite superior | NRCS-NEH650-CH02 p. 11 (S de 0,5 a 64 %); HDS-2 p. 79 (S de 0,002 a 0,02 ft/ft no Kerby-Kirpich) |

Dispersão: nas bacias menores que 2,5 km² a razão entre a maior e a menor fórmula passou de 5 [DNIT-HIDRO p. 85]; a vazão de pico é aproximadamente inversa a tc [DNIT-HIDRO p. 84]. **Mostrar sempre mais de uma fórmula e a escolha justificada.**

## 4. Limites práticos de tc

- Mínimo: 15 min [ABDER-APOSTILA p. 67]; 10 min em sistemas urbanos [DNIT-DREN p. 302]; 0,1 h no método gráfico NRCS [NRCS-NEH650-CH02 p. 11]; IDF costuma ter limite inferior de duração (conferir a faixa da equação de chuva).
- Máximo no DAEE-SP: não usar tc maior que o da fórmula do Quadro 1 da IT DPO 11 [DAEE-IT-DPO11 p. 2]; a fórmula está em imagem (a confirmar no PDF).
- Método racional: chuva com duração igual a tc [DNIT-HIDRO p. 127].

## 5. Divergências com a calculadora (`tools/dren/hidrologia.py`)

| Item | Calculadora | Primário | Consequência |
|---|---|---|---|
| `dnos` | 4,2·A^0,3·L^0,2·K/I^0,4 (A km², L km, I %) | (10/K)·A^0,3·L^0,2/I^0,4 (A ha, L m, I %) [DNIT-HIDRO p. 89] | Para A = 100 ha, L = 2.000 m, I = 1 %, K = 4: primário 45,5 min; calculadora (A = 1 km², L = 2 km) 19,3 min. **Não usar `dnos` em projeto**; calcular pela forma DNIT e abrir pendência. O memorial do Baixio de Irecê traz outra forma (4,2·A^a·L^b·k·I^-c, expoentes ilegíveis): o Tc 0,9633 h do Baixio não é reproduzível |
| `kerby` | forma HDS-2 (L m, N) | DNIT usa outra forma (L km, a, I %) | Citar qual forma foi usada |
| `kirpich` (L m, S) × `kirpich_modificada_dnit`, `california_culverts`, `giandotti` (L km) | unidades diferentes por função | — | Conferir a unidade de L em cada chamada |
| `kirpich` aviso de 3 a 10 % | vem do PMSP [PMSP-DRENURB-V2 p. 56] | HDS-2 e DNIT dão faixa por área, não por declividade | O aviso é válido, mas incompleto |
