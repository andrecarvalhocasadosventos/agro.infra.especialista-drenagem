---
name: drenagem-subsuperficial
description: >
  Drenagem subsuperficial de perímetro irrigado e de obra linear: espaçamento e profundidade de drenos agrícolas
  (Hooghoudt, Donnan, elipse, Ernst, Glover-Dumm 1,16), critérios de projeto (descarga, lençol, rebaixamento),
  vazão e DN do tubo dreno (D-86), dreno de fundo e subpressão de canal revestido (CSB, Xingó, Delmiro),
  critério hidráulico de envoltório (ILRI-56) e diagnóstico de drenabilidade (Iuiu). Use quando: "espaçamento de drenos", "Hooghoudt", "Ernst", "Glover-Dumm", "profundidade do dreno", "lençol freático", "tubo dreno de
  300 mm", "dreno de fundo do canal", "subpressão", "furo na geomembrana", "envoltório", "precisa drenar?". Não use para: vazão de bacia e bueiro (use hidrologia-de-projeto-para-drenagem,
  bueiros-e-travessias); sarjeta e dreno de pavimento (use drenagem-de-estradas-e-plataformas); canal de
  drenagem (use canais-de-drenagem-e-macrodrenagem); filtro real e k medido (Geotecnia); recarga e salinidade
  (Irrigação); norma isolada (use drenagem-normas-e-manuais); preço (custos).
---

# Drenagem subsuperficial: dreno agrícola, tubo dreno e dreno de fundo de canal

> Convenções, fluxo de 8 passos, parecer, protocolo `[DELEGAR]` e regra mestra (apontar divergência, nunca
> "corrigir" em silêncio) estão em `drenagem-fundamentos`. Aqui só o domínio. Nível padrão: anteprojeto. Tabelas
> longas em `references/`. Páginas: `[ID p. N]` = página física do PDF; ILRI-DPA16 e demais IDs do Hidráulico pelos
> IDs dele (D1).

## 1. Escopo e fronteiras

**É daqui (D5):** espaçamento e profundidade de drenos enterrados e abertos de alívio, tempo de rebaixamento, vazão e
DN do tubo dreno, drenos de obra (fundo de canal revestido, subpressão), **critério hidráulico** de envoltório,
diagnóstico "precisa drenar?". **Não é daqui:**

| Assunto | Quem | Como |
|---|---|---|
| Recarga (lâmina, eficiência de irrigação), salinidade, lençol admissível, lixiviação | `irrigacao` | `[DELEGAR: irrigacao]`; sem retorno, q e h entram como premissa rotulada (ref. `delegar-irrigacao-e-geotecnia.md`) |
| K medido, K por camada, camada impermeável, **filtro real**, envoltório de geotêxtil, piping, estabilidade do revestimento sob subpressão | `geotecnia` | `[DELEGAR: geotecnia]`; aqui só o critério (Terzaghi, ILRI-56) e o gradiente |
| Seção e NA do canal revestido; decisão canal × sifão | `hidraulica` | pede estaca, cotas, NA |
| Poço vertical de drenagem, bombeamento de drenagem (NEH 624 cap. 7, FAO-62 Anexo 22) | `hidraulica` | só localizar a fonte |
| Dreno profundo de pavimento, camada drenante, sarjeta | `drenagem-de-estradas-e-plataformas` | LOC-COMAER é pavimento, não agrícola |
| Coletor aberto e canal de drenagem | `canais-de-drenagem-e-macrodrenagem` | Manning e V admissível |
| Custo por m de dreno e por DN | `orcamento` | entrego m por DN, escavação, envoltório |
| Estrutura (caixa, PV, boca de saída) | `estruturas` | geometria funcional |

**Não cobre:** drenagem urbana e aeroportuária; recuperação de solo salino (modelo de sais, SALTMOD); drenagem
controlada e sub-irrigação (NEH 624 cap. 10) além de localizar a fonte.

## 2. Dados mínimos específicos

