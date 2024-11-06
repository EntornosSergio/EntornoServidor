dinero = float(input("Dinero a retirar: "))

multiplicador = (dinero // 1000) + 1

print("Comisión: ",10*multiplicador," euros")