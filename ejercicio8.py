def palabra_mayor():
    
    palabra_1 = len(input("Ingresa una palabra: "))
    palabra_2 = len(input("Ingresa una palabra: "))

    if palabra_1 > palabra_2:
        print(f"La primer palabra es mayor")
    else:
        print(f"La segunda palabra es mayor")

palabra_mayor()

"""Función Lambda"""

palabra_1 = len(input("Ingresa una palabra: "))
palabra_2 = len(input("Ingresa una palabra: "))
palabra_mayor = lambda palabra_1, palabra_2: print("La primer palabra es mayor") if(palabra_1 > palabra_2) else print(f"La segunda palabra es mayor")
palabra_mayor(palabra_1, palabra_2)