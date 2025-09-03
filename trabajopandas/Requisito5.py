# entregar un listado con los estudiantes de mayor a menor promedio

import pandas as pd
import numpy as np
from Estudiantes import estudiantes, limpiar_notas  # si tu archivo es Estudiantes.py

notas_limpias = limpiar_notas(estudiantes)

if notas_limpias.empty:
    print("No hay estudiantes con notas válidas.")
else:
    listado = pd.DataFrame({
        "Nombre": pd.DataFrame(estudiantes)["nombre"].loc[notas_limpias.index],
        "Promedio": notas_limpias.mean(axis=1).round(1)
    }).sort_values(by="Promedio", ascending=False).reset_index(drop=True)

    print(listado)