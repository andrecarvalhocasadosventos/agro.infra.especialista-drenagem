"""Testes de tools.dren.hecras_hdf (somente leitura de .hdf do HEC-RAS).

(a) Fixture SINTETICA (tests/dren/fixtures/sintetico.py): 2D e 1D; consistencia e avisos (valores arbitrarios).
(b) Arquivos REAIS da TPF (acervo, sem marca h): captacao no Sao Francisco, 2D, HEC-RAS 6.5. Cada .hdf tem 24-27 MB
    (> 20 MB), por isso nao estao no repo; o teste roda se existir a copia local indicada por HECRAS_FIXTURES ou
    `D:/14 - AGRO/squad/drenagem_download/hecras` e e pulado caso contrario. Numeros: casos/hec-ras/
    2026-10-09_tpf_sao-francisco_malha_e_convergencia.md (HR-02), tolerancia 5 %.
"""
import importlib.util
import json
import os
import subprocess
import sys

import pytest

pytest.importorskip("h5py")

from tools.dren import hecras_hdf as H  # noqa: E402

AQUI = os.path.dirname(__file__)
RAIZ = os.path.abspath(os.path.join(AQUI, "..", ".."))
_spec = importlib.util.spec_from_file_location("sintetico", os.path.join(AQUI, "fixtures", "sintetico.py"))
S = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(S)

REAL_DIR = os.environ.get("HECRAS_FIXTURES", "D:/14 - AGRO/squad/drenagem_download/hecras")
Q95 = os.path.join(REAL_DIR, "sao_francisco_Q95__sao_francisco.p01.hdf")
QTR100 = os.path.join(REAL_DIR, "sao_francisco_QTR100__sao_francisco.p01.hdf")
real = pytest.mark.skipif(not (os.path.isfile(Q95) and os.path.isfile(QTR100)),
                          reason="copia local dos .hdf reais ausente")


@pytest.fixture
def p01(tmp_path):
    c = str(tmp_path / "s.p01.hdf")
    S.gerar(c)
    return c


def _abrir_e_fechar(fn, caminho, **kw):
    f = H.abrir(caminho)
    try:
        return fn(f, **kw)
    finally:
        f.close()


# ----------------------------------------------------------------- sintetico
def test_plano_e_passo(p01):
    r = H.verificar(p01)
    pl = r["plano"]["plano"]
    assert pl["versao_programa"].startswith("HEC-RAS 6.5") and pl["equacao_2d"] == "SWE-ELM"
    assert pl["passo_base_s"] == 10.0 and pl["intervalo_saida_s"] == 1800.0
    assert r["passo_efetivo"]["dt_mediano_s"] == pytest.approx(10.0, rel=1e-6)


def test_malha_e_n(p01):
    r = H.verificar(p01)["malha"]["areas"]["Perimeter 1"]
    assert r["celulas"] == 100 and r["area_celula"]["mediana"] == 100.0
    assert r["tamanho_equivalente"]["mediana"] == pytest.approx(10.0)
    assert r["manning_n"]["distintos"] == 1 and r["manning_n"]["valores"][0]["n"] == pytest.approx(0.035)


def test_resultados_2d_e_estabilizacao(p01):
    r = H.verificar(p01)["resultados_2d"]["areas"]["Perimeter 1"]
    assert r["duracao_h"] == pytest.approx(24.0)
    assert r["NA_fim_celulas_molhadas"]["max"] == pytest.approx(100.5, abs=1e-3)
    assert r["estabilizacao"]["dNA_max_m"] == pytest.approx(0.0, abs=1e-6)
    assert r["velocidade_maxima_face"]["max"] == pytest.approx(6.0)


def test_avisos_basicos(p01):
    av = " ".join(H.verificar(p01)["avisos"])
    assert "n de Manning unico" in av
    assert "profundidade normal" in av
    assert "pico isolado" in av  # 6 m/s contra p95 de 0,8


def test_estabilizacao_nao_demonstrada(tmp_path):
    c = str(tmp_path / "i.p01.hdf")
    S.gerar(c, estavel=False)
    r = H.verificar(c)
    assert r["resultados_2d"]["areas"]["Perimeter 1"]["estabilizacao"]["dNA_max_m"] == pytest.approx(0.05, abs=1e-3)
    assert any("estabilizacao nao demonstrada" in a for a in r["avisos"])


def test_courant_estimado(tmp_path):
    c = str(tmp_path / "c.p01.hdf")
    S.gerar(c, dt=10.0, v_face=0.8)
    r = _abrir_e_fechar(H.courant_2d, c)
    a = r["areas"]["Perimeter 1"]
    # V = 0,8 m/s, dT = 10 s, dX = 10 m: C so com velocidade = 0,8 (pico isolado de 6 m/s -> 6)
    assert a["courant_so_velocidade"]["mediana"] == pytest.approx(0.8, rel=1e-6)
    assert a["courant_so_velocidade"]["max"] == pytest.approx(6.0, rel=1e-6)
    assert any("max 6.00 > 3.0" in x for x in r["avisos"])
    r2 = _abrir_e_fechar(H.courant_2d, c, dt_s=0.5)
    assert not [x for x in r2["avisos"] if "> 3.0" in x]


