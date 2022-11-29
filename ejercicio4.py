def inversa(frase):
    print(frase[::-1])

palabra = input('Ingresa una palabra: ')

inversa(palabra)

"""Función Lambda"""

palabra = input("Ingresa una frase: ")
inversa = lambda frase: print(frase[::-1])
inversa(palabra)