def numero_entero():
    
    numeroEntero = int(input("Ingresa un número: "))
    if numeroEntero % 2 == 0:
        print(f"El número {numeroEntero} es par.")
    else:
        print(f"El número {numeroEntero} es impar.")

numero_entero()

"""Función Lambda"""

numeroEntero = int(input("Ingresa un número: "))
numero_entero = lambda numeroEntero: print(f"El número {numeroEntero} es par.") if(numeroEntero %2 == 0) else print(f"El número {numeroEntero} es impar.")
numero_entero(numeroEntero)