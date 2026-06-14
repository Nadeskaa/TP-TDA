# Implementacion_tp3
## Descripción
Este trabajo práctico implementa una solución exacta al problema de **Hitting Set**, un problema NP-Completo, utilizando un algoritmo de **backtracking** con poda.

Dado un conjunto de elementos (jugadores) y una colección de subconjuntos (pedidos de la prensa), el objetivo es encontrar el subconjunto mínimo de jugadores que intersecta a todos los conjuntos.

El algoritmo explora todas las combinaciones posibles de selección de jugadores, utilizando una estrategia de backtracking para construir soluciones parciales y una poda basada en la mejor solución encontrada hasta el momento para reducir el espacio de búsqueda.

Además, se realizan mediciones de tiempo sobre distintas instancias de prueba para analizar el comportamiento exponencial del algoritmo en función del tamaño de la entrada.

## Estructura del repositorio
```
TP-TDA/
├─ tp3.py                     # Código principal
├─ Informe_TP3.pdf            # Informe del TP2
├─ 5.txt                      # Test
├─ 10_pocos.txt               # Test 
├─ 7.txt                      # Test
├─ 10_todos.txt               # Test
├─ 10_varios.txt              # Test 
├─ 15.txt                     # Test 
├─ 20.tx                      # Test
├─ 50.txt                     # Test
├─ 75.txt                     # Test 
├─ 100.txt                    # Test 
├─ 200.txt                      # Test
├─ Resultados Esperados.txt        # Resultados Tests
└─ README.md                  # Este archivo
```

## Ejecución

```bash
# Ejecutar el algoritmo principal
python3 tp2.py <archivo_entrada.txt>
