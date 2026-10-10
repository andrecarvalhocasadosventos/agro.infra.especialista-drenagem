"""Gera um `.p01.hdf` SINTETICO minimo com a mesma estrutura de grupos do HEC-RAS 6.5 lida por tools.dren.hecras_hdf.

Origem da estrutura: inspecao com h5py do `.p01.hdf` real da captacao no Sao Francisco (caso HR-02), 2D; a parte 1D
(secoes) segue a convencao do HEC-RAS 6.x e NAO foi verificada contra arquivo real (a TPF nao entregou 1D).
Nao e dado de projeto: valores arbitrarios, escolhidos para o teste. Os arquivos reais (24-27 MB) nao entram no repo
(teto de 20 MB).
"""
import numpy as np


def _b(x):
    return np.bytes_(x.encode("utf-8"))


def gerar(caminho, n=10, n_manning=0.035, dt=10.0, v_face=0.8, declividade=1e-4, com_1d=False, equacao="SWE-ELM",
          estavel=True, unidades="SI Units"):
    """Malha n x n de celulas 10 m x 10 m (area 100 m2), 49 saidas de 30 min (24 h), NA final 100,5 m sobre fundo
    de 98 a 99,9 m. Uma face com velocidade 6 m/s (pico isolado)."""
    import h5py
    nc = n * n
    nf = 2 * n * (n - 1)
    zmin = np.linspace(98.0, 99.9, nc).astype("f4")
    t_dias = (np.arange(49) * 0.5 / 24.0).astype("f8")
    ws = np.empty((49, nc), "f4")
    for i in range(49):
        frac = min(1.0, i / 12.0)
        ws[i] = (zmin + frac * (100.5 - zmin)).astype("f4")
    if not estavel:
        ws[-1, :5] += 0.05  # ultimas 2 h ainda variam
    ci = np.zeros((nf, 2), "i4")
    for k in range(nf):
        ci[k] = (k % nc, (k + 1) % nc)
    vface = np.full(nf, v_face, "f4")
    vface[0] = 6.0
    with h5py.File(caminho, "w") as f:
        f.attrs["File Type"] = _b("HEC-RAS Results")
        f.attrs["File Version"] = _b("HEC-RAS 6.5 February 2024")
        f.attrs["Units System"] = _b(unidades)
        f.attrs["Projection"] = _b('PROJCS["SIRGAS_2000_UTM_Zone_23S"]')
        pi = f.create_group("Plan Data/Plan Information")
        pi.attrs["Plan Title"] = _b("simulacao")
        pi.attrs["Geometry Title"] = _b("geometria")
        pi.attrs["Flow Title"] = _b("contornos")
        pi.attrs["Computation Time Step Base"] = _b("%dSEC" % dt)
        pi.attrs["Base Output Interval"] = _b("30MIN")
        pi.attrs["Time Window"] = _b("14Sep2026 01:00:00 to 15Sep2026 01:00:00")
        pp = f.create_group("Plan Data/Plan Parameters")
        pp.attrs["2D Equation Set"] = np.array([_b(equacao)])
        pp.attrs["2D Theta"] = np.array([1.0])
        pp.attrs["2D Water Surface Tolerance"] = np.array([0.003])
        pp.attrs["2D Volume Tolerance"] = np.array([0.003])
        pp.attrs["2D Maximum Iterations"] = np.array([20])
        pp.attrs["Gravity"] = 9.80665
        ru = f.create_group("Results/Unsteady")
        ru.attrs["Program Version"] = _b("HEC-RAS 6.5 February 2024")
        ru.attrs["Type of Run"] = _b("Unsteady Flow Analysis")
        g = f.create_group("Geometry/2D Flow Areas/Perimeter 1")
        g.create_dataset("Cells Surface Area", data=np.full(nc, 100.0, "f4"))
        g.create_dataset("Cells Minimum Elevation", data=zmin)
        g.create_dataset("Cells Center Manning's n", data=np.full(nc, n_manning, "f4"))
        g.create_dataset("Faces Cell Indexes", data=ci)
        at = np.zeros(1, dtype=[("Name", "S16"), ("Mann", "<f4"), ("Cell Count", "<i4")])
        at[0] = (b"Perimeter 1", n_manning, nc)
        f.create_dataset("Geometry/2D Flow Areas/Attributes", data=at)
        bc = np.zeros(2, dtype=[("Name", "S32"), ("SA-2D", "S16"), ("Type", "S8"), ("Length", "<f4")])
        bc[0] = (b"entrada", b"Perimeter 1", b"External", 100.0)
        bc[1] = (b"saida", b"Perimeter 1", b"External", 100.0)
        f.create_dataset("Geometry/Boundary Condition Lines/Attributes", data=bc)
        ec = "Event Conditions/Unsteady/Boundary Conditions/"
        f.create_dataset(ec + "Flow Hydrographs/2D: Perimeter 1 BCLine: entrada",
                         data=np.column_stack([np.arange(5.0), np.full(5, 50.0)]).astype("f4"))
        f.create_dataset(ec + "Normal Depths/2D: Perimeter 1 BCLine: saida", data=np.array([declividade], "f4"))
        ts = "Results/Unsteady/Output/Output Blocks/Base Output/Unsteady Time Series/"
        d = f.create_dataset(ts + "Time", data=t_dias)
        d.attrs["Time"] = _b("days")
        a2 = ts + "2D Flow Areas/Perimeter 1/"
        f.create_dataset(a2 + "Water Surface", data=ws)
        f.create_dataset(a2 + "Computations/Time Step", data=np.full((49, 1), dt, "f4"))
        f.create_dataset(a2 + "Computations/Volume Error", data=np.zeros((49, 1), "f4"))
        f.create_dataset(a2 + "Computations/Volume", data=np.full((49, 1), 1000.0, "f4"))
        sm = "Results/Unsteady/Output/Output Blocks/Base Output/Summary Output/2D Flow Areas/Perimeter 1/"
        f.create_dataset(sm + "Maximum Face Velocity", data=np.vstack([vface, np.zeros(nf, "f4")]))
        f.create_dataset(sm + "Maximum Water Surface", data=np.vstack([ws.max(axis=0), np.zeros(nc, "f4")]))
        cb = "Results/Unsteady/Output/Output Blocks/Computation Block/Global/Time"
        f.create_dataset(cb, data=(np.arange(0, 24 * 3600 + dt, dt) / 86400.0).astype("f8"))
        if com_1d:
            ns = 4
            x = np.zeros(ns, dtype=[("River", "S16"), ("Reach", "S16"), ("RS", "S8")])
            for i in range(ns):
                x[i] = (b"Rio Verde", b"Trecho 1", str(1000 - 250 * i).encode())
            f.create_dataset("Geometry/Cross Sections/Attributes", data=x)
            f.create_dataset("Geometry/Cross Sections/Manning's n Info", data=np.zeros((ns, 2), "i4"))
            f.create_dataset("Geometry/Cross Sections/Manning's n Values",
                             data=np.array([[0.0, 0.040], [50.0, 0.035], [90.0, 0.040]] * ns, "f4"))
            tsx = ts + "Cross Sections/"
            na = np.array([[100 + 0.1 * i + 0.5 * np.sin(k / 8.0) for i in range(ns)] for k in range(49)], "f4")
            f.create_dataset(tsx + "Water Surface", data=na)
            f.create_dataset(tsx + "Velocity Total", data=np.tile(np.array([1.0, 1.5, 2.0, 1.2], "f4"), (49, 1)))
