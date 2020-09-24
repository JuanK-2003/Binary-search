Objetivo = int(input('Escoge un número: '))
Epsilon = 0.1
Paso = Epsilon**2
Respuesta = 0.0

while abs(Respuesta**2 - Objetivo) >= Epsilon and Respuesta <= Objetivo:
    print(abs(Respuesta**2 - Objetivo), Respuesta)
    Respuesta += Paso

if abs(Respuesta**2 - Objetivo) >= Epsilon:
    print(f'No se encontro raíz cuadrada de {Objetivo}')
else:
    print(f'La raíz cuadrada de {Objetivo} es {Respuesta}')

