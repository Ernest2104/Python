texto = input("Ingrese el texto que quiere analizar: ")

"""letra1 = input("Ingrese la primera letra: ").lower()
letra2 = input("Ingrese la segunda letra: ").lower()
letra3 = input("Ingrese la tercera letra: ").lower()"""

# CUANTAS VECES APARECE EN EL TEXTO CADA UNA DE LAS LETRAS
"""info1 = list(texto.lower())
print (f"La cantidad de veces que aparece la letra {letra1} es: {info1.count(letra1)}")
print (f"La cantidad de veces que aparece la letra {letra2} es: {info1.count(letra2)}")
print (f"La cantidad de veces que aparece la letra {letra3} es: {info1.count(letra3)}")"""

# CUANTAS PALABRAS HAY EN TOTAL
palabras = texto.split(" ")
print(f"La cantidad de palabras del texto son: {len(palabras)} palabras")
