# PLANO — Especialista Drenagem (agente `engenheiro-de-drenagem`)

> Versão 0.1 (2026-10-07). Padrão: `Agent Builder/PADRAO_DO_PACOTE.md`. Processo: `Agent Builder/PROCESSO_DE_TREINAMENTO.md`.
> Este plano nasce na fase F0 e é atualizado a cada portão. Só o André decide `D-n`.
> Substitui `PENDENCIAS_DE_TREINAMENTO.md` como documento de plano; aquele arquivo fica como registro da separação (D18-Hid).

## Decisões

| ID | Decisão | Efeito no plano |
|---|---|---|
| D1 | (2026-10-07) Corpus do Hidráulico usado **por caminho** (`../Especialista Hidraulica/referencias/`, índice `C:\bibhid`), declarado em `PACOTE.yaml`. `referencias/` próprio só com as lacunas e com a pasta local do André (D8) | §5; F1 é manifesto de lacunas; F2 pequena |
| D2 | (2026-10-07) Calculadoras saem de `tools/hid` para **`tools/dren`** (testes em `tests/dren`), com `_cli.py` e `conftest.py` próprios | F5 começa pela migração; `PACOTE.yaml` muda na F5 |
| D3 | (2026-10-07) Dissipação na saída de bueiros (rip-rap, bacia de impacto) é do **Hidráulico** (`dissipadores.py`, `vertedouros-e-dissipadores`). O Drenagem entrega V de saída, Fr, y de saída e o aviso "precisa de dissipador" | §1.2; sem skill própria |
| D4 | (2026-10-07) Taxonomia de 8 skills aprovada (§2), com prefixo `drenagem-` nas skills de fonte para não colidir com `normas-e-manuais` e `casos-de-referencia` do Hidráulico | F6 |
| D5 | (2026-10-07) Drenagem agrícola subsuperficial (Hooghoudt, Ernst, Glover-Dumm, envoltório) fica no **Drenagem**; o Irrigação entrega recarga, salinidade e lençol admissível | §1.1; skill `drenagem-subsuperficial` |
| D6 | (2026-10-07) Aceitação F10 com as 8 pendências de drenagem do CDV (P-42, P-108, P-115, P-116, P-134, P-266, P-268, P-272) + P-265, P-267, D-56, D-85, D-86 | §6, F10 |
| D7 | (2026-10-07) Repositório `agro.infra.especialista-drenagem` (privado), gitdir `C:\gitdirs\especialista-drenagem` | git a partir da F0 |
| D8 | (2026-10-07) A pasta pessoal `G:\Meu Drive\DRENAGEM` (300 arquivos, 2,4 GB) entra como **fonte local**: só os PDFs da lista A/B do §5.1 são copiados para `referencias/` na F2; vídeos, DWG, instaladores e material de Civil 3D/SSA ficam fora | §5.1, F1, F2 |
| D9 | (2026-10-09) **Determinação do André:** o especialista de drenagem passa a desenvolver estudos com HEC-RAS, como no projeto da TPF. Premissa de treinamento (R0). Fronteira em uso: Drenagem = cheias, travessias e manchas de inundação; Hidráulica = canais de adução e estruturas hidráulicas; proposta com Hidráulica e Geoprocessamento congelada, decisão no `/treinar squad` (§11.3) | §11; skill nova `modelagem-hidraulica-hec-ras` (F6 posterior); F1, F2 e F4 incrementais feitas em 2026-10-09 |
| D10 | (2026-10-09, R5 aprovada pelo André) O dissipador e o rip-rap na saída do bueiro são **dimensionados pelo Hidráulico**; a Drenagem entrega a necessidade, V, Fr, y e TW de saída. Reforça D3 | `bueiros-e-travessias` §3.6 ganhou o parágrafo R5 |

Herdadas do padrão (valem sem nova decisão): calculadoras em Python testadas, o agente roda e cita (não calcula no
texto); divergência > 5 % vai para `DIVERGENCIAS.md`; nenhuma escrita no CDV fora de cartão; git invisível (a sessão
faz init, commit e push; gitdir fora do Drive); memória em quatro camadas.

