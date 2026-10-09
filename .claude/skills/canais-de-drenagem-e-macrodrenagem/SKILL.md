---
name: canais-de-drenagem-e-macrodrenagem
description: >
  Canais de drenagem e macrodrenos de perímetro irrigado e estrada de serviço: seção trapezoidal e composta por Manning, regime e Froude (A/T), velocidade admissível e mínima (DNIT Tab. 31 x EM 1110-2-1601), folga, revestimento (terra, concreto, rip-rap de canal por HEC-11, gabião por HEC-15), degraus, deságue, talvegues interceptados pela faixa do canal de adução (CDV D-56, D-85) e conferência de planilha de projetista. Use quando: "dimensionar o dreno", "macrodreno", "seção do canal de drenagem", "velocidade admissível do dreno", "folga do dreno", "rip-rap do canal", "gabião ou tubo", "deságue", "degrau do dreno", "talvegue cortado pela faixa", "dreno lateral ao adutor". Não use para: canal de adução, sifão, aqueduto (canais-abertos, Hidráulico); dissipador de saída de bueiro (D3, vertedouros-e-dissipadores); bueiro (bueiros-e-travessias); vazão (hidrologia-de-projeto-para-drenagem); sarjeta e descida (drenagem-de-estradas-e-plataformas); dreno de parcela e de fundo (drenagem-subsuperficial); preço.
---

# Canais de drenagem e macrodrenagem

> Não repete o núcleo `drenagem-fundamentos` (convenções, Froude com A/T, fluxo de 8 passos, protocolo `[DELEGAR]`, parecer, modo CDV, armadilhas transversais): aponta para ele.
> Páginas = página física do PDF. IDs do Hidráulico citados pelo ID dele (D1). Acervo em `doc:pág`, sem ✓h. Tabelas longas em `references/`.

## 1. Escopo e fronteiras

**Dentro:** canal de drenagem natural, desviado ou escavado (macrodreno, dreno coletor e de saída, dreno de proteção e de interceptação, dreno lateral a canal de adução); seção, Manning, regime, velocidade, folga, revestimento,
rip-rap **de canal**, degraus (posição e altura), deságue, interceptação de talvegues pela faixa do canal (CDV D-56 e D-85, enunciado no cartão do Gestor; ver `references/talvegues-desague-quedas.md`) e conferência de planilha de projetista.

**Fora, e para quem** (`[DELEGAR: <id>]`; o especialista solicita, o Gestor aprova):

| Assunto | Quem |
|---|---|
| Canal de adução, sifão, aqueduto, ponte-canal, borda livre e velocidade de canal de irrigação; decisão canal x sifão x aqueduto x bueiro | `hidraulica` (`canais-abertos`); o Drenagem entrega Q, TR e cota de inundação a montante |
| Dissipador, rip-rap e bacia **na saída de bueiro ou de estrutura** (D3); desenho de queda e rápido | `hidraulica` (`vertedouros-e-dissipadores`); aqui só V, Fr, y de saída e o aviso |
| IDF, chuva de projeto, ARF | `clima` (`chuvas-intensas-e-idf`); a vazão é de `hidrologia-de-projeto-para-drenagem` |
| Bueiro sob o dreno ou sob a estrada (HDS-5) | `bueiros-e-travessias` |
| Valeta, sarjeta, descida d'água de estrada | `drenagem-de-estradas-e-plataformas` |
| Dreno de parcela, dreno de fundo, subpressão sob revestimento | `drenagem-subsuperficial` |
| Talude, filtro sob rip-rap, piping, escavabilidade, rocha | `geotecnia` |
| Greide da faixa, volumes, conflito com o aterro do canal | `terraplenagem` |
| Estrutura de concreto do canal revestido | `estruturas` |
| Custo por alternativa (gabião x tubo x concreto, seção) | `orcamento` |
| Vazão excedente de irrigação que o dreno recebe | `irrigacao` |

