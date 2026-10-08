# CAC Trecho 1 (Castanhão - Curral Velho, CE) — Quadro de 59 bueiros sob o canal adutor: cota do rasto do B31 incoerente com o perfil e com o coletor
tipo: NEGATIVO (erro de transcrição/consistência no quadro do projeto executivo, detectável por teste de monotonia e de posição relativa)
qualidade: C (quadro de localização e seção, sem vazão, HW, comprimento ou método; hidráulica citada de estudo externo não presente no acervo)
fonte: doc 1131, Tomo 2 "Canais e Sifões", Vol. 1 Memória Descritiva, Projeto Executivo do Trecho 1 (Consórcio COBA/VBA/HARZA, 12/11/2002), pp. 28, 48, 64-67 (Cap. 17, Quadro 17.1). O estudo que dimensiona os bueiros ("Estudos Hidráulicos para o Dimensionamento das Estruturas de Drenagem de Proteção do Trecho 1", HARZA Hidrobrasileira, 2001, citado em 1131:65) não foi achado no acervo (busca "Drenagem de Proteção").
disciplinas: [bueiros-e-travessias]
nivel: projeto executivo
legenda de marcas: `✓` ancorado na camada de texto (todas as linhas de 1131:65-67 e 28 estão `✓` na extração: o erro está no documento, não na leitura); `✓*`/`!`/`~` nenhum; `✓h` nenhum.

## Pergunta de engenharia
Que bueiros transpõem o canal adutor trapezoidal (rasto 5,0 m, altura 3,0 m até a berma, boca 14,0 m, talude 1,0H:1,5V) e que verificação simples de consistência o quadro de localização precisa passar antes de ser usado?

## Dados de entrada
| grandeza | valor | un. | fonte doc:pág | marca |
|---|---|---|---|---|
| Nº de bueiros no Quadro 17.1 | 59 (B01 a B48, com sufixos A, B) | un. | 1131:65-67 | ✓ |
| Seção do bueiro | 46 × 1 φ800; 4 × 1 φ1200; 5 × 2 φ1200; 2 × 1 φ1000; 2 × 2 φ1500 (contagem minha) | mm | 1131:65-67 | ✓ |
| Inclinação do bueiro | 1 (todos) | % | 1131:65-67 | ✓ |
| Posição | de 3+500 (B01) a 43+780 (B48) | km+m | 1131:65-67 | ✓ |
| Cota do extradorso inferior do coletor / cota do rasto do canal | 2 colunas por bueiro, em m | m | 1131:65-67 | ✓ |
| Critério declarado | drenagem transversal por bueiros para linhas de água de importância; as menores vão por valetas e descidas ao bueiro mais conveniente | — | 1131:64-65 | texto |
| Descarga de fundo do canal | 2 bueiros de Ø interno mínimo 1,30 m para 11,0 m³/s gravitário (50 % da Q máx da 2ª etapa), independentes da drenagem transversal | — | 1131:48 | texto |
| Dreno de fundo do canal | 2 tubos PVC perfurados Ø150 mm sob o fundo, em material drenante, onde o nível freático é superficial; descarga gravitária para o bueiro mais próximo | — | 1131:28 | texto |
| Proteção na saída | enrocamento (descarga de segurança) | — | 1131:48 | texto |

## Método do projetista
Não informado nas páginas lidas: o dimensionamento está no estudo HARZA 2001. O quadro só lista seção, inclinação e as duas cotas (coletor e rasto do canal).

## Resultado
Linhas relevantes (1131:66, cotas em m):
| bueiro | km+m | seção | extradorso do coletor | rasto do canal |
|---|---|---|---|---|
| B30 | 34+553 | 1 φ800 | 91,500 | 94,246 |
| B31 | 34+926 | 1 φ800 | 92,000 | **91,189** |
| B32 | 37+336 | 1 φ1000 | 90,500 | 92,977 |

## Gabarito para a calculadora
Não há gabarito numérico de dimensionamento (nada foi publicado). Gabarito de verificação de consistência (rastro B):
- Teste 1 (monotonia): a cota do rasto de um canal de adução em declividade positiva não pode subir para jusante. Nas 59 linhas, a única violação é B31 → B32 (91,189 → 92,977 m, sobe 1,79 m em 2,41 km), precedida de B30 → B31 (94,246 → 91,189, cai 3,06 m em 0,37 km).
- Teste 2 (posição relativa): o coletor passa sob o canal; extradorso do coletor deve ficar abaixo do rasto. Em B31 o coletor (92,000) está 0,81 m acima do rasto (91,189): única violação nas 59 linhas.
- Valor coerente com a sequência: ≈ 94,2 m (entre 94,246 de B30 e 92,977 de B32; 94,189 seria a transcrição provável). Rastro C: não é dado do documento.

## Rastro
- A: as duas cotas de B30, B31, B32 (✓ na extração, texto nativo).
- B: testes de monotonia e posição aplicados às 59 linhas por varredura (script nesta sessão; só os números do quadro).
- C: o valor correto de B31 e a causa (digitação).

## Divergências
1. B31: ver Gabarito. A queda de 13 m de B10 (119,574 em 11+530) para B10A (106,341 em 13+260) e as demais variações maiores correspondem provavelmente a quedas/rápidos e sifões do trecho (1131:13-14, 48); não verificadas.
2. Inclinação 1 % em todas as linhas e seção por bueiro sem Q publicada: a escolha φ800 em 46 de 59 pontos (mínimo de manutenção) indica dimensionamento governado pelo diâmetro mínimo; não informado.
3. Descarga de fundo (1131:48): 2 × φ1,30 para 11,0 m³/s gravitário (5,5 m³/s por linha, A ≈ 1,33 m², V ≈ 4,1 m/s se a seção correr cheia); declividade e carga não informadas, sem teste possível.
4. Doc 1122:345-346 (EVT Castanhão-Gavião, estudo de viabilidade; data não informada): critérios para outro trecho do mesmo sistema (Racional < 3,5 km²; TR 50 para bueiros; C = 0,22; Ke = 0,50; V < 4 m/s; "controle na entrada", "Hw < 1,5·D", "subcrítico"; Cd = 0,95 na equação Q = Cd·Ac·√(2g(he + v²/2g − hc − Δh))). A mistura "controle na entrada" com equação que usa a altura crítica na saída e Δh interno é uma convenção do projetista, não o HDS-5; vale como caso de convenção a confrontar, não de erro. Não lido além de pp. 344-346.

## Fronteira
Greide e cota do rasto do canal: Hidráulica/Terraplenagem (a correção precisa do perfil longitudinal 1:2000, que não está no acervo textual). Carga e Q de cada travessia: estudo HARZA 2001 (ausente).
