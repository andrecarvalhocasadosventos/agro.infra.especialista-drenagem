---
name: drenagem-de-estradas-e-plataformas
description: >
  Drenagem de estradas de serviço, acessos e plataformas de irrigação: valeta de corte (VPC) e de aterro (VPA),
  sarjeta triangular, composta e trapezoidal (Izzard), comprimento crítico, folga, descida d'água, caixa coletora
  com grelha, bueiro de greide, dreno profundo de plataforma e dispositivos-tipo DNIT (Álbum IPR-736, ES 018 a 021
  e 026). Calculadora `tools/dren/estradas`. Use quando: "valeta de crista", "sarjeta da estrada", "comprimento
  crítico", "descida d'água", "caixa coletora", "dispositivo-tipo DNIT", "VPC", "Tc mínimo", "declividade mínima da
  sarjeta", "as valas da estrada do projeto estão certas?". Não use para: bueiro de talvegue (use bueiros-e-travessias),
  Q, Tc e TR (use hidrologia-de-projeto-para-drenagem), IDF (Clima), canal de drenagem (use
  canais-de-drenagem-e-macrodrenagem), dreno agrícola e de fundo (use drenagem-subsuperficial), dissipador
  (Hidráulica), greide, pavimento, preço.
---

# Drenagem de estradas e plataformas

> Núcleo (convenções, fluxo, `[DELEGAR]`, parecer, armadilhas transversais): `drenagem-fundamentos`. Aqui só o
> domínio da estrada: sarjeta, valeta, descida, caixa coletora, dreno profundo e dispositivo-tipo. Nível padrão:
> anteprojeto; básico quando pedido. Tabelas longas e códigos: `references/`.

## 1. Escopo e fronteiras

**Cobre:** dispositivos de superfície de estrada rodoviária ou de serviço (valeta de corte e de aterro, sarjeta,
descida, entrada, saída, caixa coletora, bueiro de greide), dreno profundo longitudinal de plataforma e a escolha do
dispositivo-tipo. Estrada de serviço de irrigação usa o critério rodoviário **por analogia declarada** (o corpus é
rodoviário); exigência da Codevasf ou de concessionária é de `normas-e-manuais`.

| Fronteira | Quem | O que acontece |
|---|---|---|
| Greide, plataforma, taludes, cotas de deságue, drenagem provisória de obra | `terraplenagem` | Drenagem devolve dispositivo por estaca e cota de deságue; pede greide e talude. Valeta de crista a 2-3 m da crista e deságue seguro dependem do corte e do aterro. |
| Seção do pavimento, declividade transversal, camada drenante, dreno de pavimento | `pavimentacao` | Drenagem dimensiona o dispositivo que recebe a água da plataforma; a seção e a drenagem do corpo do pavimento ficam com a Pavimentação. |
| IDF, `i(t,TR)`, P(t,TR) | `clima` | Nunca ajustar IDF. Pedir I para TR e Tc (bloco em `hidrologia-de-projeto-para-drenagem/references/delegar-climatologia.md`). |
| Dissipador na saída de valeta, descida ou bueiro | `hidraulica` (D3) | Entregar Q, V no pé, Fr e o aviso. |
| Bueiro de talvegue sob a estrada | `bueiros-e-travessias` | HDS-5; o bueiro de greide só se liga aqui (§4.3). |
| Valeta longa que vira canal (talude ou revestimento próprio, Q alto) | `canais-de-drenagem-e-macrodrenagem` | Manning e V admissível iguais; a skill de canais governa. |
| Classe de tubo, armadura de aduela, caixa estrutural | `estruturas` | Só geometria funcional. |
| Quantitativos e custo | `orcamento` | Código do dispositivo, m, tipo de boca, ES de execução. |

Drenagem urbana em rede (boca de lobo, galeria, PV) e aeroportuária: **não coberto** (núcleo §4).

## 2. Dados mínimos específicos

