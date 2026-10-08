# Dreno de fundo de canal revestido e subpressão: três critérios de projeto, nenhum reconciliado

Obra linear, não é drenagem agrícola de parcela. Os três projetos do acervo adotam critérios diferentes, com ordens de
grandeza que diferem por até duas ordens (6e-5 × 3,9e-7 m³/s por metro). Nenhum número tem `✓h`. A skill **não
escolhe**: apresenta, declara o usado, mostra o DN resultante em cada leitura e delega K, freático e estabilidade.
Regra mestra do núcleo: apontar, nunca corrigir em silêncio.

## 1. CSB GEOHIDRO (Canal do Sertão Baiano, doc 1341:74-77)

- Problema: canal revestido (membrana + placas) em corte intercepta o freático; esvaziado, sofre subpressão.
- Taxa de projeto q = **6e-5 m³/s por m de canal** (base USBR 0,0213 m³/m²/24 h, Manual Codevasf vol. 7, 1341:75-76),
  duas trincheiras de PVC ranhurado, profundidade 0,70 m (até 1,20 em corte longo) abaixo do fundo, declividade do dreno
  0,0001. Nível máximo no dreno = fundo do canal. Permeabilidade dos solos 1e-4 a 1e-6 cm/s (sem ensaio extraído).
- Capacidade por tubo (PVC ranhurado, faixa em m³/s): DN150 0,004 a 0,005; DN300 0,025 a 0,031; DN400 0,050 a 0,064;
  DN500 0,082 a 0,101 (1341:76, **sem ancoragem**: conferir a página). Manning com o **gradiente de pressão**
  (simplificação do USBR), não com a declividade do tubo.
- Escalonamento (2 tubos): 2DN150 até 200 m; 2DN300 (trecho de 800 m, acumulado 1.000 m); 2DN400 (acum. 2.000 m);
  2DN500 (acum. 3.200 m) (1341:76). Saídas de 500 m (meta).
- Subpressão limite de ruptura: **0,5 mca** (1341:77). MVF (Flap Valve Weep, USBR): 30 % da extensão, 2 MVF a cada ~10 m,
  vazão 0,5 a 2,5 L/s por MVF, atua entre 0,15 e 0,50 mca, reforço de 42,9 % (1341:77). Calculadora:
  n_MVF = 2·ceil(0,30 L/10), regra **interpretativa** do gabarito.
- Funções: `dreno_de_fundo_de_canal_revestido`, `selecionar_tubo_csb`. Testes: `test_csb_L800_2DN300`,
  `test_csb_L1000_2DN300_no_limite`, `test_csb_trechos_acumulados`, `test_csb_mvf_regra_interpretativa`. **xfail
  estrito:** `test_csb_L200_2DN150` (Q 0,006 m³/s por tubo > 0,005 do próprio memorial).

Exemplo: L = 800 m, q = 6e-5, 2 tubos, i = 1e-4 → Q = 0,048 (0,024 por tubo) → DN300 (faixa 0,025-0,031);
D por Manning pleno n = 0,011 = 0,396 m (conservador, porque o CSB usa o gradiente de pressão).

## 2. Xingó Lote I (doc 1419:18-22)

- Frequência de defeitos na geomembrana: **1 furo a cada 2.400 m²** (média de duas referências: Zornberg-Weber 1/800 m²;
  Giroud-Bonaparte 1/4.000 m²); furo de 8 mm; Cd = 0,634 (Porto, 1999). Carga H = tirante do estudo hidráulico.
- Por furo: Qc = Cd·A·√(2gH) (H = 3 m → 2,44e-4 m³/s; o caso usa g = 9,8). Por metro: Q1m = Qc·A1/2400, A1 = área de
  revestimento por metro (seção hipotética b 4 m, H 3,5 m, talude 1:1,5: A1 ≈ 16,6 m²/m → 1,8e-6 m³/s/m, ~3 % do
  CSB). Contribuição de freático desconsiderada (corte/misto: freático profundo, sem fontes). Colchão de areia
  desconsiderado (conservador). Drenos "finger" a cada 4 m + trincheira no eixo com tubo perfurado.
- Tubo: ø300 mm em todo o trecho; saídas de 20 a 3.400 m; y/d = 0,938; capacidade pela fórmula de catálogo
  **Q = 33,5 D^2,67 i^0,5** (1419:21), D = 0,30 m e i = 1e-4 → 0,0135 m³/s, equivale a Manning pleno com n ≈ 0,0093
  (não é Manning; unidades a confirmar). Com n 0,012 a 0,013 a capacidade cai 22 a 28 %.
