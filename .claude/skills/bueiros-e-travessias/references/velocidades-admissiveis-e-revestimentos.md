# Velocidades admissíveis, tensão admissível e rugosidade por revestimento

Uso aqui: canal de restituição de bueiro (velocidade de saída comparada com o material de jusante) e n do canal natural a jusante. O arquivo é compartilhado por leitura com `canais-de-drenagem-e-macrodrenagem` e `drenagem-de-estradas-e-plataformas`, que dimensionam valeta, canal, sarjeta e descida. Páginas = marcador `<!-- p. N -->` do `_texto` (página física do PDF). A página
impressa do DNIT-DREN é a física menos 4.

Regra de escolha (resumo; o dimensionamento de valeta e canal é de `canais-de-drenagem-e-macrodrenagem` e `drenagem-de-estradas-e-plataformas`): o **DNIT** dá velocidade máxima por revestimento (Tabela 31); o
**HEC-15** recomenda o método da **tensão trativa** (τp ≥ SF·τd) e **não traz tabela de velocidade admissível**
[FHWA-HEC15 p. 30, §2.2.1]. Valores de velocidade equivalente do HEC-15 abaixo são **derivados** (cálculo próprio, ver §3)
e servem só para comparar ordens de grandeza.

## 1. DNIT: Tabela 31, velocidades máximas admissíveis para a água [DNIT-DREN p. 131]

| Cobertura superficial | v máx. (m/s) |
|---|---|
| Grama comum firmemente implantada | 1,50 a 1,80 |
| Tufos de grama com solo exposto | 0,60 a 1,20 |
| Argila | 0,80 a 1,30 |
| Argila coloidal | 1,30 a 1,80 |
| Lodo | 0,35 a 0,85 |
| Areia fina | 0,30 a 0,40 |
| Areia média | 0,35 a 0,45 |
| Cascalho fino | 0,50 a 0,80 |
| Silte | 0,70 a 1,20 |
| Alvenaria de tijolos | 2,50 |
| Concreto de cimento Portland | 4,50 |
| Aglomerados consistentes | 2,00 |
| Revestimento betuminoso | 3,00 a 4,00 |

O manual manda usar essa tabela para escolher o revestimento de valetas de corte e de aterro (`[DNIT-DREN p. 159, §3.1.2]`
e `[p. 166]`), para o comprimento crítico da sarjeta (`[p. 174]`) e para descidas d'água (`[p. 188-189]`), e para comparar
com a velocidade na boca de jusante do bueiro (`[p. 34]`, `[p. 101]`). Os textos citam "tabela 26 do Apêndice B" para
sarjetas e "tabela 31" para valetas: é a mesma Tabela 31 (a Tabela 26 do manual é o n de concreto). Erro de remissão do
manual; usar a Tabela 31.

Limites adicionais do DNIT:
- Valeta ou sarjeta que não pode seguir a declividade natural: escalonar em trechos de no máximo 2 % com pequenas
  barragens espaçadas E = 100 H/(α − β) (α = declividade do terreno, β = declividade desejada, em %), com E ≤ 50 m
  [DNIT-DREN p. 163-164, Fig. 52].
- Altura da lâmina de projeto a menos de 10 % da altura crítica deve ser evitada [DNIT-DREN p. 161-162].
- Bueiro de greide: guardar rigorosamente a cota máxima da água a montante e policiar a velocidade de jusante
  [DNIT-DREN p. 202, §3.9.3].
- Drenos de terra dos casos Iuiu: v ≤ 0,80 m/s (até 1,00 m/s em trechos) [1051:321, 334]; Baixio: V ≤ 4,0 m/s em bueiro
  sob estrada [670:123]. São critérios de projeto, não da norma.

## 2. DAEE-SP: Instrução Técnica DPO nº 11/2017, limites superiores de velocidade [DAEE-IT-DPO11 p. 4, Tabela 6]

| Revestimento | v máx. (m/s) |
|---|---|
| Terra | 1,5 |
| Gabião | 2,5 |
| Pedra argamassada | 3,0 |
| Concreto | 4,0 |

Âmbito: critério para outorga de obra em corpo hídrico de domínio do **Estado de São Paulo**; fora de SP serve de referência
cruzada, não de exigência. Para revestimentos fora da tabela, a instrução manda adotar a bibliografia específica.

## 3. HEC-15 (3ª ed., 2005): tensão trativa, rugosidade e velocidade equivalente

