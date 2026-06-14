import sys
import time


def leer_archivo(ruta):
    conjuntos = []
    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()

            if linea:
                conjuntos.append(
                    [jugador.strip() for jugador in linea.split(",")]
                )
    return conjuntos

def bt(conjuntos, solucion_actual, cubiertos, mejor_solucion):

    if len(cubiertos) == len(conjuntos):

        if (not mejor_solucion or
            len(solucion_actual) < len(mejor_solucion)):

            mejor_solucion.clear()

            for jugador in solucion_actual:
                mejor_solucion.append(jugador)

        return

    if (mejor_solucion and
        len(solucion_actual) >= len(mejor_solucion)):
        return

    indice = 0

    while indice < len(conjuntos):

        if indice not in cubiertos:
            break

        indice += 1

    conjunto = conjuntos[indice]

    for jugador in conjunto:

        if jugador in solucion_actual:
            continue

        nuevos_cubiertos = cubiertos.copy()

        for i in range(len(conjuntos)):
            if jugador in conjuntos[i]:
                nuevos_cubiertos.add(i)

        solucion_actual.append(jugador)

        bt(conjuntos,solucion_actual, nuevos_cubiertos, mejor_solucion)
        solucion_actual.pop()

def hitting_set_backtracking(conjuntos):

    mejor_solucion = []

    bt(conjuntos, [], set(), mejor_solucion)

    return mejor_solucion



def main():
    if len(sys.argv) != 2:
        print("Uso: python3 tp3.py ruta/a/archivo.txt")
        return

    nombre_archivo = sys.argv[1]

    conjuntos = leer_archivo(nombre_archivo)

    inicio = time.perf_counter()

    solucion = hitting_set_backtracking(conjuntos)

    fin = time.perf_counter()

    print(
        f"Cantidad mínima: {len(solucion)} "
        f"({', '.join(solucion)})"
    )

    print(f"Tiempo: {fin - inicio:.6f} segundos")

if __name__ == "__main__":
    main()