Para a sessão interativa da F7 (Opus), não decididas: TR normativo de bueiros de perímetro irrigado (USBR 5–15 anos ×
prática do acervo 25/50); Ke de alas paralelas (DNIT 0,2 × HDS-5 0,7); limite de área do racional; os 11 xfail.

## 0. Resumo executivo

1. **Metade do trabalho técnico já existe**: 2 skills de 24 KB com ~180 valores conferidos por amostra, 3 calculadoras
   (`hidrologia` 0.2.0, `bueiros` 0.2.0, `drenos` 0.1.0), 127 testes passando e 11 xfail, 10 casos do acervo. O que
   falta é estrutura de agente (núcleo, agente, evals ≥ 50, git) e três skills novas.
2. **O pedido nº 1 da semente está resolvido**: o Clima já entrega IDF com IC 90 %, desagregação e ARF
   (`chuvas-intensas-e-idf`). O Drenagem não ajusta IDF; consome e cita.
3. **Corpus quase completo por caminho**: o Hidráulico já tem HDS-5, HEC-14/15/22, IPR-715/724/736, NEH 630/624/650,
   ILRI 16, DAEE Guia, FAO 26. A pasta do André acrescenta o que falta em português e no Brasil: Pfafstetter original,
   ABTC/NBR 8890, IME, McCuen, SisCCoH, COMAER subsuperficial.
4. **Risco principal**: os casos do acervo divergem do método (Manning plena × HDS-5, Tc e limites do racional variando
   por projeto). O agente precisa citar a divergência sem "corrigir" o projeto sozinho; isso é F7 interativa.
5. **Risco de colisão** com o Hidráulico no namespace `tools.hid` e em nomes de skill: resolvido por D2 e D4.

## 1. Escopo

### 1.1 Disciplinas (o que resolve)

| Disciplina | Problemas que resolve | Quem consome |
|---|---|---|
| Hidrologia de projeto | Tc (Kirpich, NRCS, Dooge, Giandotti, Picking, DNOS), racional, McMath, SCS-CN, hidrograma unitário, TR e risco por obra, vazão de projeto por travessia | hidraulica, terraplenagem, orcamento |
| Bueiros e travessias | bueiro tubular e celular sob controle de entrada e de saída (HDS-5), HW/D, afogamento, V de saída, cota de inundação a montante, nº de células, classe de tubo (indicativa) | hidraulica, orcamento, terraplenagem |
| Drenagem de estradas e plataformas | sarjetas, valetas de crista e de pé, descidas d'água, caixas, dissipadores-tipo DNIT (seleção), drenagem profunda de pavimento | terraplenagem, pavimentacao, orcamento |
| Canais de drenagem e macrodrenagem | canal de drenagem natural ou desviado, seção, revestimento, velocidade admissível, deságue, interceptação de talvegues pela faixa do canal (D-56, D-85) | hidraulica, terraplenagem, orcamento |
| Drenagem subsuperficial | dreno agrícola (Hooghoudt, Ernst, Glover-Dumm), espaçamento e profundidade, dreno de fundo de canal revestido, subpressão, critério hidráulico de envoltório, DN do tubo dreno (D-86) | irrigacao, hidraulica, geotecnia, orcamento |

### 1.2 Fora de escopo

| Tema | Destinatário (id) |
|---|---|
| IDF, chuva de projeto, desagregação, ARF, séries | clima |
| Canal de adução, sifão, aqueduto, decisão canal × sifão × aqueduto × bueiro, dissipador na saída de bueiro e de estrutura (D3) | hidraulica |
| Filtro real, k medido, envoltório do tubo, piping, sondagem | geotecnia |
| Greide, plataforma, taludes, volumes | terraplenagem |
| Estrutura do pavimento | pavimentacao |
| Recarga por irrigação, lâmina, salinidade, lençol admissível | irrigacao |
| Preço e composição de custo | orcamento |
| Projeto estrutural de aduela e tubo (armadura) | estruturas |
| Drenagem urbana em rede (microdrenagem de loteamento), separador água-óleo, drenagem aeroportuária | fora do squad; o agente diz que não cobre |

