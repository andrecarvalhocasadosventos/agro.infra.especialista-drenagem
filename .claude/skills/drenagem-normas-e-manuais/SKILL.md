---
name: drenagem-normas-e-manuais
description: >
  Guia das fontes do Especialista em Drenagem: edição e vigência, licença, o que cada norma ou manual
  pede, páginas-chave, armadilhas de leitura e divergências. Cobre DNIT IPR-724, IPR-715, IPR-736 (Álbum 2018), IPR-726,
  ES 018/020/021, DER/PR ES-DR, HDS-5, HEC-12/13/22, HDS-3, NEH 630 cap. 15, 624 e 650, DAEE, Pfafstetter (só localizar;
  IDF é do Clima), ABTC e NBR 8890 (fechada: citar, não transcrever), ILRI 16 e 56, EM 1601 e 2902, WSDOT. Use quando: "o
  que o IPR-724 exige", "onde está a tabela de Ke", "qual edição do HDS-5", "está vigente", "qual a página", "a NBR
  8890 está no corpus", "as fontes divergem", "o DAEE vale fora de SP". Não use para: fórmula de disciplina (use
  hidrologia-de-projeto-para-drenagem, bueiros-e-travessias, drenagem-de-estradas-e-plataformas,
  canais-de-drenagem-e-macrodrenagem, drenagem-subsuperficial); pedido amplo (use drenagem-fundamentos); caso de projeto
  (use drenagem-casos-de-referencia); IDF (Clima); fontes de canal, adutora, bomba, vertedouro e irrigação (normas-e-manuais do Hidráulico); preço (engenheiro-de-custos).
---

# Normas e manuais de drenagem: guia das fontes

Esta skill **não repete regra de disciplina**. Diz onde a regra está, em que edição, com que licença, em que página, com que
armadilha e a quem se aplica. A regra que cruza fontes (qual valor adotar quando duas divergem) mora na skill da disciplina;
aqui só se registra **que** divergem e **onde**. Páginas `[ID p. N]` são **físicas do PDF** (marcador `<!-- p. N -->`).
Nos arquivos de `references/`, **conf.** = conferido no `_texto` na F6 e **mapa** = vem de `referencias/MAPA_DE_CONHECIMENTO.md`
(corpus próprio) ou do mapa do Hidráulico H12-H15 e não foi relido.

## 1. Mapa da skill

| Pergunta | Onde |
|---|---|
| IPR-724, 715, 736, 726; ES 018/020/021; DER/PR ES-DR | seção 4 e `references/fichas-dnit-der.md` |
| HDS-5, HEC-12/13/22, HDS-3, EM 1601, EM 2902, WSDOT | seção 4 e `references/fichas-fhwa-usace-wsdot.md` |
| NEH 630 cap. 15, 624, EFH14; DAEE; Pfafstetter; ABTC e NBR 8890; ILRI 16 e 56 | seção 4 e `references/fichas-nrcs-ilri-daee-pfafstetter-abtc.md` |
| Edição, vigência, licença, paginação, erro de catálogo, **lista completa de divergências** | seções 5 a 8 e `references/edicoes-paginacao-e-divergencias.md` |
| Qual função da calculadora usa a fonte | seção 9 |

## 2. Fluxo de uso (cinco passos)

1. **Tema → fonte**: ache a fonte na tabela da seção 4; use a primária e, se houver, uma de conferência (HEC-12/13 conferem o HDS-5 e o HEC-22).
2. **Estado da fonte**: edição, vigência e licença (seção 5). Em que corpus está (próprio ou do Hidráulico) e se tem `_texto` ou só `_ocr`.
3. **Armadilha**: a tabela está em texto ou só em imagem? Qual o deslocamento de página? A extração embaralhou a fórmula?
4. **Unidade**: a fonte é imperial (HDS-3, HEC-12/13, EM 1601 e 2902)? Cite o ábaco na unidade original e entregue o resultado em SI (núcleo, seção 1).
5. **Divergência**: o valor consta na seção 8? Se sim, registre a fonte adotada e a preterida, com página, e deixe a decisão à skill da disciplina (ou à F7).

