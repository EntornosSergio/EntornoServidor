import random

nombre1 = input("Nombre 1: ")
nombre2 = input("Nombre 2: ")

a1 = random.randint(1, 10)  
a2 = random.randint(1, 10)  
d1 = random.randint(1, 15) 
d2 = random.randint(1, 15)  

jugador1 = [nombre1, a1, d1]  
jugador2 = [nombre2, a2, d2] 

empezar = random.randint(0, 1)  

print("\nInformación de cada jugador: ")
print(f"{jugador1[0]} - Ataque: {jugador1[1]}, Vida: {jugador1[2]}")
print(f"{jugador2[0]} - Ataque: {jugador2[1]}, Vida: {jugador2[2]}")

if empezar == 0:    
    print(f"\nEmpieza: {jugador1[0]}")
else:
    print(f"\nEmpieza: {jugador2[0]}")

while jugador1[2] > 0 and jugador2[2] > 0:
    if empezar == 0:
        jugador2[2] -= jugador1[1]
        print(f"-> {jugador1[0]} ha atacado a {jugador2[0]}")
        print(f"A {jugador2[0]} le quedan {jugador2[2]} de vida")
        if jugador2[2] <= 0:
            print(f"!!!! {jugador1[0]} ha ganado!!!!!")
            break
        empezar = 1  
    else:
        jugador1[2] -= jugador2[1]
        print(f"=> {jugador2[0]} ha atacado a {jugador1[0]}!")
        print(f"A {jugador1[0]} le quedan {jugador1[2]} de vida")
        if jugador1[2] <= 0:
            print(f"**** {jugador2[0]} ha ganado! ****")
            break
        empezar = 0  

