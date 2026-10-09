# Armadilhas do acervo em bueiros (casos negativos)

Tabela do `SKILL.md` §6, movida na revisão F7 (2026-10-08) para manter a skill abaixo de 25 KB. Regra: apontar com evidência e
consequência, nunca corrigir o projeto em silêncio; número do acervo sem ✓h não é gabarito.

| # | Armadilha | Onde | Como detectar e o que fazer |
|---|---|---|---|
| 1 | Bueiro só por orifício ou Manning; HW 6 a 18 % abaixo do HDS-5 (contra a segurança) | Baixio, CSB, Xingó, Salitre | HW/D ausente; `comparar_legado_hds5`; exigir HW de entrada e de saída |
| 2 | "Capacidade livre" TR 25 passa, mas Q50 > capacidade e se aceita com carga | Baixio (BU-CP0-13: 33,4 × 27,0 m³/s) | comparar Q de verificação com a capacidade crítica e calcular HW |
| 3 | Coluna "Situação OK" com folga negativa | Baixio, aba "Sob estradas" (CS1-01: −0,96 m) | refazer a folga com a cota do terreno; nunca usar a coluna como gabarito |
| 4 | Q/célula acima da capacidade crítica: entrada afoga, HW > D, só V e Yo reportados | Salitre BTCC 7 (HW/D ≈ 2,25 hipotético) | `controle_de_entrada` com a entrada declarada; X > 4 = submersa |
| 5 | V/Yo do quadro 4.7 não reproduz Manning (28,6 × 39,2 m³/s) | CSB BTCC-17 | conferir a página; HDS-5 dá HW 2,83 m (HW/D 1,4) |
| 6 | Lâmina supercrítica de perfil lida como normal (0,96 × 0,83 m) | Xingó BU-01, 06, 24 | projeto usa energia a partir da seção crítica, K = 0,5; Manning não reproduz (xfail) |
| 7 | Q 2,44 × 2 × 1,27 = 2,54 m³/s | Jaíba CS-25 | exigir Q de projeto e por célula coerentes |
| 8 | Coeficiente impresso **1,638** na vazão crítica do celular: Tabela 2 e teoria dão **1,705** (4 % a menos) | IPR-724 p. 54-56 | usar a tabela; 2,0 × 2,0 = 9,64 m³/s |
| 9 | Tabela 1 do DNIT (tubular) usa Vc = 2,56 D^0,5 do retângulo: Q crítica ≈ 7 % acima da exata (DN 1,00: 1,53 × 1,43) | IPR-724 p. 55 | usar HDS-5; `vazao_critica_exata` |
| 10 | Ke de ala paralela 0,2 (DNIT) × 0,7 (HDS-5) | IPR-724 p. 130 × HDS5 p. 216 | mostrar os dois HW; padrão provisório, decisão F7 |
| 11 | Limite de V da calculadora legada até 2× mais permissivo que o DNIT | `LIMITE_VELOCIDADE_MATERIAL_LEGADO` | desde a v0.2.0 o padrão é a Tab. 31; reproduzir o aviso de material sem linha |
| 12 | "Declividade mínima 5 %" do bueiro: provável 0,5 % ou o intervalo "0,4 a 5 %" truncado | Iuiu 2002 (1051:331) e **Iuiu 2018 (1069:125)**, mesmo texto | hipótese a confirmar no desenho; usar 0,4 % mínimo [DNIT-DREN p. 34] |
| 13 | Orifício com C = 0,62 fixo ignora L/D (0,77 em L/D = 10; 0,548 em 100) | legado (Baixio, L/D ≈ 16) | conferir L/D e carga ≤ 2 D |
| 14 | Folga ao terreno que não fecha (0,66 × 0,464 m) | Baixio BU-CP0-15 | refazer a aritmética (`DIVERGENCIAS.md`) |
| 15 | **BUC sem HW, com S e L divergentes:** quadro dá S 0,006/0,005/0,015/0,015 e L 40-50 m; o memorial de cálculo usa S 0,005/0,005/0,005/0,007 e o quantitativo L médio 19,33 m. Com S = 0,015, Fr > 1, incompatível com Fr 0,81-0,97 da tabela. y/D 79 % (BUC-5, TR 50) passa do critério | **Delmiro Gouveia** 1492:164; 1493:282-285; 1515:99 (caso B) | `tubo_parcialmente_cheio` reproduz y, V e Fr (1 %); apontar as duas versões de S e L, o efeito no controle de entrada/saída e pedir o desenho 0364-DE-20-DR-001 |
| 16 | **91 obras sem capacidade publicada:** declividade e L de cada bueiro ausentes; método RAC/MOD/HUT por faixa de área sem limite escrito; TR 25 no texto, mas as linhas HUT só trazem Q50 e as RAC só Q15 e Q25; células de 2,0 a 3,0 m contra "limite 1,50 m"; n 0,0165; 4 bueiros sem bacia | **Vale do Iuiu 2018** (1069:124-127; caso B/C) | não há gabarito de capacidade; pedir S e L e verificar por HDS-5 (ex. BU5, 3 × Ø1,50, Q25 10,10 → 3,37 m³/s por linha); comparar com 2002 (TR 50 sob canal) |
| 17 | **Cota do rasto de B31 incoerente** (91,189 m; B30 94,246; B32 92,977; coletor 0,81 m acima do rasto) em quadro de 59 bueiros sem Q, HW ou L | **CAC Trecho 1** (1131:65-67, caso C) | teste de monotonia (rasto não sobe a jusante) e de posição (coletor abaixo do rasto); apontar, **não corrigir** (94,189 é só hipótese de digitação); perfil longitudinal ausente |
| 18 | **n implícito 0,013 contra 0,015 do canal:** 22 de 23 BSTC Ø0,80 só fecham com n ≈ 0,013, sem n declarado; com n 0,015 a capacidade cai ~13 % e E4 BC-08 estoura Y/D 0,82. V até 4,8 m/s sem dissipador e sem HW | **Jaíba Etapas 3-4** (1182:43, 65-67, caso A) | `tubo_parcialmente_cheio` com n 0,013 e 0,015: BC-08 (Q 1,10, i 0,007) Y/D 0,82 × acima; sinalizar a divergência com o n do canal; V alta → `[DELEGAR: hidraulica]` |
| 19 | Capacidade de tubo do legado Xingó (33,5·D^2,67·i^0,5) equivale a n = 0,0093: com n 0,012-0,013, 22 a 28 % menor | Xingó, tubo dreno | converter para n equivalente antes de comparar |
| 20 | Gabarito do próprio manual depende de n não informado (V 6,47 × 6,07 m/s) | HDS-5 p. 280 | declarar o n |