| Cálculo | Pedir | Se faltar (rotular + consequência) |
|---|---|---|
| Espaçamento (permanente) | q (m/d); lençol de projeto e profundidade do dreno (dão h); K (m/d) por camada; D = profundidade da camada impermeável **abaixo do dreno**; raio efetivo r do dreno | K por textura `faixa_K_por_textura` (faixa de 1 a 3 ordens de grandeza, ver ref.), D como hipótese; Hooghoudt com r = 0,1 m; h sensível: espaçamento é muito sensível a h, K e q e pouco a D e r [ILRI-56 p. 45] |
| Tempo de rebaixamento | h0, ht, t, K, μ, D, r | μ por textura (tabela indicativa); declarar o critério de D médio |
| Duas camadas, dreno dentro da camada superior | Kt, Kb, espessuras Do e Db, r | sem isso, Ernst não roda: pedir à Geotecnia |
| Tubo dreno | q, L, comprimento B da linha, declividade ou perda de carga disponível, n do material, DN comercial | n por material (ref. `tubo-dreno-e-coletores.md`); área drenada +10 a 25 % [EMBRAPA-DREN-SUBT p. 18] |
| Dreno de fundo de canal | geometria do revestimento, NA externo, K sob o revestimento, taxa de infiltração ou de furos, declividade do tubo, ponto de saída | q de caso do acervo como **referência rotulada**, nunca gabarito |
| Diagnóstico | K (Porchet ou trado), profundidade da barreira, eficiência de irrigação prevista | classe só indicativa; limites são do Iuiu 2002, não de norma |

## 3. Método por nível

**Anteprojeto.** Critérios por faixa da literatura, Hooghoudt permanente (padrão) ou elipse (barreira rasa), K por
textura rotulado, tubo por Manning, dreno de fundo com q de caso do acervo rotulado. **Projeto básico.** K medido por
camada (Geotecnia), recarga e salinidade da Irrigação, Ernst quando há duas camadas, Glover-Dumm quando a recarga é
intermitente, tubo por perda de carga com a linha coletora, envoltório por critério. **Executivo/consultoria:**
ensaio de campo, modelo numérico, projeto de pilotos. O agente confere e não assina.

### 3.1 Critérios de projeto (o que define h, q e profundidade)

- **Lençol de projeto** (meio do vão): 0,8 a 0,9 m em culturas anuais; 1,0 a 1,2 m em fruteiras, conforme textura
  [FAO-IDP62 p. 113]; Embrapa/FAO 1980: 1,0 a 1,2 m (anuais), 1,0 a 1,1 m (hortícolas), 1,2 a 1,6 m (árvores), textura grossa a fina
  [EMBRAPA-DREN-SUBT p. 12, Tab. 1].
  Dreno ~0,50 m abaixo do lençol requerido (h ≈ 0,5 m) [EMBRAPA-DREN-SUBT p. 13]. Ver faixas e ILRI-56 em
  `criterios-e-tabelas.md`.
- **Descarga de projeto q:** irrigado árido 1 a 2 mm/d, irrigado com alguma chuva 2 a 4 mm/d [ILRI-56 p. 42; FAO-IDP62
  p. 114, Tab. 8: 1 a 2 mm/d]; 2 a 4 mm/d bastam para lixiviação em clima árido [FAO-IDP62 p. 113]. Brasil: 1,5 a
  4,5 mm/d [EMBRAPA-DREN-SUBT p. 13, Tab. 2]; Maniçoba 8 mm/d; Bebedouro 3,6 mm/d médio. **q vem da Irrigação**
  (recarga = lâmina × (1 − eficiência) + chuva); as faixas só calibram.
- **Regime:** permanente quando a recarga é quase contínua (gotejo, pivô); **transitório** quando é intermitente, com
  60 a 120 mm por turno [FAO-IDP62 p. 111-112]. Em turno de rega (lençol sobe e desce), Hooghoudt dimensiona pelo
  pico e sobredimensiona; Glover-Dumm dimensiona pelo critério "lençol cai x m em t dias". Rebaixamento entre duas
  regas: o que sobe deve voltar antes da seguinte; exemplo 40 mm × 5 % → 0,8 m, 30 dias → 1,3 mm/d [FAO-IDP62 p. 114].
- **Relação conhecida:** D (camada impermeável) deixa de importar quando D ≳ L/4 (d_e se estabiliza) [ILRI-56 p. 42].

### 3.2 Qual equação usar

