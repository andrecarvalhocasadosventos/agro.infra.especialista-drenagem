# Revestimento de canal de drenagem: rip-rap (HEC-11, EM-1601), gabião (HEC-15), tensão

Páginas físicas. HEC-11 e CPS 608 estão no corpus próprio; EM-1601, HEC-15, NEH 650 e DNIT-DREN no corpus do Hidráulico (citados pelo ID dele, D1).
**Fronteira (D3):** rip-rap **ao longo do canal** (fundo, talude, margem, confluência) é desta skill. Rip-rap, bacia de impacto e dissipador **na saída de bueiro ou de estrutura**
é da Hidráulica (`vertedouros-e-dissipadores`, `[DELEGAR: hidraulica]`); o Drenagem entrega V, Fr e y de saída e o aviso "precisa de dissipador".

## 1. Como escolher o critério de estabilidade

| Revestimento | Critério disponível | Na calculadora |
|---|---|---|
| Terra, grama | V admissível (tabelas) ou tensão (HEC-15 Cap. 4); NEH 650-7: capacidade com a vegetação mais densa e mais alta, estabilidade com a menos densa [NRCS-NEH650-CH07 p. 7, 11] | só V (`velocidade_admissivel`) |
| Concreto, alvenaria | V máxima da Tab. 31 (4,50; tijolo 2,50) ou do projeto; subpressão sob o revestimento é de `drenagem-subsuperficial` | só V |
| Rip-rap | D50 por velocidade (HEC-11 Eq. 6) ou D30 por velocidade local (EM-1601 Eq. 3-3); tensão (HEC-15 Cap. 6) | `d50_riprap_hec11` (Eq. 6 a 9); EM-1601 Eq. 3-3 **não implementada** |
| Gabião (colchão) | τp por D50 e por espessura (HEC-15 Eq. 7.1 e 7.2), V do fabricante ou do projeto | **nenhum** (lacuna) |

A Tab. 31 do DNIT e a Tab. 2-5 do EM-1601 **não têm linha para rip-rap nem gabião**; `bueiros.limite_velocidade` devolve o aviso "sem linha equivalente" e usa o limite legado. O HEC-15 não tem
tabela de velocidade e manda verificar por tensão: τd = γ·d·S0 (maior profundidade, Eq. 2.4 e 3.1) e τp >= SF·τd (Eq. 3.2) [FHWA-HEC15 p. 31, 35]; talude de rip-rap 1:3 ou mais suave dispensa verificar o talude;
razão largura de topo / profundidade < ~20 [p. 34]. Tensão admissível de solo e pedra: Tab. 2.3 [p. 33] (valores em `../../bueiros-e-travessias/references/velocidades-admissiveis-e-revestimentos.md`).
**Sem função de tensão no pacote**: o parecer reporta como cálculo manual rotulado e pede a função ao mantenedor (sugestão na seção 5).

## 2. Rip-rap de canal: HEC-11 (padrão do código)

Forma americana (D50 em ft, V em ft/s, d em ft): D50 = C · 0,001 V³ / (d^0,5 · K1^1,5) (Eq. 6); K1 = [1 − sen²θ / sen²φ]^0,5 (Eq. 7); C = Csg · Csf; Csg = 2,12 / (Ss − 1)^1,5 (Eq. 8); Csf = (SF/1,2)^1,5 (Eq. 9) [FHWA-HEC11 p. 48-49].
θ = ângulo do talude com a horizontal; φ = ângulo de repouso; V e d = velocidade e profundidade **médias do canal principal**; Eq. 6 vale para escoamento uniforme ou gradualmente variado, subcrítico, canal reto ou curva suave (p. 48, 50).
A calculadora recebe SI e converte (`d50_riprap_hec11(V, d, Ss=2,65, SF=1,2, z, phi)`); devolve D50 em m. O expoente de Csf (1,5) está corrompido no OCR da p. 49 e foi conferido na imagem pelo autor da calculadora: manter o aviso.

| Item | Regra | Fonte |
|---|---|---|
| Vazão de projeto | 10 a 50 anos; avaliar também vazões menores | [FHWA-HEC11 p. 37] |
| Froude | faixa 0,89 a 1,13 = escoamento instável; a calculadora avisa | [p. 38] |
| Fator de estabilidade SF | 1,0 a 1,2 reto ou curva suave (R/W > 30); 1,3 a 1,6 curva moderada; 1,6 a 2,0 curva fechada, entulho, ondas, incerteza grande; em curva por R/W: > 30 → 1,2; 30 a 10 → 1,3 a 1,6; < 10 → 1,7 | [p. 49, Tab. 1; p. 50] |
| Extensão | a montante 1,0 largura e a jusante 1,5 largura de cada curva, como ponto de partida | [p. 42, §3.6.1] |
| Graduação | seis classes AASHTO (Facing, Light, 1/4, 1/2, 1 e 2 ton), Tab. 3 | [p. 55] |
| Espessura e filtro | ver p. 55-62; filtro real (granular ou geotêxtil) é de Geotecnia | [p. 55-62] |
| Talude | não mais íngreme que 1V:1,5H [USACE-EM1601 p. 29, §3-3]; a calculadora avisa abaixo de 1,5H:1V | |

