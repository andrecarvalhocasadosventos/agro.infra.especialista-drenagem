# Caso HR-02 — Verificação da malha e da convergência do modelo 2D da captação (TPF)

**Tipo:** positivo com ressalva. **Pergunta:** o modelo entregue cumpre o que o relatório declara (malha, Manning, tempo para estabilizar) e chegou a regime permanente em 24 h?
`REL-FINAL` e `HR-SF` como em HR-01. Números lidos com `h5py` das cópias locais (somente leitura) de `sao_francisco_Q95/sao_francisco.g01.hdf`, `sao_francisco_Q95/sao_francisco.p01.hdf` e `sao_francisco_QTR100/sao_francisco.p01.hdf`. Marca B para tudo que veio de leitura do `.hdf` (derivado de arquivo, não de texto de documento); sem ✓h.

## Dados e achados
| Item | Declarado | No arquivo | Marca |
|---|---|---|---|
| Rugosidade | 0,035 (REL-FINAL:41) | 1 valor único (0,035) nas 31.313 células | B |
| Malha | 10 m onde há batimetria, 50 m fora (REL-FINAL:41) | área de célula: mediana 99,93 m² (≈ 10 m × 10 m), média 648 m², máxima 4.348 m² (≈ 66 m) | B |
| Condição inicial | não informada | cota de armazenamento inicial 382,4 m (`.u01`: `Initial Storage Elev=Perimeter 1,382.4`), contra NA final de 390,8 m (Q95) | A (arquivo) |
| Duração | não informada | 14-set 01:00 a 15-set 01:00 (24 h), passo de cálculo 10 s, intervalo de saída de 15 min e de mapeamento de 30 min no `.p01` (o `.hdf` tem 49 passos, ou seja, 30 min) | A |
| Estabilização, Q95 | — | variação máxima de NA nas células molhadas nas últimas 2 h: 0,0005 m (p99: 0,0002 m) | B |
| Estabilização, QTR100 | — | variação máxima nas últimas 2 h: 0,040 m em pelo menos uma célula (p99: 6·10⁻⁵ m) | B |
| NA em célula profunda (Q95) | — | 389,82 m no início, 390,95 m após 3 h, 391,00 m após 6 h, 391,01 m após 9 h e no fim (saídas a cada 30 min: 49 passos) | B |
| Velocidade (face), máx. | relatório só mostra mapa | Q95: p95 0,86 m/s, máx. 7,16 m/s; QTR100: p95 2,18 m/s, máx. 3,56 m/s | B |

## Método do projetista
Vazão constante por 24 h e leitura do NA final; a duração basta porque o NA de uma célula profunda estabiliza em até ~6 h no Q95 e no QTR100 (B: séries das células 20907 e 17164, amostradas de 3 em 3 h).

## Gabarito (candidato; sem ✓h)
Critério de aceitação demonstrável: ΔNA ≤ 0,01 m em 2 h (Q95: 0,0005 m passa; QTR100: 0,040 m em células isoladas não passa o limite estrito e precisa de nota). A velocidade máxima de 7,16 m/s no Q95 é de uma face, provavelmente na borda da malha ou em degrau de terreno (C: não localizada); não pode ser lida como velocidade do rio.

## Divergências
Nenhuma entre texto e arquivo na malha e no Manning. O relatório não declara condição inicial nem tempo de simulação.

## Teste que a skill deve passar
`modelagem-hidraulica-hec-ras` (F6) deve exigir no parecer: condição inicial, duração, critério de estabilização, estatística de células (mediana, p95, máx.), distinção entre máximo de face e velocidade do canal.