## 3. Escopo e fronteiras

- **Corpus (D1)**: IPR-724, 715 e 736 (versão sem OCR), HDS-5, HEC-14/15/22, NEH 630/624/650, EFH14, DAEE, ILRI-16, FAO-IDP62 e as ES 015-017/019/022-030 estão no corpus do **Hidráulico**
  (`../Especialista Hidraulica/referencias/`): **cite pelos IDs dele** (`DNIT-DREN`, `DNIT-HIDRO`, `DNIT-ALBUM`, `FHWA-HDS5`, `DAEE-IT-DPO11`...). IPR-726, ES 018/020/021, DER/PR ES-DR, HEC-11/12/13, HDS-3,
  EM 1601/2902, WSDOT, Pfafstetter, ABTC, ILRI-56, Álbum com OCR e NEH 630-15 (ed. 2010) estão no corpus **próprio**.
- **Pfafstetter**: o Drenagem **localiza e cita**; não ajusta nem entrega IDF. A IDF é do Clima (`chuvas-intensas-e-idf`, `[DELEGAR: clima]`).
- **Dissipador de saída de bueiro** (rip-rap, bacia): HEC-11 e EM 1601 cap. 3 entram só como localização; o dimensionamento é da Hidráulica (D3).
- **Não coberto**: drenagem urbana em rede (HEC-22 caps. 7-12, PMSP) e aeroportuária (`LOC-COMAER`): citar que existe, não aplicar.
- **Norma fechada**: NBR 8890:2020 e as demais ABNT **não estão no corpus** (seção 11). Citar a obra de apoio e a página; nunca transcrever.
- Regra mestra do pacote: se o projeto do acervo diverge da fonte, **apontar a divergência com evidência e consequência**, nunca corrigir em silêncio (núcleo, seção 9).

## 4. Tabela mestre: edição, licença, o que traz, páginas-chave

Licença: **oficial** = publicação oficial de uso livre com citação; **PD** = domínio público; **aberta**; **uso-interno** = obra de terceiros no acervo (citar obra e página, no máximo uma
frase curta entre aspas, sem transcrever tabela, equação longa ou exemplo). Corpus: **H** = Hidráulico; **P** = próprio.

### DNIT e DER/PR (detalhe: `references/fichas-dnit-der.md`)

| ID (corpus) | Edição / vigência | Licença | O que pede ou traz | Páginas-chave |
|---|---|---|---|---|
| `DNIT-DREN` (H) = **IPR-724** | 2ª ed. 2006; impr. = fís. − 4 | oficial | bueiro como canal no crítico (Qc = 1,538·D^2,5), orifício (HW ≥ 1,2 D, c = 0,63), BPR nº 5 (entrada e saída); **Ke Tab. 30; V máx Tab. 31; n Tab. 32-34**; valeta, sarjeta (racional por metro, **TR 10, 5 min**), descida, dissipador, dreno profundo, geotêxtil | 36-48, 89, 92, 95-126; **130, 131**, 131-134; 158-166, **171**, 186, 203, 225, 247, 315 |
| `DNIT-HIDRO` (H) = **IPR-715** | 2ª ed. 2005; impr. = fís. − 4 | oficial | risco J = 1 − (1 − 1/TR)^n; **IS-203: dimensionar o bueiro com TR 10 e verificar 20 ou 25**; 14 fórmulas de Tc; racional com n = A^−0,10; estatística, HU e CN | 24-25; 24; 83-98 (89, 90, 94); 127-133 (**131**); 35-82 |
| `DNIT-ALBUM` (H, sem texto) e `LOC-DNIT-ALBUM-2018` (P, OCR) = **IPR-736** | **5ª ed. 2018** (catálogo H diz 2006) | oficial | desenhos-tipo e quantitativos; "orientador e não normativo"; cap. 9 lineares: **TR 10 e Tc 6 min** | 23; 25-49 (superficial); 213-227 (**214**) |
| `DNIT-IPR726-2006` (P) = **IPR-726** | 3ª ed. 2006; impr. = fís. − 3 | aberta | **IS-203**: tabela de TR por obra e **Tc superficial 5 min**; faixas de área do racional; **IS-239** (vicinais): Tc 10 min; IS-210 e IS-242 (projeto de drenagem) | **258**, 259; 463-464; 305-311; 472-473 |
| `DNIT-ES018-2023` (P) | jan/2023, revisão da 018/2006 | aberta | sarjeta e valeta: **25 % (4H:1V)** junto ao acostamento; fck ≥ 20 MPa; gabaritos 3,0 m; junta 12 m; tolerância 1 % | 2-6 |
| `DNIT-ES020-2006` (P) | 2006, **sem revisão verificada** | aberta | meio-fio e guia; remete ao Álbum ENEMAX 1988 | 2-3 |
| `DNIT-ES021-2023` (P) | 2023, errata 1 (11/2024) | aberta | entrada e descida: rejunte 1:3; juntas em descida > 10 m; tolerância 1 % | 3-5 |
| `DERPR-ES-DR-01/03/05/06/07-23` (P) | 2023, Deliberação 111/2023; **estadual** | aberta | espelho de conferência: gabaritos ≤ 2,00 m, junta 12 m, **declividade < 0,5 % implica demolição** (01); drenos (06, 07) | 01: 4-10; 03: 5-7; 06: 3-12 |