Além do núcleo (§2): largura e C de cada implúvio (pista, acostamento, talude de corte ou aterro, faixa externa
contribuinte); declividade transversal Sx e longitudinal S (do greide, por estaca); revestimento e n; pontos de
deságue; TR e Tc adotados com a fonte; I da IDF (Clima) para essa duração. Sem greide, **não calcular comprimento
crítico por trecho**: usar a faixa de S e rotular. Sem a seção da plataforma: `[DELEGAR: pavimentacao]`.

## 3. Critério de projeto: TR e Tc mínimo (padrão provisório, decisão F7)

`criterio_projeto(tc_calculado, tc_min, TR)` devolve `max(tc, tc_min)`. O pacote usa **TR 10 anos e Tc mínimo 5 min
como padrão provisório, decisão F7**: o parecer rotula e mostra a alternativa. Não decidir; mostrar as fontes.

| Item | Alternativa | Fonte |
|---|---|---|
| Tc mínimo 5 min (padrão provisório) | drenagem superficial | [DNIT-IPR726 p. 258]; [WSDOT-HYDRAULICS-M2303-12 p. 102]; [LOC-IME-DRENAGEM-URBANA-RODOVIAS p. 53] |
| Tc 6 min | dispositivos lineares pré-fabricados, TR 10, lâmina ≥ 3 cm abaixo da grelha | [LOC-DNIT-ALBUM-2018 p. 214] (OCR, conferir na imagem) |
| Tc 10 min | rodovias vicinais (IS-239); Xingó (VPC e VPA, TR 10) | [DNIT-IPR726 p. 463]; caso Xingó |
| TR 10 anos | superficial e sarjeta | [DNIT-IPR726 p. 258]; [WSDOT p. 104]; [Álbum p. 214] |
| TR 5 a 10 anos | faixa usual de superficial (colunas misturadas na extração, conferir na imagem) | [DNIT-IPR726 p. 258, 463] |
| TR 25 anos | ENGEFER | [LOC-IME p. 53] |
| TR 50 em ponto baixo (sag) | WSDOT | [WSDOT p. 104] |

O Tc só pesa quando o calculado fica abaixo do mínimo (valeta curta). Passar de 5 para 10 min reduz I e aumenta o L
crítico em dezenas de por cento no semiárido: **mostrar a sensibilidade** no parecer. Estrada de serviço sem exigência
do cliente: TR 10 e Tc 5 rotulados; TR maior só por decisão do usuário. Projeto do acervo com outro valor (Xingó
10 min; ENGEFER 25 anos) **não é erro**: registrar e comparar.

## 4. Método por dispositivo

### 4.1 Valeta de proteção de corte e de aterro (VPC, VPA) e valeta de estrada

- Posição: valeta de corte a **2,0 a 3,0 m** da crista; de aterro a 2,0 a 3,0 m do pé [DNIT-DREN p. 158, 165]
  (Xingó: mais de 3,0 m da crista e mais de 1,0 m do pé, 1419:65: contexto do projeto, não regra).
- Q pelo racional por metro: **q = I Σ(Cᵢ wᵢ) / 3,6×10⁶** (I em mm/h; wᵢ em m de implúvio) [LOC-IME p. 53]. O IME
  mistura "m/h" e "cm/h" nas eqs. 4.1 e 4.2 (anomalia interna): converter sempre.
- Capacidade: Manning trapezoidal, Fr = V/√(g A/T); evitar y a menos de 10 % de yc e Fr em ±10 % de 1
  [DNIT-DREN p. 160-163; IME p. 54].
- **Comprimento crítico: L = Q_Manning / q** [IME p. 84, eq. 4.19; método do Xingó, 1419:64-65]. Além de L: saída
  d'água, descida ou caixa. `hmax` padrão 0,8 h é regra **observada** no Xingó, não declarada: aviso da calculadora.
- Folga: terra e Q ≤ 0,3 m³/s, f = 0,2 h; concreto, Tab. 4.2 (10 a 18 cm por faixa de Q até 2,8 m³/s) [IME p. 54-55];
  WSDOT 0,5 ft (≈ 0,15 m) fixo, TR 10 [WSDOT p. 109]. Terra com 0,3 < Q ≤ 10 m³/s: equação do IME ilegível,
  **não implementada** (`ValueError`); conferir na imagem do PDF.
