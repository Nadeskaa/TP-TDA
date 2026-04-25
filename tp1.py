
import sys
"""
"""
#!/usr/bin/env python3

def formatear_archivo_entrada():

    if len(sys.argv) != 2:
        sys.exit(1)
    
    rivales = []
    nombre_archivo = sys.argv[1]

    with open(nombre_archivo, 'r') as f:

        next(f)
        for linea in f:
            linea = linea.strip()
            if linea == "":
                continue
            s, a = map(int,linea.split(",")) 
            rival = [s, a]
            rivales.append(rival)
        rivales.sort(key=lambda x: x[1], reverse=True)

    return rivales


'''Calcula tiempo total mínimo'''
def analizar_rivales(rivales):
    tiempo_scaloni = 0
    tiempo_total = 0

    for s, a in rivales:
        tiempo_scaloni += s
        fin_rival = tiempo_scaloni + a

        if fin_rival > tiempo_total:
            tiempo_total = fin_rival
    return tiempo_total
    
"""
Ordena una lista de rivales en base a el tiempo de analisis del Ayudante, dejando una 
lista de rivales ordenada de mayor a menor.
"""


def main():
    rivales = formatear_archivo_entrada()
    tiempo = analizar_rivales(rivales)


    print("Tiempo total mínimo:", tiempo)

if __name__ == "__main__":
    main()


"""
FUNCION DE ORDENAMIENTO IMPLEMENTADA EN PRIMERA INSTANCIA, CAMBIADA POR TENER UNA COMPLEJIDAD TEMPORAL NO DESEADA. 
def ordenar_rivales(arr_rivales, rival):
    i = 0

    while i < len(arr_rivales) and arr_rivales[i][1] >= rival[1]:
        i += 1

    arr_rivales.insert(i, rival)
"""