**Nível.** Anteprojeto (padrão): vazão por talvegue, seção-padrão por Manning, V e folga com a fonte declarada, deságue e degraus por estaca. Básico (quando pedido): perfil com cotas, regime e transições,
rip-rap por HEC-11 com SF justificado, tensão do revestimento. Executivo: só confere a planilha do projetista (casos Salitre e Delmiro). **Não coberto:** drenagem urbana em rede e aeroportuária (núcleo, seção 4).

## 2. Dados mínimos específicos

| Dado | Unidade | Premissa aceitável se faltar (rotular, com a consequência) |
|---|---|---|
| Q por trecho, TR e método (vem de hidrologia) | m³/s | bloqueia: pedir; Q e TR não se chutam |
| Traçado e perfil: cota de fundo ou declividade S, extensão | m, m/m | S do terreno com quedas de 1,0 m onde V excede o limite (aviso) |
| Material e revestimento; n | — | n por material em `../bueiros-e-travessias/references/velocidades-admissiveis-e-revestimentos.md` §3-4; dizer se é n novo ou envelhecido |
| Talude z (H:V) e largura de fundo mínima | — | 1,5:1 a 2:1 (USBR: até 3:1 se necessário); b mínima 1 m por equipamento [CDV-MANUAL-IRRIG p. 514] |
| V admissível **e V mínima**, com a fonte | m/s | V adm: DNIT Tab. 31, critério "min"; V mín: pedir; alternativa rotulada 0,43 m/s (CPS 608) |
| Folga ou borda livre exigida | m | 25 % do tirante, **padrão provisório, decisão F7**; mostrar alternativas |
| Altura da seção adotada h (para conferir planilha) | m | — |
| Ponto de deságue: cota, NA e material do receptor | m | tailwater = lâmina normal do receptor, rotulado |
| Para talvegue interceptado: estaca, cota do talvegue e do fundo do canal, bacia, uso da faixa | — | pedir ao Hidráulico e à Terraplenagem |
| Para rip-rap: V e d médios do canal principal, talude, φ, Ss, raio de curva/largura | m/s, m | Ss 2,65; SF 1,2 em trecho reto; φ rotulado |

## 3. Método por nível

### 3.1 Anteprojeto

1. **Q e TR.** Vem de `hidrologia-de-projeto-para-drenagem`; o parecer mostra TR e risco (`hidrologia.risco_hidrologico`). TR de canal é critério, não fórmula: USBR 5 anos (proteção e travessia maior, 25 em grandes sistemas),
   NEH 650-9 10 anos em terra agrícola, HEC-15 5-10, PISF e Sertão 100 [`references/velocidade-folga-tr-por-fonte.md` §5]. Declarar a escolha; **padrão provisório, decisão F7: TR 10 em drenagem superficial**.
2. **Manning.** Q = A·R^(2/3)·S^(1/2)/n em SI (conferido: EM 1110-2-1601 App. H, Tab. H-1 [USACE-EM1601 p. 179]). Trapézio: A = (b + z·y)·y; P = b + 2y·√(1+z²); T = b + 2z·y. y normal por bissecção.
   **Fr = V/√(g·A/T)**, nunca com y ou D; Fr entre 0,89 e 1,13 é escoamento instável, evitar [FHWA-HEC11 p. 38]. Tirante crítico: Q²/g = A³/T. Seção composta (canal principal + bermas) por seção dividida, interface fora do perímetro molhado: método corrente, sem página no corpus.
3. **Velocidade.** Verificar V <= V adm **e** V >= V mín. As tabelas divergem (areia fina: DNIT 0,30-0,40; EM-1601 0,61; PISF terra 0,70; Embrapa 0,5): declarar fonte e critério (`references/velocidade-folga-tr-por-fonte.md` §1-3).
   Rip-rap e gabião não têm linha na Tab. 31 nem na Tab. 2-5: verificar por tensão (HEC-15), à mão e rotulado (sem função).
4. **Folga.** folga = h − y_n >= fração x y_n; **25 % é padrão provisório, decisão F7** (origem: memorial de Delmiro [1520:129]; não é norma). Alternativas com fonte: 0,15 m (CPS 608, HEC-15), 0,20 m (Embrapa),
   USBR por vazão (0,15 a 0,69 m nos exemplos), EM-1601 (0,6-0,8 m, escala de rio). Mostrar a tabela e o que muda na altura da seção.
