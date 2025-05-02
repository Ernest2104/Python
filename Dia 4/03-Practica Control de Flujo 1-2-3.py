# EJERCICIO 1
# num1 = input("Ingresa un número:") 
# num2 = input("Ingresa otro número:")

# if num1 > num2:
#   print(f"{num1} es mayor que {num2}")
# elif num2 > num1:
#   print(f"{num2} es mayor que {num1}")
# else:
#   print(f"{num1} y {num2} son iguales")

# EJERCICIO 2

# edad = 18
# tiene_licencia = True

# if (edad >= 18):
#   if tiene_licencia:
#       print ("Puedes conducir")
#   else:
#       print("No puedes conducir. Necesitas contar con una licencia")
# else:
#    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")

# EJERICIO 3

habla_ingles = False
sabe_python = False

if sabe_python and habla_ingles:
  print("Cumples con los requisitos para postularte")
elif not sabe_python and habla_ingles:
  print("Para postularte, necesitas saber programar en Python")
elif sabe_python and not habla_ingles:
  print("Para postularte, necesitas tener conocimientos de inglés")
else:
   print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")

