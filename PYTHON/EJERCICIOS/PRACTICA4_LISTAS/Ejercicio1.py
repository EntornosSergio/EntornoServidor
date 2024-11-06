lista=[]
pares=""
max= 0
cont=0
numero=int(input("Añade un numero: "))
while numero > 0:
    lista.append(numero)
    if lista[cont] % 2 == 0:
       pares+=str(numero) + ", "
    if max < lista[cont]:
        max=numero
    numero=(int(input("Añade un numero: ")))
    cont+=1
    
print ("los numeros pares son " + pares + " y el numero mas grande es el " + str(max))
    