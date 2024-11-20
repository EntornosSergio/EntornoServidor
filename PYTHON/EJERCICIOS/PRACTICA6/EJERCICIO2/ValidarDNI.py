def validarDNI(dni):

    letras_validas = "TRWAGMYFPDXBNJZSQVHLCKE"
    if len(dni) != 9:  # Verificar longitud
        return False
    if not dni[:-1].isdigit():  # Verificar que los primeros 8 caracteres sean dígitos
        return False
    if not dni[-1].isalpha():  # Verificar que el último carácter sea una letra
        return False

    numero = int(dni[:-1])  # Extraer los 8 dígitos como número entero
    letra = dni[-1].upper()  # Convertir la letra a mayúscula

    # Calcular la letra correspondiente
    indice = numero % 23
    letra_correcta = letras_validas[indice]

    # Comparar la letra dada con la calculada
    return letra == letra_correcta