- Declividade excessiva (V > admissível): escalonar, S de trecho ≤ 2 %, E = 100 H/(α−β), E ≤ 50 m [DNIT-DREN p. 163-164].
- Revestimento obrigatório em solo permeável; concreto fck mín. 20 MPa [DNIT-ES018-2023 p. 3] (DNIT-DREN p. 166-186:
  15 MPa; IME p. 47: 11 MPa; **divergência 1** do mapa G3). V admissível, n e tensão: ver
  `references/valetas-sarjetas-descidas.md` §1 e [FHWA-HEC15 p. 31-35].

### 4.2 Sarjeta (corte, aterro, pavimentada)

- **Triangular de Izzard:** Q = (Ku/n) Sx^1,67 S_L^0,5 T^2,67, **Ku = 0,376 (SI)**; 0,56 em unidades inglesas
  [FHWA-HEC22 p. 79 eq. 5.2; FHWA-HEC12 p. 39 eq. 4]. T = [Q n /(Ku Sx^1,67 S_L^0,5)]^0,375. Validade: seção rasa
  (T/y > 40), sem resistência do meio-fio. TR e espalhamento admissível: HEC-22 Tab. 5.1 [p. 70].
- **Composta (depressão W, Sw):** Izzard integrado por trechos [HEC-12 p. 41-43]; Eo é **calculada**, não lida da Chart 4.
- **Sarjeta de corte DNIT:** triangular 1:4 no lado do acostamento (25 % máx.) [DNIT-ES018-2023 p. 2]; L1 de 1,0 a
  2,0 m; se não bastar, trapezoidal ou retangular [DNIT-DREN p. 167-169]. Comprimento crítico DNIT:
  d = 36×10⁴ A R^(2/3) I^0,5 /(C i L n), i em cm/h (5 min, TR 10) [DNIT-DREN p. 170-174].
- **Declividade longitudinal mínima (divergência F5, não decidir): 0,5 %** [DERPR-ES-DR-01-23 p. 10] × **0,3 %**
  (0,2 % em terreno muito plano; 0,3 % a 50 ft de ponto baixo) [FHWA-HEC12 p. 19]. DNIT-ES018 não fixa valor.
  A calculadora **avisa e não bloqueia**: S < 0,3 % viola as duas fontes; 0,3 a 0,5 % viola só a DER-PR. O Xingó
  calcula desde i = 0,1 % (1419:66): **apontar** e mostrar L e V com a fonte aplicável. Reportar atendida ou violada por fonte.
- Fck, junta, gabarito e tolerância (divergências 1 a 5 do mapa): `references/dispositivos-tipo-dnit.md` §4.

### 4.3 Descida d'água, saída, caixa coletora e bueiro de greide

- Descida, método I: **Q = 2,07 L^0,9 H^1,6** (m³/s, m); V no pé V_b = √(2 g h) (superestima) [DNIT-DREN p. 188-190];
  método II por passos (eq. 3.13). **Não implementada** na calculadora (corpus próprio só tem desenhos, Álbum p. 40-47):
  calcular com `valeta_manning` e declarar. Dissipador: `hidraulica`.
- Execução: concreto fck ≥ 20 MPa e CA-50, juntas em descida > 10 m [DNIT-ES021-2023 p. 2, 4]; [DERPR-ES-DR-03-23 p. 4-5].
- **Caixa coletora com grelha** (`caixa_coletora_grelha`): vertedor Qi = Cw P d^1,5 (**Cw = 1,66 SI**); orifício
  Qi = Co A √(2 g d) (**Co = 0,67**) [HEC-12 p. 86, eqs. 17-18]. Capacidade = menor; carga = maior; sem colmatação;
  HEC-12 desaconselha grelha isolada em sag: aplicar fator de obstrução rotulado.
