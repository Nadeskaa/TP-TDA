
import sys
"""
"""
#!/usr/bin/env python3

def formatear_archivo_entrada():
    if len(sys.argv) != 2:
        sys.exit(1)
    
    res = []
    nombre_archivo = sys.argv[1]

    i = 0
    with open(nombre_archivo, 'r') as f:
 
        for linea in f[1:]:
            linea = linea.strip()
            if not linea:
                continue

            a, b = linea.split(",")
            rival = [int(a), int(b)]


            ordenar_rivales(res, linea.split(","))
    
    return res




def analizar_rivales(rivales):
    tiempo_individual = 0
    tiempo_total = 0
    for r in rivales:
        tiempo_individual = rivales[0] + rivales[1]
        if (tiempo_individual > tiempo_total):
            tiempo_total = tiempo_individual
            
# Aqui analizaria scaloni y despues los ayudantes.

    return tiempo_total
    
"""
Ordena una lista de rivales en base a el tiempo de analisis del Ayudante, dejando una 
lista de rivales ordenada de mayor a menor.
"""

def ordenar_rivales(arr_rivales, rival):
    i = 0

    while i < len(arr_rivales) and arr_rivales[i][1] >= rival[1]:
        i += 1

    arr_rivales.insert(i, rival)
