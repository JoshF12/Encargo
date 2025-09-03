# cual es la moda de todas las notas

import pandas as pd
from statistics import mode
from Estudiantes import estudiantes, limpiar_notas

notas_limpias = limpiar_notas(estudiantes)

if notas_limpias.empty:
    print("No hay notas válidas para calcular la moda.")
else:
    todas_las_notas = notas_limpias.values.flatten()
    todas_las_notas = [nota for nota in todas_las_notas if pd.notna(nota)]

    if not todas_las_notas:
        print("La lista de notas está vacía después de la limpieza.")
    else:
        try:
            moda = mode(todas_las_notas)
            print("La moda de todas las notas es:", moda)
        except Exception as e:
            print("No se pudo calcular la moda:", e)
