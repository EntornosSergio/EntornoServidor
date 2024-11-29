from EJERCICIO1.Añadir import añadirUsuario
from EJERCICIO1.Consultar import consultarUsuario
from EJERCICIO1.Eliminar import eliminarUsuario
from EJERCICIO1.Ver import verUsuarios



numero=0
print("Bienvenido al progra listin de Telefonos")
while numero!= 4:
    numero=int(input("1. Añadir \n2. Consultar \n3. Eliminar \n4. Salir y ver la lista \n"))
    if numero == 1:
        añadirUsuario()
    if numero == 2:
        consultarUsuario()
    if numero == 3:
        eliminarUsuario()
    if numero == 4:
        verUsuarios()


