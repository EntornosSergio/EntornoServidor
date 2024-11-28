inmuebles=[{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'}, 
{'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'}, 
{'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'}, 
{'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'}, 
{'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]


# • Zona A: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * año/100) • Zona B: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * año/100) * 1.5 
# Implementa una función anyadir_precio que recibe un diccionario y añade el campo precio con el  valor calculado según las fórmulas que se te han indicado 
for inmueble in inmuebles:
    metros=inmueble['metros']
    habitaciones=inmueble['habitaciones']
    garaje=inmueble['garaje']
    año=inmueble['año']
    zona=inmueble['zona']
    if garaje == True:
        garajevalor=1
    else:
        garajevalor=0
  
    if zona =='A':
            precioZA=((metros*1000)+(habitaciones*5000)+(garaje*15000)*año/100)
            inmueble['PRECIO']=precioZA
    else:        
        precioZB=(((metros*1000)+(habitaciones*5000)+(garaje*15000)*año/100)*1.5)
        inmueble['PRECIO']=precioZB
    
    print(inmueble)
    
    
    
    