### FHWA, USACE, WSDOT (detalhe: `references/fichas-fhwa-usace-wsdot.md`)

| ID (corpus) | Edição / vigência | Licença | O que pede ou traz | Páginas-chave |
|---|---|---|---|---|
| `FHWA-HDS5` (H) | **3ª ed. abr/2012**; dual | PD | controle de entrada e de saída; **vale o maior HW**; HW/D comum 1,0-1,5; ±10 %; **Tab. A.1 constantes; B.1 n; C.2 Ke** | 83-126, **72**, **196**, **197**, 204-208, **216**, DG 271-323 |
| `FHWA-HEC22` (H) | 4ª ed. (cat. 2024); fís. = impr. + 32 | PD | racional < 80 ha; sarjeta de Izzard (Ku 0,376 SI); Tab. 5.3 n; bocas e condutos (rede: fora de escopo) | **57**, **79**, 113-158, 169-210 |
| `FHWA-HEC12` (P) | 1984, **arquivada** (absorvida pelo HEC-22); fís. = impr. + 17 | PD | sarjeta triangular Eq. 4 (K = 0,56 US), composta, valeta de canteiro; 30 exemplos | 19, **39**, 41-49, 110-113 |
| `FHWA-HEC13` (P) | 1972, **arquivada** (superada pelo HDS-5) | PD | entradas melhoradas; **Tab. 1 Ke (alas paralelas 0,7)** | 33-52, **100**, 111-152 |
| `FHWA-HDS3` (P) | 1961, arquivada; fís. = impr. + 8 | PD | 83 charts de canal e tubo (US); **Chart 55 parcialmente cheio**; Tab. 1 n | **76**, **108**, 53-55 |
| `USACE-EM1110-2-1601` (P) | 1991, Change 1 de 1994 | PD | **Tab. 2-5 V permissíveis (guia)**; rip-rap (cap. 3); n (cap. 5) | **25**, 26-39, 47-62 |
| `USACE-EM1110-2-2902` (P) | 1997 + Change 1 (1998); **substituída em 2020** | PD | só carga e estrutura de conduto; **Tab. 3-1 fator de berço** | **27**, 66-72 |
| `WSDOT-HYDRAULICS-M2303-12` (P) | cat. 2025; rodapé **abr/2026** | aberta | prática estadual dos EUA: Tc mín. 5 min, TR × espaçamento, valeta lateral | 46-47, 102-109 |

### NRCS, DAEE, ILRI, Pfafstetter, ABTC (detalhe: `references/fichas-nrcs-ilri-daee-pfafstetter-abtc.md`)

