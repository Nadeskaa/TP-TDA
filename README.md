# implementacion_tp2
## Descripción
Trabajo práctico de Programación Dinámica enfocado en resolver un problema de optimización.
Se busca maximizar la ganancia total de un plan de entrenamiento de n días para la selección, decidiendo en qué días conviene entrenar o descansar. Cada día tiene una ganancia potencial, pero la energía de los jugadores disminuye al entrenar días consecutivos y se recupera al descansar.
Se desarrolla una solución mediante Programación Dinámica, incluyendo formulación de recurrencia, demostración de correctitud, reconstrucción de solución óptima y análisis de complejidad.

## Estructura del repositorio
```
TP-TDA/
├─ tp2.py                     # Código principal
├─ Informe_TP2.pdf            # Informe del TP2
├─ descanso_frecuente.txt     # Test
├─ energia_baja_rapido.txt    # Test 
├─ energia_siempre_mayor.txt  # Test
├─ ganancia_creciente.txt     # Test
├─ mixto.txt                  # Test 
├─ energia_muy_baja.txt       # Test 
├─ Resultados Test.txt        # Test 
└─ README.md                  # Este archivo
```

## Ejecución

```bash
# Ejecutar el algoritmo principal
python3 tp2.py <archivo_entrada.txt>