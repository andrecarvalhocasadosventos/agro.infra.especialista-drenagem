# Tubo dreno e coletores: vazão, capacidade, DN e o caso D-86

## 1. Vazão de projeto da linha

Q = q · L · B (m³/d ÷ 86.400 = m³/s), L = espaçamento, B = comprimento da linha (`vazao_de_dreno`). Área drenada
aumentada de 10 a 25 % para assoreamento e margem (capacidade efetiva de 90 a 75 %) [EMBRAPA-DREN-SUBT p. 17-18].
Para coletor: Lc e Bc no lugar de L e B; com mais de cinco laterais iguais, o erro de tratar a entrada como contínua é
desprezível [FAO-IDP62 p. 214]. Para dreno com infiltração lateral adicional (surgência, poço de alívio), somar a
vazão ao q e redimensionar [FAO-IDP62 p. 114]. Para o ILRI-56, a vazão que importa ao **envoltório** não é a de
projeto, e sim a máxima possível (Qdmax = mesma equação de espaçamento com o lençol na superfície) [ILRI-56 p. 43, 46].

## 2. Dois conceitos de capacidade (não misturar no mesmo parecer sem rótulo)

**A. Manning com a declividade do tubo** (calculadora: `capacidade_tubo_dreno`, `capacidade_tubo_parcial`,
`diametro_minimo_dreno`). Q = (1/n) A R^(2/3) S^(1/2); seção plena Q = 0,3117 D^(8/3) S^(1/2)/n. Fluxo livre, declividade
paralela ao gradiente hidráulico [NRCS-NEH624-CH04 p. 88]. n por material em `criterios-e-tabelas.md` §5. USBR mediu
até 1,2 vez o Manning pleno com carga de água sobre o tubo [ILRI-56 p. 46, nota 3]; a calculadora **não** usa esse
ganho (conservador). Tubo parcial: não extrapolar Manning acima de y/D ≈ 0,82 (Q máximo em y/D ≈ 0,94).

**B. Perda de carga com vazão crescente** (FAO-62 Anexo 20; **sem função na calculadora**). A inclinação do tubo não é
o parâmetro: é a **perda de carga total H** entre a cabeceira (lençol de projeto) e a saída; dreno horizontal com a
mesma perda de carga funciona igual [FAO-IDP62 p. 211-212]. O tubo coleta ao longo do comprimento: Q = q L x.
- Liso (plástico, metal, vidrado; a = 0,3164) ou tecnicamente liso (perfurado, cerâmica, cimento; a = 0,40);
  Blasius λ = a Re^(−0,25); corrugado "pequeno" por Zuidema a = 0,77 [FAO-IDP62 p. 213, Tab. A20.2].
- Comprimento admissível, diâmetro mínimo e espaçamento máximo: Eq. 6, 7, 8; carga necessária para tubo liso novo:
  Eq. 9 [FAO-IDP62 p. 214] (forma completa embaralhada no texto: **conferir na imagem**). Fórmula alternativa para tubo tecnicamente liso: Q = 89 d^2,714 s^0,571, com
  s = H/B e Q = q L B; dá quase o mesmo que as Eq. 6-9 com a = 40 [FAO-IDP62 p. 214]. Embrapa traz a mesma fórmula
  com expoente 0,572 e 50 no lugar de 89 "se o tubo só transporta" [EMBRAPA-DREN-SUBT p. 16-17]; os valores de
  d^2,714 e i^0,572 da Tab. 4 conferem (d = 100 mm → 0,00193; i = 0,10 % → 0,01923).
- Corrugado: Manning com Km = 1/n; Km = 70 se o passo da corrugação S < 10 mm; Km = 18,7 d^0,21 S^(−0,38) se S > 10 mm;
  máximo 65 por segurança [FAO-IDP62 p. 215, Eq. 11a-b]. Tab. A20.3 (Km 45 a 80: PVC 65 a 160 mm 70 a 80; PE 129 e
  196 mm: 53 e 57; PP 265 e 350 mm: 50 e 45) [FAO-IDP62 p. 216].
- **Estado de manutenção:** multiplicar Km por f (por exemplo 0,8) para tubo em condição regular, com cinco classes por
  altura de sedimento [FAO-IDP62 p. 217-218, Tab. A20.4-A20.5; tabelas não lidas em detalhe].

**Ordem de grandeza (calculadora e fórmula de Wesseling, para ver que não são intercambiáveis):**

