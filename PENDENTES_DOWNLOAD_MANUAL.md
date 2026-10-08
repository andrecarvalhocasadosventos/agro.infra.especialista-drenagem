# Pendentes de download manual (F1, 2026-10-07)

Itens abertos em que o robô não conseguiu verificar ou chegar. Nenhum foi baixado.

| Id | Obra | URL candidata | Causa | O que fazer |
|---|---|---|---|---|
| FAO-IDP38 | FAO I&D Paper 38 - Drainage design factors (1980; Ar C E F S) | https://www.fao.org/3/x0490e/x0490e0r.htm (índice dos papers, sem link para o 38); busca em https://openknowledge.fao.org/ | o repositório OpenKnowledge devolve 403 ao robô; não há versão HTML por capítulo no servidor `fao.org/3` encontrada | o André busca "Drainage design factors" em openknowledge.fao.org e salva o PDF; enviar o link/arquivo à F2 (id `FAO-IDP38` já existe no catálogo do Hidráulico como manual_needed) |
| NRCS-CPS606 | NRCS Conservation Practice Standard 606 Subsurface Drain (jul/2022) | https://www.nrcs.usda.gov/sites/default/files/2022-10/Subsurface_Drain_606_NHCP_CPS_2022.pdf | host nrcs.usda.gov reinicia a conexão (000) ao robô; URL veio de busca, não verificada | baixar no navegador |
| NRCS-CPS607 | NRCS Conservation Practice Standard 607 Surface Drain, Field Ditch (set/2020) | https://www.nrcs.usda.gov/sites/default/files/2022-10/Surface_Drain_Field_Ditch_607_CPS_9_2020.pdf | idem | baixar no navegador |
| USACE-EM1110-2-1601-OFICIAL | EM 1110-2-1601 Hydraulic Design of Flood Control Channels (fonte oficial) | https://www.publications.usace.army.mil/Portals/76/Publications/EngineerManuals/EM_1110-2-1601.pdf | publications.usace.army.mil responde 403 a robô (também EM 1110-2-2902 e 1110-2-1413); o manifesto usa espelhos | se quiser a cópia oficial, baixar no navegador e substituir a URL do espelho |
| USBR-NOVOS | USBR: capítulos de Design Standards No. 3 além do cap. 4 (corpus) e demais manuais | https://www.usbr.gov/tsc/techreferences/designstandards-datacollectionguides/finalds-pdfs/DS3-n.pdf (padrão do corpus) | usbr.gov passou a reiniciar a conexão no meio da sessão (mesmo a URL DrainMan.pdf que respondeu antes); a página de índice mostrou aviso de manutenção | repetir a verificação em outro horário; nenhum item novo foi incluído no manifesto |
| FHWA-HY8-V8 | FHWA HY-8 versão 8.0 (software e manual) | https://www.fhwa.dot.gov/engineering/hydraulics/software/hy8/ | a página responde 200, mas o manual é instalador (.exe/.zip), fora das regras de F1 | o manifesto usa a documentação da versão 7.70 (NRCS); instalador fica a critério do André |
| FHWA-HEC11-OFICIAL | HEC-11 Design of Riprap Revetment (fonte oficial) | https://rosap.ntl.bts.gov/view/dot/41174 | rosap.ntl.bts.gov responde 403 ao robô; os links diretos fhwa.dot.gov/.../hec11.pdf deram 404 | manifesto usa o espelho do condado de Snohomish |

## F2 (2026-10-08): falha no download dos itens do manifesto

| Id | Obra | URL | Causa | O que fazer |
|---|---|---|---|---|
| FDOT-DRAINAGE-MANUAL-2016 | FDOT Drainage Manual (jan/2016) | https://www.fdot.gov/docs/default-source/roadway/drainage/files/2016Jan-DrainageManual.pdf | o servidor entrega o arquivo truncado e igual nas 2 tentativas (1.844.371 bytes, Content-Length coerente, mas sem xref/EOF; PyMuPDF lê 0 páginas). O arquivo foi descartado | baixar no navegador ou obter a edição vigente (prioridade C; não bloqueia F3/F4) |
