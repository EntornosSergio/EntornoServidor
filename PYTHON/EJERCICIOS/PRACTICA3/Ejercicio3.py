def EscribirCentrado(texto, subrayado='='):
    # Definir el ancho total de la "pantalla"
    ancho_pantalla = 80
    
    # Calcular el número de espacios a la izquierda del texto
    espacios_izquierda = (ancho_pantalla - len(texto)) // 2
    
    # Imprimir los espacios y luego el texto
    print(' ' * espacios_izquierda + texto)
    
    # Imprimir la línea de subrayado centrada del mismo tamaño que el texto
    print(' ' * espacios_izquierda + subrayado * len(texto))

# Ejemplo de uso:
EscribirCentrado("Bienvenidos al curso de Python")