| DN | Declividade ou s | Manning pleno n 0,011 | n 0,016 | Wesseling 89 d^2,714 s^0,571 |
|---|---|---|---|---|
| 0,10 m | 0,001 | 1,93e-3 m³/s | | 3,33e-3 |
| 0,30 m | 0,001 | 3,61e-2 | 2,48e-2 | 6,57e-2 |
| 0,30 m | 0,0001 | 1,14e-2 | 7,86e-3 | 1,76e-2 |

A diferença (1,5 a 1,8×) é conceitual (s = perda de carga com vazão crescente) mais a rugosidade da fórmula; **não
comparar um com o outro como "erro"**. Escolher um, citar a fonte, declarar n e S (ou H e B).

## 3. DN comercial

`diametro_minimo_dreno` devolve o menor diâmetro da lista indicativa (0,05; 0,065; 0,08; 0,10; 0,125; 0,15; 0,20;
0,25; 0,30; 0,40; 0,50; 0,60 m) acima do calculado, com aviso se acima de 0,60 m (tubos em paralelo). DN nominal ≠
diâmetro interno: DN170 → Ø interno 149 mm e DN230 → 200 mm no PEAD corrugado do Delmiro (1492:105). Use o
diâmetro **interno** na capacidade e peça o catálogo.

## 4. Velocidades e assoreamento

Mínima não assoreante 0,43 m/s; máximas por solo 1,07 a 2,74 m/s [NRCS-NEH624-CH04 p. 87-88]. Abaixo de 0,43 m/s,
envoltório e armadilhas de sedimento. Tubo com Manning a meia seção, n 0,016, DN300, S = 1e-4: V = 0,11 m/s; a 1e-3,
0,35 m/s: ambas abaixo de 0,43 m/s. É característica de dreno de baixa declividade (FAO-62: declividade rara acima de
0,5 % em terra plana, e sem velocidade para mover sedimento [FAO-IDP62 p. 212]); o remédio é envoltório e inspeção,
não declividade artificial.

## 5. Dreno de fundo: DN pela tabela CSB × Manning × legado Xingó

Para Q por tubo e S dados, mostrar sempre as três leituras e a diferença (função `dreno_de_fundo_de_canal_revestido`
com `i`): tabela CSB (faixa de capacidade por DN, sem ancoragem), D por Manning n 0,011 e D pela fórmula legada do Xingó.
Exemplo (CSB, L 800 m, q 6e-5 m³/s/m, 2 tubos, i 1e-4): Q por tubo = 0,024 m³/s → DN300 da tabela (faixa 0,025-0,031);
D por Manning = 0,396 m; D legado = 0,373 m. O CSB aplica Manning com o gradiente de pressão (carga sobre o tubo),
não a declividade (1341:76), o que explica a diferença. Ver `dreno-de-fundo-e-subpressao.md`.

## 6. D-86 do CDV (tubo dreno de 300 mm): como montar o insumo

Pendência de aceitação F10; **decisão é do André**. O agente entrega parecer-insumo, sem escrever no CDV, com:
1. **Q de projeto e de qual critério** (q·L·B de dreno agrícola; q de subpressão do CSB; Darcy do Delmiro; furos do
   Xingó). Sem o critério, pedir; não escolher.
2. **Capacidade do DN300 nas três leituras** (Manning n 0,011 a 0,016; Manning parcial; legado Xingó), em m³/s, para o S
   do trecho. Para S = 1e-4: 1,14e-2 (n 0,011), 1,05e-2 (n 0,012), 9,7e-3 (n 0,013), 7,86e-3 (n 0,016) e 1,35e-2
   (legado) m³/s: queda de 22 a 28 % entre o legado e n = 0,012 a 0,013.
3. **Diâmetro interno** e catálogo do tubo (DN300 PEAD tem Ø interno menor que 300 mm).
4. **Velocidade** e risco de assoreamento (§4).
5. **Comprimento até saída ou PIL** (limite de limpeza 200 a 300 m; Delmiro, Embrapa).
6. **Fronteiras:** K e envoltório (Geotecnia), orçamento por DN (engenheiro-de-custos), seção do canal (Hidráulico).
7. Caso similar do acervo: Xingó (ø300 em todo o trecho, saídas de 20 a 3.400 m, 1419:21) e CSB (2DN300 até 1.000 m).
   Nenhum tem `✓h`; Xingó usa a fórmula legada com n implícito 0,0093.

Proposta de pendência (P-nova) se faltar dado: citar a hipótese usada e o impacto, nunca resposta inventada.
