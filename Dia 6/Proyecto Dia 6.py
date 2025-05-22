from os import system
from pathlib import Path
#import glob

base = Path.home()
print(base)
ruta = Path(base, 'Desktop', 'Python', 'Recetas')
cant_recetas = 0

for i in Path(ruta).glob("**/*.txt"):
  cant_recetas +=1

system('cls')
usuario = input('Ingresa tu nombre: ')
print(f"¡Bienvenido {usuario}!")
print(f"Las recetas se encuentran en: {ruta}")
print(f"La cantidad de recetas son: {cant_recetas}\n")

print("MENÚ:\n")
print("[1] - Leer receta")
print("[2] - Crear receta")
print("[3] - Leer categoría")
print("[4] - Leer receta")
print("[5] - Eliminar categoría")
print("[6] - Finalizar programa")

opcion = input("Ingrese su opción: ")

while opcion != 6:
  match opcion:
    case 1:
      print("1")
    case 2:
      print("")

    case 3:


