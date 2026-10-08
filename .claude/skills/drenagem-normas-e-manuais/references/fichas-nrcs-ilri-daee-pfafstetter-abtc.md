# Fichas por fonte: NRCS (NEH 630 cap. 15, 624, 650), ILRI 16 e 56, DAEE, Pfafstetter, ABTC / NBR 8890

Convenção: `[ID p. N]` = página física do PDF; **conf.** = lido no `_texto` na F6; **mapa** = vem do MAPA (F3 ou H12-H15), não relido.
NRCS e USACE: domínio público. ILRI, Waterlog e Embrapa: licença aberta. **Pfafstetter, McCuen, IME, Eslamian e ABTC: `uso-interno`**
(obra de terceiros no acervo do André: citar obra e página; no máximo uma frase curta entre aspas; sem transcrever tabela, equação longa ou exemplo).

## NRCS NEH Parte 630, cap. 15 Time of Concentration

**Duas edições no pacote**: corpus próprio `LOC-NEH-TC-ESCOAMENTO-PLANO` = **final de maio/2010** (rodapé "210-VI-NEH, May 2010"; 29 p.; "15-N" impressa = **física N + 6**);
corpus do Hidráulico `NRCS-NEH630-CH15` = **rascunho de out/2008** (30 p.; equações 15-3a/b e exemplos em p. 16-19). As numerações de equação e de página **diferem**; declarar a edição na citação (V11).

| O que traz (ed. 2010, `LOC-NEH-TC`) | Página | Status |
|---|---|---|
| Tt = ℓ/(3600·V); lag e **L = 0,6·Tc** (Eq. 15-3); método do lag (Eq. 15-4a/b; ℓ = 209·A^0,6; declividade Y por contornos) | 7-11 (L = 0,6·Tc aparece na p. 11) | conf. (11); resto mapa |
| Método da velocidade (Eq. 15-7): laminar, concentrado raso, canal | 11-15 | mapa |
| **Tab. 15-1** n de escoamento laminar (liso 0,011) p. 12; **limite do escoamento laminar de 100 ft (30 m)**, citando Merkel (2001) p. 12-13; Tab. 15-2 comprimentos máximos p. 13; **Tab. 15-3** (V = k·S^0,5; k = 20,328 pavimento, 16,135 canal gramado ...) p. 14 | 12-14 | conf. (limite 100 ft p. 12-13; Tab. 15-1 p. 12); Tab. 15-2 e 15-3 mapa |
| Eq. 15-8 laminar: Tt = 0,007·(n·ℓ)^0,8/(P2^0,5·S^0,4) em h, com P2 = chuva de 2 anos e 24 h | 12-13 | mapa |
| Exemplos: lag (Mawney Brook, Tc = 1,14 h) p. 18; velocidade em três trechos (Tc = 1,75 h) p. 18-21 | 18-21 | mapa (gabaritos 5 e 6 do MAPA G1) |
| Anexo 15A Kirpich (Eq. 15A-1, "0,007" na leitura do OCR), Kerby, Simas, Folmar-Miller; Anexo 15B | 25-29 | mapa |

Armadilhas próprias: método da velocidade **subestima Tc em 60 a 90 %** (Folmar e Miller, 39 bacias) [Hidráulico, ed. 2008, p. 14]; "Tc para vazão de 2 anos ou margens plenas"; sem Giandotti, Dooge, Picking nem Kirpich modificada (o 1,42 é do IPR-715). Kirpich: 0,007 (NEH, OCR) × 0,0078 (McCuen p. 172): conferir na imagem antes de calibrar. Código: `hidrologia.tc_laminar_neh` (usa P2), `tc_lag_scs`, `tc_onda_cinematica` (coeficiente 0,938 do McCuen; as planilhas internas usam 0,933).

