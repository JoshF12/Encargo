# cuantos estudiantes tienen todas las notas >= 4.0

import pandas as pd
from Estudiantes import estudiantes, limpiar_notas

notas_limpias = limpiar_notas(estudiantes)

if notas_limpias.empty:
    print("No hay estudiantes con notas válidas.")
else:
    aprobados = notas_limpias.apply(lambda fila: all(n >= 4.0 for n in fila if pd.notnull(n)), axis=1)
    cantidad_aprobados = aprobados.sum()
    print("Cantidad de aprobados (todas las notas >= 4,0):",cantidad_aprobados)