### 1.3 Nível de entrega

Anteprojeto (padrão); básico quando pedido; executivo confere, não substitui.

## 2. Taxonomia de skills

| Skill | Tipo | Cobre | Vizinhas (risco de colisão) |
|---|---|---|---|
| `drenagem-fundamentos` | núcleo | convenções, dados mínimos por pedido, fluxo, fronteiras, protocolo `[DELEGAR]`, parecer replicável, modo CDV | `hidraulica-fundamentos`, `clima-fundamentos` |
| `hidrologia-de-projeto-para-drenagem` | disciplina (existe, v0.1) | Tc, C, CN, racional, McMath, SCS, HU, TR por obra, pedido ao Clima | `chuvas-intensas-e-idf` (Clima) |
| `bueiros-e-travessias` | disciplina (renomear `bueiros-e-drenagem-superficial`) | HDS-5, controle de entrada e saída, HW, V saída, cota de inundação, classe de tubo indicativa | `canais-abertos`, `vertedouros-e-dissipadores` (Hid) |
| `drenagem-de-estradas-e-plataformas` | disciplina (nova; sai da seção atual de bueiros) | sarjeta, valeta, descida, caixa, dispositivos-tipo DNIT, drenagem profunda | futuras de terraplenagem e pavimentação |
| `canais-de-drenagem-e-macrodrenagem` | disciplina (nova) | canal de drenagem, revestimento, velocidade admissível, deságue, talvegues interceptados | `canais-abertos` (Hid) |
| `drenagem-subsuperficial` | disciplina (nova; `drenos.py` existe) | drenos agrícolas, drenos de obra, subpressão, envoltório (critério), DN do dreno | futura de irrigação; geotecnia |
| `drenagem-normas-e-manuais` | fonte | procedimento próprio de IPR-724, IPR-715, IPR-736, HDS-5, HEC-22, NEH 630/624, DAEE, Pfafstetter, ABTC/NBR 8890 | `normas-e-manuais` (Hid) |
| `drenagem-casos-de-referencia` | fonte | como Baixio, CSB, Iuiu, Jaíba, Salitre, Xingó e o CDV resolveram; lições negativas | `casos-de-referencia` (Hid) |

## 3. Fronteiras

Fonte única: linha de `drenagem` na `Agent Builder/MATRIZ_DE_INTERFACES.md` (§3.3). Exceções e mudanças propostas à
matriz (decididas na sessão `/treinar squad`):

- D3 confirma que o dissipador na saída de bueiro é do Hidráulico: a linha `hidraulica` da §3.3 já diz "necessidade de
  dissipador"; propor acrescentar à linha recíproca do Hidráulico "dimensiona o dissipador na saída de bueiro com V, Fr
  e y entregues pelo Drenagem".
- Drenagem urbana em rede e aeroportuária ficam fora do squad (§1.2): registrar na matriz como "não coberto".

## 4. Arquitetura do pacote

Árvore de `PADRAO_DO_PACOTE.md` §1; resolução da raiz por `PACOTE.yaml` (`DRENAGEM_ROOT`). Diferenças:

- `referencias/` pequeno (lacunas + D8); o corpus principal é o do Hidráulico por caminho (`dependencias_externas`).
- Calculadoras em `tools/dren/` a partir da F5 (D2); até lá continuam em `tools/hid/`.
- O pacote ainda não tem `tools/verificar_instalacao.py`, `INSTALL.md` nem `NAO_ABERTOS.md`: entram em F1 e F11.

## 5. Corpus

| Grupo de fonte | O que traz | Meta (itens) | Prioridade | Não abertos (ver `NAO_ABERTOS.md`) |
|---|---|---|---|---|
| Corpus do Hidráulico por caminho | HDS-5, HEC-14/15/22, IPR-715/724/736, NEH 630/624/650, EFH 14, ILRI 16, DAEE Guia, FAO 26, USBR Drainage, Embrapa, PMSP | ~45 já catalogados | A | — |
| Lacunas abertas (F1) | FAO 38 (HTML por capítulo), DAEE Manual de Vazões 1994, DNIT ES 018/021, FHWA HEC-12/HY-8, USBR Drainage Manual (conferir edição), TR de bueiros em perímetro irrigado | 10–20 | A/B | NBR 8890:2020 (ABNT, paga) |
| Pasta local do André (D8) | ver §5.1 | 16 | A/B | — |