Outros capítulos do NEH 630 (corpus do Hidráulico, ver H12): cap. 10 CN e Q = (P − Ia)²/(P − Ia + S), Ia = 0,2·S (p. 8-11), exatidão e limites (**CN não vale para vazões pequenas**, p. 25-26); cap. 9 tabelas de CN (Tab. 9-1 p. 8-9; urbano Tab. 9-5 p. 15); cap. 16 HU adimensional (PRF 484, Tab. 16-1, p. 10-12; constante varia de ~600 a ≤ 100, p. 33-35); cap. 18 frequência e risco (p. 14-38, 65-67). Regra: **ponderar Q, não CN**, quando os CN diferem muito (cap. 10 p. 17). Páginas "mapa". McCuen (corpus próprio, física = impressa + 19): Tc p. 158-173, racional p. 394-401, SCS p. 404-417, HU p. 553-561 [mapa G1]; equações de Tc (3-47 a 3-57) ilegíveis no `_texto`: ler na imagem.

## NRCS NEH 624 (Drainage of Agricultural Land) e NEH 650 EFH 14 (Water Management, Drainage)

Corpus do Hidráulico (H15). **NEH 624 CH01-CH09**: edição SCS c. 1971-73, digitalizada por OCR com **letras espaçadas** (conferir número na imagem); **CH10**: abr/2001, física = impressa + 10. **EFH 14**: **2ª ed. fev/2021**, 204 p., **substitui o NEH 650 CH14 de abr/2001** (texto quase igual; numeração de seções e figuras diferente; `duplicata_de` não existe no catálogo): **citar o EFH 14**.

| Tema | Onde | Status |
|---|---|---|
| **Elipse** (S = [4K(b² − a²)/q]^0,5; sem barreira conhecida, **supor barreira a 2 vezes a profundidade do dreno**) | EFH14 p. 72 (fig. 14-39 impr. 14.65); NEH624-CH04 p. 63-68 (elipse), p. 69-75 (Hooghoudt gráfico) | conf. (EFH14 p. 72); CH04 mapa |
| **Hooghoudt com d' de convergência** por faixa de d/L (d/L ≤ 0,31 e > 0,31) | EFH14 p. 187 (Apêndice 14E); NEH624-CH10 p. 51-61 (eq. 10-7, forma para d/L pequeno) | conf. (p. 187 existe); eq. mapa |
| **Envoltório granular**: D15 do filtro ≥ 4× d15 do solo-base e ≤ 4× d85 | EFH14 p. 85-92 (critério p. 89); critério de 1970 em NEH624-CH04 p. 96-102 (histórico) | conf. (p. 89) |
| Coeficiente de drenagem (3/8-1/2 pol/24 h mineral; irrigado 0,005-0,01 pol/h); **em irrigação brasileira vem do balanço de água e lixiviação**, não da tabela de clima úmido | NEH624-CH04 p. 49-51; EFH14 p. 65-84 | mapa |
| n de dreno: 0,011-0,016 (CH04 p. 88) × 0,015-0,020 por diâmetro (CH10 p. 50); V mínima 1,4 ft/s sem filtro; **V máx de vala** por solo (areia 2,5; argila rija 5,0 ft/s) EFH14 p. 38 | vários | mapa |

Armadilha: gráficos de 1970 (Figs. 4-28/4-29) são só conferência (±5 %); implementar a forma iterativa de 2001/2021. Regra de escolha (elipse × Hooghoudt, n, coeficiente): mora em `drenagem-subsuperficial`; aqui só a localização.

## DAEE-SP: IT-DPO 11 (30/05/2017) e Guia Prático (2005)

Corpus do Hidráulico. **IT DPO nº 11**, 10 p., ato administrativo público do Estado de SP; **só se aplica por lei a corpos d'água de domínio de SP**; fora de SP é referência. Revoga IT-DPO 02 e 04 de 2007. É a **única norma brasileira do corpus com TR e folga numéricos** para canalização e travessia.