| ID (corpus) | Edição / vigência | Licença | O que pede ou traz | Páginas-chave |
|---|---|---|---|---|
| `LOC-NEH-TC-ESCOAMENTO-PLANO` (P) = NEH 630 cap. 15 | **final mai/2010**; H tem **rascunho out/2008** | PD | lag e L = 0,6·Tc; **laminar ≤ 100 ft**; Tab. 15-1 e 15-3; Anexo 15A | 7-15, **11-13**, 18-21, 25 |
| `NRCS-NEH630-CH09/10/16/18` (H) | 2000-2007 | PD | CN, Q ponderado, Ia = 0,2·S, HU 484, frequência | CH10: 8-11, 25-26 |
| `NRCS-NEH624-*` (H) e `NRCS-EFH14` (H) | NEH 624 c. 1971-73 (CH10 2001); **EFH14 2ª ed. fev/2021** (substitui CH14 de 2001) | PD | elipse, Hooghoudt, envoltório, V de vala | EFH14: **72**, **89**, **187** |
| `DAEE-IT-DPO11` (H); `DAEE-GUIA` (H) | 30/05/2017 (só SP); Guia 2005 | ato público / técnica | **TR ≥ 25 rural e 100; C ≥ 0,25; CN ≥ 60; racional ≤ 2 km²; folga; n; V máx** | IT: **1-4**; Guia: 16-19 |
| `LOC-PFAFSTETTER-CHUVAS-INTENSAS` (P) | 1957 (MAPA); IPR-715 cita a 2ª ed. 1982 | uso-interno | só localizar: validade 5 min a 6 d e 0,2 a 100 anos; **Salvador (Ondina) único posto da BA** | **21**, 22-23, **31**, 278-280 |
| `LOC-ABTC-*` (P) e **NBR 8890:2020 (fechada)** | ALTERACOES 2020; TUBOS 2003 | uso-interno | classes PA/EA, DN > 600 armado, MF ≥ DN 500; recobrimento ≥ 0,6 m | ESPEC **4**, ALTER 1-5, TUBOS 29, 37, 45-46 |
| `ILRI-DPA16` (H); `ILRI-56-ENVELOPE` (P) | 2ª ed. rev. 1994; 2000 | aberta | Hooghoudt, Ernst, Glover-Dumm (cap. 8); envoltório e HFG | DPA16: **263**, **270**, **284**; ILRI-56: 27-72 |

## 5. Edições e vigência (regra)

A edição entra em **toda** citação do parecer. Registrar, quando o caso se apresentar: IPR-724 2ª ed. 2006, IPR-715 2ª ed. 2005, **IPR-736 5ª ed. 2018** (não 2006), IPR-726 3ª ed. 2006; ES 018 e 021 de **2023** (substituem 2006 e 2004), ES 020 de **2006 sem revisão
verificada**; HDS-5 3ª ed. 2012; HEC-12 e HEC-13 **arquivadas** (HEC-13 incorporada ao HDS-5; use como conferência); EM 2902 de **1997**, substituída em 2020; EM 1601 com Change 1 (1994); **NEH 630-15: dois textos** (final 2010 e rascunho 2008);
**EFH14 2021** em vez do NEH 650 CH14 de 2001; NEH 624 CH01-09 históricos; DAEE IT-DPO 11 de 2017 (só SP); Pfafstetter 1957 (MAPA) × 2ª ed. 1982 citada pelo IPR-715; TUBOS (ABTC) de **2003** × NBR 8890:**2020**.
Quadro completo com licença e observações: `references/edicoes-paginacao-e-divergencias.md`, seção 1.

## 6. O que cada fonte exige e a quem se aplica

- **Normativas federais de rodovia (DNIT)**: ES 018/020/021 (execução e aceitação, **sem dimensionamento**); IPR-724 e IPR-715 (manuais de projeto, "norma de fato"); IPR-726 (escopo e instruções de serviço); IPR-736 (orientador, **não normativo**). Aplicam-se a rodovia federal; em estrada de serviço de perímetro irrigado valem **por analogia, declarada**.
- **DER/PR ES-DR 2023**: estadual do Paraná; espelho de conferência e detalhe construtivo. Não vincula obra fora do PR.
- **DAEE IT-DPO 11**: **só SP por lei**; fora de SP é referência. É a única norma brasileira do corpus com TR, folga, n e V máx numéricos para canalização e travessia.
- **Manuais americanos (FHWA, USACE, NRCS, WSDOT)**: método e prática; **não são norma brasileira**. O HDS-5 é o método de bueiro do pacote; WSDOT é só contraste.
- **ABTC e NBR 8890**: a norma é fechada; as obras da ABTC são `uso-interno`. A classe de tubo no pacote é **indicativa**; estrutura é de `estruturas`.
- **Livros e apostilas** (McCuen, IME, Eslamian, Pfafstetter): apoio e localização; sem exemplo copiado.
- **Projeto do acervo**: prática, não norma. Nunca citar um número do acervo como se fosse regra do manual.