### 5.1 Pasta `G:\Meu Drive\DRENAGEM` — triagem de 2026-10-07

Inventário: 300 arquivos, 2,4 GB; ~1,9 GB são vídeos, DWG, nuvem de pontos e instaladores. Nenhum dos PDFs abaixo
está no corpus do Hidráulico ou do Clima, exceto onde indicado.

| Prioridade | Arquivo | Por que interessa | Skill |
|---|---|---|---|
| A | `PFAFSTETTER/…CHUVAS INTENSAS NO BRASIL.pdf` (251 MB, escaneado) | obra original dos coeficientes de desagregação e das equações por posto; precisa de OCR local. Útil também ao Clima (compartilhar por caminho) | hidrologia; normas |
| A | `ABTC/…ALTERAÇÕES DA NORMA NBR 8890.pdf`, `…ESPECIFICAÇÃO DE TUBOS DE CONCRETO EM LICITAÇÕES.pdf`, `…PROJETO ESTRUTURAL DE TUBOS CIRCULARES…`, `…PROJETO ESTRUTURAL DE ADUELAS.pdf` | cobre a lacuna da NBR 8890 (classes PA/PS, recobrimento) sem comprar a norma | bueiros; normas |
| A | `01. ESTUDOS/DREN - EST - RICHARD H MACCUEN - HYDROLOGIC ANALYSIS AND DESIGN.pdf` | livro-texto de hidrologia de projeto (Tc, HU, racional, frequência) com exemplos resolvidos para testes de calculadora | hidrologia |
| A | `COMAER/…EDMIR - DRENAGEM SUBSUPERFICIAL E SUBTERRÂNEA.pdf` | drenagem profunda em português | subsuperficial; estradas |
| A | `IME/…DRENAGEM URBANA E DE RODOVIAS.PDF` | sarjetas, valetas, bueiros em português, com exemplos | estradas; bueiros |
| A | `01. ESTUDOS/ESCOAMENTO PLANO/Tempo de Concentração - National Engineering Handbook.pdf` + 2 planilhas de escoamento plano | Tc de escoamento em lâmina (NRCS); planilhas viram caso numérico | hidrologia |
| A | `DNIT/…PROJETOS TIPO DE DISPOSITIVOS DE DRENAGEM (2018).pdf` (67 MB) | conferir se é texto; o IPR-736 do corpus é escaneado. Se tiver texto, substitui o OCR pendente | estradas; normas |
| B | `01. ESTUDOS/…ESLAMIAN - HANDBOOK OF ENGINEERING HIDROLOGY.pdf` | referência complementar de hidrologia | hidrologia |
| B | `SiSCCOH/Manual-Tecnico-SisCCoH_v.1.1.pdf` | manual de software brasileiro de componentes hidráulicos de drenagem; conferência cruzada | bueiros; estradas |
| B | `ABTC/…HISTÓRIA COEFICIENTE DE MANNING.pdf`, `…COMPARAÇÃO TUBOS DE CONCRETO VS POLÍMERO.pdf` | n de tubos e escolha de material | bueiros |
| B | `01. ESTUDOS/C3D E SSA/CURSO DRENAGEM RODOVIAS - ROBSON/parte-i a iv.pdf` | curso de drenagem rodoviária (slides); só se o IPR-724 não bastar | estradas |
| B | `01. ESTUDOS/RETROANÁLISE CANAL GABIÃO.xlsx` | possível caso real de canal de drenagem em gabião | canais de drenagem; casos |
| — | `DNIT/…MANUAL DE DRENAGEM DE RODOVIAS (2006)` e álbuns 2007/2010 | duplicam IPR-724/IPR-736 do corpus | — |
| — | `ENROCAMENTO - RIP RAP/Dissertação de Dissipação.pdf` | é do Hidráulico (D3); registrar como sugestão para lá | — |
| fora | C3D/SSA (vídeos, DWG, LAS, templates), SAO e API 421, FAA, COMAER DIRENG, PMI, catálogos ULMA e Alfamec, bacia de infiltração, exercícios de curso, instaladores `.exe`/`.zip` | ferramenta CAD, drenagem urbana, aeroportuária ou industrial (fora do escopo §1.2) | — |