| O que pede | Página | Status |
|---|---|---|
| Racional se **A ≤ 2 km²** | 1 | conf. |
| **TR mínimo 25 anos (zona rural) e 100 anos (urbana ou de maior porte)**; barramento por altura e risco (100 a 10.000) | 1-2 | conf. |
| **C ≥ 0,25 e CN ≥ 60** (valores mínimos; corrigir para uso futuro do solo) | 2 | conf. |
| Tc: não usar valor superior ao da fórmula do **Quadro 1** (fórmula só em imagem: ler no PDF) | 2 | conf. (existência) |
| **Folga** f ≥ 0,20·h_TR (seção aberta), f ≥ 0,20·H (contorno fechado), ponte f ≥ 0,4 m, **bueiro em carga f ≥ 0,20·H**, barramento ≥ 0,10·H_M e ≥ 0,5 m | 3 | conf. |
| n (Tab. 5): grama 0,035; gabião 0,028; pedra argamassada 0,025; aço corrugado 0,024; **concreto 0,018**. V máx (Tab. 6): terra 1,5; gabião 2,5; pedra argamassada 3,0; **concreto 4,0 m/s** | 4 | conf. |

**Guia Prático para Projetos de Pequenas Obras Hidráulicas** (DAEE/FCTH, 2005; 128 p. no PDF, 116 impressas; `DAEE-GUIA`, baixado depois do MAPA H, sem mapa): método racional para AD ≤ 2 km², **I-Pai-Wu para 2 < AD ≤ 200 km²** (p. 16), Q = 0,1667·C·i·AD (p. 17; **unidade de i e AD a confirmar no PDF**), escolha do TR e risco (p. 18-19) [conf. existência e valores].
Armadilhas: fórmulas e quadros do Quadro 1 e do I-Pai-Wu estão em imagem; o limite de 2 km² é estadual e **não é "o" limite do racional** (seção 8 do SKILL); o DAEE-SP pede TR 25/100 para canalização, o que não é critério de perímetro irrigado.

## Pfafstetter, *Chuvas Intensas no Brasil* (corpus próprio, `LOC-PFAFSTETTER-CHUVAS-INTENSAS`)

DNOS; no MAPA, edição de **1957**; o IPR-715 cita a **2ª ed. (DNOS, 1982)** [DNIT-HIDRO p. 15 e 137, conf.]: registrar a divergência de edição. 426 p., **quase todo OCR** (números "OCR, conferir na imagem"); página do livro = física − 6; licença `uso-interno`.
**Papel no Drenagem: localizar e citar. A IDF é entrega do Clima (`chuvas-intensas-e-idf`, `[DELEGAR: clima]`).**

- Expressão analítica P = K·[a·t + b·log(1 + c·t)], K = T^(α + β/T^γ), γ = 0,25 (p. 13-17, mapa); **validade 5 min a 6 dias e 0,2 a 100 anos ou mais** p. 21 (conf.); TR pelo "método californiano" T = n/m p. 10 (mapa).
- **Exemplos numéricos p. 22-23** (conf.): Campos 40 min/5 anos → 46 mm (interpolação de 44 e 50 mm); Belo Horizonte 6 h/50 anos → K = 2,10 × 58 mm = **122 mm**; Porto Alegre 2 h/102,2 mm → K = 2,84 → T = **290 anos**.
- **Salvador (Ondina), posto nº 69, é o único posto da Bahia** (lista p. 31, conf.; gráficos p. 278-280; β p. 397); **nada de Sento Sé, Sobradinho ou do semiárido baiano**; Quadro V (α) p. 393; Quadro VI (β) p. 393-398; P(T = 1 ano) por posto p. 401-425 [mapa].
- Armadilhas: (1) o **TR "californiano"** (T = n/m) difere da posição de Weibull (T = (n+1)/m) do McCuen: não misturar em IDF nova; (2) a expressão sai incompleta no OCR (conferir na imagem); (3) posto de Salvador não representa o semiárido: **não transpor sem aviso**; (4) os dados vão até ~1950 (98 postos); não é IDF no formato i = a·T^b/(t+c)^d.

## ABTC e a NBR 8890 (norma fechada: citar, não transcrever)

**NBR 8890:2020** (ABNT; substitui as NBR 9793 e 9794) **não está no corpus** (`NAO_ABERTOS.md`, NA-NBR8890). O que há são materiais da ABTC (`uso-interno`) que a explicam; cite a **obra ABTC e a página**, não a norma.

