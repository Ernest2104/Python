print("EJERCICIO 1: Remueve los caracteres a la izquierda de nuestro texto principal: , : % _ # Utiliza el método lstrip(). Imprime el resultado en pantalla: ',:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#' Busca en la documentación acerca del funcionamiento del método solicitado para saber cómo actúa y cómo es su funcionamiento. Puedes utilizar variables intermedias si las necesitas.\n")

cadena = ',:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#'.lstrip(',:%_#')

print(cadena)

print("\nEJERCICIO 2: Añade el elemento 'naranja' como el cuarto elemento de la siguiente lista 'frutas', utilizando el método insert(): frutas = ['mango', 'banana', 'cereza', 'ciruela', 'pomelo'] Busca en la documentación acerca del funcionamiento del método solicitado para saber cómo actúa y cómo es su funcionamiento.\n")

frutas = ['mango', 'banana', 'cereza', 'ciruela', 'pomelo']

frutas.insert(3,'naranja')
print(frutas)

print("\nEJERCICIO 3: Verifica si los sets a continuación forman conjuntos aislados (es decir, que no tienen elementos en común), utilizando el método isdisjoint(). Almacena dicho resultado en la variable conjuntos_aislados: marcas_smartphones = {'Samsung', 'Xiaomi', 'Apple', 'Huawei', 'LG'} marcas_tv = {'Sony', 'Philips', 'Samsung', 'LG'} Busca en la documentación acerca del funcionamiento del método solicitado para saber cómo actúa y cómo es su funcionamiento.\n")

marcas_smartphones = {'Samsung', 'Xiaomi', 'Apple', 'Huawei', 'LG'} 
marcas_tv = {'Sony', 'Philips', 'Samsung', 'LG'}

conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)

print(conjuntos_aislados)




