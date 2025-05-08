from random import randint

nombre = input("Ingresa tu nombre por favor: ")

aleatorio = randint(1, 100)
print(aleatorio)
contador = 1
while contador <= 8:
  numero = int(input(f"{nombre}, pensá un numero entre el 1 y el 100, tienes 8 intentos para adivinar (intento {contador}): "))
  if numero < 1 or numero > 100:
    print("El numero elegido debe estar en el rango 1-100")
  elif numero < aleatorio:
    print("El numero ingresado es menor")
  elif numero > aleatorio:
    print("El numero ingresado es mayor")
  else:
    print(f"Acertaste!!! Te ha tomado {contador} intento/s")
    break
  contador = contador + 1

if numero != aleatorio:
  print(f"\nLo siento se han terminado los intentos, el numero secreto es: {aleatorio}")

