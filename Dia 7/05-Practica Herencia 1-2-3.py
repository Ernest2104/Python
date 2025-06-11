print("""\nEJERICIO 1: Crea una clase llamada Persona, que tenga los siguientes atributos de instancia: nombre, edad. Crea otra clase, Alumno, que herede de la primera estos atributos.\n""")

class Persona():
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

class Alumno(Persona):
  pass

alumno_1 = Alumno('Ernesto Villagra', 48)

print(alumno_1.edad)
  
print("""\nEJERICIO 2: Crea una clase llamada Mascota, que tenga los siguientes atributos de instancia: edad, nombre, cantidad_patas. Crea otra clase, Perro, que herede de la primera sus atributos.\n""")

class Mascota():
  def __init__(self, edad, nombre, cantidad_patas):
    self.nombre = nombre
    self.edad = edad
    self.cantidad_patas = cantidad_patas

class Perro(Mascota):
  pass

perro_1 = Perro('Kyra', 4, 4)
perro_2 = Perro('Brida', 11, 4)

print(perro_1.nombre, perro_1.edad, perro_1.cantidad_patas)

print("""\nEJERICIO 3: Crea una clase llamada Vehiculo, que contenga los métodos acelerar() y frenar() (puedes dejar el código de los métodos en blanco con pass). Crea una clase llamada Automovil que herede estos métodos de Vehiculo.\n""")

class Vehiculo():

  def acelerar(self):
    print("Estoy pisando el acelerador")

  def frenar(self):
    pass

class Automovil(Vehiculo):
  pass

ford = Automovil()

ford.acelerar()