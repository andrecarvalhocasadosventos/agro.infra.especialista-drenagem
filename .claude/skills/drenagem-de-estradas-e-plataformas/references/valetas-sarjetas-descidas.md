# Valetas, sarjetas, descidas d'água e estradas de serviço

Fontes: `[DNIT-DREN]` IPR-724 (cap. 3; física = impressa + 4), `[FHWA-HEC15]`, `[FHWA-HEC22]`, `[FHWA-HEC12]`, `[LOC-IME]`
(apostila), `[DNIT-ES018-2023]`, `[DNIT-ES021-2023]`, `[DERPR-ES-DR-01-23]`. Recriado da versão da skill de bueiros e
atualizado com a calculadora `tools/dren/estradas.py` 0.1.0, o mapa G3, os casos Xingó e CAC Castanhão e as divergências F5.
A vazão afluente (racional, TR, Tc) vem de `hidrologia-de-projeto-para-drenagem`; a IDF, do Clima. Velocidade máxima
por revestimento e n: Tabelas 31 e 34 do DNIT-DREN e o arquivo `velocidades-admissiveis-e-revestimentos.md` da skill de
bueiros (ou de canais), enquanto existir.

## 1. Valeta de proteção de corte e de aterro, canal de drenagem

**Função e posição.** Valeta de corte: intercepta a água a montante e a mantém longe do talude; a **2,0 a 3,0 m** da
crista; o material escavado fica entre a valeta e a crista, apiloado. Valeta de aterro: recebe também sarjetas e valetas
de corte e leva ao bueiro; a 2,0 a 3,0 m do pé [DNIT-DREN p. 158, 165].

**Seção.** Trapezoidal (mais eficiente), retangular (rocha), triangular (cria plano preferencial: pouco recomendada para
grandes vazões). Revestir sempre que possível; obrigatório em solo permeável. Tipos: concreto (esp. mín. 0,08 m),
alvenaria de tijolo ou pedra (junta 1:4), pedra arrumada, vegetação [DNIT-DREN p. 158-160, 165-166]. Execução: DNIT ES 018
(a de 2023 está no corpus; a 018/2004 citada no manual não está).

**Cálculo (DNIT) [DNIT-DREN p. 160-163]:**
1. Q afluente pelo racional, com área limitada pela valeta e pelo divisor (C da Tab. 39 do manual; i em cm/h). Na
   calculadora: `vazao_por_metro` (q = I Σ C w / 3,6e6, I em mm/h) e `valeta_comprimento_critico`.
2. Fixar seção e declividade S₀; **V máxima** pelo revestimento (Tab. 31) e **n** (Tab. 34).
3. Tentar a altura h; A, P, R; Manning e Q = A V; comparar Q afluente × capacidade e V × V admissível (`valeta_manning`).
4. Regime pela altura crítica: retangular hc = 0,467 (Q/B)^(2/3) [= (q²/g)^(1/3)]; triangular hc = 0,728 (Q²/z²)^(1/5);
   trapezoidal por expressão em z, B e H₀ (símbolos corrompidos na extração; usar `canais_drenagem` para yc).
   **Evitar h a menos de 10 % de hc**; o `valeta_manning` avisa Fr em ±10 % do crítico [IME p. 54].
5. Folga, valeta revestida, Tab. 36 do DNIT: Q ≤ 0,25 m³/s: 10 cm; 0,25-0,56: 13; 0,56-0,84: 14; 0,84-1,40: 15;
   1,40-2,80: 18; > 2,80: 20 cm. Valeta em terra: f = 0,2 h até 0,3 m³/s; de 0,3 a 10 m³/s, **f = √(46·h)**, f e h em cm
   [DNIT-DREN p. 162, imagem conferida na F7; o `_texto` perde o radical] (provável origem da EQ. 4.7 do IME). A calculadora implementa só f = 0,2 h e a Tab. 4.2
   do IME [p. 54-55]; WSDOT usa 0,5 ft fixos [WSDOT p. 109] (divergência 11).
6. S excessiva: **escalonar** com barragens, S de trecho ≤ 2 %, E = 100 H/(α − β) (α e β em %), E ≤ 50 m [p. 163-164].
7. Ao atingir o **comprimento crítico** ou em talvegue secundário: descida d'água para a sarjeta ou caixa coletora [p. 164].