Método: τp ≥ SF·τd, com τd = γ d S₀ (profundidade máxima de escoamento), γ = 9.810 N/m³, SF ≥ 1 (1,0 como padrão)
[FHWA-HEC15 p. 31, eq. 2.4; p. 35, eq. 3.2]. A tensão no fundo é ≈ γ d S₀ para B/d > 4 (típico de canais de beira de
estrada); para B/d < 4 a expressão é conservadora [p. 31]. A tensão média no perímetro é γ R S₀ [p. 30, eq. 2.3].
Relação com a velocidade: Vp = (α/n) R^(1/6) (τp/γ)^0,5, α = 1,0 em SI [p. 32, eq. 2.6; símbolos da equação ilegíveis na
extração, forma conferida pela dedução da continuidade e pelo texto "o expoente é só 1/6"]. Largura de topo/profundidade
< ~20 [p. 34]. Taludes de enrocamento de 1:3 ou mais suaves dispensam verificação do talude [p. 34].

TR de projeto de revestimento permanente de canal de beira de estrada: **5 ou 10 anos**; revestimento de transição (vegetação
em estabelecimento): a vazão média anual, ≈ TR 2 anos [FHWA-HEC15 p. 33, §2.3.1].

### 3.1 Rugosidade de Manning por revestimento [FHWA-HEC15 p. 29, Tabelas 2.1 e 2.2]

| Revestimento | n máx. | n típico | n mín. |
|---|---|---|---|
| Concreto | 0,015 | 0,013 | 0,011 |
| Enrocamento argamassado (grouted riprap) | 0,040 | 0,030 | 0,028 |
| Alvenaria de pedra | 0,042 | 0,032 | 0,030 |
| Solo-cimento | 0,025 | 0,022 | 0,020 |
| Asfalto | 0,018 | 0,016 | 0,016 |
| Solo nu | 0,025 | 0,020 | 0,016 |
| Corte em rocha (liso, uniforme) | 0,045 | 0,035 | 0,025 |
| Tecido de malha aberta (RECP) | 0,028 | 0,025 | 0,022 |
| Manta de controle de erosão (RECP) | 0,045 | 0,035 | 0,028 |
| Manta de reforço de grama (TRM) | 0,036 | 0,030 | 0,024 |

Pedra solta, dependente da profundidade (n em canal trapezoidal 1:3, base 0,6 m, equação de Blodgett-McConaughy):

| Revestimento | y = 0,15 m | y = 0,50 m | y = 1,0 m |
|---|---|---|---|
| Cascalho D50 = 25 mm | 0,040 | 0,033 | 0,031 |
| Cascalho D50 = 50 mm | 0,056 | 0,042 | 0,038 |
| Cobble D50 = 0,10 m | n/d (profundidade relativa < 1,5) | 0,055 | 0,047 |
| Enrocamento D50 = 0,15 m | n/d | 0,069 | 0,056 |
| Enrocamento D50 = 0,30 m | n/d | n/d | 0,080 |

Profundidade relativa (média/D50) < 1,5 exige a eq. 6.2 de Bathurst, dependente da declividade [HEC15 p. 29, nota 2].

### 3.2 Tensão admissível τp [FHWA-HEC15 p. 33, Tabela 2.3]

| Revestimento | τp (N/m²) |
|---|---|
| Solo coesivo (PI = 10): areias argilosas / siltes inorgânicos / areias siltosas | 1,8 a 4,5 / 1,1 a 4,0 / 1,1 a 3,4 |
| Solo coesivo (PI > 20): areia argilosa / silte inorgânico / areia siltosa / argila inorgânica | 4,5 / 4,0 / 3,5 / 6,6 |
| Solo não coesivo (PI < 10): mais fino que areia grossa (D75 < 1,3 mm) | 1,0 |
| solo não coesivo: cascalho fino (D75 = 7,5 mm) | 5,6 |
| solo não coesivo: cascalho (D75 = 15 mm) | 11 |
| Cascalho de cobertura (gravel mulch) D50 = 25 mm / 50 mm | 19 / 38 |
| Enrocamento D50 = 0,15 m / 0,30 m | 113 / 227 |

Vegetação e RECP não têm τp independente do solo (dependem de quanto protegem o solo; HEC-15 caps. 4 e 5). Gabião (colchão
Reno): τp depende do tamanho da pedra e da espessura (§7.2, não lido aqui). Enrocamento: τp pela eq. 6.7 com parâmetro de
Shields F* = 0,047 para Re ≤ 4×10⁴ e F* = 0,15 e SF = 1,5 para Re ≥ 2×10⁵, com interpolação linear entre os dois
[FHWA-HEC15 p. 98, Tabela 6.1].

### 3.3 Velocidade equivalente (derivada, não é valor do manual)

Cálculo próprio com a fórmula do §3: Vp = (1/n)(τp/9.810)^0,5 R^(1/6), tomando R ≈ profundidade. Servem para ver a ordem
de grandeza e **não substituem** a verificação por τ.