5. **Degraus.** Onde o terreno leva V acima do limite: queda de 1,0 a 1,5 m (Salitre) ou módulos de 0,25 m (Delmiro); a skill dá posição e altura; o desenho da queda é da Hidráulica.
6. **Deságue.** Cota do receptor, tailwater, entrada lateral protegida, estaca zero no deságue (`references/talvegues-desague-quedas.md` §4).
7. **Talvegues interceptados.** Inventário por estaca, alternativa (travessia, dreno de proteção, captação limitada a 10 % da capacidade do canal), seção-padrão, afastamento mínimo 6,00 m (Sertão) (`references/talvegues-desague-quedas.md` §2-3).
8. **Reconciliar números do documento:** soma das extensões × total declarado; um limite de V ou dois; lista de trechos com folga fora do critério (`verificar_trechos`).

### 3.2 Projeto básico

- Perfil com cotas de fundo e linha d'água: em subcrítico, y_n a jusante do trecho; transição gradual de 3 m ou mais, ou pelo menos 30° em diedro (Sertão); proteção contra erosão onde a profundidade aumenta no sentido do fluxo [CDV-MANUAL-IRRIG p. 518, §11.3.5.2].
- **Rip-rap de canal (HEC-11):** D50 = C·0,001·V³/(d^0,5·K1^1,5) com V e d do canal principal, SF por curvatura, extensão 1,0 W a montante e 1,5 W a jusante da curva; n por EM-1601 ou HEC-11 (**divergem, sem conciliação, F7**); filtro é da Geotecnia.
  Detalhe, gradação e exemplo (D50 = 0,43 ft [FHWA-HEC11 p. 72]; formulário preenchido p. 78) em `references/revestimento-riprap-gabiao.md` §2.
- **Gabião (HEC-15 Cap. 7):** n por D50 da pedra; τp = maior de F*·(γs − γ)·D50 (F* = 0,10) e 0,0091·(γs − γ)·(MT + 1,24); exemplo p. 115-117 em `references/revestimento-riprap-gabiao.md` §3. A calculadora **não** tem função de tensão.
- Dreno com vazão contínua pequena e cheias intermitentes: canal piloto no eixo [CDV-MANUAL-IRRIG p. 514]. Dois estágios: NEH 654 Cap. 10 por referência do CPS 608 [NRCS-CPS608-2023 p. 2]; o capítulo está no corpus do Hidráulico [NRCS-NEH654-CH10] (Two-Stage Channel Design), não lido nesta skill.
- Grama: capacidade com a vegetação mais densa e alta, estabilidade com a menos densa [NRCS-NEH650-CH07 p. 11].
- Bueiro sob o dreno ou a estrada: `bueiros-e-travessias`; dissipador: D3.

**Exige projetista ou consultoria:** estabilidade de talude do canal em corte de rocha, filtro sob rip-rap, modelo de remanso em rede de macrodrenos com confluências (HEC-RAS, D2), sedimento.

## 4. Calculadoras (mapa fórmula → função → teste)

Módulo `tools/dren/canais_drenagem.py` v0.1.1 (stdlib). CLI: `python -m tools.dren.canais_drenagem --json '{"funcao": "...", ...}'`; `--listar` mostra as funções. Saída: `entradas`, `saidas`, `metodo`, `avisos`, `versao`.