| Situação | Equação | Função |
|---|---|---|
| Perfil homogêneo ou duas camadas com interface **na cota do dreno** | Hooghoudt L² = (8 K2 d_e h + 4 K1 h²)/q | `hooghoudt_espacamento` |
| Dreno sobre a barreira (D = 0) | Hooghoudt com d_e = 0: L² = 4 K h²/q | idem (D = 0) |
| Barreira rasa, vala ou envoltório de brita (fluxo horizontal) | Donnan / elipse | `donnan_espacamento`, `elipse_espacamento` |
| Duas camadas, dreno **dentro** da camada superior | Ernst | `ernst_duas_camadas_dreno_no_topo`, `ernst_espacamento` |
| Recarga intermitente, "lençol deve cair de h0 a ht em t dias" | Glover-Dumm 1,16 | `glover_dumm_espacamento`, `_tempo`, `_altura` |
| Subpressão e dreno de obra | Darcy e orifício | ref. `dreno-de-fundo-e-subpressao.md` |

Detalhe das equações, validade e exemplos conferidos: `references/hooghoudt-ernst-glover-dumm.md`. Resumo:

- **Hooghoudt**: d_e substitui D e embute a convergência radial; d_e depende de L (iterar). Forma de Moody (padrão) e
  série exata (`metodo_de="serie"`), 2 a 3 % abaixo [ILRI-DPA16 p. 267-268, Eq. 8.4, 8.7, 8.9-8.13]. Vale para
  regime permanente, drenos paralelos e equidistantes, K constante por camada. **L < ~10 m** invalida a hipótese.
- **Ernst**: h = h_v + h_h + h_r; u = π r (semicírculo) e fator a pela Tab. 8.2 quando o dreno está na camada
  superior [ILRI-DPA16 p. 270-272, 275, Eq. 8.17-8.23]. Exemplo 8.4: L = 38 m.
- **Glover-Dumm**: h_t = 1,16 h0 e^(−αt), α = π² K d/(μ L²); L = π√(K d t/(μ ln(1,16 h0/ht))) [ILRI-DPA16 p. 284,
  Eq. 8.32-8.33]. Vale com αt > 0,2. O fator é 1,27 (4/π) se o freático inicial for horizontal (Eq. 8.31).
  **O "D médio" tem três critérios** (ILRI d_e; USBR d_e + h0/2; Maniçoba d_e + (h0+ht)/4) que divergem até 8 %:
  declarar qual.

**Viés de campo (declarar a incerteza no parecer):** Hooghoudt superestimou L em 13,5 a 35 % em Maniçoba (solo
arenoso, campo) [EMBRAPA-MANICOBA p. 1, 8] e subestimou em 21 % no modelo de laboratório [EMBRAPA-ESPACAMENTO-1990
p. 10]. Sem sentido único: tratar como faixa de ±30 % no anteprojeto.

### 3.3 Tubo dreno (vazão e DN)

Vazão do dreno: Q = q · L · B (m³/d; `vazao_de_dreno`). Dois conceitos diferentes de capacidade, **não misturar**:

1. **Manning a seção plena ou parcial com a declividade do tubo** (`capacidade_tubo_dreno`, `capacidade_tubo_parcial`):
   conservador para tubo coletor longo. n: 0,011 (cerâmica e concreto com boa junta) a 0,016 (PEAD corrugado)
   [NRCS-NEH624-CH04 p. 88]. Velocidade não assoreante ~1,4 ft/s (0,43 m/s); máxima por solo ao redor 3,5 ft/s
   (1,07 m/s, areia) a 9 ft/s (2,74 m/s, cascalho) [NRCS-NEH624-CH04 p. 87-88].
2. **Perda de carga com vazão crescente ao longo da linha** (FAO-62 Anexo 20): o parâmetro é a perda de carga total
   H disponível, não a declividade; dreno horizontal funciona igual [FAO-IDP62 p. 211-212]. Tubo liso/técnico:
   Q = 89 d^2,714 s^0,571 (s = H/B) [FAO-IDP62 p. 214]; Embrapa grafa Q = 89 d^2,714 i^0,572 (Wesseling), 50 só para
   transporte [EMBRAPA-DREN-SUBT p. 16-17, Tab. 4]. Corrugado: Manning com Km = 1/n, máx. 65 [FAO-IDP62 p. 215-216].
   **Não há função para este conceito na calculadora** (lacuna; ver §9).

