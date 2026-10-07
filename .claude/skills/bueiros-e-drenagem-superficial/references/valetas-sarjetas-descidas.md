# Valetas, canais de drenagem, sarjetas, descidas d'água e estradas de serviço (versão resumida)

Fontes: `[DNIT-DREN]` IPR-724 (cap. 3, drenagem superficial), `[FHWA-HEC15]` (revestimentos flexíveis), `[FHWA-HEC22]` (sarjeta
pavimentada). Páginas = marcador do `_texto` (no IPR-724, física = impressa + 4). Velocidades, tensões e n por revestimento:
`velocidades-admissiveis-e-revestimentos.md`. A vazão afluente (Racional, TR) vem da hidrologia; aqui só a hidráulica do dispositivo.

## 1. Valeta de proteção de corte e de aterro, canal de drenagem

**Função e posição.** Valeta de corte: intercepta a água do terreno a montante e a mantém longe do talude; fica **2,0 a 3,0 m** da crista;
o material escavado vai entre a valeta e a crista, apiloado. Valeta de aterro: recebe também sarjetas e valetas de corte e leva ao
bueiro; fica 2,0 a 3,0 m do pé do talude [DNIT-DREN p. 158, 165].

**Seção.** Trapezoidal (mais eficiente), retangular (em rocha), triangular (cria plano preferencial de escoamento: pouco recomendada
para grandes vazões). Revestir sempre que possível, obrigatório em terreno permeável; tipos: concreto (esp. mín. 0,08 m), alvenaria
de tijolo ou pedra (junta 1:4), pedra arrumada, vegetação. Execução: DNIT 018/2004 (fora do corpus) [DNIT-DREN p. 158-160, 165-166].

**Cálculo (DNIT) [DNIT-DREN p. 160-163]:**
1. Q afluente pelo Racional com área limitada pela valeta e pelo divisor da vertente (C pela Tabela 39 do manual; i em cm/h).
2. Fixar tipo de seção, largura e talude; declividade S₀ (do projeto vertical); **velocidade máxima** pelo revestimento (Tabela 31)
   e **n** (Tabela 34).
3. Tentar a altura h; A, P, R; Manning V = (1/n) R^(2/3) S^(1/2) e Q = A V. Comparar Q afluente x capacidade e V x V admissível.
4. Regime pela altura crítica: retangular hc = 0,467 (Q/B)^(2/3) [= (q²/g)^(1/3)]; triangular hc = 0,728 (Q²/z²)^(1/5); trapezoidal por
   expressão em z, B e H₀ (símbolos corrompidos na extração; usar `canais.y_critica`). **Evitar h a menos de 10 % de hc** (instabilidade).
5. Folga: valeta revestida, Tabela 36: Q ≤ 0,25 m³/s: 10 cm; 0,25-0,56: 13; 0,56-0,84: 14; 0,84-1,40: 15; 1,40-2,80: 18; > 2,80: 20 cm. Valeta em
   terra: f = 0,2 h até 0,3 m³/s e fórmula própria até 10 m³/s (a equação impressa está corrompida: conferir no PDF, p. 162-163).
6. Se a declividade do terreno gera v > admissível: **escalonar** com barragens, declividade de trecho ≤ 2 %, espaçamento
   E = 100 H/(α − β) (α e β em %), E ≤ 50 m (2 % e 1 m de desnível) [DNIT-DREN p. 163-164].
7. Quando atingir o comprimento crítico ou houver talvegue secundário: descida d'água para a sarjeta ou caixa coletora [p. 164].

**Cálculo (HEC-15):** τd = γ d S₀ ≤ τp / SF, com SF ≥ 1 (padrão 1,0); TR 5 a 10 anos para revestimento permanente, TR 2 anos para o transitório
[HEC15 p. 31, 33, 35]. Largura de topo/profundidade < ~20; talude de enrocamento 1:3 ou mais suave dispensa verificar o talude [p. 34]. Em projeto básico verificar a valeta
**pela tensão e pela velocidade** e adotar a mais restritiva.

**Nível:** anteprojeto: Manning e Tabela 31, folga da Tabela 36. Básico: + tensão HEC-15, perfil de remanso em canal longo (`canais.remanso`), transição na saída
e proteção do pé; revestimento e detalhe seguem o dispositivo-tipo (VPC, VPA) do Álbum.

## 2. Sarjeta (corte e aterro)

**Sarjeta de corte (DNIT):** triangular com 1:4 do lado do acostamento (25 %) e a declividade do talude do outro; L1 (borda do acostamento ao fundo)
de **1,0 a 2,0 m**; se L1 = 2,0 m não bastar, trapezoidal ou retangular com meio-fio barreira com aberturas [DNIT-DREN p. 167-169]. Concreto: fck mín. 15 MPa;
espessura 0,08 m (triangular), 0,10 m (retangular e trapezoidal); formas a cada 3,00 m; juntas de dilatação a cada 12 m [p. 170].
**Cálculo** [p. 170-174]:
- Q por metro linear: q = C i A / (36×10⁴) (m³/s/m), i em cm/h para **5 min e TR 10**, A = largura do implúvio (plataforma + projeção horizontal do
  1º escalonamento do talude), C ponderado pelas larguras (eq. 3.01).
