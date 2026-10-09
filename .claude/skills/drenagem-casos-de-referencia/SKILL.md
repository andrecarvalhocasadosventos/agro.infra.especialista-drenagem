---
name: drenagem-casos-de-referencia
description: >
  Usa projetos reais do acervo como fonte de prática em drenagem: os 26 casos de casos/drenagem (Baixio de Irecê, CSB e
  Salitre, Iuiu 2002 e 2018, Jaíba, Xingó, Delmiro Gouveia, CAC, Sertão Pernambucano, gabião), mapa problema -> caso,
  lições dos casos negativos com o teste que as revela, protocolo de busca (consultar.py), marcas de ancoragem (nenhum
  caso tem ✓h), registro de caso novo e a regra de apontar divergência com evidência, sem corrigir o projeto. Use quando:
  "como o projeto X dimensionou o bueiro", "que TR/C/n o Delmiro usou", "compare com Baixio/Iuiu/Salitre", "esse número
  pode ser gabarito?", "o projeto errou?", "busque no acervo", "caso novo". Não use para: fórmula e critério
  (use hidrologia-de-projeto-para-drenagem, bueiros-e-travessias, drenagem-de-estradas-e-plataformas,
  canais-de-drenagem-e-macrodrenagem, drenagem-subsuperficial); o que a norma exige (use drenagem-normas-e-manuais);
  canal, adutora, sifão, dissipador (Hidráulico); IDF (Clima); preço; núcleo (use drenagem-fundamentos).
---

# Casos de referência de drenagem: projetos reais como gabarito de comparação

Skill "por fonte". Não traz fórmula: a fórmula está na skill da disciplina. Traz **o que projetistas reais fizeram**, a
**disciplina de uso** e os **erros que eles cometeram**. Convenções, V-regras, delegações e a regra mestra estão em
`drenagem-fundamentos` (§9). Só drenagem: caso de canal de adução, sifão, adutora ou vertedouro é do Hidráulico
(`../Especialista Hidraulica/casos/`), não duplicar aqui.

## 1. Regras de uso (valem para todo caso)

1. **Prática não é norma.** O projeto mostra o que a projetista fez. O agente compara com o método da skill da
   disciplina e **explica a diferença** (outra época, outro risco, simplificação, erro). Nunca "o projeto X adotou,
   logo vale".
2. **Todo número com fonte e marca.** `doc:página` + marca de ancoragem (`✓`, `✓*`, `~`, `!`, `·`, `✓h`, `✗h`; tabela
   no `consultar-acervo`). Planilha .xls/.docx: citar o bloco, não "página".