**Comprimento crítico (método do projetista, acervo).** L = Q_Manning(hmax) / q_racional; hmax = 0,8 h (regra observada no
Xingó, não declarada). VPC-1 do Xingó (b 0,20, topo 0,60, h 0,20, n 0,016, concreto): L = 162,57 m em i = 0,001 e 1.259,2 m
em i = 0,060, contra 162,54 e 1.259,04 m do projeto (acervo, sem ✓h; z = 1 deduzido). VPA-5, i = 0,001: Q 0,083 m³/s, V
0,539 m/s, L = 222,14 m (1419:86). Caso: `casos/drenagem/2026-10-08_xingo_lote1_valetas_protecao_comprimento_critico.md`.

**Verificação por tensão (HEC-15):** τd = γ d S₀ ≤ τp / SF, SF ≥ 1 (padrão 1,0); TR 5 a 10 anos no revestimento permanente,
TR 2 anos no transitório [HEC15 p. 31, 33, 35]. Largura de topo / profundidade < ~20; talude de enrocamento 1:3 ou mais
suave dispensa verificar o talude [p. 34]. Em projeto básico, verificar **por tensão e por velocidade** e adotar a mais
restritiva.

**Nível.** Anteprojeto: Manning, Tab. 31 e folga (Tab. 36 ou IME). Básico: + tensão (HEC-15), remanso em canal longo,
transição na saída, proteção do pé; revestimento e detalhe seguem o dispositivo-tipo (VPC, VPA) do Álbum.

**TR e Tc (padrão provisório, decisão F7):** TR 10 e Tc mínimo 5 min; alternativas 6 min (Álbum p. 214, OCR), 10 min (IS-239,
IPR726 p. 463; Xingó) e TR 25 (ENGEFER, IME p. 53). O Xingó usa Tc 10 min e TR 10: registrar, não "corrigir".

## 2. Sarjeta (corte e aterro)

**Sarjeta de corte (DNIT):** triangular com 1:4 do lado do acostamento (25 %) e a declividade do talude do outro; L1
(borda do acostamento ao fundo) de **1,0 a 2,0 m**; se L1 = 2,0 m não bastar, trapezoidal ou retangular com meio-fio
barreira com aberturas [DNIT-DREN p. 167-169; DNIT-ES018-2023 p. 2]. Concreto: fck mín. 20 MPa [ES018 p. 3] (o manual,
p. 170, registra 15 MPa: divergência 1); espessura 0,08 m (triangular) e 0,10 m (retangular, trapezoidal); formas a cada
3,00 m (DER-PR: gabaritos a 2,00 m); juntas a cada 12 m [DNIT-DREN p. 170; ES018 p. 4; DERPR-01 p. 5-6].
**Cálculo** [DNIT-DREN p. 170-174]:
- q = C i A / (36×10⁴) (m³/s/m), i em cm/h para **5 min e TR 10**, A = largura do implúvio (plataforma + projeção
  horizontal do 1º escalonamento do talude), C ponderado pelas larguras (eq. 3.01).
- Capacidade: Q = (1/n) A R^(2/3) I^(1/2) (eq. 3.02).
- **Comprimento crítico:** d = 36×10⁴ A R^(2/3) I^(1/2) / (C i L n) (eq. 3.03; d em m, L = largura do implúvio, i em cm/h);
  define a posição das saídas d'água; também limitado pela velocidade de erosão (Tab. 31).
Sarjeta de corte sem revestimento: evitar [p. 169]. Sarjeta de aterro: onde a água da pista erode a borda; meio-fio-sarjeta
conjugado é o tipo comum [p. 175-177].

**Sarjeta pavimentada, Izzard** (`sarjeta_triangular`): Q = (Ku/n) Sx^1,67 S_L^0,5 T^2,67, **Ku = 0,376 SI** [HEC22 p. 79,
eq. 5.2; HEC12 p. 39, eq. 4]; T = [Q n/(Ku Sx^1,67 S_L^0,5)]^0,375; n pela Tab. 5.3; TR e espalhamento admissível pela
Tab. 5.1 (arterial TR 10, espalhamento até o acostamento; rua local TR 5 com ½ faixa) [HEC22 p. 70]. **Composta**
(`sarjeta_composta`, depressão W e Sw junto ao meio-fio): Q = (Ku/n) S_L^0,5 {[d^(8/3) − y1^(8/3)]/Sw + y1^(8/3)/Sx},
y1 = Sx (T − W), d = y1 + Sw W; Eo = Qw/Q [HEC12 p. 41-43].
Gabaritos HEC-12 conferidos: Ex. 4 (p. 41): T 8 ft, Sx 0,025, S 0,01, n 0,015 dá 2,04 ft³/s (impresso 2,0); Ex. 5 composta:
Q 3,06 a 3,10 ft³/s e Eo 0,69. Conversão SI: 1 ft = 0,3048 m; 1 ft³/s = 0,028317 m³/s.