- Bueiro de greide: Q = soma dos dispositivos afluentes, sem carga a montante sempre que possível; com carga, guardar
  a cota máxima na caixa [DNIT-DREN p. 202]. Hidráulica do barril: `bueiros-e-travessias`.

### 4.4 Dreno profundo longitudinal de plataforma

q = K (H² − d²)/(2X) por lado (Darcy) [IME p. 82, eqs. 4.8-4.12]; Scobey Q = 0,2113 C D^2,625 I^0,5 e Hazen-Williams
Q = 0,2785 C D^2,63 I^0,54 [IME p. 83]; **L = Q/q** [p. 84]. As fórmulas dão **tubo cheio**, embora o texto diga
"meia seção" (divergência 10): `fator_capacidade` < 1 é decisão de projeto, rotular. A correlação K = 100 d10² não
está implementada (unidade ambígua). Material, filtro, boca e execução (ES 015-017; [DERPR-ES-DR-06-23 p. 3-11], fundo
≥ 1 %, p. 7): `drenagem-subsuperficial`. Camada drenante e dreno do pavimento: `pavimentacao`; IS-210 exige drenagem do
pavimento com chuva > 1.500 mm/ano e > 500 veículos comerciais [DNIT-IPR726 p. 307].

## 5. Calculadora `tools/dren/estradas.py` (versão 0.1.0)

CLI: `python -m tools.dren.estradas --json "{\"funcao\": \"...\", ...}"`; `--listar`. SI; I em mm/h (1 mm/min = 60).
Testes: `python -m pytest tests/dren/test_estradas.py -q`.

| Fórmula | Função | Teste e gabarito |
|---|---|---|
| tc = max(tc, tc_min); eco do TR | `criterio_projeto` | padrão provisório 5 min e TR 10; o aviso lista 6, 10 min e TR 25 |
| Izzard triangular, T ↔ Q | `sarjeta_triangular` | HEC-12 gabaritos 4 a 6 (Ex. 4: 2,04 ft³/s; conferido aqui: T 2,4384 m, Sx 0,025, S 0,01, n 0,015 dá 0,0572 m³/s = 2,02 ft³/s) |
| Izzard composto, T ↔ Q | `sarjeta_composta` | HEC-12 Ex. 5 (gabarito 7): Eo 0,694 × 0,69; Q 3,10 × 3,0 ft³/s |
| Manning trapezoidal, Fr com A/T | `valeta_manning` (y → Q ou Q → y) | round-trip e conferência manual |
| q = I Σ C w / 3,6e6 | `vazao_por_metro` | Xingó VPC-1: 0,9×0,60 + 0,3×10,00 = 3,54 m |
| L = Q_cap / q | `comprimento_critico`, `valeta_comprimento_critico` | Xingó VPC-1: **162,57 m (i 0,001)** e 1.259,2 m (i 0,060) × 162,54 e 1.259,04 do projeto (acervo, **sem ✓h**, tolerância 5 %) |
| folga | `folga_valeta` | `test_folga_ime` |
| grelha em sag | `caixa_coletora_grelha` | `test_caixa_coletora_grelha_hec12_p86` |
| Darcy, Scobey, HW, L do dreno | `dreno_profundo_contribuicao`, `_capacidade`, `_comprimento_critico` | só consistência (a fonte não traz exemplo) |

Exemplo (VPC-1 do Xingó, rodado): `{"funcao":"valeta_comprimento_critico","b":0.2,"z":1,"h":0.2,"n":0.016,"i":0.001,
"I_mm_h":141.18,"contribuicoes":[[0.9,0.6],[0.3,10.0]]}` → L = 162,57 m; q = 1,388×10⁻⁴ m³/s/m; Q_cap 0,0226 m³/s;
V = 0,392 m/s; Fr 0,38. z = 1 foi **deduzido** (topo 0,60 = base 0,20 + 2×0,20), não impresso.

