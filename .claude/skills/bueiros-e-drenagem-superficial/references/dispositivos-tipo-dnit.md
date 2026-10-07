# Dispositivos-tipo do DNIT: códigos, uso e especificações de serviço

**Atenção ao número da publicação.** O pedido original chamou o Álbum de "IPR-725". O PDF do corpus (`DNIT-ALBUM`) é a
**Publicação IPR-736, "Álbum de Projetos-Tipo de Dispositivos de Drenagem", 5ª edição, Rio de Janeiro, 2018** (capa e
página de rosto, PDF p. 1, 5-6); as ES do DNIT (019, 022, 023, 024, 025, 026) citam "Publicação IPR 736". O catálogo
(`_catalogo.yaml`) traz `vigencia: 2006`; a edição do arquivo é de **2018** (a URL de origem indica versão "atualizada com
emendas, reduzida, 2026"). O Manual de Drenagem de Rodovias é o **IPR-724** (2ª ed., 2006).

**Leitura do Álbum.** O PDF (227 páginas, 27,5 MB) é **escaneado, sem camada de texto** (`pendente_ocr`; no `_texto` só há as
páginas 1 a 6). Os códigos abaixo vêm do **Sumário** (PDF p. 9 a 15), lido na imagem das páginas. Os desenhos (formas,
armaduras, quantidades) **não estão transcritos**: para detalhe, abrir o PDF na folha indicada pelo número do desenho e
dizer "(página do desenho a confirmar)". O Álbum "é um documento de caráter orientador e não normativo; sua utilização não
é compulsória", cabendo ao projetista o dimensionamento que confirme a adequação [DNIT-ALBUM, Introdução, PDF p. 23]. Já as
ES mandam usar os dispositivos padronizados "na ausência de projeto específico" [DNIT-ES023 p. 3; ES025 p. 3; ES026 p. 3].
Na prática: dispositivo-tipo é o padrão de custo e de detalhe; a **hidráulica** (capacidade, velocidade, HW) é do projeto.

## 1. Bueiros de transposição de talvegue (Cap. 6) e galerias pré-moldadas (Cap. 7)

| Código e desenho (Sumário) | Dispositivo | Uso hidráulico no projeto |
|---|---|---|
| **BSTC** (6.3 a 6.5) | Bueiro Simples Tubular de Concreto, bocas normais e esconsas (I a III) | uma linha de tubo; DN 0,60 a 1,50 m na tabela de capacidade crítica do DNIT [DNIT-DREN p. 55, Tabela 1] |
| **BDTC** (6.6, 6.7) | Bueiro Duplo Tubular de Concreto (I, II) | duas linhas; Q crítica 3,07 m³/s (DN 1,00), 4,84 (1,20), 8,45 (1,50) [DNIT-DREN p. 55] |
| **BTTC** (6.8, 6.9) | Bueiro Triplo Tubular de Concreto (I, II) | três linhas; 4,60 / 7,26 / 12,67 m³/s (DN 1,00 / 1,20 / 1,50) [DNIT-DREN p. 55] |
| **BSCC, BDCC, BTCC** (6.11 a 6.31) | Bueiro Simples, Duplo e Triplo **Celular** de Concreto: corpo (formas e armaduras) 1,50 x 1,50 a 3,00 x 3,00 m; bocas normais e esconsas (formas) | seção quadrada ou retangular; a tabela de capacidade crítica cobre 1,0 x 1,0 a 3,0 x 3,0 m [DNIT-DREN p. 56, Tabela 2] |
| (6.32 a 6.39) | Armaduras das vigas de topo, esconsidade 0°/15° e 30°/45°, bueiros celulares simples, duplos e triplos | detalhe estrutural; esconsidade: ver §3 |
| (6.40 a 6.44) | Armaduras das cabeceiras (1,50, 2,00, 2,50, 3,00) e resumo | idem |
| (6.1, 6.2) | Berços para assentamento de bueiros; tubos de concreto armado | declividade > 4 % exige berço com dentes [DNIT-ES023 p. 5, Nota 3] |
| **CCT** (6.10) | Caixa Coletora de Talvegue | boca de montante abaixo do terreno: troca a boca por caixa [DNIT-DREN p. 32] |
| (6.25) | Bueiros celulares: notas e detalhes complementares | |
| (6.45) | Bueiros metálicos executados sem interrupção do tráfego | ver ES 024 e ES 096 (§2) |
| Cap. 7, 7.1 a 7.78 | **Galerias celulares pré-moldadas (aduelas)**: seções internas 1,50 x 1,50; 2,00 x 2,00; 2,50 x 2,50; 3,00 x 3,00 em tipos **I a VII** (duas folhas por tipo); seções "canal" 1,50 x 1,50 a 3,00 x 2,00; 7.77 armadura transversal; 7.78 mísulas | seção de galeria sob aterro alto ou onde o aterro não comporta bueiro tubular; capacidade pela mesma hidráulica do celular |
| Cap. 8, 8.1 a 8.4 | Bueiros de concreto **tipo minitúnel** sem interrupção do tráfego: 0,80 x 1,40; 1,00 x 1,48 e 1,20 x 1,65; 1,60 x 1,84 e 2,00 x 2,00; 2,20 x 2,60 e 2,20 x 2,70 | travessia sob estrada em operação (método não destrutivo) [ver DNIT-ES096] |

Nomenclatura (DNIT-DREN): B = bueiro; S/D/T = simples, duplo, triplo (**número de linhas**); T/C = tubular ou celular; C = concreto
(os metálicos têm outra sigla); **o código de linha é "BSTC", "BDTC", "BTTC", "BSCC", "BDCC", "BTCC"** [DNIT-DREN p. 55-56]. A
sigla **BQCC** (quádruplo celular) aparece nos casos Baixio de Irecê e Xingó, **sem desenho-tipo correspondente no Sumário do
Álbum** (só simples, duplo e triplo). Quádruplo é solução de projeto, não do Álbum. O DNIT desaconselha mais de 3 linhas por
alagar faixa ampla [DNIT-DREN p. 32].

Capacidade crítica (energia específica = altura, "como canal"), tubular e celular: tabelas 1 e 2 do DNIT. Celular: Vc = 2,56 H^0,5,
Q = (2/3) H L Vc ≈ **1,705 L H^1,5** (simples; duplo e triplo multiplicam). O texto do manual traz o coeficiente **1,638**
[DNIT-DREN p. 54-55] mas a própria Tabela 2 só fecha com 1,705 (ex.: 2,0 x 2,0 m: 9,64 m³/s; 1,638 dá 9,27, -4 %); ver
SKILL.md §6 (armadilha 8). Usar a tabela, não o coeficiente impresso.

## 2. Especificações de serviço (ES) do DNIT no corpus

| ES | Título e ano | Cobre | Itens-chave conferidos |
|---|---|---|---|
| **023** | DNIT 023/2024-ES, Bueiros tubulares de concreto (substitui 023/2006) | execução de **bueiros de greide e de grota** tubulares | NBR 8890 para tubos; fck mín. 20 MPa no berço; vala com folga lateral mín. 0,40 m por lado; **linha dupla ou tripla com folga de 0,30 m entre tubos**; escoramento obrigatório acima de 1,25 m (p. 2); junta rígida 1:3 ou elástica (p. 3-5); berço com dentes se declividade > 4 % (p. 5) [ES023 p. 2-5] |
| **024** | DNIT 024/2025-ES, Bueiros metálicos sem interrupção do tráfego | emboque direto, aba metálica, escudo, enfilagem | emboque direto, aba metálica, escudo frontal e enfilagem (definições em [ES024 p. 2]) |
| **025** | DNIT 025/2025-ES, Bueiros celulares de concreto (substitui 025/2004) | moldados in loco e pré-moldados (aduelas) | vala com folga lateral mín. **0,50 m** por lado para fôrma do berço; aterro compactado sobre as células [ES025 p. 3-5] |
| **026** | DNIT 026/2025-ES, Caixas coletoras, caixas de ligação e passagem e **bocas de bueiros** | bocas (montante e jusante), caixas | seguir o Álbum IPR-736 [ES026 p. 2]; folga lateral das caixas [ES026 p. 3-4] (página a confirmar) |
| **019** | DNIT 019/2023-ES, Transposição de sarjetas e valetas | transposição com laje de concreto armado | indicada onde não há profundidade para bueiro tubular com recobrimento [ES019 p. 2] |
| **022** | DNIT 022/2023-ES, Dissipadores de energia | dissipadores moldados in loco, com dentes, em degraus | caixa de pedra tampada com concreto fck 20 MPa, 10 cm [ES022 p. 4] (dimensionamento: `vertedouros-e-dissipadores`) |
| **030** | DNIT 030/2004-ES, Dispositivos de drenagem pluvial **urbana** | galerias, bocas de lobo, poços de visita | urbano; fck mínimo por dispositivo em [ES030 p. 3-4] (página a confirmar) |
| **096** | DNIT 096/2006-ES, Bueiros de concreto tipo minitúnel sem interrupção do tráfego | processo não destrutivo | objeto e processo [ES096 p. 1-3] |
| 015, 016, 017 | Drenos subterrâneos, sub-superficiais, sub-horizontais | drenos profundos | é de `drenagem-subsuperficial` |
| 027, 028, 029, 086 | Demolição, limpeza e desobstrução, restauração, recuperação de dispositivos | manutenção | fora do escopo de projeto |

**Referenciadas pelo manual mas ausentes do corpus:** DNIT **018**/2004 (sarjetas e valetas), DNIT **021**/2004 (descidas
d'água) e a ES de bocas e caixas anteriores à 026/2025. O IPR-724 manda segui-las no revestimento e no detalhe [DNIT-DREN p. 160,
166, 188]. Registrar como lacuna (SKILL.md §9).

NBR 8890 (tubo de concreto de seção circular para água pluvial e esgoto sanitário; substitui as NBR 9793 e 9794 citadas
no IPR-724) é **norma não aberta**: citar `[DNIT-ES023 p. 3]` e o código, sem transcrever; classes de tubo e carga de teste
são do fabricante e da Estruturas (`NAO_ABERTOS.md`).

## 3. Demais dispositivos de drenagem superficial (Cap. 1) e relação com o dimensionamento

| Código (desenhos do Sumário) | Dispositivo | Dimensionamento no manual |
|---|---|---|
| **VPC-01 a 04** | Valetas de proteção de **corte** | Racional + Manning, 2 a 3 m da crista [DNIT-DREN p. 158-161] |
| **VPA-01 a 04** | Valetas de proteção de **aterro** | idem, 2 a 3 m do pé [DNIT-DREN p. 165-166] |
| **STC-01 a 08** | Sarjetas triangulares de concreto (I e II) | comprimento crítico, TR 10 e 5 min [DNIT-DREN p. 170-173] |
| **STG-01 a 04** | Sarjetas triangulares de grama | idem, velocidade da Tabela 31 |
| **SZC-01, 02; SZG-01, 02** | Sarjetas trapezoidais de concreto e de grama | usadas quando a triangular de L1 = 2,0 m não basta [DNIT-DREN p. 167] |
| **SCC-01 a 04** | Sarjetas de canteiro central de concreto | valeta de canteiro central [DNIT-DREN p. 184-185] |
| (1.8, 1.9) | Transposição de segmentos de sarjetas (I, II) | ver ES 019 |
| **MFC-01 a 08** | Meios-fios de concreto (I, II) | |
| **EDA-01 a 04** | Entradas para descidas d'água | |
| **DAR-01 a 04** | Descidas d'água de aterros, tipo **rápido** (I a III) | Q = 2,07 L^0,9 H^1,6 e velocidade no pé [DNIT-DREN p. 188-189] |
| **DCD** | Descidas d'água de cortes em degraus | |
| **DAD** | Descidas d'água de aterros em degraus | |
| **DES** | Dissipadores de energia (I): saídas de sarjetas e valetas | `vertedouros-e-dissipadores` |
| **DEB** | Dissipadores (II): saídas de **bueiros tubulares** e descidas de aterros | idem |
| **DED** | Dissipadores (III): descidas tipo rápida | idem |
| **CCS-01 / 02** | Caixa coletora de sarjeta com grelha de concreto / de ferro | bueiro de greide [DNIT-DREN p. 199-202] |
| Cap. 9, 9.1 a 9.5 | Dispositivos **lineares** (grelhas): características, dimensionamento hidráulico, classes de carga, detalhes | capítulo novo da 5ª ed. |

Esconsidade: o bueiro é **esconso** se o eixo faz ângulo diferente de zero com a normal ao eixo da rodovia [DNIT-DREN p. 33];
os desenhos do Álbum cobrem 0°, 15°, 30° e 45° (Sumário 6.32 a 6.39). Efeito hidráulico: o esconso da **entrada** reduz pouco a
capacidade em controle de entrada (caixa 1,83 x 1,83 m: a 45° a vazão cai de 6,80 para 6,29 m³/s com HW 1,83 m, ≈ -7 %), já
embutido nos charts 11 e 12; evitar esconso em entrada afunilada e em **barris múltiplos**, onde as paredes internas
favorecem assoreamento e vazão desigual entre os barris [HDS5 p. 149-150, §5.4.2 e Tabela 5.2]. A calculadora não corrige
esconsidade: declarar a redução e usar a linha de esconso da Tabela A.1 (charts 11 e 12) só por HY-8.

Capítulos 2 a 5 do Álbum (drenagem subterrânea DPS, DPR; subsuperficial; taludes DSH; pluvial urbana: bocas de lobo, caixas CLP,
poços de visita PV): fora do escopo desta skill (`drenagem-subsuperficial`; urbano: ES 030).

## 4. Como o agente usa este arquivo

1. Escolher o dispositivo-tipo **depois** do dimensionamento hidráulico (Q, HW, V), não antes: os tipos têm seção interna
   fixa (1,00 a 3,00 m) e a hidráulica diz quantas células.
2. Citar o código do Sumário e a ES; dizer "desenho: PDF do Álbum, folha a confirmar".
3. Quantitativos para o Orçamento (V6): número de células, seção interna, comprimento, tipo de boca (normal ou esconsa), tipo de berço,
   dissipador (DES, DEB, DED), código do dispositivo e a ES de execução.
4. Estruturas: classe do tubo (NBR 8890), recobrimento, carga móvel, armadura: delegar (`[DELEGAR: estruturas]`).