def test_courant_difusao_limite_5(tmp_path):
    c = str(tmp_path / "d.p01.hdf")
    S.gerar(c, equacao="Diffusion Wave", dt=10.0, v_face=0.8)
    r = _abrir_e_fechar(H.courant_2d, c)
    assert any("> 5.0" in x for x in r["avisos"])  # pico de 6 m/s -> C = 6 > 5
    assert any("difusao" in a for a in H.verificar(c)["avisos"])


def test_contorno_normal_depth(p01):
    r = _abrir_e_fechar(H.contornos, p01)
    ev = r["evento"]["2D: Perimeter 1 BCLine: saida"]
    assert ev["declividade"] == pytest.approx(1e-4, rel=1e-5) and ev["declividade_pct"] == pytest.approx(0.01, rel=1e-4)
    q = r["evento"]["2D: Perimeter 1 BCLine: entrada"]
    assert q["valor_max"] == 50.0 and q["constante"]
    assert [x["nome"] for x in r["linhas_geometria"]] == ["entrada", "saida"]


def test_secoes_1d(tmp_path):
    c = str(tmp_path / "u.p01.hdf")
    S.gerar(c, com_1d=True)
    r = _abrir_e_fechar(H.secoes_1d, c)
    assert len(r["secoes"]) == 4
    s0 = r["secoes"][0]
    assert s0["rio"] == "Rio Verde" and s0["estacao"] == "1000"
    assert s0["NA_max"] == pytest.approx(100.5, abs=0.02) and s0["V_max"] == 1.0
    assert r["manning_n_1d"]["distintos"] == 2


def test_sem_1d_nao_inventa(p01):
    r = _abrir_e_fechar(H.secoes_1d, p01)
    assert r["secoes"] == [] and r["avisos"]


def test_somente_leitura(p01):
    antes = os.path.getmtime(p01), os.path.getsize(p01)
    H.verificar(p01)
    assert (os.path.getmtime(p01), os.path.getsize(p01)) == antes


def test_arquivo_inexistente():
    with pytest.raises(ValueError):
        H.abrir("nao_existe.hdf")


def test_comparar():
    assert H.comparar(99.9, 100.0)["dentro_da_tolerancia"]
    r = H.comparar(110.0, 100.0)
    assert not r["dentro_da_tolerancia"] and r["avisos"]


def test_cli(p01):
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    out = subprocess.run([sys.executable, "-m", "tools.dren.hecras_hdf", "--funcao", "verificar", "--arquivo", p01],
                         capture_output=True, text=True, cwd=RAIZ, env=env, encoding="utf-8")
    assert out.returncode == 0, out.stderr
    d = json.loads(out.stdout)
    assert d["saidas"]["malha"]["areas"]["Perimeter 1"]["celulas"] == 100 and d["avisos"]


# ----------------------------------------------------------------- real (HR-02), sem marca h
@real
def test_real_q95_malha_e_manning():
    m = _abrir_e_fechar(H.malha_2d, Q95)["areas"]["Perimeter 1"]
    assert m["celulas"] == 31313
    assert m["area_celula"]["mediana"] == pytest.approx(99.93, rel=0.05)
    assert m["area_celula"]["media"] == pytest.approx(648, rel=0.05)
    assert m["area_celula"]["max"] == pytest.approx(4348, rel=0.05)
    assert m["manning_n"]["distintos"] == 1 and m["manning_n"]["valores"][0]["n"] == pytest.approx(0.035, rel=0.05)


@real
@pytest.mark.parametrize("arq,molh,na_med,na_p95,dna,vp95,vmax", [
    (Q95, 21996, 390.88, 391.01, 0.0005, 0.86, 7.16),
    (QTR100, 28882, 397.67, 397.84, 0.040, 2.18, 3.56)])
def test_real_resultados_hr02(arq, molh, na_med, na_p95, dna, vp95, vmax):
    r = _abrir_e_fechar(H.resultados_2d, arq)["areas"]["Perimeter 1"]
    assert r["celulas_molhadas_fim"] == pytest.approx(molh, rel=0.05)
    assert r["NA_fim_celulas_molhadas"]["mediana"] == pytest.approx(na_med, rel=0.05)
    assert r["NA_fim_celulas_molhadas"]["p95"] == pytest.approx(na_p95, rel=0.05)
    assert r["estabilizacao"]["dNA_max_m"] == pytest.approx(dna, rel=0.05)
    assert r["velocidade_maxima_face"]["p95"] == pytest.approx(vp95, rel=0.05)
    assert r["velocidade_maxima_face"]["max"] == pytest.approx(vmax, rel=0.05)


@real
def test_real_plano_contornos_hr03():
    f = H.abrir(Q95)
    try:
        pl = H.info_plano(f)["plano"]
        c = H.contornos(f)
    finally:
        f.close()
    assert pl["versao_programa"].startswith("HEC-RAS 6.5") and pl["equacao_2d"] == "SWE-ELM"
    assert pl["passo_base_s"] == 10.0
    # HR-03: declividade 0,0093 % no arquivo contra 0,01 % do relatorio
    assert c["evento"]["2D: Perimeter 1 BCLine: saida 1"]["declividade_pct"] == pytest.approx(0.0093, rel=0.05)
    assert c["evento"]["2D: Perimeter 1 BCLine: entrada"]["valor_max"] == pytest.approx(783.77, rel=0.005)
