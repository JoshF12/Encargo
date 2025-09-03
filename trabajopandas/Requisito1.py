# calcular el promedio de cada estudiante y mostrar cual es el max y min (promedio)

import pandas as pd
from Estudiantes import estudiantes, limpiar_notas

notas_limpias = limpiar_notas(estudiantes)

if notas_limpias.empty:
    print("No hay estudiantes con notas válidas.")
else:
    notas_limpias["promedio"] = notas_limpias.mean(axis=1).round(1)
    max_promedio = notas_limpias["promedio"].max()
    min_promedio = notas_limpias["promedio"].min()

    print(notas_limpias)
    print("Promedio máximo:", max_promedio)
    print("Promedio mínimo:", min_promedio)
