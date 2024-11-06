dicc = {}

persona=" "
while persona!="*":
    persona=input("Agregue nombre: ")
    if persona=="*":
        break
    if persona not in dicc:
        gusto=input("Dime una afición: ")
        dicc[persona]=[gusto]
    else:    
        gusto=input("Dime una afición: ")
    if gusto not in dicc[persona]:
        dicc[persona].append(gusto)
        
print(dicc)