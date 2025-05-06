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

monedas = 5

while monedas > 0:
  print(f"Tengo {monedas} monedas")
  monedas -= 1
else: print("No tengo mas dinero")

respueta = 's'

while respueta == 's':
  respueta = input("Quieres seguir? (s/n)")
else:
  print("Gracias")

name = input("Tu nombre: ")

for letra in name:
  if letra == 'r':
    break
  print(letra)

print('\n')

for letra in name:
  if letra == 'r':
    continue
  print(letra)
