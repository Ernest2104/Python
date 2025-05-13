dic = {'clave1': 100, 'clave2': 500}

a = dic.popitem()

print(a)
print(dic)

# FUNCIONES

def saludar_persona(nombre):
  '''
    Esta funcion sirve para saludar a las personas
  '''
  print("Hola " + nombre)

saludar_persona("Ernesto")

# RETURN

def multiplicar(num1, num2):
  return num1*num2

resultado = multiplicar(5,10)
print(resultado)

# FUNCIONES DINAMICAS

def chequear_3_cifras(numero):
  return numero in range(100, 1000)

suma = 345 + 34

resultado = chequear_3_cifras(suma)
print(resultado)

def chequear_3_cifras_lista(lista):
  lista_3_cifras = []
  for n in lista:
    if n in range(100, 1000):
      lista_3_cifras.append(n)
    else:
      pass
  return lista_3_cifras
#  return False

resultado1 = chequear_3_cifras_lista([2002,99,6020])
print(resultado1)

# EJEMPLOS FUNCIONES

precios_cafe = [('Capuchino', 1.5), ('Expresso',2.5), ('Moka', 1.9)]

def cafe_mas_caro(lista_precios):
  precio_mayor = 0
  cafe_mas_caro = ''

  for cafe, precio in lista_precios:
    if precio > precio_mayor:
      precio_mayor = precio
      cafe_mas_caro = cafe
    else:
      pass
  
  return (cafe_mas_caro, precio_mayor)

print(cafe_mas_caro(precios_cafe))

from random import shuffle

# INTERACCION ENTRE FUNCIONES

# Lista Inicial

palitos = ['-', '--', '---', '----']

# Mezclar palitos

def mezclar(lista):
  shuffle(lista)
  return lista

# Pedirle intento

def probar_suerte():
  intento = ''

  while intento not in ['1', '2', '3', '4']:
    intento = input("Elige un numero del 1 al 4: ")
  
  return int(intento)

# print(probar_suerte())

# Comprobar intento

def chequear_intento(lista, intento):
  if lista[intento - 1] == '-':
    print("A lavar los platos")
  else:
    print("Te has salvado")

  print(f"Te ha tocado {lista[intento - 1]}")

""" palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados, seleccion) """

# ARGUMENTOS INDEFINIDOS (*args)

def suma(*args):
  total = 0
  for arg in args:
    total = total + arg
  return total

print(suma(1,2,3))

# KWARGS (**kwargs)

def suma(**kwargs):
  total = 0

  for clave, valor in kwargs.items():
    print(f"{clave} = {valor}")
    total += valor
  return total

print(suma(x=3, y=5, z=2))

def prueba(num1, num2, *args, **kwargs):
  
  print(f"el primer valor es {num1}")
  print(f"el segundo valor es {num2}")

  for arg in args:
    print(f"arg = {arg}")

  for clave, valor in kwargs.items():
    print (f"{clave} = {valor}")

# prueba(15,50,100,200,300,400,x='uno',y='dos',z='tres')

args = 100,200,300,400
kwargs = {'x':'uno', 'y':'dos', 'z':'tres'}

prueba(15,50,args,kwargs)



