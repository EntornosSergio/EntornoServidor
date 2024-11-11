cadena1="sergio"
cadena2="ser"
f=cadena1.find(cadena2)
if f!=-1:
    print("Es una subcadena")
else:
    print("No lo es")
    
if cadena1 < cadena2:
    resultado = cadena1
else:
    resultado = cadena2
    
print("La cadena anterior en orden alfabético es:", resultado)