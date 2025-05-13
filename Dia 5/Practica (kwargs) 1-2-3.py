print("""\nEJERCICIO 1: Crea una función llamada cantidad_atributos que cuente la cantidad de parámetros que se entregan, y devuelva esa cantidad como resultado.\n""")

def cantidad_atributos(**kwargs):
  cantidad = 0
  for clave in kwargs.keys():
    cantidad +=1

  return cantidad

print(cantidad_atributos(x=3, y=5, z=2))

print("""\nEJERCICIO 2: Crea una función llamada lista_atributos que devuelva en forma de lista los valores de los atributos entregados en forma de palabras clave (keywords). La función debe preveer recibir cualquier cantidad de argumentos de este tipo.\n""")

def lista_atributos(**kwargs):
  lista = []
  for valor in kwargs.values():
    lista.append(valor)
  return lista

print(lista_atributos(x=3, y=5, z=2))

print("""\nEJERCICIO 3: Crea una función llamada describir_persona, que tome como parámetros su nombre y luego una cantidad indetermida de argumentos. Esta función deberá mostrar en pantalla:

Características de {nombre}:
{nombre_argumento}: {valor_argumento}
{nombre_argumento}: {valor_argumento}
etc...
Por ejemplo:
describir_persona("María", color_ojos="azules", color_pelo="rubio")
Devolverá en pantalla:
Características de María:
color_ojos: azules
color_pelo: rubio \n""")

def describir_persona(nombre, **kwargs):
  print("Caracteristicas de {}".format(nombre))
  for clave, valor in kwargs.items():
    print(f"{clave}: {valor}")

describir_persona("Ernesto", color_ojos="marrones", color_pelo="negro")
