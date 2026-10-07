# Canal Xingó Lote I — Drenagem interna do canal revestido (subpressão): vazão por furo na geomembrana e tubo dreno (doc 1419)
fonte: v. 5. Memorial de cálculo e dimensionamentos.pdf (doc 1419; 1451 é cópia idêntica, 764 p., usar 1419):18-22
disciplinas: [drenagem-subsuperficial]
nivel: basico (Projeto Básico Lote I, ENGECORPS/TPF, ref. 1377-CDF-00-GL-RT-0021)
(Drenagem de obra linear, não agrícola. Dois casos numéricos de dreno de fundo no acervo: este e CSB GEOHIDRO.)

## Problema
Dimensionar a drenagem interna do canal de adução (drenos "finger" transversais a cada 4 m + trincheira no eixo sob o fundo com tubo perfurado) para captar vazamentos pela geomembrana e eventual freático, evitando subpressão no revestimento.

## Dados de entrada
| grandeza | valor | unidade | fonte doc:pág | ancoragem |
|---|---|---|---|---|
| Frequência de defeitos | 1 furo a cada 2400 m² de revestimento (média) | m² | 1419:20 (literatura: Zornberg&Weber 1/800 m²; Giroud&Bonaparte 1/4000 m²) | texto |
| Diâmetro do furo | 0,008 | m | 1419:20 | texto |
| Coef. de descarga do orifício | 0,634 | — | 1419:20 (Porto 1999) | texto |
| Carga | H = tirante do estudo hidráulico (m) | m | 1419:20 | texto |
| Contribuição de freático | desconsiderada (aterro: sem; corte/misto: freático profundo, sem fontes) | — | 1419:19 | texto |
| Declividade do tubo | = declividade de fundo do canal | m/m | 1419:20 | texto |
| Seção drenante | y/d = 0,938 | — | 1419:21 | texto |
| Capacidade do tubo | Q = 33,5·D^2,67·i^0,50 (m³/s; D m) — de catálogos de tubos perfurados de PEAD | m³/s | 1419:21 | texto |
| Colchão de areia e vala | capacidade drenante desconsiderada (conservador) | — | 1419:19 | texto |

## Método
Qc = Cd·A·(2gH)^0,5 = 0,634·(π·0,008²/4)·(2·9,8·H)^0,5 por furo; vazão por metro Q1m = Qc·A1/2400 (A1 = área de revestimento por metro de canal, calculada em cada estaca); Q1 por estaca (20 m) = Q1m·20; acumula-se até a saída e compara-se com a capacidade do tubo (1419:20-21).

## Resultado
Quadro 3.1 (1419:21): tubo perfurado ø300 mm em todo o trecho listado; trechos entre saídas de 20 m a 3400 m (ex.: estaca 2+640 a 5+560, saída a 3120 m; 12+620 a 16+000, 3400 m). Saídas laterais para monitoramento. (Diâmetros em coluna sem rótulo no extrator; conferir 1419:21.)

## Gabarito para calculadora
- Entrada: H = 3,0 m -> Qc = 0,634·5,0265e-5·(2·9,8·3,0)^0,5 = 2,44e-4 m³/s por furo. Saída esperada (tol. 1 %).
- Entrada: D=0,300 m, i=0,0001 -> Q = 33,5·0,300^2,67·0,0001^0,5 = 0,0135 m³/s (reproduzido por mim; dreno.py ou tubo_dreno.py deve dar o mesmo).
- Vazão por m: seção hipotética b=4 m, H=3,5 m, talude 1:1,5 -> A1 ≈ 16,6 m²/m (suposição minha) -> Q1m = Qc(3,5 m)·16,6/2400 = 1,8e-6 m³/s/m (≈ 3 % da taxa 6e-5 m³/s/m adotada no CSB) — mostra a diferença de critério entre os dois casos.

## Observações
- Premissa sem fonte numérica local: 1 furo a cada 2400 m² (escolha do projetista entre duas referências).
- Capacidade do tubo é fórmula empírica de catálogo (não Manning); n implícito não declarado.
- Páginas 22-25 (lançamentos, medição) não lidas.
