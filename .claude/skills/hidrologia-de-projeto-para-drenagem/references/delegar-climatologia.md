# O que pedir ao Clima (decisão D7) e como reconhecer IDF emprestada

O nome do arquivo é mantido (o núcleo e a skill do Clima apontam para ele). O id de delegação é **`clima`**: escrever `[DELEGAR: clima]`, nunca "climatologia".

D7: o Clima entrega a chuva (IDF, P(t, TR), incerteza, ARF, estatística de chuva antecedente e sazonalidade); o Drenagem escolhe método e TR da obra e calcula a vazão. **O Drenagem não ajusta IDF, não desagrega série e não gera máximas anuais**: consome a entrega da skill `chuvas-intensas-e-idf` do Especialista Clima e a **cita** (posto, versão do dado, n, distribuição, IC, desagregação). Se a entrega não existir, usa premissa provisória rotulada "emprestada" e emite o bloco da seção 2 (V12 e V6). O Gestor aprova o roteamento. Consulta de IDF já publicada por terceiros (TPF, SGB, regionais do Nordeste): pedir ao Clima a crítica e a comparação, não fazer aqui.

## 1. Contrato de entrega (itens do Clima, `chuvas-intensas-e-idf` seção 4)

A skill do Clima preenche item a item este checklist. Marcar o que veio; o que vier "emprestado" ou "provisório" entra no parecer com esse rótulo.

| Item | O que deve vir | Uso no Drenagem |
|---|---|---|
| A1 Forma e parâmetros | i = a·TR^b/(t + c)^d, mm/h, t em min, TR em anos, com a, b, c, d e erro do ajuste (médio e máximo); tabela i(t, TR) e P(t, TR) em mm para TR 5, 10, 25, 50, 100 e t de 10 min a 24 h | `idf_potencial`, `idf_tabela`; a intensidade do racional é i = P(Tc)/Tc |
| A2 Faixa de validade | t mínimo e máximo e TR até 2n; aviso se Tc de pequena bacia (< 15 min) cai fora | passar `faixa_TR` e `faixa_t` à calculadora (sempre) |
| A3 Posto | código, instituição, coordenadas, distância e altitude ao perímetro; pluviométrico desagregado ou pluviográfico | citar no parecer; sinais de IDF emprestada (seção 3) |
| A4 Período, n, falhas | anos válidos e excluídos | n para o K do Gumbel e para o TR máximo |
| A5 Distribuição | GEV (κ), Gumbel, método (L-momentos ou momentos), aderência | só citar; o Drenagem não reajusta |
| A6 IC | valor central, inferior e superior por TR (e por duração, com a faixa de desagregação) | Q com o limite superior da IDF (sensibilidade) |
| A7 Desagregação e fonte | fator 1 dia → 24 h (1,13 [DNIT-HIDRO p. 128] ou 1,14 CETESB; Baixio usou 1,10, doc 670:113) e razões h(t)/h24 com `[ID p. N]` | declarar qual; **não aplicar o fator duas vezes** |
| A8 Pfafstetter | parâmetros do posto (α, β, a, b, c): os 98 postos **não estão no corpus**; Salvador (Ondina) é o único posto da Bahia [LOC-PFAFSTETTER-CHUVAS-INTENSAS p. 31] | lacuna; não inventar |
| B1 P(t, TR) com incerteza | tabela com IC de 1 dia e envelope de desagregação | entrada do hietograma (`blocos_alternados`) e do SCS-CN |
| B2 Distribuição temporal | padrão regional observado (lacuna) ou o do DNIT | sem ela: blocos alternados [PMSP-DRENURB-V2 p. 21-22], rotulado |
| B3 ARF | bacia < 25 km²: 1; acima, procedimento B do DNIT, FA = 1 − 0,10·log10(A/25) [DNIT-HIDRO p. 74, 108]; ARF do semiárido: lacuna | só aplicar o que o Clima entregar; A > 25 km² pede-o |
| B4 Chuva antecedente de 5 dias | estatística de P5d e probabilidade de solo úmido por época (módulo do Clima planejado) | o CN e a escolha de ARC são **do Drenagem** (`cn-scs.md` 4) |
| B5 Sazonalidade | meses das máximas anuais | confronto com a época de irrigação (D5) |
| C1 Série de máximas | ano, valor, data, validade | conferência de eventos |
| C2 Estacionariedade | Mann-Kendall e Pettitt, S, p, nível; recomendação sobre fator de mudança do clima | se houver tendência, a IDF histórica não vale: consultoria |
| D1 TR máximo | 2n e aviso | TR acima disso exige consultoria (o aviso do `gumbel` da calculadora repete a regra) |
| D2 Eventos observados | datas, alturas e TR de cada evento pela IDF | verificação independente da vazão de projeto |

