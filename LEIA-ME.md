# Semente do Especialista em Drenagem

> Criada em 2026-10-02 (decisão D18 do Especialista em Hidráulica): o escopo de drenagem foi separado do agente
> hidráulico e passa a ser um agente próprio, a treinar depois. Esta pasta guarda **tudo o que já foi produzido sobre
> drenagem** durante o treinamento do hidráulico, pronto para ser retomado. Nada aqui é agente instalável ainda.

## Escopo previsto do agente

Hidrologia de projeto (IDF, Tc, racional, McMath, SCS-CN, hidrogramas, estatística de máximos, TR por obra, risco),
bueiros sob controle de entrada e de saída (HDS-5), canais de drenagem, valetas, sarjetas, descidas d'água e
dispositivos-tipo do DNIT, drenagem superficial de perímetro irrigado e de estradas de serviço, drenagem subsuperficial
agrícola (Hooghoudt, Ernst, Glover-Dumm, tubos e envoltórios), drenos de obra (dreno de fundo de canal revestido,
subpressão), dissipação na saída de bueiros (rip-rap, bacia de impacto: a calculadora `dissipadores.py` fica no pacote
hidráulico e é importada ou copiada).

Fronteiras: o **Especialista em Hidráulica** fica com canais, sifões, aquedutos, adutoras, transientes, estações,
vertedouros e dissipadores de estruturas de canal; ele pede ao Drenagem a vazão de projeto e o dimensionamento das
travessias de drenagem natural sob o canal (bueiros) e recebe a cota de inundação a montante. A **Climatologia**
entrega IDF e chuva de projeto com incerteza; a transformação chuva → vazão é do Drenagem (regra herdada da D7).
**Geotecnia** decide filtro real, envoltório e permeabilidade; o Drenagem especifica o critério hidráulico.

## O que já existe aqui

| Pasta | Conteúdo | Estado |
|---|---|---|
| `.claude/skills/hidrologia-de-projeto-para-drenagem/` | SKILL.md (24,9 KB) + 6 references (Tc, C, CN, TR, [DELEGAR: climatologia], gabaritos). ~60 fórmulas conferidas no primário | v0.1, revisada só por amostragem |
| `.claude/skills/bueiros-e-travessias/` | SKILL.md (25 KB) + 6 references (constantes HDS-5, velocidades, TR, dispositivos DNIT, valetas/sarjetas, exemplos). ~120 valores conferidos | v0.1, idem |
| `tools/dren/hidrologia.py` (0.2.0), `bueiros.py` (0.2.0), `drenos.py` (0.1.0) | calculadoras em Python puro, CLI JSON padrão (`python -m tools.dren.<modulo> --json ...`) | testadas |
| `tests/dren/` | 127 testes passando, 11 xfail (divergências do acervo > 5%, regra D11) | `python -m pytest tests/dren -q` |
| `casos/drenagem/` | 10 casos reais do acervo de projetos (Baixio de Irecê, CSB, Iuiu, Jaíba, Salitre, Xingó) com dados, método, gabarito e divergências | rastro A/B |
| `evals/roteamento_drenagem.yaml` | 11 casos de roteamento herdados (hid-, bue-, dsub-) | a completar |
| `tools/dren/DIVERGENCIAS.md` | divergências calculadora × acervo e entre fontes (Ke DNIT × HDS-5, Y da Tab. A.2, legado subestima HW) | para sessão com o André |
| `PENDENCIAS_DE_TREINAMENTO.md` | o que falta para virar agente | — |

Os módulos `_cli.py` e `__init__.py` e o `conftest.py` são cópias do pacote hidráulico (mesmo padrão). `drenos.py`
não depende de `canais.py`. `README.md` é o README das calculadoras na data da separação.

## O que é compartilhado e NÃO foi copiado

- **Corpus de referências** (3,1 GB, 356 PDFs, texto extraído e catálogo): `../Especialista Hidraulica/referencias/`
  (`_catalogo.yaml`, `_texto/<ID>.md` com `<!-- p. N -->`). IDs mais relevantes para drenagem: DNIT-DREN (IPR-724),
  DNIT-HIDRO (IPR-715), DNIT-ALBUM (IPR-736), DNIT-ES0xx, FHWA-HDS5, FHWA-HDS2, FHWA-HEC14, FHWA-HEC15, FHWA-HEC22,
  NRCS-NEH630-CH09/10/15/16, NRCS-NEH624-CH*, NRCS-NEH650-CH02/CH14, NRCS-EFH14, USBR Drainage Manual, EMBRAPA-DREN-*,
  EMBRAPA-PRINC-DREN, FAO-IDP62, ILRI-DMS20, PMSP-DRENURB-V1/2/3, DAEE-IT-DPO11, ENAP-*, ABDER-APOSTILA, EPA-SWMM-*,
  CDV-MANUAL-IRRIG (capítulo de drenagem).
- **Índice FTS5 do corpus**: `../Especialista Hidraulica/_BIBLIOTECA_HID/` (consultar.py; working set em `C:\bibhid`).
- **Acervo de projetos reais**: `../../03. Infraestrutura/Projetos de Referência/_BIBLIOTECA_TECNICA/` (consultar.py; `C:\bibtec`).
- **Mapa de conhecimento por fonte**: `../Especialista Hidraulica/referencias/MAPA_DE_CONHECIMENTO.md` (em produção;
  fragmentos USACE_FHWA, NRCS e BR_NORMAS_MANUAIS são os que interessam).
- **Modelo de agente, skill núcleo, brief de redação de skills, evals e processo**: `../Especialista Hidraulica/`
  (`.claude/agents/engenheiro-hidraulico.md`, `.claude/skills/hidraulica-fundamentos/`, `tools/BRIEF_SKILL.md`,
  `evals/README.md`, `PLANO.md`).

Ao treinar, decidir: corpus próprio ou compartilhado por caminho; biblioteca `tools/dren` compartilhada (um dono) ou
duplicada; repositório git próprio (sugestão: `agro.infra.especialista-drenagem`, privado).

## 2026-10-07 — pacote movido para `08. AI Squad`

O André moveu os pacotes de especialistas de `03. Infraestrutura/` para `08. AI Squad/`. Corrigidas as referências de caminho (RAIZ sem caminho absoluto; acervo de projetos em `../../03. Infraestrutura/Projetos de Referência/_BIBLIOTECA_TECNICA/`). Pendência: `ORCAMENTO_ROOT` em `~/.claude/settings.json` ainda aponta para `03. Infraestrutura/Especialista Orcamento`, que não existe.