Os livros McCuen e Eslamian têm direitos reservados: uso interno no corpus local, fora do git (`referencias/` já é
ignorado pelo padrão), sem redistribuição.

## 6. Casos reais

Origem: os 10 casos já extraídos (`casos/drenagem/`), o acervo de projetos (via `consultar.py`) e as pendências do CDV.

| Tema | Casos previstos | Fonte | Gabarito |
|---|---|---|---|
| Bueiros sob canal | 6 existentes + 2 | Baixio, CSB, Salitre, Xingó, Jaíba | memoriais (doc:pág nos casos) |
| Hidrologia (Tc, racional, SCS, HU) | 2 existentes + 3 | Baixio HUT, Iuiu, CSB | idem |
| Drenagem subsuperficial e dreno de fundo | 3 existentes + 1 | CSB, Iuiu, Xingó | idem |
| Canais de drenagem e macrodrenagem | 0 + 2 | acervo (busca na F4); retroanálise de gabião (D8) | a extrair |
| Estradas de serviço | 0 + 2 | acervo (Baixio, CAC) | a extrair |
| Aceitação CDV (F10, D6) | 13 pendências | CDV: P-42, P-108, P-115, P-116, P-134, P-265, P-266, P-267, P-268, P-272, D-56, D-85, D-86 | parecer, sem escrita no CDV |

## 7. Fases

| Fase | Entrega | Quem | Custo estimado | Portão (André) | Estado |
|---|---|---|---|---|---|
| F0 · Plano | este arquivo + D1–D8 | Agent Builder (Opus) | US$ 0 de subagentes | sim | **aprovado 2026-10-07** |
| F1 · Manifesto de fontes | `tools/fontes_candidatas.yaml` (lacunas + §5.1), `NAO_ABERTOS.md` | 1 Sonnet | ~US$ 1 | sim | brief pronto (`tools/BRIEF_F1.md`) |
| F2 · Corpus | `referencias/` (lacunas + D8), `_catalogo.yaml`, `_texto/`, OCR do Pfafstetter | script + Haiku | < US$ 1 | não | |
| F3 · Mapa de conhecimento | `MAPA_DE_CONHECIMENTO.md` só dos itens novos (o do Hidráulico cobre o resto) | 2 Sonnet | ~US$ 3 | sim | |
| F4 · Casos reais | +10 casos (canais de drenagem, estradas, hidrologia) | 2–3 Sonnet | ~US$ 4 | não | |
| F5 · Calculadoras | migração para `tools/dren` (D2); Dooge, Picking, Giandotti e DNOS no primário; Ernst com exemplo; teste da V de saída HDS-5 p. 280; módulo de sarjeta e valeta | Sonnet + revisão Opus | ~US$ 5 | não | |
| F6 · Skills | núcleo + 3 disciplinas novas + 2 de fonte; renomear bueiros; ajustar hidrologia ao Clima | 6 Sonnet em paralelo | ~US$ 8 | não | |
| F7 · Revisão técnica | amostra por skill; sessão interativa dos 11 xfail e dos pontos abertos | Opus interativo | 1 sessão | sim | |
| F8 · Agente | `.claude/agents/engenheiro-de-drenagem.md`, `memoria/`, `LICOES.md` | Agent Builder | — | não | |
| F9 · Evals | `roteamento.yaml` ≥ 50 (12 herdados), `casos_numericos.yaml`, juiz Haiku | Sonnet + Haiku | ~US$ 4 | não | |
| F10 · Aceitação offline | 13 pareceres CDV (D6) | agente novo (Sonnet) | ~US$ 5 | sim | |
| F11 · Instalação | `INSTALL.md`, `verificar_instalacao.py`, `estado: instalavel` | Sonnet + script | ~US$ 0,5 | sim | |

