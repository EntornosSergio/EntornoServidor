tupla=()
for i in range(1,11):
    edades=int(input("Introduce una edad: "))
    tupla=tupla + (edades,)
    
for i in range(len(tupla)):
    if tupla[i] > 20:
        print(tupla[i],end=" ")
        