Exemplo de livro: Exemplo 1 (canal trapezoidal, Q 5.000 cfs, S 0,0049): V 9,7 ft/s, d 11,8 ft, K1 0,73 (talude 2:1, φ ≈ 41°), Ss 2,65, SF 1,2 → **D50 = 0,43 ft** [FHWA-HEC11 p. 72; formulário p. 78]. A calculadora com V = 2,957 m/s,
d = 3,597 m, z = 2, φ = 41 devolve D50 = 0,129 m (0,425 ft), K1 = 0,732; teste `test_hec11_exemplo1_d50`.

### 2.1 n de rip-rap (Strickler) e a divergência EM-1601 x HEC-11

| Método | Fórmula | Diâmetro | Fonte |
|---|---|---|---|
| EM-1601 | n = K · D90(min)^(1/6), D em ft; K = 0,034 (velocidade e tamanho da pedra), 0,036 (média de todos os ensaios), 0,038 (capacidade e borda livre); só S < 2 %; sem perdas de forma (curva); n ≈ 15 % maior se lançado sob água | D90 da curva mínima da graduação | [USACE-EM1601 p. 29, Eq. 3-2] |
| HEC-11 | n = 0,0395 · D50^(1/6), D em ft (Anderson et al.; Strickler 1923) | D50 | [FHWA-HEC11 p. 166, Eq. 20] |
| HEC-15 | tabela por D50 e profundidade (Blodgett-McConaughy): D50 0,15 m: 0,069 (y 0,5 m) e 0,056 (y 1,0 m); D50 0,30 m: 0,080 (y 1,0 m); cascalho 25 mm: 0,040 a 0,031; **n/d com y/D50 < 1,5** (usar Eq. 6.2, depende de S) | D50 | [FHWA-HEC15 p. 29, Tab. 2.2] |
| DNIT | pedra seca (rip-rap) com fundo em cascalho: 0,023 a 0,033 | descritivo | [DNIT-DREN p. 133, Tab. 34] |

`n_riprap(D, metodo="em1601"|"hec11", uso=...)` implementa os dois e avisa; diâmetros representativos diferentes, **sem conciliação (decisão F7)**. Com D = 0,15 m, `hec11` dá n = 0,035; o HEC-15 dá 0,056 a 0,069 para a mesma pedra em lâmina de 0,5 a 1,0 m:
as fontes não concordam, e o parecer declara qual usou. D30 do EM-1601 (Eq. 3-3, p. 30-31; V_SS local, Sf, Cs, CV, CT) e D50 do HEC-11 não se comparam sem a graduação (`DIVERGENCIAS.md`).

## 3. Gabião: HEC-15 Cap. 7

- Colchão de gabião (mattress) é caixa de tela de arame com pedra, em células; espessura costuma ser menor que a do rip-rap equivalente; "raramente econômico em canal de declividade suave" [FHWA-HEC15 p. 113].
- **n**: o arame não conta; usa-se o D50 da pedra do colchão nas relações de rip-rap e cascalho (Eq. 6.1; com y/D50 < 1,5, Eq. 6.2) [FHWA-HEC15 p. 113, §7.1].
  Pedra típica no colchão: 0,076 a 0,152 m (colchão de 0,152 m) até 0,116 a 0,305 m (colchão de 0,457 m) [p. 114].
- **τp**: Eq. 7.1 τp = F*·(γs − γ)·D50, F* = 0,10, válida para D50 de 0,076 a 0,457 m; Eq. 7.2 τp = 0,0091·(γs − γ)·(MT + MTc), MTc = 1,24 m, para espessura de 0,152 a 0,457 m; vale o **maior** dos dois [p. 113-114].
  Os ensaios divergem: 140 a 190 N/m² (Simons et al.) contra ~1.700 N/m² (Clopper e Chen, ensaio de galgamento de aterro); o HEC-15 enfatiza o primeiro, conservador [p. 113].
- Exemplo em SI [p. 115-117]: Q 0,28 m³/s, S 0,09, B 0,60 m, talude 3H:1V, colchão 0,23 m, D50 0,15 m, γs 25.900 N/m³ → d = 0,185 m, n = 0,055, Q = 0,29 m³/s, τp = 241 N/m², τd = 163 N/m², SF 1,25: 241 > 1,25 · 163, estável.
- V de projeto de colchão Reno: 1,8 / 3,5 / 4,5 m/s para e = 0,17 / 0,23 / 0,30 m [SRHCE-GED-018 p. 27]; DAEE: gabião V <= 2,5 e n = 0,028 [DAEE-IT-DPO11 p. 4]. HEC-11 trata gabião nas p. 97-105 (Tab. 4 e 5; **não reaberto**, só mapeado em G4).

