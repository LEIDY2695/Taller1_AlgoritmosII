
# Programa para gestionar calificaciones de estudiantes

# Almacenar las calificaciones
calificaciones = []
#int input para la cantidad de calificaciones
cantidad = int(input("Ingrese la cantidad de calificaciones: ")) 
#for i in range(cantidad) para iterar sobre la cantidad de calificaciones
for i in range(cantidad): 
    nota = float(input(f"Ingrese una calificación {i+1}: "))
    calificaciones.append(nota) 

# Mostrar las calificaciones iniciales
print("CALIFICACIONES INICIALES: ", calificaciones)

# variable para almacenar la suma de las calificaciones
suma = 0
# Calcular la suma de las calificaciones
for nota in calificaciones:
    suma += nota

promedio_inicial = suma / len(calificaciones)

# Identificar la nota mas alta y la nota mas baja
nota_mas_alta = max(calificaciones)
nota_mas_baja = min(calificaciones)

# Modificar las notas inferiores a 3.0
for i in range(len(calificaciones)):
    # Si la calificación es menor a 3.0, se le suma 0.5, pero no puede superar el máximo de 5.0
    if calificaciones[i] < 3.0:
        calificaciones[i] = min(calificaciones[i] + 0.5, 5.0)

# variable para almacenar la suma de las calificaciones después de la modificación
calificaciones_modificadas = []
for nota in calificaciones:
    calificaciones_modificadas.append(nota)

# Calcular los resultados después de modificar las notas
suma_final = 0

for nota in calificaciones:
    suma_final += nota

promedio_final = suma_final / len(calificaciones)

# variables para contar estudiantes aprobados y reprobados
aprobados = 0
reprobados = 0

for nota in calificaciones:
    # nota es mayor o igual a 3.0 el estudiante aprueba, de lo contrario es reprobado
    if nota >= 3.0:
        aprobados += 1
    else:
        reprobados += 1

# Mostrar el informe final
print("\nRESULTADOS DEL PROCESO")
# Mostrar los resultados iniciales
print("Suma inicial:", round(suma, 2))
print("Promedio inicial:", round(promedio_inicial, 2))
print("Nota inicial más alta:", nota_mas_alta)
print("Nota inicial más baja:", nota_mas_baja)

print("\nCALIFICACIONES MODIFICADAS: ", calificaciones_modificadas)

print("\nRESUMEN FINAL")
print("Suma final:", round(suma_final, 2))
print("Promedio final:", round(promedio_final, 2))
print("Estudiantes aprobados:", aprobados)
print("Estudiantes reprobados:", reprobados)
