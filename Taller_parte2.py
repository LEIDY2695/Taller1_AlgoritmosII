
# Programa para gestionar calificaciones de estudiantes

# 1. Almacenar las calificaciones
calificaciones = []
cantidad = int(input("Ingrese la cantidad de calificaciones: ")) #int input para la cantidad de calificaciones
for i in range(cantidad): #for i in range(cantidad) para iterar sobre la cantidad de calificaciones
    nota = float(input(f"Ingrese una calificación {i+1}: "))
    calificaciones.append(nota) 

# 2. Mostrar las calificaciones iniciales
print("CALIFICACIONES INICIALES")
print(calificaciones)

# 3. Calcular la suma y el promedio inicial
suma = 0

for nota in calificaciones:
    suma += nota

promedio_inicial = suma / len(calificaciones)

# 4. Identificar la nota mayor y la menor
nota_mas_alta = max(calificaciones)
nota_mas_baja = min(calificaciones)

# 5. Modificar las notas inferiores a 3.0
for i in range(len(calificaciones)):
    if calificaciones[i] < 3.0:
        calificaciones[i] = min(calificaciones[i] + 0.5, 5.0)

# 6. Calcular los resultados después de modificar las notas
suma_final = 0

for nota in calificaciones:
    suma_final += nota

promedio_final = suma_final / len(calificaciones)

# 7. Contar estudiantes aprobados y reprobados
aprobados = 0
reprobados = 0

for nota in calificaciones:
    if nota >= 3.0:
        aprobados += 1
    else:
        reprobados += 1

# 8. Mostrar el informe final
print("\nRESULTADOS DEL PROCESO")
print("Promedio inicial:", round(promedio_inicial, 2))
print("Nota inicial más alta:", nota_mas_alta)
print("Nota inicial más baja:", nota_mas_baja)

print("\nCALIFICACIONES MODIFICADAS")
print(calificaciones)

print("\nRESUMEN FINAL")
print("Suma final:", round(suma_final, 2))
print("Promedio final:", round(promedio_final, 2))
print("Estudiantes aprobados:", aprobados)
print("Estudiantes reprobados:", reprobados)
