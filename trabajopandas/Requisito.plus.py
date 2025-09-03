##calcular el promedio de notas por cada columna(por estudiante) y el promedio general del curso usando pandas
import pandas as pd
from Estudiantes import estudiantes, limpiar_notas

notas_limpias = limpiar_notas(estudiantes)

if notas_limpias.empty:
    print("No hay estudiantes con notas válidas.")
else:
    print("Promedio por evaluación:")
    print(notas_limpias.mean().round(1).to_string())

    print("\nPromedio general del curso:", round(notas_limpias.stack().mean(), 1))