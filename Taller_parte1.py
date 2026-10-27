
import time
import numpy as np


# 1. Crear un millón de números
cantidad = 1_000_000

# Crear los datos para la lista
lista = list(range(cantidad))

# Crear los datos para el array
array = np.array(lista)

# 2. Medir el tiempo de ejecución de la lista
inicio_lista = time.perf_counter()

resultado_lista = [numero * 2 for numero in lista]

fin_lista = time.perf_counter()

tiempo_lista = fin_lista - inicio_lista

# 3. Medir el tiempo de ejecución del array
inicio_array = time.perf_counter()

resultado_array = array * 2

fin_array = time.perf_counter()

tiempo_array = fin_array - inicio_array

# 4. Mostrar los resultados
print("RESULTADOS DEL EXPERIMENTO")
print("------------------------")

print("Cantidad de datos:", cantidad)

print("Tiempo de la lista:", tiempo_lista, "segundos")

print("Tiempo del array:", tiempo_array, "segundos")

# 5. Comparar los tiempos
if tiempo_array < tiempo_lista:
    print("NumPy fue más rápido.")

    diferencia = tiempo_lista / tiempo_array

    print("El array fue aproximadamente",
          round(diferencia, 2), "veces más rápido.")

else:
    print("La lista fue más rápida en esta ejecución.")

# 6. Comprobar que los resultados sean iguales
print("¿Los resultados son iguales?:",
      resultado_lista == resultado_array.tolist())
