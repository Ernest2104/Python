print("""\nEJERCICIO 1: Crea una función llamada devolver_distintos() que reciba 3 integers como parámetros. 
Si la suma de los 3 numeros es mayor a 15, va a devolver el número mayor. 
Si la suma de los 3 numeros es menor a 10, va a devolver el número menor. 
Si la suma de los 3 números es un valor entre 10 y 15(incluidos) va a devolver el número de valor intermedio.\n""")

def devolver_distintos(int1, int2, int3):
  lista_num = []
  suma = int1 + int2 + int3
  lista_num.extend([int1, int2, int3])
  if suma > 15:
    print(f"El mayor de los 3 numeros es: {max(lista_num)}")
  elif suma < 10:
    print(f"El menor de los 3 numeros es: {min(lista_num)}")
  else:
    lista_num.sort() 
    print(f"El numero de valor intermedio es: {lista_num[1]}")

# devolver_distintos(4, 2, 0)

print("""\nEJERCICIO 2: Escribe una función (puedes ponerle cualquier nombre que quieras) que reciba cualquier palabra como parámetro, y que devuelva todas sus letras únicas (sin repetir) pero en orden alfabético.Por ejemplo si al invocar esta función pasamos la palabra "entretenido", debería devolver ['d', 'e', 'i', 'n', 'o', 'r', 't']\n""")

def palabra_letras(palabra):
  letras = list(set(palabra))
  letras_ord = sorted(letras)
  return letras_ord

# print(f"Lista de letras ordenadas y sin repetidas: {palabra_letras("eugenia")}")

print("""\nEJERCICIO 3: Escribe una función que requiera una cantidad indefinida de argumentos. Lo que hará esta función es devolver True si en algún momento se ha ingresado al numero cero repetido dos veces consecutivas.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> False
\n""")

def cero_repetido(*args):
  cont_0 = 0
  for arg in args:
    if cont_0 + 1 == len(args):
      return False
    elif args[cont_0] == 0 and args[cont_0 + 1] == 0:
      return True
    else:
      cont_0 +=1
  
  return False
  
#print(cero_repetido(5,6,1,9,3,5,0,0,7,3,2,6))

print("""\nEJERCICIO 4: Escribe una función llamada contar_primos() que requiera un solo argumento numérico.
Esta función va a mostrar en pantalla cuántos números primos hay en el rango que va desde cero hasta ese número incluido, y va a devolver la cantida de números primos que encontró. Aclaración, por convención el 0 y el 1 no se consideran primos.\n""")

def es_primo(numero):
  for n in range(2, numero):
    if numero % n == 0:
      return False
  return True

def contar_primos(num):
  primos = []
  contador = 0
  for n in range(0,num):
    if n > 1:
      if es_primo(n):
        primos.append(n)
        contador +=1
    else:
      continue
  return primos, contador

#print(f"Los numeros primos en el rango son: {contar_primos(100)[0]}")
#print(f"La cantidad de numeros en el rango son: {contar_primos(100)[1]}")
