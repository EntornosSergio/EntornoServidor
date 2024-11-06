def totalSegundos(horas,minutos,segundos):
    horasSe=horas*3600
    minutosSe = minutos * 60
    total=horasSe + minutosSe + segundos
    return total

def hora(cantidadSegundos):
    horas = cantidadSegundos // 3600
    minutos = (cantidadSegundos % 3600) // 60
    seg = cantidadSegundos % 60
    return horas, minutos, seg 


horas=(int(input("Introduce hora: ")))
minutos=(int(input("Introduce minutos: ")))
segundos=(int(input("Introduce segundos: ")))
total=totalSegundos(horas,minutos,segundos)

print("La cantidad de segundos en el tiempo dado es de: " + str(total))
cantidadSegundos=(int(input("Escribe un tiempo en segundos:")))
horas, minutos, seg = hora(cantidadSegundos)
print(f"La hora son: {horas}, minutos: {minutos} y segundos: {seg}")