| Obra no corpus | O que traz | Página | Observação |
|---|---|---|---|
| `LOC-ABTC-ALTERACOES-NBR8890` (5 p.) | 14 mudanças da edição de 2020: cimento resistente a sulfatos em rede contaminada (NBR 16697); tubos com reforço secundário de fibras (RSF) e só fibras (RF); **macho-e-fêmea só a partir de DN 500**; **DN > 600 obrigatoriamente armado, RF ou RSF**; classe acima de PA4/EA4 → galeria celular NBR 15396 | 1-5 (1 conf.) | tabelas de espessura mínima p. 2-3 |
| `LOC-ABTC-ESPEC-TUBOS-LICITACOES` (7 p.) | como especificar tubo em 8 passos; **Tab. 2 força mínima isenta de fissura e de ruptura por classe PA1-PA4 e EA2-EA4, DN 300-2000** (ruptura = 1,5 × isenta de fissura); 3 exemplos de especificação ("DN1200 PA2 MF JR"; "DN800 EA4 PB JE"; "DN400 PA4 PB JR") | Tab. 2 p. 4 (conf.); exemplos p. 6 | é a tabela de classes a usar para "classe indicativa" |
| `LOC-ABTC-PROJETO-ESTRUTURAL-TUBOS` (El Debs, 1ª ed. 2003; **baseada na NBR 8890:2003**) | cargas de solo (vala, aterro), sobrecargas, fator de berço Tab. 4.1 (A 2,25-3,4; B 1,9; C 1,5; D 1,1) p. 37; **classe do tubo Fens = γ(q + qm)/α, γ = 1,0 fissura e 1,5 ruptura** p. 45-46; **recobrimento mínimo hs ≥ 0,6 m** p. 29; impacto por cobrimento (1,3 a 1,0) Tab. 3.3 p. 33 | 16-24, 29, 33, 37, 45-46 | **edição 2003**: terminologia "carga de fissura" antiga |
| `LOC-ABTC-HISTORIA-MANNING` (ACPA 2004, trad. ABTC) | n de laboratório × de projeto: fator de 20-30 %; **projeto 0,012 (drenagem) e 0,013 (esgoto)**; lab. 0,009-0,011 | Tab. 1 p. 5; testes p. 6-9 | explica o n ≈ 0,0093 do legado do Xingó |
| `LOC-ABTC-COMPARACAO-CONCRETO-POLIMERO` | n = 0,013 independente do material; **documento de posição do fabricante** | 4-5 | tratar como fonte interessada |
| `LOC-ABTC-PROJETO-ESTRUTURAL-ADUELAS` (NBR 15396:2017) | galeria celular e canal em U; **é de estruturas**; aqui só como alternativa quando a classe passa de PA4 | 8-85 | delegar `estruturas` |

Armadilhas: (1) o `_texto` da Tab. 4 de HISTORIA sai com colunas trocadas; (2) **não há tabela de altura de aterro mínima e máxima por classe e DN** da NBR 8890:2020 (só o software da ABTC); (3) as ES do DNIT (015, 023) citam a edição **2003**; (4) TUBOS (2003) × ALTERACOES (2020): a **tabela de classes é igual**, mudam terminologia, tipos de reforço e a proibição de MF abaixo de DN 500. Classe de tubo aqui é **indicativa**; o dimensionamento estrutural é de `estruturas` (`tubos.classe_de_tubo`, `fator_berco_vala(fonte="abtc")`).

## ILRI 16 (Drainage Principles and Applications) e ILRI 56 (Envelope Design)

**ILRI-DPA16**: Pub. 16, **2ª ed. rev. 1994**, ILRI/Wageningen, 1.124 p. (`ILRI-DPA16`, corpus do Hidráulico, repositório WUR; **baixado depois do MAPA, sem mapa**); licença aberta. **Física = impressa − 2** nos trechos conferidos (Hooghoudt 8.2.1: sumário 265, texto na física 263).

