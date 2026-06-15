import sys
import os
from mediciones.enfunciondeA.disjuntos import correr_mediciones_disjuntos
from mediciones.enfunciondeA.no_disjuntos import correr_mediciones_no_disjuntos
from mediciones.enfunciondeB.enfunciondeM import correr_mediciones_enBaseM
from backtracking import hittingSetOptimo
from carga_archivo import cargar_archivo

def main():
    if len(sys.argv) != 2:
        print("Uso: python3 tp2.py ruta/a/archivo.txt")
        return

    nombre_archivo = sys.argv[1]
    if nombre_archivo=="pruebas":
        correr_mediciones_disjuntos()
        correr_mediciones_no_disjuntos()
        correr_mediciones_enBaseM()
        return
    try:
        carpeta_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_archivo=os.path.join(carpeta_actual, "correctitud", nombre_archivo)
        A, B = cargar_archivo(ruta_archivo)

        optimo = hittingSetOptimo(A, B)
        elementos_str = ", ".join(optimo)
        print(f"Cantidad minima: {len(optimo)} -> [{elementos_str}]")
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo.")
if __name__ == "__main__":
    main()