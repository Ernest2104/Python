# APERTURA - LECTURA - CIERRE DE ARCHIVOS

""" mi_archivo = open('C:\\Users\\ernesto.villagra\\Desktop\\Python\\Dia 6\\Prueba.txt') """

#print(mi_archivo.read())

#una_linea = mi_archivo.readline()
#print(una_linea)

#una_linea = mi_archivo.readline()
#print(una_linea)

""" una_linea = mi_archivo.readlines()
print(una_linea.pop())

mi_archivo.close() """

# CREAR - ESCRIBIR - MODIFICAR ARCHIVOS

""" archivo = open('C:\\Users\\ernesto.villagra\\Desktop\\Python\\Dia 6\\Prueba.txt', 'r')
archivo.write('soy el nuevo texto')
archivo.close() """

""" archivo = open('C:\\Users\\ernesto.villagra\\Desktop\\Python\\Dia 6\\Prueba.txt', 'w')
archivo.write('Soy el nuevo texto')
print(archivo.read())
archivo.close() """

# DIRECTORIOS

import os

#ruta = os.getcwd() # -> Directorio actual
#ruta = os.chdir('Aqui va la ruta') # -> Cambiar directorio
#ruta = os.makedirs('ruta + nuevo directorio') # -> Crear nuevo directorio
#elemento = os.path.basename(ruta) # -> Devuelve el nombre del archivo
#elemento = os.path.dirname(ruta) # -> Devuelve la ruta archivo
#elemento = os.path.split() # -> Devuelve tupla con ruta y archivo

#os.removedirs('ruta con carpeta a eliminar') # eliminar carpeta

#print(ruta)

from pathlib import Path

base = Path.home()

print(base)

