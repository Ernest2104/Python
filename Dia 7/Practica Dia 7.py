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

piolin = Pajaro('amarillo', 'canario')

piolin.piar()
piolin.volar(50)
