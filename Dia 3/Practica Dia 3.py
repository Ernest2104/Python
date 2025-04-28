mi_texto = "Esta es una prueba"
resultado = mi_texto[-4]
resultado = mi_texto.index("a",11)
resultado = mi_texto.rindex ("a")

print(resultado)

texto = "ABCDEFGHIJKLM"
fragmento = texto[2:10:2]
print(fragmento)

texto = "Este es el texto de Federico"
resultado = texto.upper()
resultado = texto.lower()
resultado = texto.split()

print(resultado)

a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a, b, c, d])
print (e)

resultado = texto.find("es")
print (resultado)

resultado = texto.replace ("Federico", "Todos")
print (resultado)

#PROPIEDADES DE LOS STRINGS

# LISTAS
mi_lista = ["a", "b", "c"]
mi_lista2 = ["d", "e", "f"]
mi_lista3 = mi_lista + mi_lista2
#otra_Lista = ['Hola', 55, 6.1, True]
#resultado = len(otra_Lista)
#print (type(mi_lista))
#print (mi_lista + mi_lista2)
#mi_lista3[0] = 'alfa'
#mi_lista3.append('g')
eliminado = mi_lista3.pop(0)

print(mi_lista3)
print (eliminado)

lista4 = ['z', 'r', 'o', 'd', 'y']
lista4.sort()
lista4.reverse()
print (lista4)