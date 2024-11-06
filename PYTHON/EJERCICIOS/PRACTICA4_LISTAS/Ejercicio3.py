lista=["En", "la", "granja", "la", "vaca", "pasea", "tranquila", "por", "el", "prado", "disfrutando", "del", "sol"]
cont=0
print(lista)
cadena=input("Anota la cadena: ")
print(lista)
for i in range(len(lista)):
    if lista[i]==cadena:
        cont+=1
    
print("La cadena \""+cadena+"\" apareció "+str(cont)+" veces.")

cadena2=input("Ingresa otra cadena: ")
for i in range(len(lista)):
    if lista[i]==cadena:
        lista[i]=cadena2
        
    print(lista[i],end=" ")
    