cont=0
x='inc'
while x!=str('inc') or x!=str('desc'):
    x=input("Ingresa inc o desc, o si no finaliza el programa: ")
    if x !="desc" or x !="inc":
        with open("EJERCICIOS/PRACTICA9/contador.txt","w+") as t:
            if x =="inc":
                cont+=1
                t = open("EJERCICIOS/PRACTICA9/contador.txt","w")
                t.write(str(cont))
                t.close()
            if x=="desc":
                cont-=1
                t = open("EJERCICIOS/PRACTICA9/contador.txt","w")
                t.write(str(cont))
                t.close()
        t.close()
    else:
        exit()




