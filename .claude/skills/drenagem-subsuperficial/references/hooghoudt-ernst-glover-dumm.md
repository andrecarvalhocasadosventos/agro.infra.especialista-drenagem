# Hooghoudt, Donnan, elipse, Ernst e Glover-Dumm: equações, validade e gabaritos conferidos

Símbolos: q = descarga especifica/recarga (m/d); h = carga no meio do vão acima do nível da água no dreno (m); D =
distância do dreno à camada impermeável (m); d_e = profundidade equivalente (m); r ou r0 = raio efetivo (m); K (m/d);
L = espaçamento (m); μ = porosidade drenável; t em dias. Páginas: PDF físico. Tudo abaixo sai de
`tools/dren/drenos.py` 0.2.0; a calculadora é a fonte numérica, a tabela dá o que a fonte primária confere.

## 1. Hooghoudt e Donnan (regime permanente)

- Donnan/Hooghoudt 1936 (dreno com água no nível D, lençol H): L² = 4K(H² − D²)/q [ILRI-DPA16 p. 264, Eq. 8.3].
- Perfil homogêneo: q = (8 K d h + 4 K h²)/L² [ILRI-DPA16 p. 265, Eq. 8.4]. Primeiro termo: fluxo abaixo do nível do
  dreno; segundo, acima. Dreno na interface de duas camadas: 8 Kb D h + 4 Ka h² [ILRI-DPA16 p. 265, Eq. 8.7]. Com a
  convergência radial, D é trocado por d_e: L² = (8 K2 d_e h + 4 K1 h²)/q (função: `hooghoudt_espacamento`).
- Hipóteses do próprio Hooghoudt: dreno meio cheio e sem resistência de entrada (u = π r0, Eq. 8.14) [ILRI-DPA16
  p. 268]. Se o dreno tem resistência de entrada ou envoltório volumoso, o r efetivo cresce (envoltório de brita
  conta como "dreno de vala", u = b + 2 r0, Eq. 8.15).
- **d_e, forma de Moody** (padrão `metodo_de="moody"`): d_e = d/[1 + (d/L)(2,55 ln(d/r) − C)], C = 3,55 − 1,6 d/L +
  2 (d/L)², para d/L ≤ 0,31; d_e = L/[2,55 (ln(L/r) − 1,15)] para d/L > 0,31 [USBR-DRAINAGE PDF 173-174, seção 5-5];
  confere com a Tab. 8.1 de Hooghoudt (r0 = 0,1 m) a < 1 % [ILRI-DPA16 p. 267]. Exemplo USBR: K 0,305 m/d, D 6,1 m,
  L 91 m, r 0,18 m → d_e = 4,45 m (manual 4,4 m).
- **d_e, série exata** (`metodo_de="serie"`): d = (π L/8)/[ln(L/(π r0)) + F(x)], x = 2π D/L; F = Σ 4 e^(−2nx)/(n(1 −
  e^(−2nx))), n ímpar, para x > 0,5; F = π²/(4x) + ln(x/(2π)) para x ≤ 0,5 (Dagan) [ILRI-DPA16 p. 268, Eq. 8.9-8.13].
  Fica 2 a 3 % abaixo da Tab. 8.1; confere 0,2 % com o Ex. 8.2 (D 4,8, L 72, r0 0,61 → d = 4,16 m).
- Quando D passa de ~L/4, d_e fica aproximadamente constante e D deixa de pesar [ILRI-56 p. 42].
- **Sentido de uso:** Hooghoudt vale com o dreno na interface ou numa camada homogênea. Dreno **dentro** de camada
  superior de baixo K → Ernst [ILRI-DPA16 p. 270]. O termo (Di − Dd) da nota WATERLOG-DRAINAGE-EQUATION p. 2 é
  dimensionalmente inconsistente e **não é usado**.

Gabaritos que a calculadora reproduz (testes citados em SKILL §4):

| Caso | Entradas | Resposta da fonte | Fonte |
|---|---|---|---|
| Ex. 8.1 (tubo, 1 camada) | q 0,001; h 1,0; D 4,8; r0 0,10; K 0,14 | 65 m (série: 64 m) | [ILRI-DPA16 p. 276-279] |
| Ex. 8.2 (vala) | r0 0,61; mesmos | 72 m com a série | [ILRI-DPA16 p. 276-279] |
| Ex. 8.3 (2 camadas, interface no dreno) | K_acima 0,06; K_abaixo 0,30 | 95 m | [ILRI-DPA16 p. 276-279] |
| Maniçoba (dreno sobre a barreira) | K 2,3; h = 1,60 − 1,10 = 0,50; q = 4 K h²/L² | L = 16,96 m (q 8,0 mm/d) | [EMBRAPA-MANICOBA-1988 p. 3] |
| Donnan USBR | K 3,05; a 6,7; b 7,92; q 0,025/14 | L = 347 m | [USBR-DRAINAGE p. 169-170 impr.] |

