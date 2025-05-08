print ("\n EJERCICIO 1: Para realizar el ejercicio a continuación, puedes optar por diferentes caminos. Si bien en programación el camino correcto es el que devuelve el resultado correcto, te animo a que intentes aplicar los conceptos de comprensión de listas para comenzar a afianzarlos para el futuro. ¡Pueden resultarte muy útiles en tu práctica profesional! Crea una lista valores_cuadrado formada por los números de la lista valores, elevados al cuadrado. valores = [1, 2, 3, 4, 5, 6, 9.5]\n")

valores = [1, 2, 3, 4, 5, 6, 9.5]

valores_cuadrado = [v**2 for v in valores]
print(valores_cuadrado)

print ("\n EJERCICIO 2: Crea una lista valores_pares formada por los números de la lista valores que (¡adivinaste!) sean pares. valores = [1, 2, 3, 4, 5, 6, 9.5]\n")

valores = [1, 2, 3, 4, 5, 6, 9.5]

valores_pares = [v for v in valores if v%2 == 0]
print(valores_pares)

print ("\n EJERCICIO 3: Para la siguiente lista de temperaturas en grados Fahrenheit, expresa estos mismos valores en una nueva lista de valores de temperatura en grados Celsius. La conversión entre tipo de unidades es la siguiente: °C = (°F - 32) * (5/9) o expresado de otro modo: (grados_fahrenheit-32)*(5/9) La lista de temperaturas es la siguiente: temperatura_fahrenheit = [32, 212, 275] Almacena esta nueva lista en una variable llamada grados_celsius\n")

temperatura_fahrenheit = [32, 212, 275]

grados_celsius = [(g-32)*(5/9) for g in temperatura_fahrenheit]
print (grados_celsius)