- Funções: `vazao_por_furo_geomembrana`, `vazao_infiltracao_geomembrana`, `capacidade_tubo_dreno(formula="xingo")`.
  Testes: `test_xingo_vazao_por_furo_H3`, `test_xingo_tubo_D300_i1e4`, `test_xingo_n_implicito_da_formula_legada`,
  `test_xingo_vazao_por_metro_secao_hipotetica`.
- Premissa **sem fonte numérica local**: 1 furo/2.400 m². Declarar a faixa 1/800 a 1/4.000 e o efeito (fator 3 em cada
  sentido na vazão e, portanto, no DN).

## 3. Delmiro Gouveia (AL) (doc 1492:102-106)

- Seção: trapezoidal 1,5H:1V, base 1,35 m, tirante 0,90 m, geomembrana PEAD + proteção de concreto.
- **Darcy**: qd = K H²/(2X) por lado, ×2 lados = K H²/X. K = 1e-6 m/s (1e-4 cm/s, areno-siltoso, ensaio não citado), H = 1,26 m,
  X = 4,06 m → **qd = 3,91e-7 m³/(s·m)** (memorial 3,910e-7). A forma da equação está em imagem: reconstituída
  (`vazao_unitaria_darcy_dreno_fundo`, "rastro C"). K máximo normal ("tendência ao superdimensionamento"); o projetista
  admite que K pode variar uma ordem de grandeza.
- PEAD corrugado parede simples n = 0,016 (parede dupla 0,010); DN170 (Ø int. 149 mm) e DN230 (200 mm); S = 3e-4 ("de
  projeto do canal", a do tubo pode ser outra); meia seção. Memorial: Q = 1,518e-4 e 4,929e-4 m³/s; Lmáx = Q/qd = 388 e
  1.260 m (reproduz a 1 %). Concepção: trechos de até 250 m com PIL; DN170 até 350 m, transição a DN230 acima (1492:106).
- **Divergência:** Manning meia seção com os dados do memorial dá 1,05e-3 (DN170) e 2,31e-3 m³/s (DN230): 6,9× e 4,7×
  o declarado; a razão DN230/DN170 deveria ser (200/149)^(8/3) ≈ 2,19 e o memorial dá 3,25 (equivale a Q ∝ D⁴).
  Consequência: inócua no projeto (limite de manutenção 250 m governa); com K 10× maior, Lmáx pelos valores do
  documento cairia para ≈ 39 m (DN170) e pelo Manning para ≈ 270 m: o erro só pesaria com K alto. **Não ajustar**:
  2 xfail estritos (`test_delmiro_capacidade_dn170/dn230_declarada`); pedir S e n usados; hipóteses (S do tubo, n,
  transcrição) não documentadas.
- Funções: `capacidade_tubo_parcial`, `vazao_unitaria_darcy_dreno_fundo`, `comprimento_maximo_dreno_fundo`. Testes:
  `test_tubo_parcial_meia_secao_e_geometria_exata`, `test_delmiro_qd_darcy_e_lmax`,
  `test_delmiro_razao_entre_dn_segue_d_8_3`, `test_delmiro_tubo_recalculo_manning_acervo_sem_h`.

## 4. Comparação (para o parecer)

| Projeto | Critério | q (m³/s/m) | Tubo | Saída |
|---|---|---|---|---|
| CSB | taxa USBR | 6e-5 | 2DN150 a 2DN500 | 200 a 1.200 m por trecho |
| Delmiro | Darcy, K máx. | 3,9e-7 | DN170/DN230 | ≤ 250 m (PIL) |
| Xingó | furos, 1/2.400 m² | ≈ 1,8e-6 (hipotético) | ø300 | 20 a 3.400 m |
| CAC Trecho 1 | 2 PVC ø150 perfurados, sem cálculo (doc 1131:28) | | | bueiro mais próximo |

Nenhum documento reconcilia as ordens de grandeza. Se o pedido é "qual vazão de subpressão?", responder: depende do
critério (infiltração por área do revestimento × freático × defeito); mostrar os três; delegar K e freático
(`[DELEGAR: geotecnia]`), seção e NA (`[DELEGAR: hidraulica]`).

## 5. O que pedir para fechar um dreno de fundo

Revestimento (placa, membrana), NA externo e do canal nos cenários (cheio, vazio, rápido esvaziamento), K sob o
revestimento (medido), perfil geológico (corte/aterro), comprimento entre saídas viáveis, cota de deságue e talvegue
receptor (caixa de medição, vertedor triangular), declividade do tubo, DN e Ø interno do catálogo, n do material,
envoltório (Geotecnia). Subpressão e estabilidade do revestimento são Hidráulica/Geotecnia; o DN do tubo é daqui.
