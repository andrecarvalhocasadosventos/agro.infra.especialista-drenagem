# O que pedir à Climatologia (decisão D7) e como reconhecer IDF emprestada

D7: a Climatologia entrega a chuva (IDF, séries, chuva de projeto por TR e duração) **com incerteza**; o hidráulico escolhe o método, o TR da obra e calcula a vazão. O hidráulico não gera IDF por conta própria. Se ela não existir, usa uma premissa provisória rotulada e emite o bloco abaixo (D13). O Gestor aprova o roteamento.

## 1. Checklist do pedido

Marcar o que veio e o que falta antes de calcular vazão.

**A. IDF ou equação de chuva**
- [ ] Forma e parâmetros: i = a·TR^b/(t + c)^d (mm/h, t em min, TR em anos) ou tabela i(t, TR); unidade declarada (mm/h ou mm/min).
- [ ] Faixa de validade em duração (mínima e máxima, em min) e em TR; Tc de pequena bacia costuma ser < 15 min.
- [ ] Posto(s) de origem, distância e diferença de altitude ao perímetro; se pluviográfico ou pluviométrico desagregado (e com qual fator de 24 h para 1 h).
- [ ] Período de dados (anos, falhas), tamanho da amostra por duração e distribuição ajustada (Gumbel, GEV, outra).
- [ ] Incerteza: intervalo de confiança (ex. 90 %) por TR e duração, ou erro-padrão. Pedir os valores central, inferior e superior.
- [ ] Regra de desagregação usada, se houver: P24h = 1,13 × P1dia [DNIT-HIDRO p. 128] ou 1,10 (Baixio, Taborga Torrico 1975, doc 670:113). Pedir a que o posto usa e a fonte.
- [ ] Se a equação é do tipo Pfafstetter: parâmetros do posto, α, β, a, b, c [DNIT-HIDRO p. 107]. Os parâmetros dos 98 postos não estão no corpus.

**B. Chuva de projeto**
- [ ] Altura de chuva P(t, TR) para TR = 5, 10, 25, 50, 100 e t = 10, 15, 30, 60, 120, 360, 1.440 min (tabela, com incerteza).
- [ ] Distribuição temporal observada na região (padrão por duração) e a razão entre blocos, se existir. Sem ela, o hidráulico usa blocos alternados [PMSP-DRENURB-V2 p. 21-22] e rotula.
- [ ] Fator de redução de chuva por área (ARF) para bacias acima de 25 km² (DNIT: FA = 1 − 0,10·log(A/25) no procedimento B [DNIT-HIDRO p. 74, 108]) e a fonte do ARF para o semiárido.
- [ ] Chuva antecedente de 5 dias e probabilidade de solo úmido por época (para a escolha de ARC; ver `references/cn-scs.md`).
- [ ] Sazonalidade: meses das chuvas máximas (irrigação coincide ou não com a chuva).

**C. Séries e estatística**
- [ ] Série de máximas anuais diárias e, se existir, de 1 h e 24 h, com datas.
- [ ] Teste de estacionariedade e tendência, e a recomendação sobre mudança do clima (adotar fator? qual?).
- [ ] Série de vazões máximas anuais, se houver posto fluviométrico na bacia ou em bacia semelhante (para calibrar o método chuva-vazão).

**D. Para decisão**
- [ ] Recomendação de TR máximo extrapolável com a série (regra do tool: aviso se TR > 2n).
- [ ] Eventos extremos já observados na região (data, altura, duração) para verificação independente da IDF.

## 2. Bloco de pedido

```
[DELEGAR: climatologia]
pedido:      IDF local com incerteza e chuva de projeto por TR e duração para <bacia/perímetro, coordenadas, área, Tc estimado>
entrego:     Tc estimado <valor e faixa, min>; TR de projeto <valores por obra>; método hidrológico previsto <racional/McMath/SCS-CN> e a faixa de durações necessária <min a h>
preciso de:  i(t, TR) em mm/h para TR 5, 10, 25, 50, 100 e t de 10 min a 24 h, com intervalo de 90 % por TR; forma a·TR^b/(t+c)^d com faixa de validade; posto, período, n de anos e distribuição; distribuição temporal da chuva de projeto; ARF para A > 25 km²
premissa provisória: IDF do <posto/estudo X> (<fonte>), com acréscimo de <x> % de margem de segurança, rotulada "emprestada"
impacto se mudar: Q de pico muda aproximadamente na mesma proporção que i (racional) e mais que proporcional no SCS-CN (P entra elevada ao quadrado acima de Ia); diâmetro e HW dos bueiros podem mudar
urgência:    bloqueia a resposta (projeto básico) | refina a resposta (anteprojeto)
```

Quando o dado é só um valor de P1dia por TR (como no Iuiu): pedir também a regra de passagem de 1 dia para a duração de Tc e a incerteza dessa passagem (a fórmula do Iuiu, i = 2,31·P1dia·Tc^-0,55 com Tc em min, é regra do projeto, não do corpus).

## 3. Sinais de IDF emprestada ou frágil

Sem critério numérico de distância no corpus; os sinais abaixo são para pedir justificativa, não para rejeitar sozinhos.

1. A equação não traz faixa de duração nem de TR, ou o Tc cai fora dela (Wilken, SP, vale de 10 a 1.440 min [PMSP-DRENURB-V2 p. 19]).
2. Posto de região climática diferente (litoral, serra, outro estado) para um perímetro semiárido. Ex.: a IDF de Wilken (São Paulo) não serve ao sertão baiano.
3. Mesmos parâmetros usados em bacias separadas por centenas de km. O DNIT admite escolher o posto de referência cujas precipitações relativas (posto local ÷ posto de referência, por duração) mais se parecem com as do local, e observa que elas variam pouco com o TR [DNIT-HIDRO p. 128-129]; essa comparação deve ser mostrada.
4. Expoente b muito diferente do usual dos ajustes brasileiros do acervo (0,17 a 0,25 em CSB e Wilken). Não é erro por si, mas pede conferência.
5. Equação sem posto, ano ou n; "a = 23,7 e b = 0,895" do Baixio de Irecê não traz a equação que os define (caso baixio_irece_vazoes_hut_scs).
6. Unidade ambígua (mm/min no texto, mm/h nos números): o Iuiu diz mm/min e só fecha em mm/h.
7. Incerteza ausente: série curta (< 20 anos, aviso do `gumbel_P_TR`) ou TR maior que o dobro da amostra.
8. Comparação com a curva média dos 98 postos do DNIT para TR 10 (P em mm: 5 min 15,3; 15 min 32,2; 30 min 44,7; 1 h 59,4; 2 h 74,7; 4 h 91,1; 8 h 107,8; 24 h 139,0) [DNIT-HIDRO p. 130, Tab. 23]: razão P1h/P24h = 0,43 nessa média. IDF cuja razão se afaste muito pede explicação. É conferência de ordem de grandeza, não critério.
9. Desagregação de 1 dia para 24 h sem fonte (1,10 ou 1,13).

## 4. O que o hidráulico devolve à Climatologia

Tc de cada bacia e sua faixa; durações pedidas; TR por obra; sensibilidade de Q a ±1 desvio da IDF; se a obra é sensível a duração longa (volume, reservatório) ou curta (pico).
