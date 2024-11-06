import random

numero = random.randint(1, 10)
numteclado=0
while numero != numteclado:
    numteclado = (int(input("Introduce numero: ")))
    if numteclado > numero:
        print("Es menor")
    elif numteclado < numero:
        print("Es mayor")
    else:
        print("¡ADIVINASTE EL NÚMERO; ERA EL " + str(numero) + "!")
        
        