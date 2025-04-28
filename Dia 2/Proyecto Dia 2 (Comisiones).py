nombre = input("¿Me puedes decir cual es tu nombre?: ")
venta = input("¿Me puedes informar el importe de tu venta?: ")

print (f"Ok {nombre}. Este mes ganaste $ {round(float(venta)*(13/100), 2)}")