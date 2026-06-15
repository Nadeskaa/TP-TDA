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

def obtener_argumentos_exp2(n):
    nombre_archivo = f"a_{int(n)}_b_15.txt"
    
    raiz_proyecto = Path(__file__).resolve().parent.parent.parent
    ruta_completa = raiz_proyecto / "sets" / "enfunciondeA" / "disjuntos" / nombre_archivo
    jugadores, equipos = cargar_archivo(ruta_completa)
    return (jugadores, equipos)

def correr_mediciones_disjuntos():
    n_exp2 = np.array([15, 30, 45,60], dtype=float)
    resultados_exp2 = time_algorithm(hittingSetOptimo, n_exp2, obtener_argumentos_exp2)
    tiempos_exp2 = np.array([resultados_exp2[n] for n in n_exp2])
    f_recta = lambda x, A, B: A  + B*x
    
    # Le aplicamos logaritmo a los tiempos medidos
    tiempos_log = np.log(tiempos_exp2)
    params_recta, _ = sp.optimize.curve_fit(f_recta, n_exp2, tiempos_log)
    A_opt, B_opt = params_recta

    # coeficientes exponenciales 
    c_exp = [np.exp(B_opt), np.exp(A_opt)] 
    
    # Error cuadrático total sobre la escala real
    f_exponencial = lambda x, c1, c2: c1 * (c2 ** x)
    r_exp = np.sum((f_exponencial(n_exp2, c_exp[0], c_exp[1]) - tiempos_exp2)**2)

    print(f"Ecuación obtenida: T(n) = {c_exp[0]:.6e} * ({c_exp[1]:.4f})^n")
    print(f"Error cuadrático total (r): {r_exp:.6f}")
    fig, ax = plt.subplots(figsize=(8, 6))

    # Puntos medidos reales
    ax.plot(n_exp2, tiempos_exp2, 'o-', label="Medición Real (Promedio)", zorder=3)
    
    # Generamos un rango fino de puntos intermedios para que la curva se dibuje suave y curva
    n_suave = np.linspace(min(n_exp2), max(n_exp2), 100)
    ax.plot(n_suave, f_exponencial(n_suave, c_exp[1], c_exp[0]), 'r--', label="Ajuste Exponencial Teórico")
    
    ax.set_title('Tiempo de ejecucion set disjuntos en funcion de Jugadores')
    ax.set_xlabel('Tamaño del Universo de Jugadores (N)')
    ax.set_ylabel('Tiempo de ejecución (s)')
    ax.grid(True, linestyle=':', alpha=0.5)
    ax.legend()
    plt.savefig('grafico_experimento2.png', dpi=300)
    plt.show()