| Revestimento | τp (N/m²) | n adotado | R (m) | Vp equivalente (m/s) |
|---|---|---|---|---|
| Argila inorgânica PI > 20 | 6,6 | 0,020 | 0,30 | 1,06 |
| Cascalho fino (D75 = 7,5 mm) | 5,6 | 0,020 | 0,30 | 0,98 |
| Cascalho (D75 = 15 mm) | 11 | 0,020 | 0,30 | 1,37 |
| Cascalho de cobertura D50 = 25 mm | 19 | 0,033 | 0,50 | 1,19 |
| Enrocamento D50 = 0,15 m | 113 | 0,069 | 0,50 | 1,39 |
| Enrocamento D50 = 0,30 m | 227 | 0,080 | 1,0 | 1,90 |

Leitura: os valores de tensão do HEC-15 para solo e pedra pequena são **mais restritivos** que as velocidades do DNIT ou do
DAEE (ex.: "terra" 1,5 m/s no DAEE; "enrocamento" 3 m/s na tabela da calculadora). Em projeto básico de valeta em solo,
verificar também τ.

## 4. Rugosidade de Manning para canais e valetas: DNIT e DAEE

| Revestimento | n | Fonte |
|---|---|---|
| Concreto, acabamento a colher / desempenadeira / sem acabamento | 0,011-0,012 / 0,013-0,015 / 0,014-0,017 | [DNIT-DREN p. 133, Tabela 34] |
| Concreto sobre escavação em rocha boa / irregular | 0,017-0,020 / 0,022-0,027 | [DNIT-DREN p. 133] |
| Pedra aparelhada em argamassa / irregular em argamassa / alvenaria rebocada / rejuntada | 0,015-0,017 / 0,017-0,020 / 0,016-0,020 / 0,020-0,025 | [DNIT-DREN p. 133] |
| Pedra seca (rip-rap) com fundo em cascalho | 0,023-0,033 | [DNIT-DREN p. 133] |
| Terra, reto e uniforme, limpo recém-concluído / após intempérie | 0,016-0,018 / 0,018-0,022 | [DNIT-DREN p. 134] |
| Terra, saibro uniforme / com grama curta / com pedregulho | 0,022-0,025 / 0,022-0,027 / 0,022-0,025 | [DNIT-DREN p. 134] |
| Terra sinuosa, sem vegetação / com grama / vegetação densa | 0,023-0,025 / 0,026-0,030 / 0,030-0,035 | [DNIT-DREN p. 134] |
| Asfalto liso / áspero | 0,013 / 0,016 | [DNIT-DREN p. 133] |
| Terra com grama (DAEE) / gabião / pedra argamassada / aço corrugado / concreto | 0,035 / 0,028 / 0,025 / 0,024 / 0,018 | [DAEE-IT-DPO11 p. 4, Tabela 5] |
| Casos do acervo: drenos de terra (Iuiu) / concreto armado, alvenaria de pedra, grama (CSB) | 0,03 / 0,015, 0,020, 0,024 | [1051:321]; [1341:73] |

(Os dois números por linha da Tabela 34 do DNIT correspondem às duas colunas impressas, sem rótulo na extração nem na
imagem da página; tratar como faixa mínimo-máximo.)

A Tabela 34 traz também faixas para cursos d'água naturais (Tabelas 32 e 33, p. 131-132), úteis para o TW do canal
natural a jusante do bueiro.

## 5. Sarjeta pavimentada

Movida para `drenagem-de-estradas-e-plataformas` (n do HEC-22 Tab. 5.3 e Izzard: `bueiros.sarjeta_triangular_izzard`).

## 6. Tabela de velocidade da calculadora x fontes (estado após a v0.2.0)

`dissipador_necessario` e `dimensionar_bueiro` usam por padrão a **Tabela 31 do DNIT** (`LIMITE_VELOCIDADE_DNIT`, faixa mín-máx, critério
"min" = conservador) [DNIT-DREN p. 131]. A tabela antiga (tipo Fortier-Scobey, sem página) ficou em
`LIMITE_VELOCIDADE_MATERIAL_LEGADO` (até 2x mais permissiva: areia fina 0,75; cascalho fino 1,5; concreto 6,0 x 4,5 m/s) e só entra com
`fonte="legado"` ou para cascalho grosso e enrocamento (sem linha na Tab. 31; aviso). **HEC-15 não traz tabela de velocidade.**
Alternativa com fonte: EM 1110-2-1601 Tab. 2-5 p. 25 (areia fina 2,0 fps = 0,61 m/s) contra DNIT 0,30-0,40 m/s;
`canais_drenagem.velocidade_admissivel(fonte=...)` obriga a escolher (`DIVERGENCIAS.md`). No parecer: declarar a fonte e o critério
(min ou max) do limite e reproduzir o aviso de material sem equivalente.
