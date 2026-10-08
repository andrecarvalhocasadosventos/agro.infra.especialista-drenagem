# Fichas por fonte: FHWA (HDS-5, HEC-12/13/22, HDS-3), USACE (EM 1601, EM 2902) e WSDOT

Convenção: `[ID p. N]` = página física do PDF; **conf.** = lido no `_texto` na F6; **mapa** = vem do MAPA (F3 ou H12-H15), não relido.
Licença: domínio público (FHWA, USACE); WSDOT: manual estadual aberto, **prática, não norma brasileira**. Unidades: pés, cfs e psi, salvo HDS-5 e
HEC-22 (duais). Converter e citar o ábaco na unidade original (núcleo, seção 1).

## FHWA-HDS5, Hydraulic Design of Highway Culverts (corpus do Hidráulico)

**3ª ed. abr/2012** (FHWA-HIF-12-026), 323 p., dual (SI e US). É a primária de bueiro. Precisão declarada **±10 % em HW** (entrada) ou na perda (saída), p. 196, conf.

| O que pede / traz | Página | Status |
|---|---|---|
| Cap. 2: dados de sítio e **HW admissível**; HW/D definido pela agência, **comumente 1,0 a 1,5**; checar a cheia de 100 anos contra o aumento de nível regulatório | 63-82; 72 | conf. (72) |
| Cap. 3: controle de entrada e de saída; perdas He + Hf + Ho; HWo = TW + HL − L·S; galgamento Q = Cd·L·HW^1,5; **vale o maior HW** | 83-126 (perdas p. 91; nomogramas p. 102-107) | conf. (91, 106); resto mapa |
| Cap. 5: **baixa carga (irrigação)** p. 137-139; curvas, junções, sifões, escavação, múltiplos barris, broken-back, dissipadores | 137-162 | mapa |
| **Tab. A.1** constantes K, M, c, Y de entrada (círculo, caixa, entrada cônica); **Tab. A.2** arco e elipse; A.3 a A.6 | 190-201 (Tab. A.1 p. 197) | conf. (197); A.2 p. 198 via `DIVERGENCIAS.md` |
| **Tab. B.1** n de Manning de barril (concreto 0,010-0,011; anelar 5×1 0,025-0,026; 6×2 0,033-0,035); nomogramas usam 0,012 e 0,024 | 203-208 (204 conf.) | conf. (204); valores mapa H13 |
| **Tab. C.2 Ke** (concreto, CMP, caixa); **caixa com muros de ala paralelos e aresta viva = 0,7**; tubo de concreto com muro de testa e aresta viva 0,5, com bolsa 0,2 | 216 | conf. |
| Design Guidelines (DG1 nomogramas; DG2 sem gráficos; DG3 entrada cônica e broken-back; DG4 roteamento); gabarito de V de saída 6,47 m/s com n 0,012 e 6,07 com n 0,013 | 271-323 (p. 280) | índice conf.; p. 280 via núcleo |

Armadilhas próprias:
- **Constante Y da submersa de arco/elipse projetante**: Tab. A.2 (p. 198) dá Y = 0,57, o exemplo A.3.1 (p. 191) usa 0,53. O código usa 0,57 e trava o valor no teste `test_arco_projetante_usa_Y_da_tabela_A2_nao_do_exemplo`.
- **Ke das alas paralelas**: 0,7 (Tab. C.2 p. 216 e HEC-13 Tab. 1 p. 100) × 0,2 (IPR-724 Tab. 30 p. 130). Ke só entra no controle de **saída**; o controle de entrada não depende dele.
- **Nomogramas só em imagem** (Apêndice C e Design Guidelines); nunca "completar" valor por memória. Em baixa carga, o critério governante no perímetro irrigado é o remanso admissível no canal, não HW/D (H13 do Hidráulico, divergência 37).
- Transição 3,5 < Ku·Q/(A·D^0,5) < 4,0: o HDS-5 usa curva tangente; o código interpola linearmente (`DIVERGENCIAS.md`).

## FHWA-HEC22, Urban Drainage Design Manual (corpus do Hidráulico)

**4ª ed.** (catálogo 2024), 313 p.; **física = impressa + 32** (Tab. 5.3 impressa 47, física 79). Absorveu o HEC-12.

