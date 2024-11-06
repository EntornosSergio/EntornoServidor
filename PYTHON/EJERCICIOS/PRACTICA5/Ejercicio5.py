dicc={}

español=" "
while español!="*":
    español=input("Escribe una palabra en español: ")
    if español=="*":
        break
    else:
        ingles=input("Escribe una palabra en ingles: ")
        dicc[español]=ingles

print(dicc)
frase=input("Introduce una frase en español: ")
palabras=frase.split()
for palabra in palabras:
    if palabra in dicc:
        print(dicc.get(palabra),end=" ")
    else:
        print(palabra,end=" ")
    