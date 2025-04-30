mi_texto = "Esta es una prueba"
resultado = mi_texto[-4]
resultado = mi_texto.index("a",11)
resultado = mi_texto.rindex ("a")

print(resultado)

texto = "ABCDEFGHIJKLM"
fragmento = texto[2:10:2]
print(fragmento)

texto = "Este es el texto de Federico"
resultado = texto.upper()
resultado = texto.lower()
resultado = texto.split()

print(resultado)

a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a, b, c, d])
print (e)

resultado = texto.find("es")
print (resultado)

resultado = texto.replace ("Federico", "Todos")
print (resultado)

#PROPIEDADES DE LOS STRINGS

# LISTAS
mi_lista = ["a", "b", "c"]
mi_lista2 = ["d", "e", "f"]
mi_lista3 = mi_lista + mi_lista2
#otra_Lista = ['Hola', 55, 6.1, True]
#resultado = len(otra_Lista)
#print (type(mi_lista))
#print (mi_lista + mi_lista2)
#mi_lista3[0] = 'alfa'
#mi_lista3.append('g')
eliminado = mi_lista3.pop(0)

print(mi_lista3)
print (eliminado)

lista4 = ['z', 'r', 'o', 'd', 'y']
lista4.sort()
lista4.reverse()
print (lista4)

# DICCIONARIOS

diccionario = {'c1':'valor1', 'c2':'valor2'}
print (type(diccionario))
print (diccionario)

resultado = diccionario['c1']
print(resultado)

cliente = {'nombre':'Juan', 'apellido':'Fuentes', 'peso':80, 'talla': 1.76}
consulta = cliente['apellido']
print(consulta)

dic = {'c1': 55, 'c2':[10,20,30], 'c3':{'s1':100, 's2':200}}
print(dic['c1'])
print(dic['c2'][0])
print(dic['c3'])
print(dic['c3']['s2'])

dic1 = {'c1':['a','b','c'], 'c2':['d','e','f']}
print(dic1['c2'][1].upper())

dic2 = {1:'a', 2:'b'}
dic2[3] = 'c'
print(dic2)
dic2[2] = 'B'
print(dic2)

print(dic2.keys())
print(dic2.values())
print(dic2.items())

# TUPLAS

mi_tuple = (1,2,3,4)
mi_tuple2 = (1,2,(10,20),4)
print(type(mi_tuple))
print(mi_tuple2[2])
mi_tuple2 = list(mi_tuple2)
print(type(mi_tuple2))

t = (1,2,3,1)

w,x,y,z = t

print(w,x,y,z)

# SET

mi_set = set([1,2,3,4,5])
print(type(mi_set))
print(mi_set)

otro_set = {1,2,3,4,5}
print(type(otro_set))
print(otro_set)

print(len(mi_set))
print(2 in mi_set)

s1 = set([1,2,3])
s2 = set([3,4,5])
s3 = s1.union(s2)
print(s3)

s1.add(4)
print(s1)
s1.remove(1)
print(s1)

# BOOLEANOS

var1 = True
var2 = False

print(type(var1))
print(var1)

numero = 5 > 2 + 3
print(type(numero))
print(numero)

lista = [1,2,3,4]
control = 5 in lista
print(type(control))
print(control)