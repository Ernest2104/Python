print("\nEJERCICIO 1: Crea una función llamada potencia que tome dos valores numéricos como argumentos. Deberá devolver el número que resulte de resolver una potencia, utilizando el primer número como base, y el segundo como exponente.\n")

def potencia(base, exp):
  return base**exp

resultado = potencia(3, 4)

print(resultado)

print("\nEJERCICIO 2: Crea una función llamada usd_a_eur que tome como único parámetro un valor numérico (un monto en dólares estadounidenses), y devuelva como resultado el monto equivalente en euros. A fines de este ejemplo, tomaremos la conversión 1 USD = 0.85 EUR. \n")

def usd_a_eur(dolares):
  #dolares = float(input("Ingrese el valor en dolares que desea convertir: "))
  return dolares*0.85

conversion = usd_a_eur(100)

print(f"El valor equivalente es: {conversion} EUR")

print('''\nEJERCICIO 3: Crea una función llamada invertir_palabra que tome los caracteres de una palabra dada como argumento, invierta el orden de sus caracteres y los devuelva de ese modo y en mayúsculas.
Por ejemplo, si le proporcionamos la palabra "Python", deberá devolver: "NOHTYP"
También, deberás crear una variable llamada palabra, que contenga el string que tú prefieras, para sumisitrarle como argumento a la función creada.\n''')

def invertir_palabra(palabra):
  return palabra[::-1].upper()
  
invertida = invertir_palabra('Ernesto')
print(invertida)