## 7. Armadilhas de leitura (resumo; completo na seção 3 de `references/edicoes-paginacao-e-divergencias.md`)

- **Página impressa × física**: IPR-724 e 715 impr. = fís. − 4; IPR-726 − 3; HEC-12 − 17; HEC-22 + 32 (física maior); HDS-3 + 8; NEH 630-15 "15-N" = N + 6; ILRI-16 impr. − 2; ILRI-56 + 20; Pfafstetter livro = fís. − 6; McCuen + 19.
- **Só em imagem**: nomogramas do HDS-5 e do IPR-724 (Figs. 13-32), charts do HDS-3, HEC-12 e HEC-13, quadro de Tc do DAEE, equações 3-47 a 3-57 do McCuen. Abrir o PDF; nunca completar valor por memória.
- **OCR a conferir**: Pfafstetter, Álbum 2018 (24 p. sem OCR), NEH 624 (letras espaçadas), Embrapa Bebedouro.
- **Fórmula embaralhada**: o racional do IPR-715 p. 131 fecha com **A/3,6**, mas o `_texto` mostra "6,3". Conferir pelo exemplo (0,385·96,1·10,5/3,6 = 107,9).
- **Remissão interna errada**: IPR-724 p. 169 manda ver a "tabela 26" para velocidade de revestimento; a tabela é a **31** (p. 131).
- **Edição errada no catálogo**: Álbum (2006 × 2018); EM 1413 (1987 × revisão recente); WSDOT (2025 × 2026); HEC-13 "ano a conferir" (a p. 1 confirma 1972); `DNIT-ES018` "título inferido" (a p. 1 confirma).
- **Duas fontes, mesma tabela**: HEC-13 Tab. 1 = HDS-5 Tab. C.2 (Ke). Citar o HDS-5.
- **Constante interna inconsistente no HDS-5**: Y de arco projetante 0,57 (Tab. A.2 p. 198) × 0,53 (exemplo p. 191); o código usa 0,57.

## 8. Divergências que o agente deve conhecer antes de citar

Lista completa, com páginas e fontes, em `references/edicoes-paginacao-e-divergencias.md`, seção 4. **Os quatro pontos abertos da F7** (não decidir; escrever "padrão provisório, decisão F7" e mostrar as alternativas):

1. **TR de bueiro de perímetro irrigado**: IPR-726 p. 258 (tubular 15 como canal / 25 como orifício; celular 25 / 50) e IPR-715 p. 24 (dimensionar com 10, verificar 20 ou 25) × DAEE p. 1 (≥ 25 rural, 100) × USBR 5-15 (núcleo) × acervo 25/50. Norma específica de perímetro: **não achada** (`NAO_ABERTOS.md`).
2. **Ke de alas paralelas**: HDS-5 p. 216 e HEC-13 p. 100 = **0,7** × IPR-724 p. 130 = **0,2**. O código usa 0,7.
3. **Limite de área do racional**: IPR-726 p. 259 (4 km², 10 km²) × DAEE p. 1 (2 km²) × HEC-22 p. 57 (80 ha) × IPR-715 p. 131 (sem teto, com A^−0,10) × projetos (50 ha a 3,5 km²). O código avisa acima de 2 km² (`racional(limite_km2=2.0)`, critério do DAEE, só SP).
4. **Tc mínimo de drenagem superficial**: 5 min (IPR-726 p. 258; WSDOT; HEC-22) × **6 min** (Álbum p. 214, só para **dispositivo linear pré-fabricado**, com i "com base na NBR 10.844:1989", norma predial) × **10 min** (IPR-726 p. 463, vicinais).