**Declividade mínima (F5, divergência 6; não decidir):** 0,5 % [DERPR-ES-DR-01-23 p. 10] × 0,3 %, 0,2 % em terreno muito
plano [HEC12 p. 19]; DNIT-ES018 não fixa. A calculadora avisa e não bloqueia.

## 3. Descida d'água, saída d'água e bueiro de greide

**Descida (DNIT):** conduz a água de valetas e sarjetas pelo talude; tipo **rápido** (calha) ou **degraus**; seções
retangular, meia-cana ou tubo; **módulos de concreto desaconselhados** (a ação dinâmica descalça e desjunta); confinar a
descida e proteger o talude [DNIT-DREN p. 186-188]. Execução: concreto fck ≥ 20 MPa, CA-50, junta de dilatação em
descida > 10 m [DNIT-ES021-2023 p. 2, 4]; DER-PR: descida de corte em degraus com caixa e de aterro rápida ou em degraus
com caixa dissipadora [DERPR-ES-DR-03-23 p. 3-5].
Dimensionamento [DNIT-DREN p. 188-190] (**não implementado** na calculadora):
- **Método I** (empírico): **Q = 2,07 L^0,9 H^1,6** (m³/s; L largura da descida e H altura média das paredes, m).
- Velocidade no pé: V_b = √(V_a² + 2 g H_b), na prática √(2 g h); **superestima a real**. Serve ao dissipador
  (entregar a `vertedouros-e-dissipadores`).
- **Método II:** perfil por passos (eq. 3.13, ΔX = ΔE/(I₀ − I_f)), supercrítico para jusante; yc retangular 0,467 (Q/b)^(2/3);
  circular, Tab. 38. Planilha de passos: Tab. 37.

**Saída d'água e caixa coletora** [DNIT-DREN p. 164, 195-200]: levam a água da sarjeta ou valeta ao terreno ou à caixa do
bueiro de greide. `caixa_coletora_grelha`: vertedor Qi = Cw P d^1,5 (Cw = 1,66 SI, 3,0 inglês); orifício Qi = Co A √(2 g d)
(Co = 0,67) [HEC12 p. 86, eqs. 17-18]; sem colmatação.

**Bueiro de greide** [DNIT-DREN p. 202, §3.9.3]: Q = soma dos dispositivos afluentes (ou bacia), TR "função do vulto
econômico da obra"; **sempre que possível sem carga a montante**; com carga, guardar a cota máxima na caixa e policiar
a velocidade de jusante. A hidráulica do barril é de `bueiros-e-travessias`.

## 4. Estrada de serviço de projeto de irrigação (analogia declarada)

O corpus cobre estrada rodoviária. Para estradas de serviço do projeto de irrigação, usar **por analogia declarada**:
1. Valeta lateral de proteção de corte e de aterro (§1), revestimento pela velocidade e pela tensão;
2. Bueiro de talvegue (`bueiros-e-travessias`) e de greide (§3), TR do núcleo e HW com folga ao subleito;
3. Sarjeta só onde a estrada for pavimentada e tiver meio-fio; senão, valeta e saídas d'água;
4. Passagem molhada e queda com bacia (Iuiu: 30 passagens e 159 quedas): caso `iuiu_2002_drenagem_superficial_drenos_bueiros.md`
   e `vertedouros-e-dissipadores`.
Declarar no parecer que o critério é rodoviário aplicado por analogia; exigência da Codevasf ou de concessionária é de
`normas-e-manuais`. Greide e taludes: `[DELEGAR: terraplenagem]`; seção pavimentada: `[DELEGAR: pavimentacao]`.
Valores dos casos: drenos de terra n = 0,03 e v ≤ 0,80 m/s (até 1,00 em trechos), 95 descidas reduzidas a 11 ao subir a
velocidade de 0,80 a 1,00 m/s [1051:321, 334]; valetas trapezoidais 1V:1,5H em grama, com v > 2,00 m/s só em alvenaria de
pedra [1341:71, 73]. Xingó: VPC em concreto n 0,016, TR 10, Tc 10 min, I 2,353 mm/min (km 0 a 33+890) e 1,789 mm/min
depois [1419:65-66, 98]. CAC Castanhão: valas de crista e coletores com Tc 5 min, C 0,6 a 0,8, n 0,015, Y/D < 0,5 e
tensão de arraste > 2 kN/m² [1128:106-107, 112]; **P = 23,2 mm foi usada como mm/h** (Q 12 vezes menor): caso negativo
`2026-10-08_cac_castanhao_estrada_acesso_valas_chuva_como_intensidade.md`; não reproduzir os Q do Quadro 5.6.