| O que traz | Página | Status |
|---|---|---|
| Racional "para áreas menores que **200 ac (80 ha)**" (remete ao HDS-2) | 57 | conf. |
| Sarjeta de Izzard Q = (Ku/n)·Sx^1,67·S^0,5·T^2,67, **Ku = 0,56 (US) e 0,376 (SI)**; **Tab. 5.3** n de sarjeta e pavimento | 79 | conf. |
| Bocas de lobo em greide e em sag, localização e espaçamento | 113-158 | mapa |
| Condutos pluviais (Manning pleno, Ko = 0,4 em poço, V mínima 3 ft/s) | 169-210 | mapa |
| Exemplos com "tc mínimo de 5 min" e TR 0,1 AEP (10 anos) como critério do exemplo | 149-152, 198-202 | conf. |

Uso no pacote: sarjeta e boca de lobo de **estrada** (não rede urbana, fora de escopo). Tc mínimo de 5 min é critério de exemplo do HEC-22, não regra geral.

## FHWA-HEC12, Drainage of Highway Pavements (corpus próprio)

1984 (FHWA-TS-84-202); **arquivada**, marca d'água "Archival/Superseded" (conteúdo absorvido pelo HEC-22); 155 p.; **impressa = física − 17**. Útil como
conferência (30 exemplos resolvidos; gabaritos de sarjeta).

- Greide longitudinal mínimo de sarjeta 0,3 % (0,2 % em terreno muito plano) p. 19 (seção 2.1; valor mapa); Tab. 1 declividades transversais p. 21 [mapa].
- Racional e C (Tab. 2 p. 29), Tc por onda cinemática (eq. 2 em imagem, K = 56 US) p. 31, **sarjeta triangular Eq. 4 com K = 0,56** p. 39 (conf.; nomograma Chart 3 p. 40), composta p. 41-43, circular p. 48-49, bocas p. 53+, valeta de canteiro Charts 16-17 p. 111-112 [mapa].
- Exemplos úteis para estrada de serviço: 1, 2, 4, 5, 6, 8, 23-25 (p. 32, 34, 41-43, 46, 49, 110-113). **Gabaritos**: Ex. 4 (T = 8 ft, Sx = 0,025, S = 0,01, n = 0,015 → Q = 2,0 ft³/s; recálculo 2,04) e Ex. 5 composta (Q = 3,0; reproduz 3,06) [mapa, recalculados no MAPA G3 nº 4 e 7].
- Armadilha: equação 2 (Tc) ilegível no `_texto`; reconstrução dá 21 min contra 20 min impresso (só ordem de grandeza). Leitura de nomograma: tolerância 5 %.

## FHWA-HEC13, Hydraulic Design of Improved Inlets for Culverts (corpus próprio)

Circular nº 13, ago/1972; **arquivada** ("superseded by HDS-5 3rd ed. 2012"), 185 p. Entradas melhoradas (biselada, cônica lateral e de fundo, anel biselado) p. 33-52;
19 charts (1-19) p. 79-97; **Tab. 1 Ke p. 100 (conf.; igual à Tab. C.2 do HDS-5)**; exemplos 1-5 p. 111-152 (caixa 7×6 ft; tubo D = 7 ft; CMP 48 in). Só unidades inglesas. Usar como
**conferência cruzada de Ke e de entrada melhorada**, não como método (o método é o HDS-5).

## FHWA-HDS3, Design Charts for Open-Channel Flow (corpus próprio)

1961 (FHWA-EPD-86-102); arquivada, sem substituta direta; 116 p.; **impressa + 8 = física**. 83 charts em unidades inglesas; **Chart 55 (relações parciais Q/Qfull, V/Vfull por d/D) p. 76 (conf.)**; tubo circular Charts 35-54 (p. ~45-72); 25 exemplos
(10-17 tubo circular, p. 53-55); **Tab. 1 n de Manning p. 108 (conf.)**, Tab. 2-3 velocidades permissíveis p. 109 [mapa]. Charts-base com n = 0,015 no circular; escalas auxiliares 0,012 e 0,024. Gabaritos 3 a 8 do MAPA G2 (Ex. 10, 12, 14-17), tolerância 1 %; leitura de gráfico dá até 1,3 %.
Armadilha: sem tubo parcialmente cheio em SI; o código usa geometria exata, não "0,60·D²" (`tubo_parcialmente_cheio`).

