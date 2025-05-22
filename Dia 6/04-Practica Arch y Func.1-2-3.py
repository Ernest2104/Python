print("""\nEJERCICIO 1: Crea una función llamada abrir_leer() que abra (open) un archivo indicado como parámetro, y devuelva su contenido (read).\n""")

def abrir_leer(archivo):
  arch1 = open(archivo, 'r')
  return arch1.read()

print(abrir_leer('texto.txt'))

print("""\nEJERCICIO 2: Crea una función llamada sobrescribir() que abra (open) un archivo indicado como parámetro, y sobrescriba cualquier contenido anterior por el texto "contenido eliminado"\n""")

def sobrescribir(archivo):
  arch2 = open(archivo, 'w')
  return arch2.write("contenido eliminado")

sobrescribir('prueba.txt')
print(abrir_leer('prueba.txt'))

print("""\nEJERCICIO 3: Crea una función llamada registro_error() que abra (open) un archivo indicado como parámetro, y lo actualice añadiendo una línea al final que indique "se ha registrado un error de ejecución". Finalmente, debe cerrar el archivo abierto.\n""")

def registro_error(archivo):
  arch3 = open(archivo, 'a')
  return arch3.write('\nse ha registrado un error de ejecución')

registro_error('texto.txt')
print(abrir_leer('texto.txt'))