Margens: área drenada +10 a 25 % [EMBRAPA-DREN-SUBT p. 18]; declividade 0,02 a 1,0 %; linha < 300 m por
manutenção [EMBRAPA-DREN-SUBT p. 17, 20]. Detalhes, Km, a de Blasius, fator de manutenção e **D-86**:
`references/tubo-dreno-e-coletores.md`.

### 3.4 Dreno de fundo de canal revestido e subpressão

Três critérios de projeto distintos, três ordens de grandeza, nenhum reconciliado nos documentos:

| Projeto | Critério | Ordem de grandeza |
|---|---|---|
| CSB GEOHIDRO (doc 1341:76) | taxa de projeto q = 6e-5 m³/s por m de canal, 2 trincheiras (USBR 0,0213 m³/m²/24 h) | 6e-5 m³/s/m |
| Delmiro (doc 1492:105) | Darcy no solo, qd = K H²/X (2 lados), K máximo | 3,9e-7 m³/s/m (~150× menor) |
| Xingó (doc 1419:20) | furos na geomembrana: Q = Cd A √(2gH), 1 furo/2400 m², d = 8 mm | ≈ 1,8e-6 m³/s/m (seção hipotética do caso) |

A skill **não escolhe** entre eles: mostra os três, declara o usado e a consequência no DN, e delega a decisão
(K, freático, risco de subpressão) à Geotecnia e a seção ao Hidráulico. Limite de subpressão do CSB: 0,5 mca
(1341:77). `references/dreno-de-fundo-e-subpressao.md`.

### 3.5 Envoltório (só o critério hidráulico)

`criterio_de_filtro_hidraulico` (Terzaghi: D15f ≤ 5 D85s e D15f ≥ 5 D15s; o código usa fator 4 conservador, DNIT 5
[DNIT-DREN p. 252-253]), `necessidade_envoltorio_ilri56` (fluxograma, HFG) e `envoltorio_granular_pontos_controle`
(pontos 1 a 7). **Saída é indicativa.** Filtro real, geotêxtil e piping: `[DELEGAR: geotecnia]`. Em solo com
argila > 25-40 %, o ILRI-56 indica que o envoltório filtrante não é necessário para evitar assoreamento (checar HFG)
[ILRI-56 p. 46-47]. `references/envoltorio-e-filtro.md`.

### 3.6 Diagnóstico "precisa drenar?"

`diagnostico_drenabilidade(K, prof_barreira)` reproduz a decisão do Iuiu 2002: K 0,4 a 2,1 m/d e barreira > 1,5 m →
classe boa/restrita → sem drenagem subterrânea parcelar (1051:162-163). **Os limites são do projeto, não de norma.**
Resultado: indicação, com o alerta do próprio projeto: o lençol pode subir com irrigação de baixa eficiência
(1051:163). Não é "erro" do Iuiu não ter dimensionado dreno: é uma decisão fundamentada em Porchet e sem lençol.

## 4. Calculadoras (`tools/dren/drenos.py` 0.2.0): fórmula → função → teste

CLI: `python -m tools.dren.drenos --json "{\"funcao\": \"...\", ...}"` (ponto decimal; unidades m, m/d, m³/s, dias).
Rodar sempre e gravar `comando.txt` e `saida_*.json`. Exemplo (eval dsub-01: K 0,8 m/d, barreira a 4,5 m, dreno a
1,6 m, lençol a 1,0 m, q 5 mm/d, r 0,1 m → D = 2,9 m, h = 0,6 m):

```
python -m tools.dren.drenos --json "{\"funcao\":\"hooghoudt_espacamento\",\"q\":0.005,\"K\":0.8,\"h\":0.6,\"D\":2.9,\"r\":0.1}"
```
→ L = 43,5 m (d_e Moody = 2,16 m); `"metodo_de":"serie"` → 42,9 m (saída desta calculadora, sem gabarito de projeto).

