import numpy as np

# 1. Configuración de la matriz (500 alumnos x 6 materias)
NUM_ALUMNOS = 500
NUM_MATERIAS = 6

# Genera calificaciones aleatorias entre 5.0 y 10.0
np.random.seed(42)
matriz_calificaciones = np.round(np.random.uniform(5.0, 10.0, size=(NUM_ALUMNOS, NUM_MATERIAS)), 1)

# 2. Búsqueda del Alumno 321 y Materia 5
alumno_objetivo = 321
materia_objetiva = 5

indice_alumno = alumno_objetivo - 1
indice_materia = materia_objetiva - 1

calificacion_encontrada = matriz_calificaciones[indice_alumno, indice_materia]

# -------------------------------------------------------------------
# IMPRESIÓN DE DATOS
# -------------------------------------------------------------------
print("=" * 65)
print(f"BÚSQUEDA: Alumno #{alumno_objetivo}, Materia #{materia_objetiva}")
print(f"CALIFICACIÓN ENCONTRADA: {calificacion_encontrada}")
print("=" * 65)

# Encabezado de la tabla
encabezado = f"{'Alumno':<10} | " + " | ".join([f"Mat {i+1}" for i in range(NUM_MATERIAS)])
print(encabezado)
print("-" * len(encabezado))

# BUCLE PARA IMPRIMIR LOS 500 ALUMNOS (SIN CORTAR NINGUNO)
for i in range(NUM_ALUMNOS):
    fila_str = " | ".join([f"{calif:>5.1f}" for calif in matriz_calificaciones[i]])
    
    # Si es el alumno 321, le ponemos una marca para identificarlo fácil
    if (i + 1) == alumno_objetivo:
        print(f"Alumno {i+1:<3}  | {fila_str}  <-- [ALUMNO BUSCADO]")
    else:
        print(f"Alumno {i+1:<3}  | {fila_str}")

print("=" * 65)