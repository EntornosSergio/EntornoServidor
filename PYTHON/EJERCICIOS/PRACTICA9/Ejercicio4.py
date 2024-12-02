cont=0
conteo = {}
with open("EJERCICIOS/PRACTICA9/Ejercicio4.txt","r") as t:
    for linea in t:
        pal=linea.split()
        for i in pal:
            if i in conteo:
                conteo[i]+=1
            else:
                conteo[i]=1

print(conteo)
print("Palabra que mas se repite: " + max(conteo, key=conteo.get) )

