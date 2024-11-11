cadena = input("Escribe una cadena: ")
letra = cadena.split()

nueva_cadena = ""  
cadena2 = cadena.title() 
cadenaA = "" 

for p in letra:
    nueva_cadena += p[0]  
    if p[0].lower() == "a":  
        cadenaA += p + " "  

print("Primera letra de cada palabra:", nueva_cadena)
print("Cadena en formato título:", cadena2)
print("Palabras que comienzan con 'a' o 'A':", cadenaA.strip())
