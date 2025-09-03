# cuantos estudiantes tienen almenos una nota < 4.0

import pandas as pd
from Estudiantes import estudiantes, limpiar_notas

notas_limpias = limpiar_notas(estudiantes)

if notas_limpias.empty:
    print("No hay estudiantes con notas válidas.")
else:
    estudiantes_con_nota_baja = (notas_limpias < 4.0).any(axis=1)
    porcentaje = round((estudiantes_con_nota_baja.sum() / len(notas_limpias)) * 100, 1)
    print(f"Porcentaje de estudiantes con al menos una nota bajo 4.0: {porcentaje}%")