Total estimado de subagentes: ~US$ 32, mais as sessões Opus de F7 e F8.

## 8. Riscos

| Risco | Probabilidade | Impacto | Mitigação |
|---|---|---|---|
| Colisão de `tools.hid` com o Hidráulico no mesmo PYTHONPATH | alta até a F5 | médio | D2 na primeira tarefa da F5 |
| Corpus por caminho muda de lugar ou é reorganizado pelo Hidráulico | média | alto | `dependencias_externas` no `PACOTE.yaml`; IDs, não caminhos, nas citações; o verificador confere |
| Pfafstetter escaneado (251 MB) com OCR ruim | média | médio | OCR local; conferir 10 páginas de tabela contra a imagem |
| Skills que "corrigem" o projeto do acervo em vez de apontar a divergência | média | alto | regra no núcleo; casos negativos em `drenagem-casos-de-referencia`; F7 |
| Sobreposição com o Clima na desagregação (CETESB, Pfafstetter) | média | baixo | o Drenagem cita a entrega do Clima; não reimplementa |
| Material com direito autoral (McCuen, Eslamian) vazar para o git | baixa | médio | `referencias/` no `.gitignore`; só `_catalogo.yaml` e o mapa vão para o git |

## 9. Estado

Atualizado ao fim de cada sessão (data, fase, o que falta). Critério de instalável: `PADRAO_DO_PACOTE.md` §8.

| Data | Fase | Situação | Próximo passo |
|---|---|---|---|
| 2026-10-02 | — | semente separada do Hidráulico (D18-Hid) | — |
| 2026-10-07 | F0 | plano v0.1 aprovado (D1–D8); git vinculado; pasta local triada | F1: rodar `tools/BRIEF_F1.md` (1 Sonnet) |
| 2026-10-07 | F1 | manifesto: 28 abertos + 21 locais | portão F1 |
| 2026-10-08 | F2–F6 | corpus 6.527 p.; mapa; 26 casos; 6 calculadoras (269 passed, 14 xfail); 8 skills | F7 |
| 2026-10-09 | F7 (auto), F8, F9 | revisão Opus das 8 skills; agente; evals 97,7 % | **portão F7: `PARA_O_ANDRE_F7.md`**; depois F10 e F11 |
| 2026-10-09 (servidor) | Passo 0, R5, D9 (HEC-RAS) | caminhos, PACOTE.yaml e FTS no espelho (52 doc., 8.194 p.); 269 testes passaram, 14 xfail; 4 manuais HEC-RAS 6.6 no corpus; 6 casos HEC-RAS (3 negativos) | **portão F7 pendente (André)**; plano HEC-RAS §11; F3 dos manuais, F5 do verificador, F6 da skill; depois F10 e F11 |

## 10. Pendências abertas

Herdadas de `PENDENCIAS_DE_TREINAMENTO.md` §2 (calculadoras) e §4 (lições do acervo): entram na F5 e na F7.

## 11. Escopo HEC-RAS (D9, 2026-10-09) — treinamento incremental

**Origem:** determinação do André em 2026-10-09: o especialista de drenagem passa a desenvolver estudos com HEC-RAS, como no projeto da TPF. Premissa de treinamento, não decisão de projeto do CDV (R0). Conduzido como F1, F2 e F4 incrementais (feitas nesta sessão) e F6 posterior (plano abaixo).

### 11.1 Feito em 2026-10-09 (servidor)
- Inventário (`casos/hec-ras/INVENTARIO_TPF.md`): 8 documentos; modelos HEC-RAS 6.5 só para a captação no São Francisco (2D, 6 vazões) e para os riachos Recife/Ferreira (2D, TR 2-100); rio Verde só em texto (Standard Step, sem arquivo).
- F1: 4 PDFs v6.6 do USACE HEC com URL verificada (HTTP 200, `application/pdf`) e 3 links online (Applications Guide, Release Notes, hgt); licença: domínio público (obra do governo federal dos EUA). FHWA: URLs candidatas sem resposta do servidor (código 000); nenhum item FHWA entrou (sem URL verificada).
- F2: `USACE-HECRAS-HRM-66` (482 p.), `-2DUM-66` (286 p.), `-UM-66` (837 p.), `-MAPPER-66` (193 p.) baixados, texto extraído, FTS reconstruído no espelho (52 documentos, 8.194 páginas). Applications Guide e Release Notes ficam `link_only` (só HTML em árvore Confluence).
- F4: 6 casos em `casos/hec-ras/` (3 positivos, 3 negativos), nenhum com ✓h.

