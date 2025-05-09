print("EJERCICIO 1: Crea una lista formada por todos los números desde el 2500 al 2585 (inclusive). Almacena dicha lista en la variable mi_lista.\n")

# mi_lista = list(range(2500, 2586))
# print(mi_lista)

print("EJERCICIO 2: Utilizando la función range(), crea en una única linea de código una lista formada por todos los números múltiplos de 3 desde el 3 al 300 (inclusive). Almacena dicha lista en la variable mi_lista.")

# mi_lista = list(range(3, 301, 3))
# print(mi_lista)

print("EJERCICIO 3: Utiliza la función range() y un loop para sumar los cuadrados de todos los números del 1 al 15 (inclusive). Almacena el resultado en una variable llamada suma_cuadrados. Para ello: Crea un rango de valores que puedas recorrer en un loop para cada uno de estos valores, calcula su valor al cuadrado (potencia de 2). Puede que necesites crear variables intermedias (de manera opcional). Suma todos los valores al cuadrado obtenidos. Acumula la suma en la variable suma_cuadrados.\n")

suma_cuadrados = 0
rango = list(range(1,16))

for num in rango:
  suma_cuadrados = suma_cuadrados + num**2
print(f"El resultado es: {suma_cuadrados}")

# 1 + 4 + 9 + 16 + 25 + 36 + 49 + 64 + 81 + 100 + 121 + 144 + 169 + 196 + 225