| Fórmula / cálculo | Função | Teste (`tests/dren/test_canais_drenagem.py`) | O que conferir nos `avisos` |
|---|---|---|---|
| Manning trapezoidal, y normal e crítico, V, Fr (A/T), regime, folga | `canal_trapezoidal(Q,b,z,n,S,h_secao,fracao_folga)`, `manning_trapezoidal`, `profundidade_normal`, `profundidade_critica` | `test_em1601_tab_h1_*`, `test_acervo_salitre_*`, `test_acervo_delmiro_ds11c_*`, `test_critica_retangular_*` | Fr 0,89-1,13 instável; folga < mínimo; transborda; "padrão provisório, decisão F7" |
| Capacidade com a seção cheia (coluna "Q DRENO" das planilhas) | `capacidade_trapezoidal(b,z,h,n,S)` | `test_acervo_salitre_dt416a_manning` | é capacidade, não demanda: não confundir com y_n |
| Seção composta | `manning_composto`, `profundidade_normal_composta` | `test_composto_*` | "bermas secas" se y <= h_main; sem teste de livro |
| V admissível (DNIT Tab. 31 ou EM-1601 Tab. 2-5) | `velocidade_admissivel(material, fonte, criterio)` | `test_velocidade_admissivel_dnit_e_em1601_divergem` | material sem linha → limite legado; nota 2 da grama; escolher a fonte |
| V <= V_max e V >= V_min | `verificar_velocidade(V, V_max, V_min)` | `test_verificar_velocidade_vmin_sem_padrao` | "V_min não informada: sedimentação não verificada" |
| Dois limites no mesmo documento | `verificar_limites_alternativos(V, limites)` | `test_salitre_n2_dois_limites_de_velocidade` | `conflito = true`: pedir qual vale |
| n de rip-rap | `n_riprap(D, metodo, uso)` | `test_n_riprap_strickler_forma_e_divergencia` | S < 2 % (EM-1601); D90 min x D50; divergência registrada |
| D50 de rip-rap de canal | `d50_riprap_hec11(V,d,Ss,SF,z,phi,K1)` | `test_hec11_exemplo1_d50`, `test_hec11_k1_*`, `test_hec11_correcoes_*` | θ >= φ → erro; talude mais íngreme que 1,5H:1V; SF < 1; SF por curvatura |
| Borda livre; tirante x altura; lote de trechos | `borda_livre`, `verificar_secao`, `verificar_trechos` | `test_borda_livre_provisoria_25_pct`, `test_acervo_delmiro_d1_*`, `test_verificar_trechos_*` | folga negativa = transborda; % de trechos fora do critério |
| Extensões | `reconciliar_extensoes(parcelas, total)` | `test_salitre_n1_reconciliacao_de_extensoes` | diferença e parcela omitida |

Exemplo: `python -m tools.dren.canais_drenagem --json '{"funcao": "canal_trapezoidal", "Q": 0.518, "b": 0.6, "z": 1.5, "n": 0.025, "S": 0.00368, "h_secao": 0.45}'` → y_n 0,4316 m, V 0,962 m/s, Fr 0,576, folga 0,018 contra mínimo 0,108 m: aviso.
**Não implementado:** D30 do EM-1601 (Eq. 3-3, Sf, Cs, CV, CT incompletos); tensão trativa e τp (HEC-15); escolha automática da seção-padrão; remanso; dissipador de saída (D3). Dado dessas lacunas, rotular o cálculo manual.

## 5. Critérios de verificação

Aplicam as verificações mínimas do núcleo (seção 3, passo 4). Reportar cada uma como atendida, violada ou não aplicável.

| Verificação | Critério nesta disciplina | Como reportar |
|---|---|---|
| Regime e Froude | Fr com A/T; fora de 0,89-1,13; supercrítico só com estrutura que o admita | valor e regime |
| Velocidade | V <= V adm da fonte declarada; V >= V mín declarada; **ambos os limites do documento se houver dois** | resultado por limite; conflito destacado |
| Folga | h − y_n >= critério declarado (padrão 25 %, provisório); folga < 0 = transborda | % de trechos fora; lista |
| Coerência de perfil | cotas de fundo monótonas; S de projeto = (desnível − quedas)/L; degrau coerente (Hd = cota montante − jusante) | trecho a trecho |
| Cota de inundação | nível a montante de travessia abaixo da cota do aterro e da faixa | m de margem |
| Faixa de validade | n em 0,010-0,100; EM-1601 Eq. 3-2 só S < 2 %; HEC-11 só escoamento uniforme ou gradualmente variado | aviso reproduzido |
| Interfaces | Q e TR de Clima/hidrologia citados; travessia e dissipador delegados | bloco `[DELEGAR]` |
| Total e contagem do documento | soma das parcelas = total declarado; chave única por dreno | `reconciliar_extensoes` |

