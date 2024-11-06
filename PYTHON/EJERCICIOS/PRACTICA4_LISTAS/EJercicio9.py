import random

for i in range(0,51):
    if i %10 ==0 and i!=0:
        print(i)
    else:
        print(i,end=" ")

tupla1=()
for i in range(6):
    num1=int(input("Ingrese un numero: "))
    tupla1=tupla1 + (num1,)

tupla2=()
for i in range(6):
    num2 = random.randint(0,51)
    tupla2=tupla2 + (num2,)
    
print(f"Tus numeros: {tupla1}")
print(f"Numeros del sorteo: {tupla2}")

for num in tupla1:
    if num in tupla2:
        print(f"Habeis coincidico en el numero: {num}")

