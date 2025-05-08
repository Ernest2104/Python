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

resultado = chequear_3_cifras(65)
print(resultado)