Outras que mordem: método de bueiro (IPR-724 crítico/orifício × HDS-5 entrada e saída); n do tubo de concreto (0,012 ABTC × 0,011-0,013 HDS-3 × 0,015 base dos charts × 0,018 DAEE); V máx no concreto (4,5 IPR-724 × 4,0 DAEE × 1,8-2,4 CDV);
fck de sarjeta (20 × 15 × 11 MPa); tolerância (1 × 5 × 10 %); Tc laminar (McCuen 0,938 × planilhas 0,933 × NEH 15-8); Kirpich (0,007 × 0,0078; modificada 1,42; **sem "1,5×" em fonte alguma do corpus**); TR californiano (Pfafstetter) × Weibull (McCuen).

## 9. Calculadoras que implementam as fontes (`tools/dren/`)

`python -m tools.dren.<módulo> --listar` mostra as funções; entradas de calculadora em ponto decimal; reproduza os `avisos`. Testes: `python -m pytest tests/dren -q`. Função "não conferida" na docstring (Dooge, DNOS, NERC, Bransby-Williams) não vira método.

| Fonte | Função | Teste e o que conferir |
|---|---|---|
| HDS-5 Tab. A.1, B.1, C.2 | `bueiros.controle_de_entrada`, `controle_de_saida`, `ke_entrada(fonte_ke="hds5"\|"dnit")`, `dimensionar_bueiro` | `test_bueiros.py`; aviso de Ke e do n adotado; maior HW governa |
| IPR-724 p. 36-48, 89-92 (crítico, orifício) | `bueiros.hw_legado_orificio`, `verificacao_manning_plena`, `vazao_critica_legado_dnit` (+7,7 % sobre `vazao_critica_exata`), `comparar_legado_hds5` | `test_baixio_legado_vs_hds5_5pct` (xfail rotulado) |
| IPR-724 Tab. 31 | `bueiros.limite_velocidade`, `canais_drenagem.velocidade_admissivel(fonte="dnit")` | tabela legada ainda existe (até 2× mais permissiva) |
| IME p. 151-152 | `bueiros.regime_critico_tubular_ime` | A_c = 0,601·D² vem de fórmula impressa |
| HDS-3 Chart 55 | `bueiros.tubo_parcialmente_cheio` | geometria exata; y/D ≤ 0,75 é padrão provisório |
| IPR-724 p. 171; HEC-12 Eq. 4; HEC-22 Eq. 5.2 | `estradas.sarjeta_triangular`, `bueiros.sarjeta_triangular_izzard`, `estradas.vazao_por_metro`, `valeta_comprimento_critico`, `criterio_projeto` | `test_estradas.py`; unidade de i (cm/h × mm/h) e K SI 0,376 |
| IPR-715, NEH 630-15, McCuen | `hidrologia.tc_com_avisos`, `tc_laminar_neh`, `tc_lag_scs`, `tc_onda_cinematica`, `racional(limite_km2=2.0)`, `chuva_efetiva`, `hidrograma_unitario_triangular`, `risco_hidrologico` | `test_hidrologia.py`; gabaritos 1-10 do MAPA G1 |
| ABTC, EM 2902 | `tubos.classe_de_tubo`, `selecionar_tubo`, `fator_berco_vala(fonte="abtc")`, `d_load_em2902` | `test_tubos.py`; EM 2902 p. 71-72 **não** é gabarito |
| EM 1601 Tab. 2-5; HEC-11 Eq. 6 | `canais_drenagem.velocidade_admissivel`, `d50_riprap_hec11`, `verificar_limites_alternativos` | `test_canais_drenagem.py`; dissipador é D3 |
| ILRI-16, EFH14, NEH 624, Embrapa | `drenos.hooghoudt_espacamento`, `ernst_espacamento`, `glover_dumm_espacamento(fator=1.16)`, `capacidade_tubo_dreno`, `criterio_de_filtro_hidraulico` | `test_drenos.py`; declarar o viés do método |
| Pfafstetter, DAEE-GUIA (I-Pai-Wu) | **sem função** | IDF é do Clima; I-Pai-Wu não implementado |

