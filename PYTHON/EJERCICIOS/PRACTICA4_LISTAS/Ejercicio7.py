num=0
nombres=[]
l_frecuencias={}
while True:
    nombre = input("Introduce nombres (escribe -1 para terminar): ")
    
    if nombre == "-1":
        break
    
    if nombre in l_frecuencias:
        l_frecuencias[nombre] += 1
    else:
        l_frecuencias[nombre] = 1
        
print(l_frecuencias)