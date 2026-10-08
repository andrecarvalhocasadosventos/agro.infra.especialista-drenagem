# Brief F5 — calculadoras do Especialista Drenagem (2026-10-08)

Base: `../Agent Builder/modelos/BRIEF_CALCULADORAS.md` (leia; vale integralmente: docstring com fórmula, `[ID p. N]`
conferido, faixa de validade, avisos; testes de livro 1 %, de acervo 5 %; divergência > 5 % vira
`xfail(strict=True)` e nunca se ajusta fórmula; sem rede; não alterar `_cli.py`).
RAIZ = `08. AI Squad/Especialista Drenagem`. Calculadoras em `tools/dren/` (CLI: `python -m tools.dren.<modulo>
--json '{...}'`), testes em `tests/dren/`. Estado de partida: 127 passed, 11 xfailed (`python -m pytest tests/dren -q`;
neste ambiente use `rtk proxy python -m pytest ...` para ver a saída).

Fontes: `referencias/MAPA_DE_CONHECIMENTO.md` (seção do seu grupo, em especial "Gabaritos para calculadora" e
"Pendências para a F5/F7"), `referencias/_texto/<ID>.*` (Grep em `<!-- p. N -->`), e o corpus do Hidráulico por
caminho `../Especialista Hidraulica/referencias/_texto/` + seu mapa (H12–H15). Para conferir fórmula com raiz/expoente
perdido no texto, renderize a página do PDF (PyMuPDF → PNG em pasta temporária) e leia a imagem. Casos:
`casos/drenagem/_INDICE.md` (nenhum tem ✓h: casos de acervo entram como teste de 5 % rotulado "acervo, sem ✓h" ou
como xfail documentado, nunca como gabarito de livro). Pendências antigas: `PENDENCIAS_DE_TREINAMENTO.md` §2.

**Arquivos compartilhados**: NÃO edite `tools/dren/README.md`, `tools/dren/DIVERGENCIAS.md` nem `__init__.py` (há
5 agentes em paralelo). Escreva suas linhas em `tools/dren/_fragmentos/<modulo>.md` com duas seções: `## README`
(módulo | função | fórmula | fonte | teste) e `## DIVERGENCIAS` (item | fonte A | fonte B/acervo | tratamento).
Edite só o seu módulo e o seu arquivo de teste. Ao fim, rode a suíte inteira `tests/dren` e informe o total.
Não decida D-n: parâmetro cujo valor é decisão aberta (TR, Ke, Tc mínimo, limite do racional) entra como argumento
com padrão provisório documentado e aviso "padrão provisório, decisão F7".

Módulos:
- **M1 hidrologia.py** (existente, v0.2.0 → 0.3.0): conferir no primário Dooge (unidade de S), Giandotti (faixa de
  área), Picking (unidade; IME p. 29), DNOS (expoentes, tabela K por terreno, DNIT-HIDRO p. 89), Kirpich modificada
  (×1,42 do DNIT-HIDRO p. 87–93 × "1,5" atual), Ven Te Chow; testes com os gabaritos G1 (McCuen, NEH-630 cap. 15
  escoamento em lâmina, planilhas de escoamento plano) e casos L2 (HUT BHD1 Delmiro; NERC × Kirpich). Função NERC/
  Bransby-Williams se o caso pedir.
- **M2 bueiros.py** (existente, v0.2.0 → 0.3.0): teste da V de saída do exemplo HDS-5 p. 280 (6,47 m/s); A_c do
  tubular com fonte IME p. 151–152 (atualizar docstring); Manning circular parcialmente cheio com geometria exata
  (caso Delmiro D 0,80/n 0,015/S 0,005/Q 0,499 → y 0,454, Fr 0,89); gabaritos G2 de bueiro; e **novo** módulo
  `tools/dren/tubos.py` (seleção indicativa de classe de tubo de concreto NBR 8890 pela ABTC: carga de Marston,
  fator de berço, exemplos ABTC e EM 1110-2-2902 do mapa G2), com testes `tests/dren/test_tubos.py`.
- **M3 drenos.py** (existente, v0.1.0 → 0.2.0): Ernst com exemplo WATERLOG-ENDRAIN p. 10 (a divergência de 3,5 %
  entre impresso e reconstituição: conferir contra ILRI-16 do Hidráulico antes de fixar), Hooghoudt (exemplos 65 m e
  95 m do G4 e NEH-624), fator 1,16 de Glover-Dumm (Maniçoba p. 2–3, 12,72 m; procurar a página na ILRI-16/FAO-62),
  critério de envoltório (ILRI-56), capacidade de tubo dreno corrugado (caso Delmiro dreno de fundo: registrar a
  divergência de 4,7–6,9×), tabelas "a confirmar" com página.
- **M4 estradas.py** (novo, 0.1.0): sarjeta triangular/trapezoidal (Izzard/HEC-22 e HEC-12; se já houver função de
  sarjeta em bueiros.py, reaproveitar importando), comprimento crítico de sarjeta e de valeta de crista/pé (racional
  por metro × Manning; caso Xingó VPC-1: 162,5 m em i 0,001 e 1259 m em i 0,060), descida d'água em degraus/rápida
  (capacidade, só se houver fórmula com página), caixa coletora (orifício/vertedor), dreno profundo longitudinal
  (vazão de contribuição e capacidade). Tc mínimo e TR padrão como argumentos (padrão provisório 5 min e TR 10;
  registrar 6 min do Álbum e 10 min da IS-239 como divergência). `tests/dren/test_estradas.py`.
- **M5 canais_drenagem.py** (novo, 0.1.0): canal de drenagem trapezoidal/retangular/composto por Manning (normal,
  crítica, Froude com profundidade hidráulica A/T, nunca y), velocidade admissível por revestimento/solo (DNIT-DREN
  Tab. 31 já usada em bueiros; EM 1110-2-1601; HEC-15 do Hidráulico), n de rip-rap (EM-1601 × HEC-11, divergência),
  D50 de rip-rap de revestimento de canal (EM-1601/HEC-11; dissipador de saída de bueiro é do Hidráulico, D3: não
  implementar), borda livre de dreno (critério de 25 % do tirante do caso Delmiro como opção documentada), verificação
  tirante × altura da seção e reconciliação de extensões (testes de consistência dos casos negativos). Testes com
  Salitre DT 4.1.6/A (V ≈ 1,139; Q ≈ 3,484) e DS 4.1, Delmiro DS-1.1/C, gabião, e exemplos de HDS-3/EM-1601.
  `tests/dren/test_canais_drenagem.py`.

Resposta ≤ 15 linhas no formato do brief base, incluindo o resultado da suíte inteira.
