import re

def añadir_precio(cadena):
    for diccionario in cadena:
        metros = diccionario['metros']
        habitaciones = diccionario['habitaciones']
        garaje = diccionario['garaje']
        año = diccionario['año']
        zona = diccionario['zona']
        
        if zona == "A":
            precioA = ((metros * 1000 + habitaciones * 5000 + garaje * 15000) * año / 100)
            diccionario["Precio"] = precioA  
        else:
            precioB = ((metros * 1000 + habitaciones * 5000 + garaje * 15000) * año / 100) * 1.5
            diccionario["Precio"] = precioB 
    return cadena