| Fórmula | Função | Teste | Conferir nos `avisos` |
|---|---|---|---|
| d_e de Hooghoudt (Moody) | `d_equivalente_hooghoudt` | `test_ilri16_tab_8_1_d_equivalente_moody` | d/L ≤ 0,31 |
| d (série, exata) | `d_equivalente_serie` | `test_ilri16_exemplo_8_2_d_serie` | r0 = u/π |
| Hooghoudt (K ou 2 camadas) | `hooghoudt_espacamento` | `test_ilri16_exemplo_8_1…8_3`, `…manicoba_dreno_na_barreira_16_96` | L < 10 m; d_e ≪ D; regime permanente |
| Donnan | `donnan_espacamento` | `test_donnan_usbr_exemplo_1` | sem correção de convergência |
| Elipse (NEH 624 Eq. 4-8) | `elipse_espacamento` | `test_elipse_neh624_exemplo_1` | a > 8m: sem convergência radial |
| Fator a de Ernst | `fator_geometrico_ernst` | `test_fator_geometrico_ernst_tabela_8_2` | 0,1 < Kb/Kt < 1 fora da grade |
| Ernst | `ernst_espacamento`, `ernst_duas_camadas_dreno_no_topo` | `test_ernst_ilri16_exemplo_8_4_38_m`, `…u_padrao_semicirculo` | Dr > L/4, Db > L/4 |
| Glover-Dumm | `glover_dumm_altura/_tempo/_espacamento`, `d_medio_glover_dumm`, `tempo_de_drenagem` | `test_glover_dumm_manicoba_12_72_m`, `…fator_116_ilri16`, `…criterios_divergem` | t/j < 0,2; D médio fixo |
| Vazão do dreno | `vazao_de_dreno` | `test_vazao_de_dreno` | |
| Tubo pleno / parcial | `capacidade_tubo_dreno`, `capacidade_tubo_parcial`, `diametro_minimo_dreno` | `test_capacidade_manning_pleno_formula_fechada`, `test_tubo_parcial_meia_secao_e_geometria_exata` | y/D > 0,82; "xingo" é legado |
| Dreno de fundo | `dreno_de_fundo_de_canal_revestido`, `selecionar_tubo_csb`, `vazao_por_furo_geomembrana`, `vazao_infiltracao_geomembrana` | `test_csb_*`, `test_xingo_*` | faixa de capacidade CSB sem ancoragem |
| Darcy do dreno de fundo | `vazao_unitaria_darcy_dreno_fundo`, `comprimento_maximo_dreno_fundo` | `test_delmiro_qd_darcy_e_lmax` | forma reconstituída |
| Envoltório | `criterio_de_filtro_hidraulico`, `necessidade_envoltorio_ilri56`, `envoltorio_granular_pontos_controle` | `test_criterio_de_filtro_terzaghi`, `test_necessidade_envoltorio_hfg_ilri56`, `test_envoltorio_pontos_de_controle_ilri56` | indicativo; D15 > 0,09 mm |
| Tabelas | `faixa_K_por_textura`, `coeficiente_drenagem_tipico` (paginadas), `porosidade_drenavel`, `recomendacao_indicativa` (**sem página**, não usar em projeto) | `test_tabelas_paginadas_ilri56`, `test_tabelas_indicativas_com_aviso` | |
| Diagnóstico | `diagnostico_drenabilidade` | `test_iuiu_drenabilidade_sem_dreno_parcelar` | limites do Iuiu |

xfail estritos (reportar, não ajustar fórmula): `test_delmiro_capacidade_dn170/dn230_declarada`,
`test_csb_L200_2DN150`.

## 5. Critérios de verificação (ligados às V-regras do perfil)

