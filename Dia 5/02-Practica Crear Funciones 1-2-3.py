print("EJERCICIO 1: Declara una función llamada saludar, que cada vez que sea llamada imprima en pantalla '¡Hola mundo!'\n")

def saludar():
  print("Hola mundo!")

saludar()

print("\nEJERCICIO 2: Declara una función llamada bienvenida, que tome como argumento el nombre de una persona, y que cada vez que sea llamada imprima en pantalla '¡Bienvenido {nombre_persona}!' Para probar su funcionamiento, crea la variable nombre_persona, y almacena dentro de la misma el nombre que prefieras.\n")

def bienvenida(nombre_persona):
  print("¡Bienvenido/a " + nombre_persona + "!")

bienvenida("Ernesto")

print("\nEJERCICIO 3: Declara una función llamada cuadrado, que tome como argumento un número cualquiera, y que cada vez que sea llamada, imprima en pantalla el cuadrado de dicho número (es decir, la potencia 2 del valor). El nombre del argumento que debe tomar dicha función es un_numero. Crea dicha variable y asígnale un número cualquiera para probar la función creada.\n")

def cuadrado(un_numero):
  print(f"El cuadrado de {un_numero} es: {un_numero**2}")

cuadrado(3)



