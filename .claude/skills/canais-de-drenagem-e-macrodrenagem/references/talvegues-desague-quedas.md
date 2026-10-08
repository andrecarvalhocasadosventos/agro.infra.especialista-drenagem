# Talvegues interceptados pela faixa do canal, drenos de proteção, deságue e degraus

Páginas físicas; acervo em `doc:pág` (casos de 2026-10-08, sem ✓h). Lacuna de entrada: o pacote **não tem o texto** das decisões CDV **D-56** e **D-85**; o enunciado vem no cartão do Gestor (modo CDV: parecer, sem escrita no CDV,
dúvida vira P-nova com a hipótese usada). No quadro 8.13 do Sertão Pernambucano há drenos numerados D-056 e D-085 [1390:431-440]: **homonímia**, não presumir que sejam as decisões do CDV.

## 1. Problema e quem decide

A faixa de um canal de adução (aterro ou meia encosta) corta talvegues. A água de chuva a montante não pode entrar no canal nem represar contra o aterro. Cadeia:
(1) **Drenagem** inventaria o talvegue (bacia, Q e TR por `hidrologia-de-projeto-para-drenagem`) e dimensiona o dreno de proteção, o canal de desvio e a cota de inundação a montante;
(2) **Hidráulica** decide travessia: bueiro, sifão ou aqueduto sob ou sobre o canal (V3 da matriz: estaca, cotas do greide e do fundo, NA do canal; `canais-abertos` e `[DELEGAR: hidraulica]`);
(3) **Terraplenagem** dá greide e faixa, e confere conflito com o corpo do aterro; (4) **Geotecnia**: piping no contato bueiro-aterro, filtro, taludes; (5) **Orçamento**: m de dreno por seção, m³ de escavação, custo por alternativa.
O canal de adução em si é do Hidráulico; o dreno que corre ao lado dele e a água que ele recebe do exterior são desta skill.

## 2. Alternativas para um talvegue interceptado

| Alternativa | Quando serve | Critério e fonte |
|---|---|---|
| Travessia sob o canal (bueiro) | talvegue com vazão relevante e cota que permite | `bueiros-e-travessias`; USBR: tubo de bueiro de canal diâmetro mínimo 60 cm (preferência 80 cm), colares contra piping, TR de travessia igual ao do dreno de proteção [CDV-MANUAL-IRRIG p. 316, §6.3.7.2; p. 514-515, §11.3.3] |
| Dreno de proteção no lado montante, levando a água ao talvegue ou à travessia mais próxima | pequenos e médios talvegues em meia encosta; solução do Sertão Pernambucano | "drenos de proteção interceptam enxurradas do lado ascendente dos canais e as conduzem aos coletores, que passam sobre os canais em calhas ou sob eles em bueiros" [CDV-MANUAL-IRRIG p. 513, §11.2.3]; TR do dreno de proteção maior que o do sistema; 25 anos nos grandes sistemas, com estudo a 100 anos onde o dano seria grave [p. 514-515] |
| Captação da água pelo canal | só se inevitável | evitar, sobretudo em canal revestido de concreto; limitar a 10 % da capacidade de projeto; acima disso, vertedouro de descarte; captação por conduto (vazão pequena, diâmetro mínimo 45 cm, enrocamento na saída se o canal é de terra) ou por estrutura de concreto [CDV-MANUAL-IRRIG p. 316-317, §6.3.8, Fig. 6.57] |
| Aterro em pequeno vale | vale raso, evita travessia | usado no Sertão Pernambucano [1390:431]; exige verificar represamento e infiltração (Geotecnia) |

**Nunca** deixar enxurrada chegar a um dreno escorrendo pelo talude: aterro de bordo no lado montante para canalizar o fluxo para a entrada do dreno; entrada tubular de chapa corrugada >= 500 mm, n = 0,021, V <= 3 m/s, declividade >= 0,01,
saída 0,3 m além do ponto onde a lâmina normal encontra a margem, riprap sob a saída se o solo for erosivo, colar de concreto [CDV-MANUAL-IRRIG p. 515, §11.3.5.1]. Colocar transição logo a montante de cada entrada principal de dreno [p. 518, §11.3.5.2].
Se o dreno de proteção ficar fundo em relação ao canal, afastá-lo para que o lençol vindo do canal não intercepte o fundo do dreno [p. 514, §11.3.2]. Bueiro de estrada sobre dreno: tubo cheio com V <= 1,5 m/s dispensa transição e dissipador [p. 518, §11.3.5.4].

## 3. Método do Sertão Pernambucano (caso positivo, anteprojeto 2014)

