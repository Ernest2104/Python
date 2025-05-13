print('''\nEJERCICIO 1: Crea una función llamada suma_cuadrados que tome una cantidad indeterminada de argumentos numéricos, y que retorne la suma de sus valores al cuadrado.
Por ejemplo para los argumentos suma_cuadrados(1,2,3) deberá retornar 14 (1+4+9).\n''')

def suma_cuadrados(*args):
  suma = 0
  for arg in args:
    suma = suma + arg**2
  return suma

print("La suma de los valores al cuadrado es: {}".format(suma_cuadrados(2,2,2)))

print("""\nEJERCICIO 2: Crea una función llamada suma_absolutos, que tome un conjunto de argumentos de cualquier extensión, y retorne la suma de sus valores absolutos (es decir, que tome los valores sin signo y los sume, o lo que es lo mismo, los considere a todos -negativos y positivos- como positivos).\n""")

def suma_absolutos(*args):
  suma = 0
  for arg in args:
    suma = suma + abs(arg)
  return suma

print(f"La suma absoluta de los numeros es: {suma_absolutos(2,-5,0,1,-7)}")

print("""\nEJERCICIO 3: Crea una función llamada numeros_persona que reciba, como primer argumento, un nombre, y a continuación, una cantidad indefinida de números.
La función debe devolver el siguiente mensaje:'{nombre}, la suma de tus números es {suma_numeros}'\n""")

def suma_numeros(*args):
  suma = 0
  for arg in args:
    suma = suma + arg
  return suma

def numeros_persona(nombre, numeros):
  return print(f"{nombre}, la suma de tus números es {numeros}")

numeros_persona('Ernesto', suma_numeros(2,3,4,10,100))