| Tema | Página física (impressa) | Status |
|---|---|---|
| Cap. 4 Estimating Peak Runoff Rates (CN, hidrograma): 4.4 Curve Number Method | impr. 111-142 (CN impr. 121) | índice conf.; páginas físicas a confirmar |
| Cap. 8 Subsurface Flow to Drains: **Hooghoudt (8.2.1) p. 263; Ernst (8.2.2) p. 270 (eq. 8.21 p. 272); Glover-Dumm (8.3.1) p. 283-284; De Zeeuw-Hellinga; comparação estacionário × transiente p. 290-292** | 263-292 | conf. |
| Recomendação do ILRI: **usar Hooghoudt também em 2 camadas quando o dreno está na interface** (Eq. 8.7); Ernst é para dreno acima ou abaixo da interface; "com perfil homogêneo, Ernst dá ≈ Hooghoudt, e **o Hooghoudt não tem a restrição de profundidade**" | 274 | conf. |
| Exemplos resolvidos de espaçamento (q = 1 mm/d; K = 0,14 m/d; D = 4,8 m; dois estratos; Glover-Dumm em irrigação Ex. 8.5) | 276-286 | conf. |
| Cap. 12 condutividade hidráulica; cap. 10 ensaios de aquífero; cap. 9 percolação de canal (9.7) | impr. 332, 341 | índice conf. |

Armadilhas: (1) página impressa × física (−2): use a física com a impressa entre parênteses; (2) a restrição de profundidade do Ernst (espaçamento calculado "geralmente pequeno" para camada impermeável funda) [p. 274]; (3) o **fator 1,16** do Glover-Dumm **não está no ILRI 56**; vem das Embrapa Maniçoba p. 2 e Bebedouro p. 5 e do NEH (`drenos.glover_dumm_espacamento(fator=1.16)`); (4) o caso Embrapa Maniçoba mostra Hooghoudt superestimando L em 24 % e Glover-Dumm subestimando em 30 % (p. 1): **declarar a incerteza do método**.

**ILRI-56-ENVELOPE** (Vlotman, Willardson, Dierickx, 2000; 380 p.; edição única; aberta; fronteira com geotecnia, D-86 do CDV; **PDF = impressa + 20**): necessidade de envoltório e discrepâncias entre critérios p. 27-47 (**fluxograma Fig. 7 p. 47**, HFG = exp(0,332 − 0,132·K + 1,07·ln PI)); critérios hidráulico e de retenção granulares p. 53-72 (pontos de controle p. 66-68; **ponte** p. 70); sintético p. 76-88; K por granulometria p. 173-176 (Tab. 14 p. 175); critérios existentes p. 269-301 [mapa; p. 47 conf.]. **Sem exemplo numérico completo de envoltório** (Figs. 11-12 são faixas desenhadas). O que é critério hidráulico entra no Drenagem (`criterio_de_filtro_hidraulico`); **filtro real, piping e ensaio são da Geotecnia**.

## Outras fontes de drenagem agrícola e canais (só localizar)

`EMBRAPA-MANICOBA-1988` (campo, Juazeiro-BA, p. 1-3, 7-8), `EMBRAPA-BEBEDOURO-1986` (OCR degradado: **não usar número sem a imagem**), `EMBRAPA-ESPACAMENTO-1990` (laboratório; Donnan-Hooghoudt S médio 154,5 cm contra 149 cm, p. 10), `WATERLOG-DRAINAGE-EQUATION` e `WATERLOG-ENDRAIN` (conferência com ILRI 16; exemplos 1-4 p. 7-10; L = 51,8 m no Ex. 4), `LOC-COMAER-EDMIR` (drenagem de **pavimento aeroportuário**, não agrícola), `NRCS-CPS608-2023` (sem limite numérico de velocidade), `FHWA-HEC11` (rip-rap de canal, Eq. 6 p. 48; dissipador é do Hidráulico), `USGS-WSP1849` (n por fotos de 50 canais, p. 16-215), `FAO-IDP62` (Hidráulico; leiaute p. 109-122, diâmetro de dreno com a = 0,3164/0,40/0,77 p. 211-224). **FAO-38 e NRCS-CPS606/607 não foram abertos** (`PENDENTES_DOWNLOAD_MANUAL.md`, `NAO_ABERTOS.md`).
