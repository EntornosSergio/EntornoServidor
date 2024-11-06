caracter = input("Escribe un carácter: ")

if caracter.isupper():
    print("Está en mayúsculas")
elif caracter.islower():
    print("Está en minúsculas")
elif caracter.isdigit():
    print("Es un dígito")
else:
    print("No es una letra ni un dígito")
