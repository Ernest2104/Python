# POO - CLASES

""" class Pajaro:
  pass

mi_pajaro = Pajaro()
otro_pajaro = Pajaro()

print(mi_pajaro)
print(otro_pajaro)
print(type(mi_pajaro)) """

# POO - ATRIBUTOS

class Pajaro:

  alas = True #atributo de clase

  def __init__(self, color, especie):
    self.color = color
    self.especie = especie

mi_pajaro = Pajaro('negro', 'cuervo')
print(mi_pajaro.color)
print(mi_pajaro.especie)

print(f"mi pajaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}")

print(Pajaro.alas)
print(mi_pajaro.alas)

# METODOS

class Pajaro:

  alas = True #atributo de clase

  def __init__(self, color, especie):
    self.color = color
    self.especie = especie
  
  def piar(self):
    print('pio, mi color es {}'.format(self.color))

  def volar(self, metros):
    print(f"El pajaro ha volado {metros} metros")
    self.piar()

  def pintar_negro(self):
    self.color = 'negro'
    print(f"Ahora el pajaro es {self.color}")
  
  @classmethod
  def poner_huevos(cls, cantidad):
    print(f"Puso {cantidad} huevos")
    cls.alas = False

  @staticmethod
  def mirar():
    print("El pajaro mira")

""" piolin = Pajaro('amarillo', 'canario')

piolin.piar()
piolin.volar(50)

piolin.alas = False
print(piolin.alas) """

Pajaro.poner_huevos(3)
print(Pajaro.alas)

# TIPOS DE METODOS

Pajaro.mirar()

#HERENCIA

class Animal():
  def __init__(self, edad, color):
    self.edad = edad
    self.color = color

  def nacer(self):
    print('Este animal ha nacido')

  def hablar(self):
    print('Este animal emite un sonido')

  
class Pajaro(Animal):

  def __init__(self, edad, color, altura_vuelo):
    """ self.edad =edad
    self.color = color """
    super().__init__(edad, color)
    self.altura_vuelo = altura_vuelo

  def hablar(self):
    print("Pio")

  def volar(self, metros):
    print(f"El pajaro vuela {metros} metros")

piolin = Pajaro(3, 'Amarillo', 30)
mi_animal = Animal(5, 'negro')

piolin.nacer()

piolin.hablar()

piolin.volar(100)

# HERENCIA MULTIPLE 

class Padre():
  def hablar(self):
    print("Hola")

class Madre():
  def reir(self):
    print("JaJa")
  def hablar(self):
    print("Que tal")

class Hijo(Madre, Padre):
  pass

class Nieto(Hijo):
  pass

mi_nieto = Nieto()

mi_nieto.hablar()

print(Nieto.__mro__)

#mi_nieto.reir()