## 10. Critérios de verificação (da consulta a uma fonte)

1. **Página citada**: todo `[ID p. N]` foi conferido no `_texto` (ou marcado "página a confirmar"). Número de OCR sai marcado "OCR, conferir na imagem".
2. **Edição e vigência** declaradas (seção 5); fonte arquivada ou substituída aparece como tal.
3. **Licença respeitada**: `uso-interno`, norma fechada e `FORNECIDA-PELO-USUARIO` só em citação curta; nenhuma tabela da NBR 8890 transcrita.
4. **Unidade**: ábaco imperial citado na unidade original e convertido (núcleo, seção 1); i em cm/h do IPR-724 convertida.
5. **Divergência registrada** quando o valor está na seção 8, com a fonte adotada e a preterida.
6. **Aplicabilidade declarada**: fonte estadual, estrangeira ou orientativa usada "por analogia" e rotulada.
7. **Pontos F7** escritos como "padrão provisório, decisão F7", com as alternativas.

## 11. Protocolo de citação e consulta

1. **Citação**: `[ID p. N]` (N = física); em `_ocr/` N = página do livro (Pfafstetter, Álbum) e a física vai junto quando inferida. Acervo: `Nome.pdf:N` com marca de ancoragem; calculadora: `tools/dren/<módulo>.<função>` com as entradas.
2. **Navegar, não ler**: Grep por termo e por `<!-- p. ` em `referencias/_texto/<ID>.md` (próprio) ou `../Especialista Hidraulica/referencias/_texto/<ID>.md` (H); ler só o intervalo. Mapas: `referencias/MAPA_DE_CONHECIMENTO.md` (G1-G4) e H12-H15 do Hidráulico.
3. **Índices FTS5**: próprio `<SQUAD_LOCAL>/bibdren/db/corpus.sqlite` (`busca_pagina`); Hidráulico `<SQUAD_LOCAL>/bibhid`. O `<id>` do índice não é o ID do catálogo.
4. **Abrir o PDF** quando: figura, nomograma, tabela com coluna fundida, equação quebrada, número que vira gabarito, página sem texto.
5. **Não está no corpus**: dizer e pedir ao usuário (seção 12). **Norma fechada**: citar obra e página.
6. **Acervo de projetos** (`consultar-acervo`): prática, não norma; número com `!`, `~` ou `✓*` não vira gabarito sem `✓h`; nenhum número dos casos de 2026-10-08 tem `✓h`.

## 12. Lacunas do corpus e o que pedir ao usuário

Fechadas ou ausentes (`NAO_ABERTOS.md`, `PENDENTES_DOWNLOAD_MANUAL.md`): **NBR 8890:2020** (compra ABNT; sem tabela de altura de aterro por classe), NBR 15645 e 16085, **DAEE Manual de Vazões 1994**, **FAO-38**, NRCS CPS 606/607, FDOT (PDF truncado), AASHTO e ASCE MOP 77, Chow-Maidment-Mays, Tucci, e o **critério de TR de perímetro irrigado** (pedir à Codevasf e ao DNOCS). IPR-724, 715 e 736 só em edição única (2006, 2005, 2018); ES 019/030/086 só no corpus do Hidráulico.
Sem texto ou com texto ruim: Álbum (24 p.), Pfafstetter (OCR), slides Robson I-IV. Sem caso do acervo com Hooghoudt, Ernst ou Glover-Dumm calculado. Quando o pedido depender de fonte ausente, o parecer diz qual, cita a obra e pede o PDF.

## 13. Nível de projeto

- **Anteprojeto**: citar a fonte e a página, a edição, e a divergência quando houver; critérios por analogia rotulados.
- **Projeto básico**: conferir página e tabela no PDF (não só no `_texto`), explicitar o método de bueiro (HDS-5) e a edição.
- **Executivo**: só confere; norma de execução (ES) e aceitação são do projetista e do contratante.

## Revisão técnica

**2026-10-08, revisor Opus (F7).** Conferência por amostra no `_texto` (marcador `<!-- p. N -->`), sem PDF renderizado.