3. **Nenhum caso de drenagem tem `✓h`.** Os 16 casos de 2026-10-08 dizem isso por escrito ("Nenhum `✓h`", "pendente
   de `✓h`" ou "`✓h` (nenhum)", no cabeçalho ou na seção de rastro); os 10 herdados (2026-10-02) também não têm
   conferência humana registrada. Logo: todo
   número de caso entra no parecer como **"valor do projeto, não conferido"**. `!`, `~`, `✓*` e `·` nunca viram
   gabarito sem `✓h`. Promover = emitir o comando de conferência pontual (§4) e esperar o veredito do André.
4. **Qualidade do rastro** (índice): A reproduzível; B método ou entradas literais com coeficiente ou coluna inferido;
   C descritivo. Só A serve de gabarito numérico de teste, e ainda como "acervo, sem check-h". B e C ilustram método e
   armadilha. Inferência é rotulada ("n inferido", não "n do projeto").
5. **Divergência > 5 % entre calculadora e projeto** vira `xfail(strict=True)` + linha em `tools/dren/DIVERGENCIAS.md`
   com a hipótese; a fórmula **não** é ajustada "para bater". Tolerância: 1 % contra livro, 5 % contra acervo.
   Divergência < 5 % é nota.
6. **Nível do documento** (anteprojeto, básico, executivo) vem no campo `nivel` do caso; comparar o mesmo nível.
7. **Não copiar o projeto.** Memória de terceiros dá método e ordem de grandeza. Premissa de projeto novo vem dos dados
   do próprio empreendimento.

## 2. Regra mestra: apontar a divergência, não corrigir o projeto

Diante de projeto do acervo (ou do usuário) que diverge do método, o agente escreve **quatro linhas**, sempre:

1. **O que o projeto fez**: valor, `doc:pág`, marca.
2. **O que o método dá**: comando da calculadora com as entradas (ou `[ID p. N]`), e os `avisos`.
3. **Diferença e consequência**: em % e em efeito (HW, folga, velocidade, custo, segurança). Diz se é contra ou a favor
   da segurança.
4. **O que decidir e quem decide**: projetista (esclarecer entrada), André (`D-xx`), ou F7 (padrão provisório).

Proibido: reescrever em silêncio o número do projeto, "ajustar" n, C, Tc ou Ke até fechar, ou chamar de "erro" o que é
critério diferente. Se faltam entradas do projetista (S, L, hietograma), o resultado é **"sem gabarito: faltam
entradas"**, não "o projeto está errado". Os casos negativos abaixo foram achados assim; os que dependem de leitura
humana trazem o rótulo "conferir na página".

## 3. Os 26 casos: catálogo e mapa

Catálogo (3 a 5 linhas por projeto, documentos, qualidade): `references/catalogo-de-projetos.md`. Mapa problema -> caso,
com marca e o que **falta**: `references/mapa-problema-caso.md`. Resumo:

| Problema | Casos (arquivo em `casos/drenagem/`) | Rastro |
|---|---|---|
| Tc, racional, limite de área | `delmiro_gouveia_drenos_lotes_racional_manning`; `cac_trecho1_hidrologia_racional_3_5km2_e_hut`; `xingo_lote1_drenagem_transversal_bueiros` | A; B; B |
| HUT/SCS (CN, Tc, hietograma) | `delmiro_gouveia_hut_bhd1_tr50_bransby_williams`; `baixio_irece_vazoes_hut_scs` | A; B (pico não reproduz) |
| Bueiro tubular ou celular, Manning | `salitre_rc500_800_bueiros_celulares`; `jaiba_etapas3e4_bueiros_greide_manning_y_d_082`; `delmiro_gouveia_bueiros_tubulares_sob_canal_principal` | A; A; B |
| Bueiro com capacidade livre + orifício, TR 25/50 | `baixio_irece_bueiros_dimensionamento`; `iuiu_2002_drenagem_superficial_drenos_bueiros`; `iuiu_2018_bueiros_sob_canal_91_obras` | A; A; B/C |
| Bueiro CSB / Xingó (energia, supercrítico) | `csb_geohidro_drenagem_pluvial_bueiros`; `xingo_lote1_drenagem_transversal_bueiros` | B; B |
| Bueiro afogado, sifão como bueiro | `jaiba_etapas3e4_sifao_bueiro_afogado_controle_saida` | B |
| Valeta de crista/pé, comprimento crítico | `xingo_lote1_valetas_protecao_comprimento_critico`; `cac_castanhao_estrada_acesso_valas_chuva_como_intensidade` | A; B (negativo) |
| Macrodreno trapezoidal, V, deságue | `salitre_etapa2_macrodrenos_trapezoidais_manning`; `sertao_pernambucano_canais_drenagem_laterais_adutor` | A; B |
| Dreno de lote, folga | `delmiro_gouveia_drenos_lotes_racional_manning`; `delmiro_gouveia_drenos_secao_subdimensionada_folga` | A; B (negativo) |
| Dreno de fundo / subpressão | `csb_geohidro_dreno_fundo_canal_subsuperficial`; `delmiro_gouveia_dreno_fundo_canal_comprimento_maximo`; `xingo_lote1_drenagem_interna_canal_subsuperficial` | B; B (negativo); A |
| Drenabilidade do solo, decisão de não drenar | `iuiu_2002_drenabilidade_subterranea_diagnostico` | B |
| Canal em gabião x tubo | `retroanalise_canal_gabiao_vs_tubo_manning` | B |

(Casos de 2026-10-08 têm o prefixo `2026-10-08_` no nome do arquivo.)

**Sem caso**: dreno agrícola com Hooghoudt, Ernst ou Glover-Dumm calculado (nenhum projeto lido o faz: o parecer de
dreno agrícola não tem gabarito de acervo, só de livro: ILRI-DPA16, USBR, Embrapa); sarjeta e descida d'água com
memória de cálculo; documento específico dos CDV D-56/D-85; estudo HARZA 2001 do CAC (citado, ausente do acervo).

## 4. Protocolo de busca (acervo e corpus)

Detalhe e exemplos: `references/protocolo-de-busca.md`. Resumo:

```
$env:PYTHONIOENCODING="utf-8"; $env:ACERVO_RAIZ="C:\bibtec"
# em ../../03. Infraestrutura/Projetos de Referência/_BIBLIOTECA_TECNICA/02_PIPELINE/
python consultar.py buscar "bueiro celular TR 50" --disciplina HID --limite 20
python consultar.py buscar "tempo de concentracao" --doc 1493     # a página dentro do volume
python consultar.py doc 1131                                      # ficha: rotas, extração
python consultar.py parametros --doc 1131 --so-ancorados
python consultar.py ler 1131 --pagina 65                          # teto: 8 páginas por chamada
python 89_app_revisao.py --ids parametro:<id>                     # conferência pontual (humana)
python verificar_acervo.py                                        # deve terminar em OK antes de confiar
```

Ordem: `MAPA.md` -> `buscar` -> `doc` -> `parametros`/`itens` -> `ler`; parar no primeiro passo que responde. Primeiro,
sempre, `casos/drenagem/_INDICE.md`. Somente leitura. Ausência na busca não é ausência no acervo (sinônimo, radical
com `*`, sem filtro); documento de rota `imagem` não é alcançável por texto. Catálogo degradado: dizer antes de
responder. Corpus próprio e do Hidráulico: `drenagem-fundamentos` §7 (cite pelos IDs do corpus, `[ID p. N]`).

**Duplicatas**: Delmiro Gouveia 1520 = 1492 (memorial) e 1521 = 1493 (cálculo) são o mesmo conteúdo; citar um e
anotar o outro; **não contar como duas confirmações**. Idem SRHCE-EI-* do corpus do Hidráulico x acervo.

**Marcas**: nenhum caso de drenagem tem `✓h`. O número `✓*` vai com os dois candidatos; `!` vai com o campo que
diverge; `·` = lido por `ler` (sem linha em `parametros`); "lido na página" é dito assim.

## 5. Como responder "como o projeto X resolveu"

1. Abrir `_INDICE.md` e o caso. Dizer: problema, dados (com marca), método da projetista, resultado, **o que a skill da
   disciplina diz** e a diferença. Citar `doc:pág` e marca; dizer que **não há `✓h`**.
2. Se não há caso, seguir o protocolo (§4) e parar no primeiro passo que responde.
3. Rodar a calculadora (`tools/dren/`) com as entradas do projeto. Veredito: **reproduz** (≤ 5 % ou tolerância do
   caso), **diverge** (> 5 %: §2 e `DIVERGENCIAS.md`) ou **sem gabarito** (faltam entradas).
4. Nomear a diferença: outro limite, outra fórmula de Tc, outro n, unidade trocada, erro de transcrição, simplificação
   (Manning plena no lugar do HDS-5). Consultar `references/licoes-dos-casos-negativos.md` **antes** de aceitar um
   número do acervo.
5. Número que vai para entregável (gabarito de teste, premissa de parecer): conferência pontual e espera do `✓h`. Sem
   ela: "valor do projeto, não conferido".
6. Fechar com o que o caso **não** mostra (nível, premissa ausente, página não lida, coluna inferida).

## 6. Lições dos casos negativos (com o teste que as revela)

Tabela completa, com fonte, números e consequência: `references/licoes-dos-casos-negativos.md`. As nove que mais custam:

| # | Lição | Caso | Teste que revela |
|---|---|---|---|
| 1 | P (mm) usada como i (mm/h): Q 12 vezes menor | CAC Castanhão, valas (1128:106-112) | conferir a dimensão: C·P·A/3,6e6 reproduz as 7 linhas; com I = P·60/tc, Q(VC2) = 2,05 e não 0,171 m³/s |
| 2 | Tc de fórmula com rótulo trocado e velocidade em km/h | Delmiro BHD1 (1494:31, 64; 1492:155) | NERC(13,21 km; 32 m) = 7,65 h e Kirpich = 4,92 h; v = L/tc = 0,49 m/s < 0,5 (`test_delmiro_nerc_x_kirpich_rotulo_e_velocidade`) |
| 3 | Declividade impressa 0,0618 onde as cotas dão 0,0043 | Delmiro BH4.5 (1492:142) | S = ΔH/L em cada linha do Quadro 3.50; marcar \|razão − 1\| > 5 % (57 de 58 conferem) |
| 4 | Capacidade de tubo dreno 4,7 a 6,9 vezes menor que Manning | Delmiro dreno de fundo (1492:105) | `drenos.capacidade_tubo_parcial`; razão entre DN deveria ser D^(8/3) = 2,19 (Ø interno 149 e 200 mm) e o memorial dá 3,25 (2 xfail strict) |
| 5 | Seção menor que o tirante e folga < 25 % em 43 % dos trechos | Delmiro ZTT01 em DT-2.23.1 (1521:165) | `canais_drenagem.verificar_trechos`: tirante 0,331 m > h 0,20 m; 84 de 194 trechos |
| 6 | Total de extensão que não fecha; dois limites de V; talvegue de 20 km | Salitre Etapa 2 (1584:97-105) | `reconciliar_extensoes` (74.884,41 e não 72.858,41 m); `verificar_limites_alternativos` (1,2 x 1,5 m/s); razão L/área |
| 7 | Cota do rasto que sobe 1,79 m para jusante | CAC Trecho 1, B31 (1131:66) | monotonia do perfil e coletor abaixo do rasto (B31 viola os dois) |
| 8 | Bueiro por orifício ou Manning plena: HW 6 a 18 % abaixo | Baixio, CSB, Xingó, Salitre | `bueiros.comparar_legado_hds5`; o maior HW (entrada x saída) governa |
| 9 | n implícito do bueiro 0,013 contra n do memorial 0,015 | Jaíba (1182:43, 65-67) | n que fecha Q = A·R^(2/3)·i^(1/2)/n; com 0,015 a capacidade cai 13 % e 2 linhas passam de Y/D 0,82 |

Também: Froude com y (Baixio; usar A/T), declividade "5 %" onde o contexto pede 0,5 % (Iuiu 2018; planilha do gabião
com 0,003 sob rótulo "%"), limite de altura de célula 1,50 m do texto contra células de 2,00 a 3,00 m (Iuiu 2018), TR 25
no texto e Q50 nas linhas (Iuiu 2018), hmáx repetido em VPC-5/6/7 (Xingó), comparação gabião x tubo com lâminas
diferentes (80 % x 85 %).

## 7. Divergências de acervo já registradas (xfail)

Fonte: `tools/dren/DIVERGENCIAS.md`. São **matéria de treinamento**: o parecer reporta a divergência, não ajusta a
fórmula. Lista com teste, valores e hipótese em `references/divergencias-xfail.md`. Resumo: Baixio (folga ao TN; legado x
HDS-5 em −8,0, −6,4 e −7,8 %; HUT TR 25 6,03 x 2,70 m³/s), CSB (BTCC-N17 −27 %; 2DN150 até 200 m), Xingó (BU-01/06/24:
lâmina de perfil x Manning normal), Iuiu (DP11 McMath +24 %), Delmiro (DN170 e DN230; pico BHD1 +5,3 %). Marcadores
`xfail` em `tests/dren/`: não estritos nos testes de Baixio, CSB BTCC-17, Xingó e Iuiu/Baixio HUT; `strict=True` em
CSB 2DN150, Delmiro DN170/DN230 e BHD1. Contagem (pytest 2026-10-08): 10 funções `xfail`, 14 resultados
`xfailed` (Baixio legado e Xingó são parametrizados, 3 casos cada); suíte 269 passed, 14 xfailed.

## 8. Registrar um caso novo

Formato de `casos/drenagem/<AAAA-MM-DD>_<slug>.md`: cabeçalho (título), `fonte` (doc:páginas), `disciplinas`, `nivel`,
`tipo` (positivo ou negativo), `qualidade` (A/B/C), `marcas` (e "Nenhum `✓h`"), depois **Problema, Dados de entrada
(grandeza, valor, unidade, fonte, marca), Método do projetista, Resultado, Gabarito para a calculadora (candidato),
Rastro (A/B/C por item), Divergências, Fronteira (delegar)**. Linha no `_INDICE.md`. O caso vira teste em
`tests/dren/test_<módulo>.py` (reproduz na tolerância, ou `xfail(strict=True)` se > 5 % com linha em `DIVERGENCIAS.md`)
rotulado "acervo, sem check-h". Passo a passo: `references/registrar-caso-novo.md`. O registro escreve **só neste
pacote**; caso de canal de adução ou adutora vai ao Hidráulico.

## 9. Fronteiras

- **Hidráulica** (`[DELEGAR: hidraulica]`): canal de adução, sifão, aqueduto, adutora e o dissipador na saída do bueiro
  (D3). A decisão canal x sifão x aqueduto x bueiro sob o canal é dela; o caso do CAC aqui é só o quadro de bueiros.
- **Clima** (`[DELEGAR: clima]`): IDF, P(t,TR), desagregação. Caso com IDF emprestada ou ilegível (Baixio HUT, CSB)
  é dito assim, sem "corrigir" a chuva.
- **Orçamento**: casos não trazem preço; custo de alternativa vai ao `orcamento` com quantitativos.
- **Normas e manuais**: "o que a norma exige" -> `drenagem-normas-e-manuais`.
- **Pontos abertos** (padrão provisório até **decisão do André**, sessão F7; mostrar alternativas com fonte): TR de
  bueiro de perímetro irrigado (USBR Drainage Manual [USBR-DRAINAGE p. 57]: 5 a 15 anos para drenos superficiais,
  25 onde a estrutura é cara; acervo: Baixio 25 com verificação 50, Iuiu 2002 50 sob canal e 25 sob estrada, Iuiu
  2018 25, Delmiro 20 com verificação 50, Salitre e CSB 100); Ke de alas
  paralelas (DNIT 0,2 x HDS-5 0,7); limite de área do racional (50 ha, 100 ha, 350 ha, 2 km², 3,5 km²); Tc mínimo (5, 6
  ou 10 min; Xingó usa 10).

## 10. Calculadoras que dão o gabarito de comparação

| Problema do caso | Função (`tools/dren/`) | Conferir nos `avisos` |
|---|---|---|
| Tc, racional, HUT | `hidrologia.tc_com_avisos`, `racional`, `hidrograma_unitario_triangular`, `chuva_efetiva` | faixa de validade do Tc; limite de área; NERC e Bransby-Williams "não conferida" |
| Bueiro HDS-5 x legado | `bueiros.dimensionar_bueiro`, `comparar_legado_hds5`, `tubo_parcialmente_cheio` | qual controle governa; Ke (`fonte_ke`); y/D 75 % provisório |
| Valeta, comprimento crítico | `estradas.valeta_comprimento_critico`, `sarjeta_triangular` | tc_min e TR provisórios; hmax |
| Macrodreno e dreno de lote | `canais_drenagem.canal_trapezoidal`, `verificar_trechos`, `verificar_limites_alternativos`, `reconciliar_extensoes` | Fr com A/T; folga 25 % provisória |
| Dreno de fundo | `drenos.dreno_de_fundo_de_canal_revestido`, `capacidade_tubo_parcial` | S e n do tubo; meia seção |

Comando: `python -m tools.dren.<módulo> --json "{\"funcao\": \"...\", ...}"`; `--listar` lista as funções.

## 11. Lacunas

- Nenhum caso com `✓h`; nenhum com Hooghoudt/Ernst/Glover-Dumm; sem sarjeta ou descida d'água com memória.
- Estudo HARZA 2001 (bueiros do CAC), Vol. 3 do Iuiu 2018 (declividades dos bueiros), plantas SD do Sertão
  Pernambucano e hietograma do Baixio (tabela T-K) e do Delmiro (polinômio cúbico) não estão no acervo textual.
- Casos B e C dependem de coluna ou coeficiente inferido; promover a gabarito exige página conferida por pessoa.
- Documentos de rota `imagem` não são alcançáveis por texto.

## Revisão técnica

**2026-10-08, revisor Opus (F7).** 16 itens numéricos amostrados, 15 funções e 17 testes citados conferidos.
Resultado: 13 conferidos sem mudança, 3 corrigidos, 0 erros de calculadora.

- **Conferidos** (recalculados à mão ou no primário): CAC valas, Q(VC2) 0,171 com P tomado como i e 2,05 m³/s com
  I = 278,4 mm/h (caso 1128:112); Delmiro: Kirpich 4,92 h, NERC 7,65 h, v 0,48 e 0,49 m/s, S(BH4.5) 0,0043 com razão
  14,4; DN170/DN230 por Manning meia seção 1,05e-3 e 2,31e-3 m³/s (`capacidade_tubo_parcial` dá o mesmo), Lmáx 388 e
  1.260 m (2,7 e 5,9 km com Manning); Salitre 74.884,41 m, V 1,2 x 1,5 m/s (1584:105; 1585:97-123); CAC B31 sobe 1,79 m
  e o coletor fica 0,81 m acima; Jaíba 0,013/0,015 = −13 %; CSB BTCC-N17 3 x 9,54 = 28,6 m³/s (−27 %); Xingó
  4,48/(1,5·0,96) = 3,11 m/s e Kirpich S1 9,07 x 8,91 h; Baixio folga 0,464 m; Ke de alas paralelas 0,7 [HDS-5 p. 216]
  x 0,2 [DNIT-DREN p. 130, Tab. 30]. Todas as funções do §10 existem em `tools/dren/` com o nome citado, e todos os
  testes do §6, §7 e das references existem em `tests/dren/`, com o `strict` declarado no §7.
- **Corrigidos**: (1) §1 regra 3: os casos não trazem a frase "gabaritos são candidatos até conferência humana, F7"
  (só 3 dos 16 falam em "conferência humana"); todos dizem "Nenhum `✓h`" ou "pendente de `✓h`". (2) §9: o Delmiro usa
  TR 20 com verificação TR 50 nos bueiros (caso `delmiro_gouveia_bueiros_tubulares_sob_canal_principal`, 1493:282-285;
  1492:164), não 25/50; os pontos abertos passam a "decisão do André", e entra o primário do USBR. (3) §7 e
  `references/divergencias-xfail.md`: contagem de xfail. Também: "dissipador" no "Não use" da description (D3) e
  "Ø interno 149 e 200 mm" na lição 4.
- **Fronteiras**: conferem com a `MATRIZ_DE_INTERFACES.md` (Clima entrega IDF; Hidráulica decide canal x sifão x
  aqueduto x bueiro, D18-Hid; dissipador é do Hidráulico, D3). A description não colide com `casos-de-referencia`
  do Hidráulico, que exclui drenagem e aponta para `casos/drenagem/`. A regra "apontar, não corrigir" (§2) está
  aplicada nas lições e nos casos.

**Pendências para o André**

1. **TR de bueiro de perímetro irrigado** (dado novo para o ponto do `PLANO.md`): [USBR-DRAINAGE p. 57] pede 5 a 15
   anos para drenos superficiais e 25 onde a estrutura é cara ou o dano justifica. O acervo usa 20/50 (Delmiro),
   25/50 (Baixio; Iuiu 2002 é 50 sob canal e 25 sob estrada), 25 (Iuiu 2018) e 100 (Salitre, CSB). Efeito: I100/I25
   ≈ 1,3 a 1,4 com as IDFs do acervo (CSB TR^0,241; Delmiro a50/a20), mais o C quando ele cresce com o TR. Recomendação: 25 para bueiro sob canal, com verificação a 50 (o
   USBR dá apoio ao 25, e o acervo verifica a 50); 100 só quando a falha põe o canal adutor em risco.
2. **Ke de alas paralelas**: as duas páginas conferem (0,7 x 0,2). Nas outras linhas a Tab. 30 coincide com a C.2 do HDS-5
   (`DIVERGENCIAS.md` v0.2.0), o que sugere erro de transcrição só nesta linha. Efeito: He = Ke·V²/2g, com V 3 m/s dá 0,32 x 0,09 m. Recomendação:
   manter o padrão 0,7, como está no código.
3. **xfail não estritos**: a regra 5 pede `strict=True`, mas 6 funções de acervo (Baixio folga, legado e HUT; CSB
   BTCC-N17; Xingó; Iuiu DP11) estão com `strict=False`. Não muda número; muda só o alarme se o teste passar a
   fechar. Recomendação: tornar estritos. O "11 xfail" do `drenagem-fundamentos` §9 e do `PLANO.md` deve virar 10
   funções e 14 resultados.
4. Seguem pendentes, sem dado novo: limite de área do racional, Tc mínimo, y/D 75 %, folga 25 % e NERC e
   Bransby-Williams sem primário (F5).
