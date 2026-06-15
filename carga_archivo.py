
def cargar_archivo(nombre_archivo):

    with open(nombre_archivo,'r') as archivo:

        lineas = archivo.readlines()
        A=[]
        B=[]
        aux=set()
        datos=[]
        for linea in lineas:
            linea_bien=linea.strip()
            if linea_bien.endswith('.'):
                linea_bien = linea_bien[:-1]
            if not linea_bien:
                continue
            datos=[]
            jugadores=linea_bien.split(",")
            for j in jugadores:
                jugador=j.strip()
                datos.append(jugador)
                if jugador not in aux:
                    aux.add(jugador)
                    A.append(jugador)
            B.append(datos)
        return A,B
