print('***EJERCICIO 1***')

alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]

for alumno in alumnos_clase:
  print(f"Hola {alumno}")

print('\n')
print('***EJERCICIO 2***')


lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0

for numero in lista_numeros:
  suma_numeros = suma_numeros + numero

print(suma_numeros)

print('\n')
print('***EJERCICIO 3***')

lista_numeros1 = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for num in lista_numeros1:
  if (num%2 == 0 or num == 0):
    suma_pares = suma_pares + num
  else:
    suma_impares = suma_impares + num

print(suma_pares)
print(suma_impares)