204 canais de drenagem laterais ao adutor, 162,464 km, vazão por deflúvio crítico TR 100 de curvas área x vazão, concreto simples em todos, trapezoidal 1V:1H, 13 seções-padrão ST (lista em `revestimento-riprap-gabiao.md` §5),
**afastamento mínimo de 6,00 m** entre a borda do dreno e o offset do canal adutor, transições em diedro com 30° de convergência ou divergência; critério de velocidade crítica citada **sem valor**; deságue em talvegue, curso d'água, reservatório ou a montante/jusante de bueiro BU-nn
[1390:429-431]. Quadro 8.13: canal, margem, estaca inicial e final, extensão, base, altura, deságue (311 trechos; 135 a montante de BU, 15 a jusante, 26 em talvegue, 23 em reservatório, 5 em curso d'água) [1390:431-440].
Exemplos: D-056 (CP-V, margem direita, 24+310 a 24+008, 292 m, 0,60 x 0,50, a montante de BU-17); D-085 (CP-VIII, margem esquerda, 40+810 a 41+130, 325 m, 0,60 x 0,50, em reservatório). Não há Q nem declividade no trecho lido: **gabarito é inventário**, não vazão (qualidade B; a extração cola canal, margem e estaca em parte das linhas; abrir a página antes de citar).
Anomalia a registrar: 8 trechos com extensão diferindo do desnível de estaca em mais de 60 m e 15 % (D-001: 192 m para 85 m de estaca), provável desvio em planta, **não explicado**.
Para parecer com este caso: dado Q (TR 100) e declividade do projeto, achar a menor seção ST que escoa Q com V <= V_adm informada pelo usuário e folga declarada; depois reconciliar a extensão total por soma de trechos (`reconciliar_extensoes`).

Nível: anteprojeto = inventário de talvegues por estaca + seção-padrão + deságue; básico = perfil do dreno com cotas de fundo, degraus, transição e cota de inundação nos pontos de travessia.

## 4. Deságue

| Ponto | Regra e fonte |
|---|---|
| Cota do receptor | a linha de energia do dreno parte dos pontos de controle: cotas das áreas baixas servidas, linha dos tributários e **o deságue**; ficar abaixo do nível de projeto mais folga, ou mínimo 0,5 ft [NRCS-CPS608-2023 p. 2] |
| Tailwater | padrão do núcleo: lâmina normal do canal de jusante, rotulada; cheia do receptor e chuva local coincidentes: frequência coincidente (USACE-EM1110-2-1413, mapa G1, p. 48; aderência baixa, planície com dique) |
| Estaca zero | no deságue; as estacas crescem contra o fluxo [CDV-MANUAL-IRRIG p. 514, §11.3.1] |
| Dreno de saída | segue o leito do talvegue natural, se existir; canais naturais devem ser aproveitados e incorporados [CDV-MANUAL-IRRIG p. 511-513, §11.1 e 11.2.5] |
| Entrada lateral | proteger onde dreno raso entra em dreno fundo: rápidos, quedas, tubos de queda, canais gramados, entradas conformadas [NRCS-CPS608-2023 p. 3] |
| Estabilidade do deságue | desvio e dreno devem ter saída estável; deságue por sobrequeda ou em velocidade excessiva erode [NRCS-NEH650-CH09 p. 15, "Outlets"] |
| Confluência | evitar Fr de 0,89 a 1,13 no dreno receptor [FHWA-HEC11 p. 38]; Salitre: 9 deságues com Am − Bm = 2·z·Hm (DQ-4.1.4.4: 9,98 − 6,00 = 3,98 = 2·1·1,990) [1584:108, Quadro 3.56] |
| Proteção do receptor | rip-rap de margem e de pé no ponto de deságue: HEC-11 (esta skill); bacia ou dissipador de estrutura: Hidráulica |

Interferência com drenagem subsuperficial: fundo do dreno aberto >= 1 ft abaixo do invert dos drenos que deságuam nele [NRCS-CPS608-2023 p. 2]; Salitre fixou 1,80 m de profundidade nos drenos do entorno das áreas irrigáveis [1584:105]
(só 10 de 83 trechos têm h = 1,80 m nas planilhas; o enquadramento "entorno das áreas irrigáveis" não vem no texto lido).

## 5. Degraus e quedas ao longo do dreno

| Fonte | Regra |
|---|---|
| Salitre Etapa 2 | quedas de 1,00 e 1,50 m onde a declividade natural levaria V erosiva; 9 degraus; Hd = cota montante do degrau − cota jusante; LT = b + 2·Hd com talude 1:1 [1584:106, 108, Quadro 3.57] |
| Delmiro Gouveia | módulos de 0,25 m agrupados em quedas de 1,00 m (4 módulos); Io = (desnível do terreno − n° de quedas x queda unitária)/L [1520:129; 1521:120] |
| Embrapa/CPATSA | declividade de fundo de 0,2 a 0,5 %; quedas onde o terreno é mais íngreme [EMBRAPA-DREN-SUP p. 7-8] |
| USBR | a tabela de diretrizes por altura de queda da superfície d'água está **ilegível na extração** (faixas e tipos de estrutura embaralhados; só se lê que acima de 1,5 m servem as estruturas de canal do subitem 6.3.4): conferir no PDF antes de citar faixa [CDV-MANUAL-IRRIG p. 518, §11.3.5.3]. Drenos com muito entulho: evitar queda em tubulação |
| DNIT (valeta de estrada) | pequenas barragens espaçadas E = 100·H/(α − β) com E <= 50 m, trechos de no máximo 2 % [DNIT-DREN p. 163-164], ver `drenagem-de-estradas-e-plataformas` |

**Fronteira (a confirmar com o Gestor):** a D3 só trata o dissipador de saída de bueiro; a estrutura de queda e a bacia de dissipação de degrau de dreno é projeto hidráulico de estrutura (`vertedouros-e-dissipadores`). Esta skill decide **onde** e **quanto** de queda, pelo limite de V; o desenho da estrutura é `[DELEGAR: hidraulica]`.
