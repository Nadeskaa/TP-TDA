import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import sys
from pathlib import Path
raiz_proyecto = Path(__file__).resolve().parent.parent.parent
if str(raiz_proyecto) not in sys.path:
    sys.path.append(str(raiz_proyecto))

from util import time_algorithm
from backtracking import hittingSetOptimo
from carga_archivo import cargar_archivo

def obtener_argumentos_exp2_no_disjuntos(n):
    nombre_archivo = f"a_{int(n)}_b_15.txt"
    raiz_proyecto = Path(__file__).resolve().parent.parent.parent
    ruta_completa = raiz_proyecto / "sets" / "enfunciondeA" / "no_disjuntos" / nombre_archivo
    jugadores, equipos = cargar_archivo(ruta_completa)
    return (jugadores, equipos)


def correr_mediciones_no_disjuntos():
    n_exp2 = np.array([15, 30, 45, 60], dtype=float)

    print("Corriendo Experimento 2 (Variación de N - Sets NO Disjuntos)...")
    resultados_exp2 = time_algorithm(hittingSetOptimo, n_exp2, obtener_argumentos_exp2_no_disjuntos)
    tiempos_exp2 = np.array([resultados_exp2[n] for n in n_exp2])
    # Modelo Teórico: T(n) = c1 * n + c2
    f_lineal = lambda x, c1, c2: c1 * x + c2
    c_lin, _ = sp.optimize.curve_fit(f_lineal, n_exp2, tiempos_exp2)
    
    # Calculamos el error cuadrático total (residuos)
    r_lin = np.sum((f_lineal(n_exp2, c_lin[0], c_lin[1]) - tiempos_exp2)**2)

    print(f"Ecuación obtenida: T(n) = {c_lin[0]:.6e} * n + ({c_lin[1]:.4f})")
    print(f"c_1 (pendiente / costo por jugador) = {c_lin[0]}")
    print(f"c_2 (ordenada al origen / overhead) = {c_lin[1]}")
    print(f"Error cuadrático total: {r_lin:.6f}")
    fig, ax = plt.subplots(figsize=(8, 6))
    # Puntos medidos reales (Azules)
    ax.plot(n_exp2, tiempos_exp2, 'o-', label="Medición Real (Promedio)", color='blue', markersize=8, zorder=3)

    # Línea de ajuste teórica (Roja) pasada por los mismos puntos de N
    n_suave = np.linspace(min(n_exp2), max(n_exp2), 100)
    tiempos_teoricos = f_lineal(n_suave, c_lin[0], c_lin[1])
    ax.plot(n_suave, tiempos_teoricos, 'r--', label=f"Ajuste Lineal Teórico: {c_lin[0]:.2e}*n + {c_lin[1]:.2f}")
    ax.set_title('Tiempo de ejecucion Set no disjunto en funcion de Jugadores')
    ax.set_xlabel('Tamaño del Universo de Jugadores (N)')
    ax.set_ylabel('Tiempo de ejecución (s)')
    ax.grid(True, linestyle=':', alpha=0.5)
    ax.legend()
    plt.savefig('grafico_experimento2_lineal.png', dpi=300, bbox_inches='tight')
    plt.show()