| ID | Verificar | Atendida se |
|---|---|---|
| DS1 | Unidades: q em m/d (1 L/s/ha = 8,64 mm/d), K em m/d, tempo em dias | conversão declarada; q de projeto dentro da faixa da fonte ou justificado |
| DS2 | Hipóteses da equação | regime, camadas, posição do dreno e L ≥ 10 m conferidos; D medido **abaixo do dreno** |
| DS3 | Sensibilidade | variar h, K e q (±) e mostrar L; K por textura = faixa, não valor |
| DS4 | Método declarado | `metodo_de` e critério de D médio no parecer; viés de campo ±30 % citado |
| DS5 | Tubo | Q = q L B com +10 a 25 %; capacidade com n declarado; V ≥ 0,43 m/s ou tubo com envoltório/armadilha de sedimento [NRCS-NEH624-CH04 p. 87-88]; linha < 300 m |
| DS6 | Saída | cota de descarga acima do NA do coletor (≥ 10 cm) [EMBRAPA-DREN-SUBT p. 20]; deságue em coletor aberto = `canais-de-drenagem-e-macrodrenagem` |
| DS7 | Dreno de fundo | q e DN do **mesmo** critério; capacidade do tubo recalculada com n e S declarados; saída intermediária se Q > capacidade |
| DS8 | Envoltório | só critério; "filtro real" delegado |
| DS9 | Interfaces | q e h vieram da Irrigação ou são premissa rotulada; K e D, da Geotecnia ou premissa |
| DS10 | Divergência com projeto | aponta com `doc:pág`, comando e consequência; não corrige |

Reproduzir todo `avisos`. Sem K, D e q medidos, o resultado é **ordem de grandeza**.

## 6. Armadilhas do acervo (casos negativos de treinamento)

| Armadilha | Onde | Como detectar e o que fazer |
|---|---|---|
| Capacidade do tubo dreno declarada 4,7 a 6,9× menor que Manning com os dados do memorial; razão DN230/DN170 = 3,25, mas D^(8/3) dá 2,19 | Delmiro 1492:105 | `capacidade_tubo_parcial` (D 0,149 → 1,05e-3 m³/s; 0,200 → 2,31e-3). Pedir S e n; não ajustar. Inócuo no projeto (limite de manutenção 250 m governa), relevante se K real for alto |
| Fórmula legada embutida: Q = 33,5 D^2,67 i^0,5 = Manning pleno com n ≈ 0,0093; com n 0,012 a 0,013 a capacidade cai 22 a 28 % | Xingó 1419:21 | converter para n equivalente antes de comparar; DN300, i = 1e-4: 1,35e-2 (legado) × 7,9e-3 (n 0,016) × 9,7e-3 (n 0,013) m³/s |
| Três critérios de q de dreno de fundo sem reconciliação (6e-5, 3,9e-7, ~1,8e-6 m³/s/m) | CSB, Delmiro, Xingó | tabela §3.4; sem gabarito; delegar K e freático |
| CSB usa Manning com o **gradiente de pressão**, não a declividade do tubo ("simplificação do USBR"); D por declividade i dá mais: 800 m, 2 tubos, i = 1e-4, n 0,011 → 0,40 m × DN300 do memorial | CSB 1341:76 | citar a diferença como regra do USBR, não erro; capacidades dos tubos sem ancoragem |
| `q` em L/s/ha lido como mm/d (1,2 L/s/ha = 10,4 mm/d, 5 a 10× a faixa de irrigado árido) | evals dsub-03/04 | converter e comparar com a faixa; perguntar à Irrigação |
| Hooghoudt com o termo extra (Di − Dd) da nota WATERLOG: dimensionalmente inconsistente | WATERLOG-DRAINAGE-EQUATION p. 2 | usar a forma de ILRI-16 Eq. 8.4/8.7 |
| Ernst do exemplo de Ritzema sem o fator a: 51,8 m contra 38 m (36 %) | WATERLOG-ENDRAIN p. 10 × ILRI-DPA16 Ex. 8.4 | usar a Tab. 8.2 (a = 3,9) |
| Dreno de fundo com pouca declividade e saída a mais de 250 m; PIL ausente | Delmiro 1492:106 | limite de manutenção 200 a 300 m |
| D medido da superfície em vez de abaixo do dreno | recorrente | D = cota da barreira − cota do dreno |
| Premissa de projeto sem fonte numérica local: "1 furo/2400 m²" (literatura 1/800 a 1/4000 m²) | Xingó 1419:20 | declarar a faixa da literatura e o efeito no DN |
| Tabelas de μ e de profundidade/espaçamento por K **sem página** na calculadora | `drenos.py` | `porosidade_drenavel` difere da Tab. 3 de [EMBRAPA-DREN-SUBT p. 14]; usar a Tab. 3 paginada; `recomendacao_indicativa` não vai a parecer |
| Nenhum projeto do acervo traz Hooghoudt, Ernst ou Glover-Dumm calculado | `casos/drenagem/_INDICE.md` | sem gabarito de projeto: gabaritos são de livro (ILRI-16, Embrapa) |

