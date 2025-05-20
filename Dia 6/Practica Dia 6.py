# APERTURA - LECTURA - CIERRE DE ARCHIVOS

mi_archivo = open('C:\\Users\\ernesto.villagra\\Desktop\\Python\\Dia 6\\Prueba.txt')

#print(mi_archivo.read())

#una_linea = mi_archivo.readline()
#print(una_linea)

#una_linea = mi_archivo.readline()
#print(una_linea)

una_linea = mi_archivo.readlines()
print(una_linea.pop())

mi_archivo.close()

# CREAR - ESCRIBIR - MODIFICAR ARCHIVOS

""" archivo = open('C:\\Users\\ernesto.villagra\\Desktop\\Python\\Dia 6\\Prueba.txt', 'r')
archivo.write('soy el nuevo texto')
archivo.close() """

archivo = open('C:\\Users\\ernesto.villagra\\Desktop\\Python\\Dia 6\\Prueba.txt', 'w')
archivo.write('Soy el nuevo texto')
print(archivo.read())
archivo.close()