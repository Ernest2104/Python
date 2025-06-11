print("""EJERICIO 1: Si la clase Hija ha heredado de su padre la forma de reir, y de su madre la vocación, y hoy tienen el mismo trabajo en la Fiscalía, crea la herencia múltiple que le permita a esta clase heredar correctamente de Padre y Madre.Completa el código suministrado a continuación para lograrlo.\n""")

class Padre():
  def trabajar(self):
    print("Trabajando en el Hospital")
  def reir(self):
    print("Ja ja ja!")

class Madre():
  def trabajar(self):
    print("Trabajando en la Fiscalía")

class Hija(Madre, Padre):
  pass

hija1 = Hija()

hija1.reir()
hija1.trabajar()

print("""\nEJERCICIO 2: "El ornitorrinco es una de las criaturas más raras del mundo: aunque es un mamífero, pone huevos; y amamanta a sus crías pero no tienen mamas." (National Geographic)
Crea una clase Ornitorrinco que herede de otras clases: Vertebrado, Pez, Reptil, Ave y Mamifero, tal que "construyas" un animal que tiene los siguientes métodos y atributos:

- poner_huevos()
- tiene_pico = True
- vertebrado = True
- venenoso = True
- nadar()
- caminar()
- amamantar()\n""")



