import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import os
import sys
from pathlib import Path
raiz_proyecto = Path(__file__).resolve().parent.parent.parent
if str(raiz_proyecto) not in sys.path:
    sys.path.append(str(raiz_proyecto))

from util import time_algorithm
from backtracking import hittingSetOptimo
from carga_archivo import cargar_archivo
def obtener_argumentos_exp1(m):
    nombre_archivo = f"datos_n40_m{int(m)}.txt"
    raiz_proyecto = Path(__file__).resolve().parent.parent.parent

    ruta_completa = raiz_proyecto / "sets" / "enfunciondeB" / "n_40" / nombre_archivo
    
    jugadores, equipos = cargar_archivo(ruta_completa)
    return (jugadores, equipos)

def correr_mediciones_enBaseM():
    m_exp1 = np.array([5, 10, 20, 50, 75, 100], dtype=float)
    resultados_exp1 = time_algorithm(hittingSetOptimo, m_exp1, obtener_argumentos_exp1)
    tiempos_exp1 = np.array([resultados_exp1[m] for m in m_exp1])
    f_lineal = lambda x, c1, c2: c1 * x + c2
    c_lin, _ = sp.optimize.curve_fit(f_lineal, m_exp1, tiempos_exp1)
    r_lin = np.sum((f_lineal(m_exp1, c_lin[0], c_lin[1]) - tiempos_exp1)**2)
    print(f"c_1 = {c_lin[0]}, c_2 = {c_lin[1]}")
    print(f"Error cuadrático total: {r_lin}")

    fig, ax = plt.subplots()
    ax.plot(m_exp1, tiempos_exp1, 'o-', label="Medición Real (Promedio)")
    ax.plot(m_exp1, [c_lin[0] * m + c_lin[1] for m in m_exp1], 'r--', label="Ajuste Lineal Теórico")
    ax.set_title('Tiempo de ejecución en funcion de subconjuntos')
    ax.set_xlabel('Cantidad de Restricciones (M)')
    ax.set_ylabel('Tiempo de ejecución (s)')
    ax.grid(True, linestyle=':', alpha=0.5)
    ax.legend()
    plt.show()