### 11.2 Plano da skill `modelagem-hidraulica-hec-ras` (F6 posterior)

**Escopo.** Estudos de cheia e de remanso para travessias, canais de drenagem e manchas de inundação com HEC-RAS 6.x: o especialista especifica, confere e interpreta o modelo; a calculadora (F5) lê e verifica arquivos, não executa o modelo (HEC-RAS não está instalado no servidor).

**Taxonomia (seções da skill):**
1. **Escolha do modelo:** 1D permanente (Standard Step), 1D não permanente, 2D (SWE-ELM × difusão), 1D/2D acoplado, chuva na malha. **1D × 2D:** 1D para canal confinado com seções reais (remanso, ponte, bueiro, travessia com Q conhecido); 2D para planície, riachos paralelos ao canal, escoamento sem direção única, confluência e mancha; 1D/2D quando a calha é bem definida e a planície, larga. Equação 2D: SWE-ELM por padrão; difusão só para planície lenta e como teste [USACE-HECRAS-2DUM-66 p. 196-203]. *Nota F3 (2026-10-10): o padrão do programa é a equação de difusão [USACE-HECRAS-2DUM-66 p. 196, 211]; a escolha SWE × difusão por caso está na skill `modelagem-hidraulica-hec-ras`, que prevalece sobre este plano.*
2. **Dados mínimos por tipo:** terreno (LIDAR/MDT, resolução e data; batimetria quando houver), Q de projeto e TR (do Clima/hidrologia, com ARF), hidrogramas por sub-bacia (pico, tempo ao pico, volume), n por uso do solo, contornos de jusante com fonte (curva-chave, NA conhecido, declividade medida), estruturas (ponte, bueiro, vertedouro: geometria), datum, nível inicial.
3. **Contornos:** normal depth só com declividade medida e seção uniforme [USACE-HECRAS-2DUM-66 p. 144-145]; preferir NA ou curva-chave quando houver barragem ou remanso a jusante (caso HR-06: soleira sem carga).
4. **Malha:** tamanho de célula pela escala da feição, breaklines na calha e em obras, teste de sensibilidade com 2 resoluções [USACE-HECRAS-2DUM-66 p. 53, 11]; passo de tempo por Courant [USACE-HECRAS-2DUM-66 p. 201-203].
5. **Rugosidade e calibração:** n por tabela de referência e por mapa de uso; calibração com marca de cheia, curva-chave ou NA observado; **sensibilidade de n (±20 %)** obrigatória [USACE-HECRAS-UM-66 p. 328; USACE-HECRAS-HRM-66 p. 389].
6. **Estruturas:** ponte (coeficientes de contração e expansão) e bueiro (controle de entrada e de saída) no HEC-RAS [USACE-HECRAS-HRM-66 p. 180, 218-220]; o **dimensionamento do bueiro segue `bueiros-e-travessias` e o do dissipador é da Hidráulica (R5)**; o HEC-RAS só confere a cota de montante.
7. **Critérios de aceitação de modelo** (checklist do parecer, tirados dos casos HR-01 a HR-06): versão e unidades; terreno e datum; n e fonte; malha (mediana, máx.) e sensibilidade; contornos com fonte; condição inicial e duração; estabilização (ΔNA ≤ 0,01 m em 2 h nas células de interesse, ou justificado); balanço de volume; Courant; comparação com dado observado; sensibilidade de n e de TR; conferência dos hidrogramas de entrada contra a hidrologia (pico, volume); discrepância texto × arquivo; nenhuma cota de projeto tirada de um único n sem calibração.
8. **Entregáveis:** parecer replicável (arquivos `.prj/.g/.p/.u`, versão, resumo de entradas, tabela de NA e velocidade por cenário e local, mapas com escala, lista de premissas sem dado, sensibilidade, o que falta); nunca "NA = x" sem ponto, TR e incerteza.

