""" 
-choice
-funciones:
  -pedir letra
  -validar letra
  -chequear letra
  -ver si ganó
-1ro.funciones y luego implementación    
"""
from random import choice

def obtener_palabra():
  lista_palabras = ['perro', 'gato', 'casa', 'celular', 'remera']
  palabra_secreta = choice(lista_palabras)
  print(palabra_secreta)
  return palabra_secreta

def pedir_letra():
  letra = input("Ingrese la letra: ")
  return letra

def validar_letra():
  letra_elegida = pedir_letra()
  while letra_elegida not in ('abcdefghijklmnñopqrstuvwxyz') or len(letra_elegida) != 1:
    print('No es una letra valida, ingrese otra.\n')
    letra_elegida = pedir_letra()
  #  continue
  else:
    return letra_elegida


def reemplazar_caracteres(palabra, caracter):
  nueva_palabra = ''.join([caracter if c != caracter else c for c in palabra])
  return nueva_palabra


def chequear_letra():
  lista_incorrectas = []
  palabra_correcta = ''
  aux_palabra = []
  vidas = 6
  pal_sec = obtener_palabra()
  print(f"La palabra secreta contiene ({len(pal_sec)} caracteres): {pal_sec.replace(pal_sec, '_'*len(pal_sec))}")
  print("Tiene un total de 6 intentos para adivinar\n")
  while vidas > 0:
    letra = validar_letra()
    if letra not in pal_sec:
      lista_incorrectas.append(letra)
      vidas -=1
      print(f"La letra '{letra}' no está en la palabra. Le quedan {vidas} intentos.\n")
      print(f"Las letras incorrectas ingresadas son: {lista_incorrectas}\n")
    else:
      print("La letra si está en la palabra")
      aux_palabra.append(''.join([letra if l == letra else '_' for l in pal_sec]))
      """ while '_' not in aux_palabra:
        aux_palabra = ''.join([letra if l == letra else '_' for l in pal_sec])
        print(aux_palabra) """
      print('_'.join(aux_palabra))

  print(f"Lo siento a perdido, la palabra era: {pal_sec}")

chequear_letra()
  