Para a chuva de 2 anos e 24 h (P2) do método laminar do NEH (`tc_laminar_neh`): pedir o item B1 com TR 2 e t = 1.440 min.

## 2. Bloco de pedido

```
[DELEGAR: clima]
pedido:      IDF local com incerteza e chuva de projeto por TR e duração para <bacia/perímetro, coordenadas, área, Tc estimado>
entrego:     Tc estimado <valor e faixa, min>; TR de projeto <valores por obra>; método hidrológico previsto <racional/McMath/SCS-CN> e a faixa de durações necessária <min a h>
preciso de:  itens A1 a A7, B1, B3 e D1 do contrato (chuvas-intensas-e-idf, seção 4): i(t, TR) em mm/h para TR 5, 10, 25, 50, 100 e t de 10 min a 24 h com IC 90 % por TR; forma a·TR^b/(t+c)^d com faixa de validade; posto, período, n e distribuição; desagregação com fonte; ARF para A > 25 km²; P2 de 24 h se o laminar do NEH for usado
premissa provisória: IDF do <posto/estudo X> (<fonte>), com acréscimo de <x> % de margem, rotulada "emprestada"
impacto se mudar: Q de pico muda aproximadamente na proporção de i (racional) e mais que proporcionalmente no SCS-CN (P entra elevada ao quadrado acima de Ia); diâmetro e HW dos bueiros podem mudar
urgência:    bloqueia a resposta (projeto básico) | refina a resposta (anteprojeto)
```

Quando o dado é só um valor de P1dia por TR (como no Iuiu): pedir também a regra de passagem de 1 dia para a duração de Tc e a incerteza dela (a forma i = 2,31·P1dia·Tc^-0,55, Tc em min, é regra do projeto, não do corpus).

## 3. Sinais de IDF emprestada ou frágil

Sem critério numérico de distância no corpus; os sinais são para pedir justificativa ao Clima, não para rejeitar sozinhos.

1. A equação não traz faixa de duração nem de TR, ou o Tc cai fora dela (Wilken, SP, vale de 10 a 1.440 min [PMSP-DRENURB-V2 p. 19]).
2. Posto de região climática diferente (litoral, serra, outro estado) para perímetro semiárido: a IDF de Wilken (São Paulo) não serve ao sertão baiano.
3. Mesmos parâmetros em bacias separadas por centenas de km. O DNIT admite escolher o posto de referência cujas precipitações relativas (posto local ÷ referência, por duração) mais se parecem com as do local [DNIT-HIDRO p. 128-129]; mostrar a comparação.
4. Expoente b muito diferente do usual dos ajustes brasileiros do acervo (0,17 a 0,25 em CSB e Wilken): pede conferência.
5. Equação sem posto, ano ou n: "a = 23,7 e b = 0,895" do Baixio de Irecê não traz a equação que os define.
6. **Unidade ou base de tempo ambígua**: mm/min no texto e mm/h nos números (Iuiu, só fecha em mm/h); **altura de chuva usada como intensidade** (CAC Castanhão: P = 23,2 mm em 5 min tratada como mm/h, vazão 12 vezes menor; i = P·60/tc = 278,4 mm/h). Teste: razão Q impressa / Q recalculada = tc/60.
7. Incerteza ausente: série curta (< 20 anos) ou TR maior que 2n.
8. Comparação com a curva média dos 98 postos do DNIT para TR 10 (P em mm: 5 min 15,3; 15 min 32,2; 30 min 44,7; 1 h 59,4; 2 h 74,7; 4 h 91,1; 8 h 107,8; 24 h 139,0) [DNIT-HIDRO p. 130, Tab. 23]: P1h/P24h = 0,43 nessa média. Conferência de ordem de grandeza, não critério. O Clima compara com razões da Bahia e do SGB.
9. Desagregação de 1 dia para 24 h sem fonte (1,10, 1,13 ou 1,14), ou aplicada duas vezes.
10. Projeto que ancora a chuva em P1dia de Gumbel por momentos (amostra infinita) com n pequeno: `gumbel_K(TR, n)` mostra o quanto o quantil subestima (n = 10, TR 25: K = 2,8468 contra 2,04).

## 4. O que o Drenagem devolve ao Clima

Tc de cada bacia e sua faixa; durações pedidas; TR por obra; sensibilidade de Q a ±1 desvio da IDF; se a obra é sensível a duração longa (volume, reservatório) ou curta (pico); a lista de projetos do acervo cuja chuva tem sinal da seção 3 (para o Clima criticar a IDF, não o Drenagem).