**Avisos que o parecer reproduz:** Tc mínimo e TR provisórios (decisão F7); `hmax = 0,8 h` não declarada; declividade
< 0,3 % e < 0,5 %; V > v_max; Fr em ±10 % do crítico; grelha sem colmatação; dreno "meia seção". **Não calculado:**
descida d'água, folga em terra com Q > 0,3 m³/s, dissipador (Hidráulica), sarjeta em sag e espaçamento de bocas de
lobo (urbano). Fornecer exatamente um entre Q e T (ou y), senão `ValueError`.

## 6. Critérios de verificação (V-regras do perfil)

1. I corresponde à **duração = Tc adotado** (≥ Tc mínimo) e ao TR rotulado; vem do Clima ou é rotulada "emprestada".
2. P (mm) **nunca** entra como I (mm/h): I = P·60/t (caso CAC Castanhão).
3. Froude com A/T; distância a yc > 10 %; V ≤ V admissível do revestimento e τ ≤ τp/SF (HEC-15).
4. Folga declarada (0,2 h, Tab. 4.2 ou 0,15 m) e hmax declarada; folga recalculada, não lida da coluna "OK".
5. Declividade ≥ 0,5 % (DER-PR) e ≥ 0,3 % (HEC-12), cada uma reportada, sem escolher.
6. L real do trecho ≤ L crítico; senão, saída d'água ou caixa; V no pé da descida entregue ao Hidráulico.
7. Cotas de deságue e seção da plataforma vêm de terraplenagem e pavimentação, ou são premissa rotulada.
8. Divergência com o projeto do acervo: **apontar** (o que fez, `doc:pág`; o que o método dá; diferença e consequência;
   quem decide), nunca corrigir em silêncio; número do acervo sem `✓h` não é gabarito.

## 7. Armadilhas do acervo

| Armadilha | Onde | Como detectar e o que fazer |
|---|---|---|
| **P (23,2 mm, 5 min) usada como I (mm/h)**: Q 12 vezes menor (VC2: 0,171 contra 2,05 m³/s; Q/Qf ≈ 5,5) | CAC Castanhão, Quadro 5.6, 1128:106-112 | Recalcular Q = C·(P·60/tc)·A/3,6e6; razão = 60/tc. Não reproduzir 0,171; apontar e pedir o PDF ou a planilha (✓h). P = 0,959 tc + 18,04 dá 22,84, não 23,20 (18,40 reproduz) |
| Sarjeta e valeta com S de 0,1 %, abaixo das duas fontes | Xingó VPC e VPA, 1419:66 | Aviso da calculadora; mostrar L e V; decisão do projetista ou do cliente |
| Mesma hmax e mesma capacidade (0,083 m³/s) em VPC-5, 6 e 7 (h 0,30, 0,35 e 0,40 m) | Xingó, 1419:78-80 | Indício de linha copiada; efeito conservador; não "corrigir" |
| `hmax = 0,8 h` não declarada; z não impresso; C 0,30, 0,70 e 0,90 sem fonte | Xingó | Rotular como regra observada |
| Duas chuvas (2,353 e 1,789 mm/min) no mesmo TR 10 e Tc 10; origem do corte em km 33+890 não informada | Xingó, 1419:66, 98 | Pedir a IDF por trecho ao Clima |
| TR 10 e Tc 10 min na valeta com bueiros a TR 25/50/100 no mesmo projeto, sem justificativa | Xingó | Registrar; coerente com o porte, critério não explicado |
| V até 3,0 m/s em concreto sem V admissível declarada (S 6 %) | Xingó, 1419:66 | Conferir na Tab. 31 e propor escalonamento |
| Kirpich < 5 min em todo trecho: o mínimo comanda; área de 4,4 ha com L 250 m | CAC Castanhão | Declarar `minimo_comanda`; discutir o Tc real até a vala |
| Colunas das tabelas de Q que não reproduzem (Quadros 5.3 e 5.4) | CAC Castanhão | Não usar sem ver o PDF |
| Dreno de tubo "meia seção" × fórmula de seção plena | IME p. 83 | `fator_capacidade` rotulado |
| Concreto da sarjeta 11, 15 ou 20 MPa conforme a fonte | IME; DNIT-DREN; ES018 | Citar a vigente (ES018-2023, 20 MPa) e registrar |
| Descida em módulos de concreto (descalça e desjunta) | DNIT-DREN p. 186 | Preferir rápida ou degraus confinados |

