print("EJERCICIO 1: Crea un Loop While que se imprima en pantalla los números del 10 al 0, uno a la vez.\n")

numero = 0

while numero <= 10:
  print(numero)
  numero +=1

print("\nEJERICIO 2: Crea un Loop While que reste de uno en uno los números desde el 50 al 0 (ambos números incluídos) con las siguientes condiciones adicionales: - Si el número es divisible por 5, mostrar dicho número en pantalla (¡recuerda que aquí puedes utilizar la operación módulo dividiendo por 5 y verificando el resto!) - Si el número no es divisible por 5, continuar ejecutando el loop sin mostrar el valor en pantalla (no te olvides de seguir restando para que el programa no corra infinitamente).\n")

number = 50

while number > 0:
  if (number%5 == 0):
    print(number)
  number -=1

print("\nCrea un loop For a lo largo de la siguiente lista de números, imprimiendo en pantalla cada uno de sus elementos, e interrumpe el flujo en el momento que encuentres un valor negativo: lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3] No debes cambiar el orden de la lista.\n")

lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for num in lista_numeros:
  if num >= 0:
    print(num)
  else: break
