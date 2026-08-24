import os
os.system("cls")

# La Batalla de Invernalia 
# Contexto de la misión: El Rey de la Noche se acerca a Invernalia con su ejército de Caminantes Blancos. Jon Snow y Daenerys Targaryen te han nombrado su Consejero Táctico. Tu deber es crear un programa en Python que evalúe si las fuerzas aliadas sobrevivirán a la noche, calculando el tamaño del ejército, el armamento disponible y las condiciones climáticas.
# Requisitos del programa:
# 1. Define las siguientes CONSTANTES al inicio de tu código:
# •	VIDRIAGON_POR_SOLDADO: Cada soldado necesita exactamente 3 dagas de vidriagón para ser efectivo.
# •	TEMPERATURA_CONGELACION: El punto crítico donde los soldados humanos pierden eficacia es a los -15 grados.
VIDRIAGON_POR_SOLDADO = 3
TEMPERATURA_CONGELACION= -15
# 2. Solicita al usuario que ingrese las siguientes VARIABLES (o defínelas tú mismo en el código):
soldados_Inmaculados=int( input("ingrese la cantidad de soldados inmaculados: "))
soldados_Dothrakis =int(input("cantidad de soldados: "))
Cantidad_dagas =int(input ("cantidad de dagas:"))
Temperatura_actual = float(input("ingrese la temperatura: "))
Daenerys_dragones  = input( "daenerys llevo sus dragones? si / no: ")
# 3. Crea las VARIABLES AUXILIARES y usa OPERADORES MATEMÁTICOS para calcular:
# •	Ejército total: La suma de Inmaculados y Dothrakis.
# •	Vidriagón necesario: El ejército total multiplicado por la constante de armas requeridas por soldado.
# •	Déficit de armas: Cuántas dagas de vidriagón faltan (vidriagón necesario menos el disponible).
ejercito_total = soldados_Dothrakis + soldados_Inmaculados

vidragon = ejercito_total * VIDRIAGON_POR_SOLDADO

deficit_arma = Cantidad_dagas - vidragon

# 4. Usa lógica condicional (if, elif, else) y OPERADORES LÓGICOS (and, or) para predecir el resultado de la batalla:
# •	Condición 1 (Victoria Absoluta): Si el ejército total es mayor o igual a 20.000 soldados Y tienen a los dragones Y el vidriagón disponible es mayor o igual al necesario.  Imprimir: "¡Victoria Absoluta! El Rey de la Noche ha sido derrotado sin problemas."
if ejercito_total >= 20000 and Daenerys_dragones == "si" and Cantidad_dagas >= vidragon:
    mensaje ="¡Victoria Absoluta! El Rey de la Noche ha sido derrotado sin problemas!"
elif ejercito_total >=10000 and Daenerys_dragones == "si" and Temperatura_actual <= TEMPERATURA_CONGELACION and deficit_arma < 0:
    mensaje = f"Victoria Amarga: Sobrevivimos gracias al fuego de dragón, pero las bajas por el frío y la falta de armas fueron catastróficas. Faltaron {deficit_arma} dagas."
#•	Condición 2 (Victoria Amarga): Si el ejército total es mayor o igual a 10.000 Y tienen a los dragones, PERO la temperatura actual es menor o igual a la constante de congelación O hay un déficit de armas (faltan dagas).  Imprimir: "Victoria Amarga: Sobrevivimos gracias al fuego de dragón, pero las bajas por el frío y la falta de armas fueron catastróficas. Faltaron [Mostrar déficit de armas] dagas."
elif ejercito_total < 10000 and Daenerys_dragones == "si" or Temperatura_actual <= TEMPERATURA_CONGELACION:
    mensaje =  "No somos suficientes, pero los dragones nos dieron tiempo para huir hacia el sur"
else:
    mensaje = "Derrota Total: Invernalia ha caído. Comienza la Larga Noche..."

print(mensaje)
# •Condición 3 (Retirada Táctica): Si el ejército es menor a 10.000 Y tienen a los dragones, Y la temperatura es mayor a la constante de congelación.  Imprimir: "Retirada Táctica: No somos suficientes, pero los dragones nos dieron tiempo para huir hacia el sur."

# Condición 4 (Derrota Total): Para cualquier otro escenario (por ejemplo, si no hay dragones y no se cumplen las condiciones de tamaño del ejército).  Imprimir: "Derrota Total: Invernalia ha caído. Comienza la Larga Noche..."


