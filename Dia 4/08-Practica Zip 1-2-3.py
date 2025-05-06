print("EJERCICIO 1: Muestra en pantalla frases como la del siguiente ejemplo: 'La capital de Alemania es Berlín' Utiliza la función zip, loops, y las siguientes listas de países y capitales para resolverlo rápida y eficientemente. capitales = ['Berlín', 'Tokio', 'París', 'Helsinki', 'Ottawa', 'Canberra'] paises = ['Alemania', 'Japón', 'Francia', 'Finlandia', 'Canadá', 'Australia']\n")

capitales = ['Berlín', 'Tokio', 'París', 'Helsinki', 'Ottawa', 'Canberra'] 
paises = ['Alemania', 'Japón', 'Francia', 'Finlandia', 'Canadá', 'Australia']

pais_capital = list(zip(paises, capitales))

for pais, capital in pais_capital:
  print("La capital de {} es {}: ".format(pais, capital))

print("\nEJERCICIO 2: Crea un objeto zip formado a partir de listas, de un conjunto de marcas y productos que tú prefieras, dentro de la variable mi_zip. marcas = productos =\n")

productos = ['auto', 'gaseosa', 'celular', 'monitor']
marcas = ['Fiat', 'Pepsi', 'Tecno', 'Samsung']
mi_zip = list(zip(productos, marcas))
print(mi_zip)

print("\nEJERCICIO 3: Crea el zip con las traducciones de los números del 1 al 5 en español, portugués e inglés (en el mismo orden), y convierte el objeto generado en una lista almacenada en la variable numeros: uno / um / one, dos / dois / two, tres / três / three, cuatro / quatro / four, cinco / cinco / five. El resultado deberá seguir la estructura: [('uno', 'um', 'one'), ('dos', 'dois', 'two'), ... ]\n")

esp = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
por = ['um', 'dois', 'três', 'quatro', 'cinco']
ing = ['one', 'two', 'three', 'four', 'five']

numeros = list(zip(esp, por, ing))
print(numeros)