## 7. O que a norma exige e a quem se aplica

Não há norma brasileira de espaçamento de dreno agrícola no corpus. O que existe: **DNIT-DREN cap. 5** (drenos
profundos de rodovia, Terzaghi, p. 249-282: não é dreno agrícola); **DNIT-ES015/016/017** (execução de drenos
subterrâneos, sub-superficiais e sub-horizontais, p. 3-7: material, tubo, filtro; sem dimensionamento);
**CDV-MANUAL-IRRIG** p. 251-255 e 511-513 (subdrenagem sob revestimento e tipos de drenos, remetendo ao Manual do
USBR); manuais Embrapa e FAO-62 (diretrizes, não norma). O pedido "o que a norma exige" fecha com: diretriz, não
exigência; ver `drenagem-normas-e-manuais`.

## 8. Referências (IDs e páginas-chave)

- ILRI-DPA16 (Hidráulico): Hooghoudt Eq. 8.3-8.7 p. 264-266; Tab. 8.1 p. 267; d série Eq. 8.9-8.14 p. 268; Ernst
  Eq. 8.17-8.21 p. 270-272, Tab. 8.2 p. 272, Ex. 8.1-8.4 p. 276-281; Glover-Dumm Eq. 8.28-8.33 p. 283-284.
- USBR-DRAINAGE (PDF = impr. + 19): d_e de Moody p. 173-174; exemplo transitório p. 187; Donnan p. 188-190; tubo e
  envoltório p. 231-256 (mapa H15; página exata a confirmar).
- NRCS-NEH624-CH04: elipse Eq. 4-8 p. 63-66; grades e velocidades p. 87-88; dimensionamento de linha p. 93; filtros
  p. 96-102.
- FAO-IDP62: critérios p. 111-114; Anexo 20 (tubos) p. 211-217; Anexo 17 (fórmulas) p. 193-200.
- ILRI-56-ENVELOPE (próprio): p. 42-47, 66-68, 175 (PDF = impr. + 20).
- EMBRAPA-DREN-SUBT p. 12-18, 20; EMBRAPA-MANICOBA-1988 p. 1-3, 7-8; EMBRAPA-ESPACAMENTO-1990 p. 5-10;
  EMBRAPA-BEBEDOURO-1986 (números degradados, só localização); WATERLOG-ENDRAIN p. 7-10; DNIT-DREN p. 252-253.
- Casos: `csb_geohidro_dreno_fundo_canal_subsuperficial`, `xingo_lote1_drenagem_interna_canal_subsuperficial`,
  `iuiu_2002_drenabilidade_subterranea_diagnostico`, `2026-10-08_delmiro_gouveia_dreno_fundo_canal_comprimento_maximo`.
  Nenhum número tem `✓h`.
- Divergências: `tools/dren/DIVERGENCIAS.md`, seção "drenos".

## 9. Lacunas

- FAO Paper 38 e o Skaggs não estão no corpus: tabelas indicativas antigas "a confirmar"; os valores paginados
  vêm de EMBRAPA-DREN-SUBT, ILRI-56 e FAO-IDP62.
- **Calculadora sem:** perda de carga em tubo coletor com vazão crescente (FAO-62 Anexo 20, Wesseling); Toksöz-Kirkham
  e anisotropia (FAO-62 Anexo 17); Kirkham; efeito de resistência de entrada; elipse modificada (NEH 624 Ex. 2,
  196 ft, gráfico); critérios de uniformidade e D50 do DNIT.
- Sem exemplo numérico de envoltório com resposta (só figuras, ILRI-56 Figs. 11-12).
- Sem caso do acervo com dreno agrícola calculado; D-86 (tubo dreno de 300 mm) é pendência de aceitação F10: este
  skill entrega a análise (ref. `tubo-dreno-e-coletores.md`); **só o André decide D-86**.
- Nada nesta skill depende dos quatro pontos abertos da F7 do núcleo. Marcado "padrão provisório, decisão F7": n do
  tubo e uso de Manning pleno × parcial no tubo dreno (a calculadora usa pleno; o ILRI-56 e o NEH 624 admitem
  pleno e até 1,2× com carga).