## 6. Armadilhas do acervo (casos negativos reais)

Regra mestra do núcleo: **apontar a divergência com evidência e consequência; nunca corrigir o projeto em silêncio.** Detalhes e comandos em `references/casos-e-gabaritos.md`.

| Armadilha | Onde apareceu | Como detectar |
|---|---|---|
| Seção menor que o tirante: ZTT01 h 0,20 m com y_n 0,331 m (folga −0,131 m) | Delmiro DT-2.23.1 [1521:165; 1520:134] | `verificar_secao`; tirante <= altura em todos os trechos |
| Folga adotada < 25 % do tirante em 84 de 194 trechos (43 %); memorial admite "folgas menores" | Delmiro [1520:129; 1521:120-187] | `verificar_trechos`; relatar % e lista |
| Seção cheia = tirante (folga 0,008 m), coluna de borda livre vazia | Salitre DS-4.1/A [1585:99] | comparar h × y_n; é lacuna do memorial, não violação |
| Extensão total não fecha (72.858,41 contra 74.884,41; falta Mulungú 2.026,00 m) | Salitre N1 [1584:97] | `reconciliar_extensoes` |
| Dois limites de V (0,30-1,2 contra 0,3-1,5); seis trechos mudam de status | Salitre N2 [1584:105; 1585:97-123] | `verificar_limites_alternativos` |
| Critério de 1,80 m aplicado só em parte dos drenos; seção 2,1 a 2,6 vezes a demanda | Salitre N3 | comparar Q dreno × Q trecho |
| Talvegue com L = 20.040 m (dez vezes o das vizinhas) | Salitre 4W21-6 [1584:99] | razão L/área fora do envelope; checar antes de Tc |
| "V mínima" citada sem valor; V < 0,5 m/s em 10 trechos | Delmiro D4 [1520:129; 1521:171] | pedir o valor; sem padrão |
| Nomes de dreno duplicados e prefixos trocados no quadro de extensões | Delmiro D3 [1520:136-137] | chave única; conciliar quadros por nome |
| n do gabião 0,02-0,035 na planilha, abaixo do HEC-15 (0,047-0,069 para D50 0,10-0,15 m); lâmina 80 % x 85 %; rótulo "declividade (%)" com valor em m/m | retroanálise gabião x tubo (D8) | `capacidade_trapezoidal` com n alternativo; conferir rótulo × unidade |
| Q dreno (capacidade) lido como demanda | planilhas Salitre | separar "Q trecho" e "Q DRENO" |
| Dreno recebendo enxurrada pelo talude; captação de chuva em canal revestido sem limite | prática USBR [CDV-MANUAL-IRRIG p. 316-317, 515] | aterro de bordo e entrada conformada; captação <= 10 % da capacidade |

## 7. O que a norma exige e a quem se aplica

Detalhe de cada fonte em `drenagem-normas-e-manuais`; aqui só a regra que cruza fontes.

- **Nenhuma norma brasileira fixa** V, folga ou TR de dreno de perímetro irrigado. DNIT-DREN (IPR-724, 2006) é manual de **rodovia**: Tab. 31 de velocidade [DNIT-DREN p. 131] e Tab. 34 de n [p. 132-134] são referência cruzada para dreno agrícola, não exigência.
- EM 1110-2-1601 (1994) e HEC-11 (1989), HEC-15 (2005): manuais norte-americanos de **canal de controle de cheia, rip-rap e canal flexível**; critério de comparação, escala de rio (borda livre de 0,6 a 0,8 m).
- NRCS CPS 608 (ago/2023, vigente): padrão para dreno principal ou lateral **agrícola**; V mínima 1,4 fps sem informação local, folga 0,5 ft, n envelhecido [NRCS-CPS608-2023 p. 2]; não dá V máxima numérica.
- USBR, Manual de Irrigação (cap. 11, tradução Codevasf): referência de dreno de irrigação, TR 5, 25 e 100 conforme a obra; **tabela de V do cap. 11 ilegível na extração**.
- Material `FORNECIDA-PELO-USUARIO` ou não aberto (CPS 582, NBR 8890; NEH 654 Cap. 10 existe no corpus do Hidráulico, ainda não lido): citar obra e página, não transcrever. A tabela do DAEE vale como critério de outorga em SP; fora de SP é referência.
- O número do projetista não é gabarito sem ✓h; o do método não vira "o certo" sem os dados que o projetista tinha.

