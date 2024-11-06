import random

numero = random.randint(1, 10)
numteclado=0
intentos = 0
while numero != numteclado:
    numteclado = (int(input("Introduce un numero y tienes 3 intentos para adivinarlo: ")))
    if intentos == 3:
        print("Superastes el numero de intentos")
        break
    elif numteclado > numero:
        print("Es menor")
        intentos = intentos+1
    elif numteclado < numero:
        print("Es mayor")
        intentos = intentos+1
    else:
        print("¡ADIVINASTE EL NÚMERO, ERA EL " + str(numero) + " Y HAS NECESITADO " + str(intentos) + " INTENTOS PARA ADIVINARLO")
        
        