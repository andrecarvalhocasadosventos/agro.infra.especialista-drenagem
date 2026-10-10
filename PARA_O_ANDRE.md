# PARA_O_ANDRE — Especialista Drenagem

> O portão F7 continua em `PARA_O_ANDRE_F7.md` (20 decisões, 3 pedidos, 14 xfail). Esta sessão não o respondeu nem o contornou.

## 2026-10-09 (servidor)

1. **Instalar o HEC-RAS no SRVCVERSP.** O especialista passa a fazer estudos com HEC-RAS (D9) e hoje só confere arquivos, não roda. Opções: (a) instalar o HEC-RAS 6.6 (gratuito, USACE HEC; `https://www.hec.usace.army.mil/software/hec-ras/`) — permite rodar e validar o `ras-commander`; (b) não instalar e ficar só na conferência de modelos entregues por terceiros com `rashdf`/`h5py`. Recomendação: (b) até a F5 do verificador; (a) quando houver um modelo próprio a rodar. Fica parado: execução de planos, `ras-commander`, automação por COM.
2. **Fronteira Drenagem × Hidráulica × Geoprocessamento para HEC-RAS** (`PLANO.md` §11.3). Interface congelada; premissa em uso: Drenagem = cheias, travessias e manchas de inundação; Hidráulica = canais de adução e estruturas hidráulicas. Opções: aceitar a tabela de §11.3 ou redesenhar (ex.: remanso de canal de adução também na Drenagem). Recomendação: aceitar. A decisão é do `/treinar squad` (matriz e roteamento não foram tocados). Fica parado: F6 da skill `modelagem-hidraulica-hec-ras`.
3. **Arquivos do rio Verde e nota do Standard Step da TPF.** O acervo não traz modelo do rio Verde (HR-06); o NA de 397 m não é reprodutível. Opções: pedir à TPF os arquivos e as seções; ou aceitar 397 m como preliminar. Recomendação: pedir. Fica parado: gabarito do HR-06.
4. **Conferência humana (✓h) dos números dos casos HR-01 a HR-06.** Nenhum virou gabarito. Opção: conferir 10 números-chave contra o PDF. Recomendação: conferir Tab. 5 e Tab. 8 (REL-FINAL p. 42 e 56-57) primeiro. Fica parado: `evals/casos_numericos.yaml` de HEC-RAS.
5. **Leitura do Data Room.** A listagem completa de `4. Relatórios\` do Data Room não foi feita (Drive saturado). Só o `2026.09.29 - HECRAS` foi lido. Pode haver outros arquivos HEC-RAS sem texto indexado. Recomendação: a sessão `/treinar squad` pode rodar a listagem quando o Drive estiver livre.
6. **FHWA (HEC-18/HDS-7 sobre pontes) sem URL verificada**: o servidor não alcançou `fhwa.dot.gov` (código 000). Recomendação: tentar de outra máquina; item de prioridade B.

## 2026-10-10 (servidor) - HEC-RAS: F3, F5, F6

1. **Skill pronta para o seu aceite; criterios de aceitacao sao premissa de treinamento.** Sem numero nos manuais para: estabilizacao (dNA <= 0,01 m em 2 h), limiar de sensibilidade de n (0,3 m), erro de volume e tamanho de celula. Opcoes: aceitar como estao (rotulados) ou fixar valores do CDV. Recomendacao: aceitar. Fica parado: nada.
2. **Layout 1D do `hecras_hdf.py` nao verificado em arquivo real** (a TPF so entregou 2D). Pedir a TPF um `.hdf` 1D (o rio Verde, ja pedido no item 3 de 2026-10-09) ou um exemplo do HEC-RAS (Muncie). Fica parado: `secoes_1d` valido so com fixture sintetica.
3. **Falha preexistente do `verificar_citacoes.py`**: FHWA-HEC11 p. 48-49 (expoente 1,5 de C_sf, conferido na imagem, triagem manual da sessao anterior). Nao alterei a skill `canais-de-drenagem-e-macrodrenagem`.