- Capacidade: Q = (1/n) A R^(2/3) I^(1/2) (eq. 3.02).
- **Comprimento crítico:** d = 36×10⁴ A R^(2/3) I^(1/2)/(C i L n) (eq. 3.03; d em m, L = largura do implúvio, i em cm/h); gera a curva d = f(I) e define a posição das saídas
  d'água; também limitado pela velocidade de erosão (Tabela 31).
Sarjeta de corte sem revestimento: evitar [p. 169]. Sarjeta de aterro: onde a água da pista erode a borda; meio-fio-sarjeta conjugado é o tipo comum; revestimento
segue a velocidade limite [p. 175-177].

**Sarjeta pavimentada (HEC-22, essencial):** Izzard modificada, Q = (Ku/n) Sx^1,67 S_L^0,5 T^2,67 (**Ku = 0,376 em SI**) [HEC22 p. 79, eq. 5.2]; espalhamento
T = [Q n/(Ku Sx^1,67 S_L^0,5)]^0,375; n pela Tabela 5.3; **TR e espalhamento admissível** pela Tabela 5.1 (ex.: arterial TR 10, espalhamento até o acostamento;
rua local de baixo tráfego TR 5 com ½ faixa) [HEC22 p. 70]. Exemplo conferido em `exemplos-de-conferencia.md` §3.

## 3. Descida d'água, saída d'água e bueiro de greide

**Descida d'água (DNIT):** conduz a água de valetas e sarjetas pelo talude; tipo **rápido** (calha) ou **degraus**; seções retangular, meia-cana ou tubo;
**módulos de concreto desaconselhados** (a ação dinâmica descalça e desjunta); confinar a descida e proteger o talude; execução DNIT 021/2004 [DNIT-DREN p. 186-188].
Dimensionamento [p. 188-190]:
- **Método I** (empírico): **Q = 2,07 L^0,9 H^1,6** (Q em m³/s; L largura da descida e H altura média das paredes, em m); fixar L e achar H.
- Velocidade no pé: V_b = √(V_a² + 2 g H_b), na prática V_b = √(2 g h) (desprezando V_a); **superestima a real**. Serve ao dimensionamento do
  dissipador (entregar a `vertedouros-e-dissipadores`).
- **Método II:** perfil da linha d'água por passos (eq. 3.13, ΔX = ΔE/(I₀ − I_f)), supercrítico para jusante; profundidade crítica retangular
  y_c = 0,467 (Q/b)^(2/3) [= (q²/g)^(1/3)]; circular pela Tabela 38. Planilha de passos: Tabela 37.

**Saída d'água e caixa coletora** [DNIT-DREN p. 164, 195-200]: levam a água da sarjeta ou da valeta ao terreno ou à caixa coletora do bueiro de greide.

**Bueiro de greide** [DNIT-DREN p. 202, §3.9.3]: Q = soma das vazões dos dispositivos afluentes (ou bacia de contribuição), com TR "função do vulto econômico da obra";
**sempre que possível sem carga a montante**; se com carga, guardar rigorosamente a cota máxima da água na caixa coletora e policiar a velocidade de jusante.

## 4. Drenagem de estrada de serviço de projeto de irrigação (analogia)

O corpus cobre estrada rodoviária. Para estradas de serviço do projeto de irrigação, usar como **analogia declarada**:
1. Valeta lateral de proteção de corte e de aterro (§1) com revestimento pela velocidade e pela tensão;
2. Bueiro de talvegue (HDS-5, `SKILL.md` §3) e bueiro de greide (§3), com TR 25 como premissa do núcleo e HW com folga ao subleito;
3. Sarjeta só onde a estrada for pavimentada e tiver meio-fio; senão, valeta e saídas d'água;
4. Passagem molhada e queda com bacia (Iuiu, 30 passagens e 159 quedas): ver o caso `iuiu_2002_drenagem_superficial_drenos_bueiros.md` e `vertedouros-e-dissipadores`.
Declarar no parecer que o critério é rodoviário aplicado por analogia; exigência de concessionária ou da Codevasf é de `normas-e-manuais`.
Valores adotados nos casos: drenos de terra n = 0,03 e v ≤ 0,80 m/s (até 1,00 em trechos), 95 descidas reduzidas a 11 ao subir a velocidade de 0,80 a 1,00 m/s
[1051:321, 334]; valetas trapezoidais 1V:1,5H em grama com v > 2,00 m/s para alvenaria de pedra [1341:71, 73].
