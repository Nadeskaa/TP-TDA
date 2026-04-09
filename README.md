
# TP1 Teoría de Algoritmos – Algoritmos Greedy

## Descripción

En este trabajo práctico se aborda el **diseño y análisis de algoritmos greedy**, una técnica clave en problemas de optimización.  
El objetivo es ayudar a Scaloni a analizar los próximos `n` rivales de la selección campeona del mundo, de manera que el tiempo total necesario para completar todos los análisis sea **mínimo**.

Cada rival debe ser analizado primero por Scaloni (`si` minutos) y luego por un ayudante (`ai` minutos). Los ayudantes pueden trabajar **en paralelo**, siempre después de que Scaloni haya terminado su análisis.  

El desafío consiste en:

- Minimizar el tiempo total para que todos los análisis estén completos.
- Garantizar que los ayudantes trabajen en paralelo eficientemente.
- Aplicar la **estrategia greedy** basada en el tiempo de análisis de los ayudantes.

---

## Estructura del repositorio
```
TP-TDA/
├─ tp1.py                 # Código principal con algoritmo greedy
├─ ayudantes mayor.txt     # Test case: ai >> si
├─ scaloni mayor.txt       # Test case: si >> ai
├─ soluciones optimas.txt  # Soluciones óptimas de ejemplo
├─ tiempos iguales.txt     # Test case: si == ai
├─ tiempos similares.txt   # Test case: ai ≈ si
└─ README.md               # Este archivo
```
## Ejecución

```bash
# Ejecutar el algoritmo principal
python3 tp1.py <archivo_entrada.txt>
