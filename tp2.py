import sys

def archivo_entrenamiento(nombre_archivo):

    with open(nombre_archivo,'r') as archivo:

        lineas = archivo.readlines()
        E = []
        S = []
        datos = []
        for linea in lineas:
            datos.append(int(linea.strip()))
            n = datos[0]

        for e in range(1,n+1):
            E.append(datos[e])

        for s in range(n+1,2*n + 1):
            S.append(datos[s])
        return E,S

def entrenamiento(E,S):

    cantidad_dias = len(E)
    entrenamiento_optimo = []

    for i in range (cantidad_dias + 2):
        fila = []
        for j in range (cantidad_dias + 2):
            fila.append(0)
        entrenamiento_optimo.append(fila)

    for dia_actual in range (cantidad_dias,0,-1):

        for dias_seguidos in range(1, cantidad_dias + 1):

            ganancia_entrenar = min(S[dias_seguidos - 1], E[dia_actual-1]) + entrenamiento_optimo[dia_actual + 1][dias_seguidos + 1]
            ganancia_descansar = entrenamiento_optimo[dia_actual + 1][1]

            if ganancia_entrenar > ganancia_descansar:
                entrenamiento_optimo[dia_actual][dias_seguidos] = ganancia_entrenar
            else:
                entrenamiento_optimo[dia_actual][dias_seguidos] = ganancia_descansar
    return entrenamiento_optimo


def reconstruir_entrenamiento(entrenamiento_optimo,E,S):
    
    cantidad_dias = len(E)
    dias_seguidos= 1

    decisiones = []

    for dia_actual in range(1,cantidad_dias + 1):

        ganancia_entrenar = min(S[dias_seguidos - 1], E[dia_actual - 1]) + entrenamiento_optimo[dia_actual + 1][dias_seguidos + 1]

        ganancia_descansar = entrenamiento_optimo[dia_actual + 1][1]

        if ganancia_entrenar >= ganancia_descansar:
            decisiones.append("Entrenar")
            if dias_seguidos < len(S):
                dias_seguidos += 1
        else:
            decisiones.append("Descansar")
            dias_seguidos = 1
    return decisiones
    


def main():
    if len(sys.argv) != 2:
        print("Uso: python3 tp2.py ruta/a/archivo.txt")
        return

    nombre_archivo = sys.argv[1]

    E, S = archivo_entrenamiento(nombre_archivo)

    tabla = entrenamiento(E, S)

    print("Ganancia máxima:", tabla[1][1])

    decisiones = reconstruir_entrenamiento(tabla, E, S)
    print("Plan de entrenamiento:", decisiones)


if __name__ == "__main__":
    main()
