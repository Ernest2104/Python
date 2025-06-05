print("""\nEJERICIO 1: Crea un método estático respirar() para la clase Mascota. Cuando se llame, debe imprimir en pantalla "Inhalar... Exhalar"\n""")

class Mascota():

  @staticmethod
  def respirar():
    print("Inhalar... Exhalar")

Mascota.respirar()

print("""\nEJERCICIO 2: Crea un método de clase revivir() que actúa sobre el atributo de clase vivo de la clase Jugador, estableciéndolo en True cada vez que es invocado. El valor predeterminado del atributo vivo, debe ser False.\n""")

class Jugador():

  vivo = False

  @classmethod
  def revivir(cls):
    cls.vivo = True

Jugador.revivir()

print(Jugador.vivo)