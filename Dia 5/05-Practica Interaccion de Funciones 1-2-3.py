print('''\nCrea una función (lanzar_dados) que arroje dos dados al azar y devuelva sus resultados (la función debe retornar dos valores resultado, que se encuentren entre 1 y 6).
Proporciona el resultado de estos dos dados a una función que se llame evaluar_jugada (es decir, esta segunda función debe recibir dos argumentos) y que retorne un mensaje según la suma de estos valores:
Si la suma es menor o igual a 6:
"La suma de tus dados es {suma_dados}. Lamentable"
Si la suma es mayor a 6 y menor a 10:
"La suma de tus dados es {suma_dados}. Tienes buenas chances"
Si la suma es mayor o igual a 10:
"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
Pistas: utiliza el método choice o randint de la biblioteca random para elegir un valor al azar entre 1 y 6.\n''')

from random import randint, choice

def lanzar_dados():
  valor = randint(1,6)
  return valor

def evaluar_jugada(valor1, valor2):
  print(valor1, valor2)
  suma_dados = valor1 + valor2
  if suma_dados <= 6:
    return print(f"La suma de tus dados es {suma_dados}. Lamentable")
  elif suma_dados > 6 and suma_dados < 10:
    return print(f"La suma de tus dados es {suma_dados}. Tienes buenas chances")
  else: #Si la suma es mayor o igual a 10:
    return print(f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora")

print ("Tirando los dados...\n")
evaluar_jugada(lanzar_dados(), lanzar_dados())

print("""\nEJERCICIO 2: Crea una función llamada reducir_lista() que tome una lista (lista_numeros) como argumento, y devuelva la misma lista, pero eliminando duplicados (dejando un solo número si hay repetidos) y eliminando el valor más alto. El orden de los elementos puede modificarse.
Por ejemplo, si se le proporciona la lista [1,2,15,7,2] debe devolver [1,2,7].
Emplea la lista devuelta por la primera función y calcula el promedio de los valores de sus elementos, creando una nueva función llamada promedio().\n""")

lista_numeros = [1,2,15,7,2,3,20,5]

def reducir_lista(lista_num):
  lista_reducida = list(set(lista_num))[:-1]
  #return print(f"La lista sin duplicados y sin el mayor numero es la siguiente: {lista_reducida}\n")
  return lista_reducida

def promedio(lista_num):
  suma = sum(lista_num)
  cantidad = len(lista_num)
  return print(f"El promedio de los valores de la lista es el siguiente: {suma/cantidad}")

print(f"La lista sin duplicados y sin el mayor numero es la siguiente: {reducir_lista(lista_numeros)}\n")
promedio(reducir_lista(lista_numeros))

print('''\nEJERCICIO 3: Crea una función (llamada lanzar_moneda) que devuelva el resultado de lanzar una moneda (al azar). Dicha función debe poder devolver los resultados "Cara" o "Cruz", y no debe recibir argumentos para funcionar.
Crea una segunda función (llamada probar_suerte), que tome dos argumentos: el primero, debe ser el resultado del lanzamiento de la moneda. El segundo argumento, será una lista de números cualquiera (lista_numeros).
Si se le proporciona una "Cara", debe mostrar el mensaje al usuario: "La lista se autodestruirá", y eliminarla (devolverla como lista vacía []).
Si se le proporciona una "Cruz", debe imprimir en pantalla: "La lista fue salvada" y devolver la lista intacta.
Pistas: utiliza el método choice de la biblioteca random para elegir un elemento al azar de una secuencia.\n''')

lista_numeros = [1,2,3,4,5]

def lanzar_moneda():
  resultado = choice(('Cara', 'Cruz'))
  return resultado

def probar_suerte(resultado, lista):
  if resultado == 'Cara':
    print("La lista fue salvada")
    return lista
  else:
    print("La lista se autodestruirá")
    lista.clear()
    return lista
  

print(probar_suerte(lanzar_moneda(), lista_numeros))