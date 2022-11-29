def es_palindromo(palabra):
    if (palabra) == str(palabra) [::-1]:
        print(True)
    else:
        print(False)

palabra = input('Ingresa una palabra: ')

es_palindromo(palabra)

"""Función Lambda"""

palabra = input('Ingresa una palabra: ')
es_palindromo = lambda palabra: print(True) if((palabra) == str(palabra) [::-1]) else print(False)
es_palindromo(palabra)