## 8. O que a norma exige e a quem se aplica

O Álbum IPR-736 é **orientador e não normativo** [DNIT-ALBUM p. 23]; as ES mandam usar os dispositivos padronizados
"na ausência de projeto específico" (ES 023, 025, 026). Dispositivo-tipo dá detalhe e custo; a hidráulica é do projeto.
As ES de execução (018, 019, 020, 021, 026; DER-PR DR-01, 03, 05) fixam material, junta, tolerância e medição; **não
dimensionam**. O IPR-724 é rodoviário federal; em perímetro irrigado vale como analogia. IS-210 e IS-242 listam os
dispositivos de projeto e exigem memória de cálculo [DNIT-IPR726 p. 307-308, 472-473]. Códigos, ES e o que o Álbum
cobre: `references/dispositivos-tipo-dnit.md`.

## 9. Referências e lacunas

IDs: `DNIT-DREN` (IPR-724, física = impressa + 4), `DNIT-ALBUM` / `LOC-DNIT-ALBUM-2018` (IPR-736, OCR parcial, confiança
0,72), `DNIT-ES018-2023`, `DNIT-ES020-2006`, `DNIT-ES021-2023`, `DNIT-IPR726-2006`, `DERPR-ES-DR-01-23`, `-03-23`,
`-05-23`, `-06-23`, `FHWA-HEC12`, `FHWA-HEC15`, `FHWA-HEC22`, `LOC-IME-DRENAGEM-URBANA-RODOVIAS`,
`WSDOT-HYDRAULICS-M2303-12`. Mapa: `referencias/MAPA_DE_CONHECIMENTO.md` (G3) e H14 do Hidráulico (DNIT-DREN).
Casos: `casos/drenagem/2026-10-08_xingo_lote1_valetas_protecao_comprimento_critico.md` (VPC-1 e VPA-5 qualidade A,
sem ✓h), `2026-10-08_cac_castanhao_estrada_acesso_valas_chuva_como_intensidade.md` (negativo),
`iuiu_2002_drenagem_superficial_drenos_bueiros.md`.

**Lacunas:** sem exemplo numérico brasileiro de sarjeta, valeta ou espaçamento de descidas; sem V admissível e n por
revestimento no corpus próprio (Tab. 27, 28, 31 e 34 do IPR-724 estão no corpus do Hidráulico); descida e dissipador só
em desenho (Álbum p. 40-47, OCR); Álbum com 24 p. sem OCR e números a conferir na imagem; ES 019 e 030 fora do corpus
próprio; EQ. 4.7 do IME (folga em terra, Q > 0,3 m³/s) ilegível; HEC-12 arquivado (absorvido pelo HEC-22), em unidades
inglesas; WSDOT sem gabarito numérico. Pontos abertos para a F7: Tc mínimo (5, 6, 10), TR da superficial e declividade
mínima (0,5 × 0,3 %): **padrão provisório, decisão F7**.

**Testes adicionais sugeridos:** (1) Xingó VPA-5, i = 0,001: L = 222,14 m (1419:86), hmax 0,24, contribuições
0,9×1,00 + 0,7×8,00 + 0,3×10,00 = 9,5 m; (2) CAC VC2: A = 44.110 m², C 0,6, P 23,2 mm em 5 min: Q = 2,05 m³/s com
I = 278,4 mm/h; (3) HEC-12 Ex. 8 (swale circular, p. 49): d 0,30 ft, T 2,37 ft; (4) HEC-12 Ex. 23 (p. 110): d e V da
valeta; (5) Xingó com I = 1,789 mm/min: L(0,001) = 213,76 m (1419:98).
