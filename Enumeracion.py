# Este es un programa para practicar Enumeración exaustiva
# Averiguaremos la raíz cuadrada de un número

Objetivo = int(input("Escoge un número entero: "))
Respuesta = 0;

while Respuesta**2 < Objetivo:
    print(Respuesta)

if Respuesta**2 == Objetivo:
    print(f"La raíz cuadrada de {Objetivo} es {Respuesta}")

else:
    print(f"{Objetivo} no tiene una raíz cuadrada exacta")
