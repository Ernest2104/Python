texto = input("Ingrese el texto que quiere analizar: ")

letra1 = input("Ingrese la primera letra: ").lower()
letra2 = input("Ingrese la segunda letra: ").lower()
letra3 = input("Ingrese la tercera letra: ").lower()

print("\n")
print("CUANTAS VECES APARECE EN EL TEXTO CADA UNA DE LAS LETRAS")
info1 = list(texto.lower())
print (f"La cantidad de veces que aparece la letra '{letra1}' es: {info1.count(letra1)}")
print (f"La cantidad de veces que aparece la letra '{letra2}' es: {info1.count(letra2)}")
print (f"La cantidad de veces que aparece la letra '{letra3}' es: {info1.count(letra3)}")

print("\n")
print("CUANTAS PALABRAS HAY EN TOTAL")
palabras = texto.split(" ")
print(f"La cantidad de palabras del texto son: {len(palabras)}")

print("\n")
print("CUAL ES LA PRIMERA LETRA Y CUAL ES LA ULTIMA")
#primera_letra = texto[0]
print ("La primera letra de la frase es la: '{}'".format(texto[0]))
print ("La última letra de la frase es la: '{}'".format(texto[-1]))

print("\n")
print("PALABRAS EN ORDEN INVERSO")
palabras.reverse()
texto_invertido = " ".join(palabras)
print ("La frase con las palabras invertidas es: {}".format(texto_invertido))

print("\n")
print("APARECE LA PALABRA 'PYTHON' EN EL TEXTO")
esta_palabra = "Python" in texto
dic = {True: "si", False: "no"}
print(f"La palabra 'Python'{dic[esta_palabra]} se encuentra en el texto")