### 3.1 Caso retroanálise gabião x tubo (planilha do André, fonte local D8)

A planilha usa n do canal de **0,02 a 0,035** (caso-base 0,035), canal retangular 1,59 x 1,00 m, lâmina 80 %, S 0,003: Q = 1,0784 m³/s; tubo DN 1000 a 85 %: Q = 1,7591 m³/s.
**Divergência a apontar, sem corrigir a planilha:** o n do HEC-15 para pedra de D50 0,10 a 0,15 m em lâmina de 0,5 a 1,0 m é 0,047 a 0,069 (Tab. 2.2, geometria 1:3 e b 0,6 m; ordem de grandeza, aplicar a Eq. 6.1 à seção real);
o DAEE dá 0,028. Consequência por Manning (calculadora, mesma seção, y = 0,80 m, S = 0,003): n 0,047 → Q = 0,803; n 0,055 → 0,686; n 0,069 → 0,547 m³/s. Com n do canal >= 0,047 o canal escoa **menos** que o
tubo de concreto (n 0,015: Q = 1,17) em toda a grade, e a conclusão "88 % / 48 %" da planilha muda. Quem decide o n do gabião (D50 e espessura de projeto) é o projetista; o Drenagem pede o valor.
Outras ressalvas do caso: rótulo "declividade (%)" com 0,003 usado como m/m; lâmina 80 % x 85 %; sem Q de projeto, V, Fr nem borda livre.

## 4. Revestimentos de terra, grama e concreto: pontos práticos

- n de dreno de terra escavado: Salitre 0,030 [1584:105]; Delmiro 0,025 [1520:129]; Iuiu 0,03; PISF 0,030 (rocha alterada, sem revestimento) e 0,035 (rocha sã) [SRHCE-GED-030 p. 20]; HEC-15 solo nu típico 0,020
  (0,016 a 0,025) [FHWA-HEC15 p. 29]. NRCS CPS 608: n pela condição **envelhecida** do canal, com o crescimento provável de vegetação sob manutenção normal [NRCS-CPS608-2023 p. 2]. Delmiro e Salitre não dizem se é n de projeto novo ou envelhecido.
- Dreno de vala aberta em projeto de irrigação: seção parecida com a de canal de terra, geralmente sem revestimento (exceto solo muito permeável); b mínimo 1 m, ditado pelo equipamento de construção e limpeza; talude 1,5:1 a 2:1,
  até 3:1 ou mais suave; sem compactação do talude, exceto casos especiais; manter limpo de vegetação alta; **canal piloto** no eixo quando há vazão contínua pequena e cheias intermitentes (evita meandro e fundo molhado) [CDV-MANUAL-IRRIG p. 514, §11.3.2].
  Seção em dois estágios: NEH 654 Cap. 10 por referência do CPS 608 [NRCS-CPS608-2023 p. 2].
- Concreto em dreno: seção-padrão do Sertão Pernambucano [1390:430] (ver `talvegues-desague-quedas.md`); drenos do PISF: V <= 3,00 m/s [SRHCE-GED-030 p. 20].
- Profundidade máxima do dreno: 4,0 m no PISF [SRHCE-GED-030 p. 20, §6.2.5]; Salitre: 1,80 m onde o dreno serve à drenagem subterrânea [1584:105]; CPS 608: fundo >= 1 ft (0,30 m) abaixo do invert de dreno subsuperficial que deságua nele [p. 2].

## 5. Sugestões de função e de teste (para o mantenedor; não implementadas)

| Sugestão | Fonte e números |
|---|---|
| `tensao_trativa(d, S)` e `verificar_tensao(tau_p, d, S, SF)` | HEC-15 Eq. 2.4, 3.1, 3.2; exemplo do gabião p. 117: τd = 9810·0,185·0,09 = 163 N/m²; τp = 241 N/m²; SF 1,25 |
| `tau_p_gabiao(D50, MT)` | Eq. 7.1 e 7.2; exemplo: Eq. 7.1 dá 241 N/m² (0,10·16.090·0,15); Eq. 7.2 com MT 0,23: 0,0091·16.090·(0,23 + 1,24) = 215 N/m² (recalculado, conferir); vale o maior |
| `escolher_secao_padrao(Q, S, n, V_adm, secoes)` | 13 seções ST do Sertão Pernambucano, base x altura em cm: 40x50, 60x50, 60x80, 60x100, 60x120, 60x150, 80x80, 80x100, 80x120, 80x150, 100x80, 100x150, 100x200, talude 1:1 [1390:430, Quadro 8.12] |
| Teste NEH 650-9 Tab. 9-1 | TR e folga por tipo de desvio [NRCS-NEH650-CH09 p. 16] |
| Teste CPS 608 | V mínima 1,4 fps = 0,4267 m/s e folga mínima 0,5 ft = 0,1524 m [NRCS-CPS608-2023 p. 2] |
