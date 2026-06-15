
def _BThittingSetOptimo(A,sets,indice,parcial,set_p,optimo):
    
    if len(parcial)>=len(optimo):
        return optimo
    if len(sets)==indice:
        return parcial[:]
    b=sets[indice]
    if any(x in set_p for x in b):
        return _BThittingSetOptimo(A,sets,indice+1,parcial,set_p,optimo)
    for x in b:
        if x not in set_p:
            parcial.append(x)
            set_p.add(x)
            optimo=_BThittingSetOptimo(A,sets,indice+1,parcial,set_p,optimo)
            parcial.pop()
            set_p.remove(x)
    return optimo

def hittingSetOptimo(jugadores, equipos):
    
    indice_inicial = 0
    parcial_inicial = []
    optimo_inicial = list(jugadores)
    
    return _BThittingSetOptimo(jugadores, equipos, indice_inicial, parcial_inicial,set(), optimo_inicial)
