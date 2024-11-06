minutos = int(input("Ingresa una cantidad de mimutos: "))

horas = minutos // 60
minutos_restantes = minutos % 60
    
print(minutos, " minutos son ", horas, " horas y ", minutos_restantes, " minutos restantes")