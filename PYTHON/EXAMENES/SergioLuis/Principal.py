from Funciones import generar_diccionario
from Funciones import ordenar_diccionario
from Funciones import menor_numero_tiradas
from Funciones import igualar_tiradas
from Funciones import generar_lista_tuplas
from Funciones import jugador_ganador
from Funciones import printar

cadena="iceman,25,3,9;hammer,50,36,3;iceman,9,12,17;lion,9,24,21;"
printar("APARTADO_1",cadena)

dic=generar_diccionario(cadena)
printar("APARTADO_2",dic)

ordenado=ordenar_diccionario(dic)
printar("APARTADO_3",ordenado)

igual=igualar_tiradas(ordenado)
printar("APARTADO_4",igual)

lista=generar_lista_tuplas(igual)
printar("APARTADO_5",lista)

ganador=jugador_ganador(lista)
printar("APARTADO_6",ganador)

