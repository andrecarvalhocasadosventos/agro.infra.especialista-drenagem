# Divergências de acervo registradas como xfail (matéria de treinamento)

Fonte: `tools/dren/DIVERGENCIAS.md` e `tests/dren/`. Regra: divergência > 5 % não se corrige ajustando fórmula; o
teste fica `xfail`, a linha entra em `DIVERGENCIAS.md` com a hipótese, e abre-se sessão com o André. O parecer reporta
a divergência com os quatro itens da SKILL §2. Referência do método: HDS-5 3ª ed. (2012), Tab. A.1.

| Caso | Projeto | Calculado | Teste | xfail | Hipótese registrada |
|---|---|---|---|---|---|
| Baixio BU-CP0-15, folga ao TN | folga 0,66 m (TN 408,31) | 408,31 − 407,846 = 0,464 m | `test_baixio_folga_ao_tn` | sim | aritmética do gabarito do caso (TN implícito 408,51); conferir a planilha 897:1 |
| Baixio, legado (orifício C 0,62) x HDS-5, BU-CP0-13/15/18 | HW 3,31 / 4,51 / 5,02 m | 3,60 / 4,82 / 5,44 m (−8,0 / −6,4 / −7,8 %) | `test_baixio_legado_vs_hds5_5pct` | sim | orifício não vê a contração de entrada; contra a segurança; BU-CP0-27 e BU-CS1-01 ficam em −4,3 % (passam) |
| CSB BTCC-N17 (3 cel. 2x2, i 0,0045) | Q 39,18 m³/s | 28,6 m³/s (Manning n 0,015, y 1,5) | `test_csb_btcc17_capacidade_manning` | sim | V/Yo da Tab. 4.7 (1341:205) mal lidos ou outra lâmina; HDS-5 daria HW 2,83 m (HW/D ≈ 1,4) |
| Xingó BU-01/06/24 | y 0,96 / 1,76 / 1,87; V 3,10 / 4,46 / 4,36 | Manning normal y 0,83 / 1,42 / 1,50; V 3,6 / 5,5 / 5,4 | `test_xingo_lamina_normal_vs_doc` | sim | perfil por energia (K 0,5, 1419:154), não uniforme; V = Q/(B·y) confere |
| Iuiu DP11 t1 (McMath, A 189 ha) | 2,34 m³/s | 2,90 (+24 %) com S 0,0028, Tc Kirpich 125 min | `test_iuiu_dp11_mcmath` | sim | S e Tc da bacia não constam; i implícito 41,9 mm/h daria 2,34 |
| Baixio HUT BU-CP0-11 (323,4 ha, CN 62,04, TR 25) | 6,03 m³/s | 2,70 m³/s | `test_baixio_hut_pico_tr25` | sim | geometria do HU reproduz (tlag 0,578 h; tp 0,658 h; tb 1,758 h); hietograma (tabela T-K) irrecuperável |
| CSB 2DN150 até 200 m | Q 0,012 → 0,006 por tubo | > 0,005 (limite do DN150) | `test_csb_L200_2DN150` | **strict** | capacidades dos tubos sem ancoragem |
| Delmiro dreno DN170 | 1,518e-4 m³/s | 1,05e-3 (6,9x) | `test_delmiro_capacidade_dn170_declarada` | **strict** | S do tubo ≠ 3e-4? n? transcrição? |
| Delmiro dreno DN230 | 4,929e-4 m³/s | 2,31e-3 (4,7x) | `test_delmiro_capacidade_dn230_declarada` | **strict** | idem |
| Delmiro BHD1 TR 50 | 58,71 m³/s | 61,8 (+5,3 %) | `test_delmiro_bhd1_pico_58_71` | **strict** | hietograma por polinômio cúbico (Quadro 3.3) irrecuperável |

## Notas que não são xfail

- **Reproduzem** (tolerância do caso): Baixio Manning 2,5x2,5 (V 4,136; Q 24,82) e 2x2 (V 3,556), orifício TR 50
  (cota 407,846); Salitre BTCC1/2/7 e BDCC5 (3 %); Jaíba (hf 0,024; NA 480,138 x 480,13); CSB bacia 45 (Tc 112 x
  114,09 min; Q 9,6 x 9,58); Iuiu (Gumbel P1d, DP08 Q 0,83); Xingó Kirpich S1 (9,08 x 8,91 h, +1,9 %); Xingó VPC-1 (L
  162,57 x 162,54 m).
- **Entre fontes** (não é acervo): Ke de alas paralelas 0,7 (HDS-5 p. 216) x 0,2 (DNIT-DREN p. 130); `fonte_ke="dnit"`.
  Tc mínimo 5, 6 ou 10 min; TR da drenagem superficial 10 x 25; V admissível DNIT x EM-1601; Ernst com `a` (ILRI-16
  38 m x WATERLOG 51,8 m). Todos "padrão provisório, decisão F7".
- Funções NERC e Bransby-Williams estão "não conferidas": só reproduzem projeto do acervo; não são método do pacote.
- 11 xfail no total de `tests/dren/` segundo o núcleo (`drenagem-fundamentos` §9); a tabela acima lista os 10 de acervo
  achados no código. O que muda entre os dois números deve ser conferido contra `python -m pytest tests/dren -q`.
