print("\nEJERCICIO 1: Crea una función (todos_positivos) que devuelva True si todos los valores de una lista (lista_numeros) son positivos, y False si al menos uno de los valores es negativo.\n")

def todos_positivos(lista_numeros):
  for n in lista_numeros:
    if n < 0:
      return False
    else:
      pass
  return True

resultado = todos_positivos([2,3,-4,10])
print(resultado)

print("\nEJERCICIO 2: Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros) siempre y cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma.\n")

def suma_menores(lista_numeros):
  suma = 0
  for n in lista_numeros:
    if n in range(0,1000):
      suma = suma + n
    else:
      pass
  return suma

resultado = suma_menores([2,3,-4,20])
print("El resultado de la suma es: {}".format(resultado))

print("\nEJERCICIO 3: Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen en una lista (lista_numeros), y devuelva el resultado de dicha suma.\n")

def cantidad_pares(lista_numeros):
  cuenta_pares = 0
  for n in lista_numeros:
    if n%2 == 0:
      cuenta_pares +=1
    else:
      pass
  return cuenta_pares

resultado = cantidad_pares([2,3,-4,20,8,23])
print("La cantidad de pares de la lista es: {}".format(resultado))