## 8. Referências

| ID | Uso | Páginas-chave |
|---|---|---|
| USACE-EM1601 (EM 1110-2-1601, Ch. 1, 1994) | V admissível, rip-rap, borda livre, n | Tab. 2-5 p. 25; borda livre p. 23; Eq. 3-2 p. 29; Cap. 3 p. 26-39; App. H p. 178-179 |
| FHWA-HEC11 (1989) | rip-rap de revestimento | Froude p. 38; Eq. 6-9 p. 48-49; SF p. 49-50; extensão p. 42; Tab. 3 p. 55; Exemplo 1 p. 70-75 (D50 p. 72, formulário p. 78); Eq. 20 p. 166 |
| FHWA-HEC15 (2005) | n por revestimento, tensão, gabião | Tab. 2.1-2.2 p. 29; τd p. 31; Tab. 2.3 p. 33; TR e folga p. 33-34; gabião p. 113-117 |
| NRCS-CPS608-2023 | dreno agrícola principal e lateral | p. 1-3 |
| NRCS-NEH650-CH09 (2009) e CH07 (2007) | desvio, TR e folga; canal gramado | Tab. 9-1 p. 16; saídas p. 15; CH07 p. 7, 11, 22 |
| DNIT-DREN (IPR-724) | V máxima, n | Tab. 31 p. 131; Tab. 32-34 p. 131-134 |
| CDV-MANUAL-IRRIG (USBR) | drenos de irrigação, captação de chuva no canal | cap. 11 p. 511-518; §6.3.8 p. 316-317 |
| SRHCE-GED-030, GED-018 | PISF: n, V, borda livre USBR, profundidade máxima | GED-030 p. 20; GED-018 p. 27 |
| EMBRAPA-DREN-SUP (1984) | dreno de pivô central, semiárido | p. 5-8 |
| Casos (`casos/drenagem/`) | Salitre, Delmiro, Sertão, gabião | índice em `_INDICE.md` |

## 9. Lacunas do corpus e pontos abertos

- **Pontos abertos F7 tocados aqui** (não decididos): folga de 25 % (alternativas em `velocidade-folga-tr-por-fonte.md` §4); n de rip-rap EM-1601 x HEC-11; TR 10 e tc_min 5 min de drenagem superficial (hidrologia).
- Sem função de tensão, de τp de gabião, de D30 (EM-1601), de remanso, de escolha de seção-padrão. HEC-11 gabião (p. 97-105) e Cap. 4-5 do HEC-15 (vegetação, RECP) não reabertos.
- Tabela de V do USBR (p. 515) e de quedas (p. 518) com extração corrompida: conferir no PDF. EM-1601 Plates 29-30 (pedra maior que cascalho fino) não lidas.
- Sem texto de CDV D-56 e D-85 (vem no cartão); sem V crítica nem Q por dreno do Sertão Pernambucano; gabarito de planilha sem ✓h; Salitre N4 e N5 pedem conferência humana na página.
- IDF para o norte da Bahia: Clima. Sedimento e remanso em rede: consultoria.
- Testes sugeridos (ID, página, números): HEC-15 exemplo de gabião (p. 115-117: Q 0,28; S 0,09; B 0,60; z 3; d 0,185 m; n 0,055; τp 241; τd 163 N/m²); NEH 650-9 Tab. 9-1 (p. 16); CPS 608 (V mín 1,4 fps = 0,4267 m/s; folga 0,5 ft = 0,1524 m, p. 2); PISF borda livre (GED-030 p. 20).

## Revisão técnica

2026-10-08, revisor Opus (F7). **21 itens amostrados; 18 conferidos sem mudança, 3 corrigidos, 3 pendentes.**

