# Conferências numéricas com primário (candidatas a teste da calculadora)

Páginas = página física do PDF. Os valores da última coluna foram calculados com `tools/hid/hidrologia.py` nesta redação.

| Primário | Entradas | Resultado do primário | Resultado da calculadora |
|---|---|---|---|
| DNIT-HIDRO p. 130 (racional) | c = 0,1828; P(40 min) = 67,33 mm, logo i = 67,33·60/40 = 101,0 mm/h; A = 2,4 km² | 12,31 m³/s (com 3,6, não "6,3") | `racional(C = 0,1828, i = 101,0, A = 2,4)`: 12,31 |
| DNIT-HIDRO p. 131 (racional, outra bacia) | c = 0,385; i = 96,1 mm/h; A = 10,5 km² | 107,9 m³/s; 28 % acima de 84,4 m³/s por descargas específicas | — |
| NRCS-NEH630-CH16 p. 16, ex. 16-1 | A = 4,6 mi² (11,914 km²); Tc = 2,3 h; ΔD = 0,3 h; Q = 1 pol (25,4 mm) | Tp = 1,53 h; qp = 1.455 ft³/s | `hidrograma_unitario_triangular`: tp = 1,53 h; qp = 1,6197 m³/s/mm = 1.453 ft³/s por pol (−0,15 %) |
| NRCS-NEH630-CH10 p. 19, ex. 10-3 | P = 5,1 pol (129,54 mm); CN 75 e 69 | Q = 2,53 e 2,03 pol | `chuva_efetiva`: 2,531 e 2,030 pol |
| NRCS-NEH630-CH10 p. 12, Tab. 10-1 | CN 74 | S = 3,51 pol | `retencao_S`: 3,514 pol |
| PMSP-DRENURB-V2 p. 21-22 (blocos alternados, Wilken, TR 5) | i = 57,71·TR^0,172/(t + 22)^1,025 mm/min; t de 10 a 100 min, Δ = 10 min | Alturas acumuladas 21,8; 33,0; 39,7; 44,2; 47,5; 49,9; 51,7; 53,2; 54,4; 55,3 mm; blocos reordenados 1,2; 1,8; 3,2; 6,7; 21,8; 11,2; 4,5; 2,4; 1,4; 0,9 mm. A coluna "Intensidade (mm/h)" da tabela impressa traz (t + 22)^1,025 e não a intensidade | `idf_potencial(TR = 5, t, a = 57,71·60, b = 0,172, c = 22, d = 1,025)·t/60`: 21,81; 33,01; 47,50 (t = 50) e 55,33 mm (t = 100) |
| FHWA-HDS2 p. 132, Tab. 5.13 (Gumbel) | n = 10, TR 25 (prob. 0,04): K = 2,8468 | X = x̄ + K·s | Série de 10 valores (60, 72, 55, 90, 110, 65, 70, 80, 95, 58): K de n dá 126,8; `gumbel_P_TR` dá 112,3 (K = 2,04) |
| ABDER-APOSTILA p. 69 (racional com retardo) | A = 8,5 km² = 850 ha; C = 0,35; i = 65,89 mm/h; φ = 1/(100·8,5)^(1/6) = 0,325 | Q = 17,9 m³/s | 0,00278·0,35·65,89·850·0,3249 = 17,7 m³/s (−1 %) |
| ABDER-APOSTILA p. 67 (Kirpich) | L = 0,49 km; i = 7 % | Tc = 0,106 h = 6,3 min | `kirpich(L = 490, S = 0,07)`: 6,40 min (+1,6 %) |
| USBR-DRAINAGE p. 57 × EMBRAPA-DREN-SUP p. 5 (McMath) | conversão de unidades | 0,0091 (S m/m) e 0,0023 (S m/km) | 0,02832/25,4·2,471^0,8 = 0,0023; × 1.000^0,2 = 0,00915 |
