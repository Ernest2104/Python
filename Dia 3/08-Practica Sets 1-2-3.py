# EJERCICIO 1

mi_set_1 = set([1, 2, "tres", "cuatro"])
mi_set_2 = set(["tres", 4, 5])

mi_set_3 = mi_set_1.union(mi_set_2)

print(mi_set_3)

# EJERCICIO 2

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}

eliminado = sorteo.pop()
print(eliminado)
print(sorteo)

#EJERCICIO 3

sorteo1 = set(["Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"])
sorteo1.add('Damián')
print(sorteo1)
