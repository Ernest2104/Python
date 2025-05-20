print('''\nEJERCICIO 1: Abre el archivo texto.txt e imprime su contenido.
Nota: el archivo se encuentra guardado en la misma carpeta donde se aloja tu código\n''')

archivo = open('C:\\Users\\ernesto.villagra\\Desktop\\Python\\Dia 6\\texto.txt')

print(archivo.read())
archivo.close()

print("""\nEJERCICIO 2: Imprime la primera línea del archivo texto.txt
No olvides abrir el archivo y cerrarlo luego de ejecutar tu código.
Nota: el archivo se encuentra guardado en la misma carpeta donde se aloja tu código\n""")

archivo = open('C:\\Users\\ernesto.villagra\\Desktop\\Python\\Dia 6\\texto.txt')
print(archivo.readline())
archivo.close()

print("\nEJERCICIO 3: Abre el archivo texto.txt e imprime únicamente la segunda línea.\n")

archivo = open('C:\\Users\\ernesto.villagra\\Desktop\\Python\\Dia 6\\texto.txt')
print(archivo.readlines()[1])
archivo.close()
