# Taller de Laboratorio: Listas y Arrays

## 1. Introducción

En este taller se realizó dos actividades, en la parte  1 se realizó  una comparacion entres las listsa de phyton y Arrays de NumPy, co el objetivo de conocer si diferencias y observar cual tiene un  mejor rendimiento al trabajar con grandes cantidades de datos. 

Para la actividad de la parte 2 se realizo un algoritmo para gestionar las notas de un grupo de estudiantes, realizando calculos, ,odificaciones y mostrando los resultados obtenidos. 

## 2. Actividad Parte 1: Comparacion de Listas y Arrays 

Descripcion del experimento 
Para realizar la prueba, se definió una cantidad de un millon de numeros, se utiliza una lista Python y un Array de NumPy.
En ambas estructuras se aplicó la misma operacion, sumar 1 a cada numero. 
Se utiliza la funcion time.time() para medir el tiempo que tardaba cada estructura en realizar la operacion y asi poder comparar los resultados. 

## resultados del experimento 
Los resultados obtenidos durante la ejecución del programa fueron los siguientes:

Tiempos con Listas de Python 0.07210 segundos 
Tiempos con Array de NumPy   0.00730 segundos
De acuerdo con los resultados registrados, la estructura que presentó el menor tiempo de ejecución fue Numpy.

## Analisis Comparativo 
Durante la prueba se observo que el array de NumPy realizó la operación en menos tiempo que la lista de Python.

Esto se debe a que las listas procesan los datos elemento por elemento, mientras que NumPy permite realizar operaciones sobre varios valores de manera más eficiente.

También se debe tener en cuenta que las listas son fáciles de utilizar y permiten almacenar diferentes tipos de datos, mientras que los arrays de NumPy son especialmente útiles para trabajar con grandes cantidades de datos numéricos.

## Respuestas a las preguntas del reto 

**¿Qué diferencias observas en el tiempo de ejecución al realizar la misma operación con una lista y con un array, y a qué crees que se deben esas diferencias?**

Se observó que NumPy fue mas rapido que la lista Pytho, esto se debe a que permite realizar operaciones matematicas de manera mas eficiente y utilice mejor la memoria. 

**¿Cómo influye la forma en que cada estructura almacena los datos en memoria en el rendimiento obtenido durante la ejecución?**

 Las listas almacenan referencias a los elementos, mientras que los Arrays de NumPy guardan los datos numericos de una forma que facilita su procesamiento, esto permite que NumPy trabaje de manera mas eficiente y utilice mejor la memoria. 

**Si tuvieras que elegir una de estas estructuras para procesar grandes volúmenes de datos numéricos, ¿cuál seleccionarías y por qué?**

Seleccionaria los Array de Numpy porque permiten realizar operaciones matematocas en menos tiempo cianod se trabaja grandes cantidades de numeros. Sin embargo las listas tambien son muy utiles cuando se necesita manejar informacion de manera sencilla y flexible.

## 3. Actividad Parte 2 Gestion de Notas 

Descripcion del algoritmo 

Para esta parte del taller se desarrolló un programa que permite gestionar las notas de un grupo de estudiantes utilizando una lista de Python.

inicialmente se pide al usuario ingresar la cantoidad de notas y sobre ellas se realizan las siguientes operaciones:

- Calcula el promedio general de las notas.
- Identifica la nota más alta y la más baja.
- Cuenta cuántos estudiantes aprobaron y reprobaron.
- Modifica las notas: Si la calificación es menor a 3.0, se le suma 0.5, pero no puede superar el máximo de 5.0
- Muestra las notas originales y las modificadas.

## Justificacion de la estructura seleccionada 

Se utilizó una lista de Python porque permite almacenar las notas, recorrerlas y realizar diferentes cálculos de manera sencilla.

Para este ejercicio, la lista es una estructura adecuada porque facilita el manejo de las calificaciones y permite modificar los valores cuando sea necesario.

## conclusion

Con el desarrollo de este taller se pudo comprender que la elección de una estructura de datos puede influir en el tiempo que tarda un programa en realizar una operación.

En la comparación realizada, NumPy obtuvo un mejor tiempo de ejecución que las listas de Python al sumar 1 a un millón de números.

También se aprendió que las listas son útiles para manejar información de manera sencilla, mientras que NumPy resulta más conveniente para realizar operaciones matemáticas con grandes cantidades de datos.

Finalmente, mediante el algoritmo de gestión de notas se aplicaron conocimientos de listas, ciclos, condiciones y cálculos para organizar y analizar la información de los estudiantes.
