print('''\nCrea una función llamada suma_cuadrados que tome una cantidad indeterminada de argumentos numéricos, y que retorne la suma de sus valores al cuadrado.
Por ejemplo para los argumentos suma_cuadrados(1,2,3) deberá retornar 14 (1+4+9).\n''')

def suma_cuadrados(*args):
  for arg in args:
    suma = 0
    suma = suma + arg**2
  return suma

print(suma_cuadrados(2,2,2))