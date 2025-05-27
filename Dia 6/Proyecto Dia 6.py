import os
from os import system
from pathlib import Path

base = Path.home()
print(base)
ruta = Path(base, 'Desktop', 'Python', 'Recetas')
cant_recetas = 0

for i in Path(ruta).glob("**/*.txt"):
  cant_recetas +=1

""" system('cls')
usuario = input('Ingresa tu nombre: ')
print(f"¡Bienvenido {usuario}!")
print(f"Las recetas se encuentran en: {ruta}")
print(f"La cantidad de recetas son: {cant_recetas}\n") """

def menu():
  while True:
    print("MENÚ:\n")
    print("[1] - Leer receta")
    print("[2] - Crear receta")
    print("[3] - Leer categoría")
    print("[4] - Leer receta")
    print("[5] - Eliminar categoría")
    print("[6] - Finalizar programa")
    
    opcion = input("\nSeleccione una opción: ")
    
    match opcion:
      case '1':
        print("Has seleccionado la Opción 1")
        break
      case '2':
        print("Has seleccionado la Opción 2")
        break
      case '3':
        print("Has seleccionado la Opción 3")
        break
      case '4':
        print("Has seleccionado la Opción 4")
        break
      case '5':
        print("Has seleccionado la Opción 5")
        break
      case '6':
        print("Saliendo de la aplicación")
        break
      case _:
        system('cls')
        print("Opción inválida. Por favor, ingrese una opción correcta (1, 2, 3, 4, 5, 6).\n")

def obtener_categorias():
  categoria = os.listdir(ruta)
  return categoria

def obtener_recetas(ruta):
  recetas = os.listdir(ruta)
  return recetas

#menu()

def leer_receta():
  num_receta = 1
  print("Que categoria desea ver:")
  for c in obtener_categorias():
    print(f"{num_receta} - {c}")
    num_receta +=1
  cat_ele = input(f"Ingrese la categoria (1-{num_receta-1}): ")
  if cat_ele == "1":
    ruta_cat1 = Path(base, 'Desktop', 'Python', 'Recetas', obtener_categorias()[0])
    recetas_cat_1 = obtener_recetas(ruta_cat1)
    print(f"Que receta desea ver:\n1-{recetas_cat_1[0]} 2-{recetas_cat_1[1]}\n")
    receta_ele = input("Ingrese la receta que desea ver (1,2): ")
    if receta_ele == "1":
      print(Path(ruta_cat1, recetas_cat_1[0]).read_text())
    elif receta_ele == "2":
      print(Path(ruta_cat1, recetas_cat_1[1]).read_text())
  elif cat_ele == "2":
    ruta_cat2 = Path(base, 'Desktop', 'Python', 'Recetas', obtener_categorias()[1])
    recetas_cat_2 = obtener_recetas(ruta_cat2)
    print(f"Que receta desea ver:\n1-{recetas_cat_2[0]} 2-{recetas_cat_2[1]}\n")
    receta_ele = input("Ingrese la receta que desea ver (1,2): ")
    if receta_ele == "1":
      print(Path(ruta_cat2, recetas_cat_2[0]).read_text())
    elif receta_ele == "2":
      print(Path(ruta_cat2, recetas_cat_2[1]).read_text())

leer_receta()

  

