import time # librería para medir el tiempo de ejecución
import numpy as np # libreria para trabajar con arrays


# 1. Crear un millón de números
cantidad = 1_000_000

# prueba con listas de Python
inicio_lista = time.time()
lista = list(range(cantidad))

# operacon matemática: sumar 1 a cada elemento usando comprensión de listas
resultado_lista = [x + 1 for x in lista]
tiempo_lista = time.time() - inicio_lista

# 2. Prueba con arrays de NumPy
inicio_array = time.time()  
array = np.arange(cantidad) # array de NumPy con los mismos datos

resultado_array = array + 1 # operación matemática vectorizada
tiempo_array = time.time() - inicio_array

print(f"Tiempo con Listas de Python: {tiempo_lista:.5f} segundos")
print(f"Tiempo con Arrays de NumPy: {tiempo_array:.5f} segundos")

# Comparación de tiempos
if tiempo_lista > tiempo_array:
    print("NumPy es más rápido que las listas de Python.")  
else:
    print("Las listas de Python son más rápidas que NumPy.")

print(f"Factor de velocidad: {tiempo_lista / tiempo_array:.2f} veces más rápido con NumPy.")