- **Conferidos no primário:** CPS 608 V mín 1,4 fps e folga 0,5 ft [NRCS-CPS608-2023 p. 2]; Fr 0,89-1,13 [FHWA-HEC11 p. 38]; Eq. 6 (0,001 V³/(d^0,5 K1^1,5)) p. 48, Eq. 8 (2,12/(Ss−1)^1,5) p. 49, SF por R/W p. 50, extensão 1,0 W/1,5 W p. 42, Eq. 20 (0,0395 D50^(1/6)) p. 166; HEC-15 Tab. 2.1-2.2 p. 29, Tab. 2.3 p. 33, TR 5-10 p. 33, folga 0,15 m p. 34, gabião F* 0,10 e Eq. 7.2 (MTc 1,24 m) p. 113-114, exemplo τp 241 / τd 163 N/m² p. 117 [FHWA-HEC15]; EM-1601 Tab. 2-5 (os 14 valores do código) p. 25, Eq. 3-2 (K 0,034/0,036/0,038; S < 2 %) p. 29, borda livre 2-2,5 ft p. 23, Tab. H-1 p. 179 [USACE-EM1601]; DNIT Tab. 31 (areia fina 0,30-0,40) p. 131 e Tab. 34 p. 132-134 [DNIT-DREN]; b mín 1 m, talude 1,5:1-2:1 (até 3:1), canal piloto p. 514, transição ≥ 3 m p. 518, captação ≤ 10 % p. 316 [CDV-MANUAL-IRRIG]; PISF V 0,70/3,00/4,50/5,00 e borda livre USBR por log Q [SRHCE-GED-030 p. 20]; NEH 650-9 Tab. 9-1 [NRCS-NEH650-CH09 p. 16]; Embrapa V 0,5, Fr 0,89, folga 0,20 m [EMBRAPA-DREN-SUP p. 7].
- **Calculadora:** as 16 funções do §4 existem com o nome e a assinatura citados; os 16 padrões de teste existem em `tests/dren/test_canais_drenagem.py` (33 passam); o exemplo do §4 reproduz (y_n 0,4316; V 0,962; Fr 0,576; folga 0,018 x 0,108).
- **Corrigido:** (1) versão do módulo v0.1.0 → v0.1.1; (2) Exemplo 1 do HEC-11: o D50 = 0,43 ft está na p. 72 (p. 78 é o formulário), também em `references/revestimento-riprap-gabiao.md` §2; (3) NEH 654 Cap. 10 constava como "não aberto": está no corpus do Hidráulico [NRCS-NEH654-CH10].
- **Pendentes:** tabela de V do USBR (p. 515) e de quedas (p. 518) ilegíveis no texto: conferir no PDF; HEC-11 Tab. 3 p. 55 não aberta; números do acervo (Salitre, Delmiro) seguem sem ✓h.
- **Fronteiras:** D3 e matriz §3.3 coerentes com o §1; descriptions das skills irmãs apontam para esta sem colisão. Fora desta skill: `vertedouros-e-dissipadores` (Hidráulico), tabela de fronteiras, devolve "rip-rap e bacia de impacto na saída de bueiro" ao Drenagem, contra D3 e contra a própria description.
- **Decisões do André** (não decididas aqui): (a) **V mínima de dreno**: sem padrão (código atual) x 0,43 m/s (1,4 ft/s) [NRCS-CPS608-2023 p. 2] x 0,30 m/s (Salitre [1584:105]); efeito: no Delmiro, o trecho de V 0,292 falha nos dois pisos e os demais dos 10 abaixo de 0,5 dependem do piso; recomendação: 0,43 m/s rotulado quando o projeto não declara. (b) **Folga** (F5, "folga de dreno"), dado novo: com max(0,25 y; 0,15 m), que soma o 25 % ao mínimo de CPS 608 p. 2 e HEC-15 p. 34, DS-1.1/C passa de 0,108 a 0,15 m (h mín 0,54 → 0,58 m) e Salitre DS-4.1/A fica em 0,373 m; recomendação: adotar o max.
