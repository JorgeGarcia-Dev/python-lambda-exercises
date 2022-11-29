def vocales(vocal):
    if vocal == 'a' or vocal == 'e' or vocal == 'i' or vocal =='o' or vocal == 'u':
        print(True)
    else:
        print(False)

vocal = input("Ingresa una letra: ")

vocales(vocal)

"""Función Lambda"""

vocal = input("Ingresa una letra: ")
vocales = lambda vocal: print("Es vocal.") if(vocal in 'aeiou' or vocal in 'AEIOU') else print("No es vocal, es una consonante.")
vocales(vocal)