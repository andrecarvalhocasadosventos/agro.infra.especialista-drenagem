# Canal do Sertão Baiano — Drenagem de fundo (subpressão) do canal revestido, drenos trincheira e MVF (doc 1341)
fonte: Memoriais descritivo e de cálculo - Sistema de drenagem.pdf (doc 1341):74-77
disciplinas: [drenagem-subsuperficial, bueiros-e-drenagem-superficial]
nivel: anteprojeto
(Não é drenagem agrícola de parcela; é drenagem subsuperficial de obra linear de canal revestido. Registrado porque é o único caso de drenagem subterrânea com memória numérica achado.)

## Problema
Canais de adução revestidos (membrana + placas de concreto) em corte interceptam freático e sofrem subpressão quando o canal é esvaziado. Dimensionar drenos longitudinais de fundo, escalonamento de tubos, lançamentos e minadores com válvula flap (MVF).

## Dados de entrada
| grandeza | valor | unidade | fonte | ancoragem |
|---|---|---|---|---|
| Infiltração do revestimento (taxa de projeto) | 0,00006 | m³/s por m de canal | 1341:76 (base: USBR 0,0213 m³/m²/24 h, Manual Codevasf vol.7 p.269-270, 1341:75) | ✓ |
| Profundidade da trincheira abaixo do fundo | 0,70 (até 1,20 em cortes longos) | m | 1341:76, 75 | ✓ |
| Declividade longitudinal do dreno / canal | 0,0001 | m/m | 1341:75, 77 | ✓ |
| Permeabilidade dos solos | 1e-4 a 1e-6 | cm/s | 1341:76 | · (sem valor extraído) |
| Subpressão limite para ruptura | 0,5 | mca | 1341:77 | ✓ |
| Espaçamento meta entre saídas | 500 | m (Transposição SF) | 1341:75 | texto |
| Desnível inicial até 1ª caixa / adicional na caixa de medição | 0,30 / 1,05 | m | 1341:75 | texto |
| PV a cada 100 m, declive do ramal | 0,001 | m/m | 1341:75 | texto |

## Método
- Vazão linear acumulada q = 0,00006 m³/s/m em duas trincheiras com PVC ranhurado; nível máximo no dreno = fundo do canal; Manning aplicado com o gradiente de pressão em vez da declividade do tubo, "simplificação adotada pelo USBR" (1341:76).
- Capacidade por tubo (PVC ranhurado): DN150 0,004–0,005; DN300 0,025–0,031; DN400 0,050–0,064; DN500 0,082–0,101 m³/s (1341:76; valores sem ancoragem '·', conferir).
- Escalonamento (2 tubos): 2DN150 até 200 m; 2DN300 trecho 800 m (acum. 1000 m); 2DN400 1000 m (acum. 2000 m); 2DN500 1200 m (acum. 3200 m) (1341:76 ✓).
- MVF (Flap Valve Weep, USBR): 30 % da extensão de cada trecho de dreno profundo, 2 MVF a cada ~10 m, 15 % para cada lado do centro entre duas saídas; vazão 0,5–2,5 l/s por MVF; 2 flaps atendem no máx. 0,002/0,00006 = 33,3 m; ponteira DN38 mm; atua entre 0,15 e 0,50 mca; reforço de 42,9 % sobre a vazão subterrânea admitida (1341:77).

## Resultado
Tabela de tubos/trechos acima; drenagem por gravidade (sem bombeamento), lançamentos em talvegues com caixas de medição (vertedor triangular) tipo I e II. Desenhos/planilhas por trecho em 1:25000 (1341:77, não lidos).

## Gabarito para calculadora
- Entradas: extensão L até a saída (m), q=6e-5 m³/s/m, duas trincheiras. Saída: Q = q·L; tubo mínimo conforme tabela. Ex.: L=800 m -> Q=0,048 m³/s total (0,024 por tubo) -> 2DN300 (0,025–0,031 por tubo) ✓ coerente. L=1000 m -> 0,060 (0,030/tubo) -> 2DN300 no limite acumulado 1000 m. Tolerância: seguir a faixa da tabela de capacidades, não um valor único.
- MVF: n de flaps = ceil(L_trecho·0,30 / 10)·2 aproximado (regra interpretativa; não está literal).

## Observações
- Capacidades dos tubos e permeabilidade têm marca '·' no extrator: conferir pág. 76 antes de usar.
- Não há cálculo de rebaixamento de lençol, espaçamento de drenos nem condutividade hidráulica -> não serve como caso de drenagem agrícola.
