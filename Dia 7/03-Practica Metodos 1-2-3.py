print("""\nEJERCICIO 1: Crea una clase Perro. Dicho perro debe poder ladrar. Crea el método ladrar() y ejecútalo en una instancia de Perro. Cada vez que ladre, debe mostrarse en pantalla "Guau!".\n""")

class Perro:

  def ladrar(self):
    print('Guau')

kyra = Perro()

kyra.ladrar()

print("""\nEJERCICIO 2: Crea una clase llamada Mago, y crea un método llamado lanzar_hechizo() (deberá imprimir "¡Abracadabra!"). Crea una instancia de Mago en el objeto merlin, y haz que lance un hechizo.\n""")

class Mago:
  
  def lanzar_hechizo(self):
    print("¡Abracadabra!")

merlin = Mago()
merlin.lanzar_hechizo() 

print("""\nEJERCICIO 3: Crea una instancia de la clase Alarma, que tenga un método llamado postergar(cantidad_minutos). El método debe imprimir en pantalla el mensaje: "La alarma ha sido pospuesta {cantidad_minutos} minutos"\n""")

class Alarma():

  def postergar(self, cantidad_minutos):
    print("La alarma ha sido pospuesta {} minutos".format(cantidad_minutos))

alarma1 = Alarma()

alarma1.postergar(10)

print("""\nEJERCICIO 3: \n""")