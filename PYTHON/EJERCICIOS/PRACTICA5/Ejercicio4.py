gustos_personas = {
    "Ana": ["leer", "viajar", "fotografía"],
    "Juan": ["fútbol", "cine", "videojuegos"],
    "María": ["pintura", "jardinería", "yoga"],
    "Luis": ["cocina", "música", "senderismo"],
    "Sofía": ["dibujo", "animales", "escalada"]
}

print(gustos_personas)

bucle = True
while bucle:
    persona = input("Elige una persona o añádela. Si pones '*' acaba el programa: ")
    
    if persona == "*":
        bucle = False  
        break
    
    if persona not in gustos_personas:
        gustos = input("¿Qué gustos tienes? (separa los gustos con comas): ")
        lista_gustos = [gusto.strip() for gusto in gustos.split(",")]
        gustos_personas[persona] = lista_gustos
    else:
        print(f"Gustos de {persona}: {gustos_personas[persona]}")
        
print("Gustos actualizados:")
print(gustos_personas)