## USACE EM 1110-2-1601, Hydraulic Design of Flood Control Channels (corpus próprio)

1991, **Change 1 de 30/06/1994** (cópia com marcação "1 Jul 91" na p. 25); 183 p.; unidades US; host oficial devolve 403 a robô (`PENDENTES_DOWNLOAD_MANUAL.md`). Duas colunas intercaladas.

- **Tab. 2-5** velocidades médias máximas permissíveis (areia fina 2,0 fps; argila 6,0; grama de bermuda em silte-areia 6,0; Kentucky blue 5,0; rocha ruim): **guia, não limite**; "valores devem vir de experiência de campo ou ensaio" p. 25 (conf.). Com V ou τ acima do permissível, pavimentar ou revestir a margem.
- Cap. 3 rip-rap p. 26-39: graduação (Tab. 3-1 p. 28); n de rip-rap de Strickler Eq. 3-2 p. 29; D30 Eq. 3-3 p. 30-31; pé e espessura Tab. 3-2 p. 35-36 [mapa]. **Dimensionar dissipador de saída de bueiro é da Hidráulica (D3)**; aqui só proteção de canal.
- Cap. 5 (Change 1) previsão de n p. 47-62; Tab. 2-1 k equivalente p. 12; Apêndice B (placas) p. 100-122; Apêndice H exemplos de pedra p. 178-179 [mapa].
- Lacunas: sem tabela de gramíneas por retardância; concreto e gabião só como k equivalente.

## USACE EM 1110-2-2902, Conduits, Culverts, and Pipes (corpus próprio; **edição antiga**)

**31/out/1997, Change 1 de 31/mar/1998** (catálogo diz 1998; cabeçalho da p. 1 imprime "2909" por erro); **substituída pela edição de 31/12/2020**. 87 p. Só carga e estrutura: **não traz hidráulica de bueiro**.

- **Tab. 3-1 fator de berço Bf em vala: comum 1,5; primeira classe 1,9; berço de concreto 2,5** p. 27 (conf.); Tab. 3-2 constantes χ e η p. 27; Eq. 3-2 D0,01 = Hf·W_T/(Si·Bf), Hf = 1,3 p. 25 [mapa].
- Apêndice B exemplos: Cd = 1,274 e We1 = 55.483 N/m (Kμ' = 0,15, H = 2,44 m, Bd = 1,52 m, γ = 18.850 N/m³) p. 66-68, conferidos pelo MAPA G2 nº 2.
- **Armadilha**: o D-load do exemplo das p. 71-72 usa Bf = 6,098, que não reproduz D0,01 = 57 N/m/mm (exigiria Bf ≈ 3,33); **Eq. 3-1 truncada**. Não usar como gabarito sem conferir na imagem (`tubos.d_load_em2902`).
- Concorda com a Tab. 4.1 do ABTC (El Debs 2003) onde há correspondência (1,5; 1,9; 2,5) e nos χ e η.

## WSDOT Hydraulics Manual M 23-03.12 (corpus próprio)

Catálogo "2025"; **rodapé de todas as páginas diz "April 2026"** (registrar a divergência). 325 p.; PDF = impressa + 14 (cap. 1), + 36 (cap. 2), + 86 (cap. 4), + 100 (cap. 5). **Prática estadual dos EUA, não norma**; não usar para impor critério ao projeto brasileiro, só como contraste.

- Racional com **Tc mínimo de 5 min** p. 46-47 (conf.) e p. 102 (cap. 5, pavimento); inlet de ranhura proibido p. 103; **TR × espaçamento permitido** Tab. 5-1 p. 104-105 (sag com TR 50) [mapa]; valeta lateral com **TR 10, folga 0,5 ft, talude ≤ 2H:1V, grama só se < 6 % e < 5 fps** p. 109 [mapa]; coletores n = 0,013 p. 128; subdreno ≥ 6 in, limpeza a cada 150 ft p. 128-129 [mapa].
- Equações do cap. 2 e 5 estão em imagem; **sem exemplo numérico extraído** (sem gabarito).