- **Amostrados: 24 afirmações; conferidas 24; corrigidas 0 por erro numérico; 3 precisões de texto.** Conferidos: IPR-724 Qc = 1,538 D^2,5 (p. 48), HW ≥ 1,2 D (p. 89), c = 0,63 (p. 92), Ke 0,2 de alas paralelas (Tab. 30, p. 130), V máx. do concreto 4,50 m/s (Tab. 31, p. 131, impr. 127 = fís. − 4), TR 10 e 5 min da sarjeta com i em cm/h (p. 171), "tabela 26" errada na p. 169 (a Tab. 26 é o n do concreto, p. 114); IPR-715 IS-203 10 e 20/25 anos e risco J (p. 24), "6,3" do `_texto` e n = A^−0,10 (p. 131); IPR-726 TR por obra e Tc 5 min (p. 258), 4 e 10 km² (p. 259, impr. 256 = fís. − 3), Tc 10 min (p. 463); Álbum "não normativo" (p. 23) e TR 10 e Tc 6 min (p. 214); HDS-5 Ke 0,7 (p. 216), HW/D 1,0-1,5 (p. 72), Y 0,57 (p. 198) × 0,53 (p. 191); HEC-13 0,7 (p. 100); HEC-22 80 ha (p. 57, impr. 25 = fís. − 32) e Ku 0,376/0,56 (p. 79); HEC-12 K 0,56 (p. 39, impr. 22); DAEE ≤ 2 km², TR 25/100, C 0,25, CN 60 (p. 1-2), n 0,018 e V 4,0 do concreto (p. 4); ES 018 25 % (4H:1V) e fck 20 MPa; ES 021 traço 1:3 e juntas em descida > 10 m; DER/PR ES-DR-01 < 0,5 % implica demolição e gabaritos de 2,00 m; NEH 630-15 L = 0,6 Tc e laminar ≤ 100 ft; EM 1601 Tab. 2-5 (p. 25) e Change 1; EM 2902 berço de concreto 2,5 (p. 27); Pfafstetter, validade de 5 min a 6 d e de 0,2 a 100 anos (p. 21), Salvador (Ondina) (p. 31, 280); EFH14 2ª ed. fev/2021.
- **Precisões feitas:** seção 8, item 4: o Tc de 6 min do Álbum vale só para dispositivo linear pré-fabricado, com i pela NBR 10.844 (p. 214). Item 1: a ordem 15/25 é "como canal / como orifício" (p. 258). Item 3: o código usa 2 km² (DAEE) como limite padrão. Na description, o limite com o `normas-e-manuais` do Hidráulico ficou explícito.
- **Calculadoras:** as 38 funções da seção 9 existem em `tools/dren/` com o nome e o argumento citados. O teste `test_baixio_legado_vs_hds5_5pct` existe. Nenhum erro numérico encontrado nas constantes conferidas (Ku 0,376; 3,6; A^−0,10; risco J; TC_MIN 5; TR 10).
- **Fronteiras:** D3 (dissipador → Hidráulico), IDF → Clima e travessia → Hidráulico estão de acordo com a `MATRIZ_DE_INTERFACES.md` §3.3. Não há colisão de description dentro do pacote. Com o `normas-e-manuais` do Hidráulico há gatilhos em comum (HDS-5, DAEE, NBR 8890), mas os dois ficam em pacotes separados e cada um remete ao outro.
- **Pendentes (para o André):** (a) decisão 4: o "6 min" do Álbum não é um Tc mínimo geral, e sim o de canaleta pré-fabricada com critério predial. Recomendação: 5 min (IPR-726 p. 258) para plataforma e estrada de serviço, 10 min só em vicinal (p. 463). (b) Decisão 3: o padrão de 2 km² do `racional` segue o DAEE (só SP), enquanto o IPR-726 p. 259 permite racional até 4 km² e racional corrigido até 10 km². Entre 2 e 4 km² o código avisa e o DNIT aceita. O aviso cita "2-3 km²", e o 3 não tem fonte. Recomendação: manter 2 km² por conservadorismo, mas citar o IPR-726 no aviso. (c) Página física do PDF não conferida nos ábacos (só o `_texto`). Em projeto básico, abrir o PDF.
