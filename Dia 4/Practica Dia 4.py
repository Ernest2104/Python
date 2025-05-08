mi_bool = 5+5 == 18-8
mi_bool2 = 'blanco' == 'negro'

print(mi_bool)
print(mi_bool2)

# LOOP FOR

#lista = ['a', 'b', 'c']

#for letra in lista:
#  numero_letra = lista.index(letra) + 1
#  print(f"Letra {numero_letra}: {letra}")

lista = ['Pablo', 'Laura', 'Fede', 'Luis', 'Julia']

for nombre in lista:
  if nombre.startswith('l'):
    print(nombre)
  else:
    print('Nombre que no comienza con L')

numeros = [1,2,3,4,5]
mi_valor = 0

for numero in numeros:
  mi_valor = mi_valor + numero

  print(mi_valor)

palabra = 'python'

for letra in palabra:
  print(letra)

lista2 = [[1,2], [3,4], [5,6]]

for objeto in lista2:
  print(objeto)

for (a,b) in lista2:
  print(b)

dic = {'clave1': 'a', 'clave2': 'b', 'clave3': 'c'}

for item in dic:
  print(item)

for item in dic.items():
  print(item)

for item in dic.values():
  print(item)

for (a,b) in dic.items():
  print(a,b)

# LOOP WHILE

# monedas = 5

# while monedas > 0:
#   print(f"Tengo {monedas} monedas")
#   monedas -= 1
# else: print("No tengo mas dinero")

# respueta = 's'

# while respueta == 's':
#   respueta = input("Quieres seguir? (s/n)")
# else:
#   print("Gracias")

# name = input("Tu nombre: ")

# for letra in name:
#   if letra == 'r':
#     break
#   print(letra)

# print('\n')

# for letra in name:
#   if letra == 'r':
#     continue
#   print(letra)

# RANGE

for numero in range(1,5):
  print(numero)

lista = list(range(1,101, 2))
print(lista)

# ENUM
lista = ['a', 'b', 'c']
indice = 0

for item in enumerate(lista):
  print(item)

for indice, item in enumerate(lista):
  print(indice, item)

for indice, item in enumerate(range(50, 55)):
  print(indice, item)

mis_tuples = list(enumerate(lista))
print(mis_tuples)
print(mis_tuples[1][0])

# ZIP

nombre = ['Ana', 'Hugo', 'Valeria']
edades = [65,29,42]
ciudades = ['Lima', 'Madrid', 'Mexico']

combinados = list(zip(nombre, edades, ciudades))
print(combinados)

for nombre, edad, ciudad in combinados:
  print(f"{nombre} tiene {edad} años y vive en {ciudad}")

# MIN & MAX

menor = min(58,98,72,64,35)
mayor = max(58,98,72,64,35)
print(menor)
print(mayor)

lista = [58,98,72,64,35]
print(f"El menor es {min(lista)} y el mayor es {max(lista)}")

string = 'Carlos'
print(min(string.lower()))

dic = {'c1': 45, 'c2': 11}
print(min(dic))
print(min(dic.values()))

# RANDOM

from random import randint
from random import *

aleatorio = randint(1, 50)
print(aleatorio)

aleatorio2 = round(uniform(1, 5),2)
print(aleatorio2)

aleatorio3 = random()
print(aleatorio3)

colores = ['azul', 'rojo', 'verde', 'amarillo']
aleatorio4 = choice(colores)
print(aleatorio4)

numeros1 = list(range(5,50,5))
shuffle(numeros1)
print(numeros1)

# COMPRENSION DE LISTAS

metros = [10, 20, 30, 40, 50]
pies = [p*3.281 for p in metros]

print (pies)