**Antes da F6:** F3 (mapa de conhecimento dos 4 manuais), F5 (verificador, 11.4) e a confirmação do André (11.5).

### 11.3 Fronteira proposta com Hidráulico e Geoprocessamento (INTERFACE CONGELADA — pendência para `/treinar squad`)
Premissa em uso: **Drenagem = cheias, travessias e manchas de inundação; Hidráulica = canais de adução e estruturas hidráulicas.** Proposta a decidir:

| Tema | Dono proposto | Observação |
|---|---|---|
| Mancha de inundação e NA de cheia de rio/riacho; travessia (aqueduto, sifão, bueiro) sob cheia; remanso causado por estrutura de drenagem | **Drenagem** | HR-01, HR-04, HR-06 |
| Remanso em canal de adução (permanente, seção revestida, estruturas de controle) | **Hidráulica** (`canais-abertos`, passo padrão) | HEC-RAS só como conferência, se a Hidráulica pedir |
| Vertedouro, bacia de dissipação, comporta | **Hidráulica** | |
| Captação em rio: NA e velocidade na captação | **Drenagem** produz NA/velocidade; **Hidráulica** projeta captação e bombas | HR-01 |
| MDT, batimetria, LIDAR, ANADEM, hidrografia, delimitação de bacia | **Geoprocessamento** (onda 2) | Drenagem consome, cita fonte e resolução; até lá pede à equipe |
| Q de projeto, IDF, ARF | **Clima** | ARF é do Clima |

Pendência: o `/treinar squad` decide se registra na `MATRIZ_DE_INTERFACES.md`. Esta sessão não editou matriz nem ROTEAMENTO.

### 11.4 Calculadora (F5 posterior) — recomendação sobre bibliotecas

| Opção | O que faz | Avaliação |
|---|---|---|
| `rashdf` 0.12.0 (PyPI; Python ≥ 3.11) | lê `.hdf` do HEC-RAS (geometria, séries, máximos) sem o programa | **recomendada** para o verificador (somente leitura); licença não informada na metadata do PyPI: conferir no repositório antes de adotar |
| `h5py` 3.16 (BSD-3) | leitura genérica de HDF5 | **já usada nesta sessão** (HR-02; instalada no venv do squad); fallback |
| `ras-commander` 0.104.0 (PyPI; Python ≥ 3.10) | automatiza a execução de HEC-RAS 6.x (rodar planos, editar arquivos) | só depois que o André instalar o HEC-RAS; licença a conferir; escrita em arquivos exige pasta de trabalho local |
| HEC-RAS Controller (COM, Windows) | controla o programa instalado | só com HEC-RAS instalado; frágil por versão; alternativa à `ras-commander` |
| `pyras` 0.2.1 (MIT) | wrapper antigo | não recomendada (versão antiga, sem evidência de manutenção) |

Recomendação: F5 começa por `tools/dren/hecras_verifica.py` com `rashdf`/`h5py` (somente leitura): conferir `.p01`/`.u01`, n, malha (área de célula), contornos, estabilização, extrair NA/velocidade e comparar com a tabela do relatório. Execução e `ras-commander` ficam para depois da instalação. **Nada foi instalado no servidor** (h5py entrou só no venv do squad).

### 11.5 Itens para o André (também em `PARA_O_ANDRE.md`)
1. Instalar o HEC-RAS 6.6 no SRVCVERSP (gratuito, USACE HEC; `https://www.hec.usace.army.mil/software/hec-ras/`). Sem ele, o especialista confere modelos, mas não roda.
2. Confirmar a fronteira de 11.3 e levá-la ao `/treinar squad`.
3. Pedir à TPF os arquivos HEC-RAS do rio Verde e a nota de cálculo do Standard Step (HR-06).
4. Conferência humana (✓h) dos números dos casos HR-01 a HR-06 antes de usá-los como gabarito.
