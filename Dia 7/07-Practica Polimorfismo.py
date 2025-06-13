print("""\nEJERCICIO 1: La función incorporada en Python len() tiene un comportamiento polimórfico, ya que calcula el largo de un objeto en función de su tipo (strings, listas, tuples, entre otros), devolviendo la cantidad de items o caracteres que lo componen.

Crea un iterador que recorra los siguientes objetos: palabra, lista, tupla y muestre en pantalla (print()) para cada uno de ellos su longitud con la función len().

Puedes recordar cómo implementar la función len() siguiente enlace: https://docs.aws.amazon.com/es_es/redshift/latest/dg/r_LEN.html\n""")

""" def iterador(objeto):
  for e in objeto:
    return len(e)

print(iterador(("apple", "banana", "cherry"))) """

palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

for dato in [palabra, lista, tupla]:
    print(len(dato))

"""\nEJERICIO 2: Cuentas con tres clases de personajes en un juego, los cuales cuentan con sus métodos de ataque específicos.
Crea un iterador que logre un ataque conjugado en el siguiente orden: Arquero, Mago, Samurai, llamando al método atacar() de cada uno de los personajes. Deberás crear instancias de cada una de las clases anteriores para construir un iterable (una lista llamada personajes) que pueda recorrese en dicho orden.\n"""

class Arquero():
  def atacar(self):
     print("Ataque de Arquero")

class Mago():
  def atacar(self):
     print("Ataque de Mago")

class Samurai():
  def atacar(self):
     print("Ataque de Samurai")