Valores de EnDrain (67, 77 e 98 m para os mesmos exemplos) são método alternativo e **não** são padrão do pacote
[WATERLOG-ENDRAIN p. 7-10].

**Validade:** drenos paralelos e equidistantes; K constante por camada; regime permanente; L ≥ ~10 m. Hooghoudt
**não** descreve bem dreno sobre a camada impermeável (d = 0) em laboratório [EMBRAPA-ESPACAMENTO-1990 p. 1, 10]. Viés
de campo e de laboratório: SKILL §3.2.

## 2. Elipse e Donnan para fluxo horizontal

S = √[4K(m² + 2 a m)/q] (K e q na mesma unidade) [NRCS-NEH624-CH04 p. 63-65, Eq. 4-8]; equivale a Donnan com b = a + m.
Exemplo 1: K 2 pol/h, q 0,01 pol/h, a 7 ft, m 3 ft → 202 ft (gráfico 203 ft; p. 65-66). Use quando a barreira é rasa
(a ≤ 2× a profundidade do dreno), há vala ou envoltório de brita. O Exemplo 2 (196 ft) é solução gráfica da elipse
modificada: **não implementado**.

## 3. Ernst (solo estratificado)

h = h_v + h_h + h_r, com h_v = q Dv/Kv, h_h = q L²/(8 Σ KD), h_r = q L W_r/(π Kr), W_r = ln(a Dr/u)
[ILRI-DPA16 p. 270-272, Eq. 8.17-8.21]. Σ KD limitada a espessuras ≤ L/4. Fator geométrico a: Tab. 8.2 [ILRI-DPA16
p. 272] (Kb/Kt de 1 a 50, Db/Dt de 1 a 32; Kb/Kt < 0,1 → a = 1; > 50 → a = 4; entre 0,1 e 1 a tabela não traz valor: a
calculadora usa a linha Kb/Kt = 1 com aviso). u = π r0 (padrão da calculadora, Eq. 8.14).

Dreno na camada superior (Eq. 8.23): Dv = h; Dr = Do; Σ KD = Kb Db + Kt (Do + h/2); Kv = Kr = Kt; a pela Tab. 8.2.
**Ex. 8.4** (q 0,007; h 0,70; Kt 0,5; Kb 2,0; Do 1,0; Db 4,0; r0 0,05): L = **38 m** (h_v 0,01, h_h 0,15, h_r 0,54 m;
a = 3,9; u = 0,157 m) [ILRI-DPA16 p. 280-281]. A nota WATERLOG-ENDRAIN p. 10 dá 51,8 m porque **omite o fator a**
(com a = 1 a calculadora reproduz 51,4 m): registrar quando alguém trouxer esse número.

## 4. Glover-Dumm (regime transitório)

h_t = fator · h0 · e^(−αt), α = π² K d/(μ L²); j = 1/α = μ L²/(π² K d). Fator **1,16** (freático inicial em parábola de
4º grau, Dumm 1960) [ILRI-DPA16 p. 284, Eq. 8.32]; fator 4/π = 1,27 se o freático inicial for horizontal (Eq. 8.31).
Espaçamento: L = π √[K d t/(μ ln(1,16 h0/ht))] (Eq. 8.33). Validade: αt > 0,2; drenos paralelos acima da barreira;
sem recarga durante o rebaixamento. Fator 1,16 conferido em duas fontes independentes (ILRI-DPA16 e Maniçoba).

| Critério de D médio | Fórmula | Fonte |
|---|---|---|
| `ilri` | d = d_e | [ILRI-DPA16 p. 284, Eq. 8.29] |
| `usbr` (padrão) | d_e + h0/2 | [USBR-DRAINAGE p. 187 (impr. 168), Ex. 5-10] |
| `manicoba` | d_e + (h0 + ht)/4 | [EMBRAPA-MANICOBA-1988 p. 3] |

Os três dão tempos diferentes (no exemplo do USBR: 31,8 d com o do USBR; 34,4 d com o de Maniçoba, +8 %): **declarar**.
Gabaritos: Maniçoba K 2,3; μ 0,15; h0 0,8; ht 0,4; t 3 d; D = 0,3 m → L = **12,72 m** [EMBRAPA-MANICOBA-1988 p. 3]
(a calculadora devolve 12,7217 m); USBR (K 0,305; d_e 4,4; h0 2,7; μ 0,07; L 91; ht 1,2) → t = 32 d (manual 31,8 d).

## 5. Quando o regime não é nem permanente simples nem Glover-Dumm

Toksöz-Kirkham, anisotropia, drenagem sob percolação vertical (Anexo 18) e não permanente completo (Anexo 19) estão
em [FAO-IDP62 p. 193-212] e **não** estão na calculadora. Diante deles: dizer que o método não é do pacote, mostrar o
resultado da calculadora como ordem de grandeza e delegar a verificação (consultoria).
