lista_numeros = [5,7,9,10,15,54,7]

def numeros_iguales():
    
    if lista_numeros[0] == lista_numeros[-1]:
        print(lista_numeros[0], "Es igual que", lista_numeros[-1])
    else:
        print(lista_numeros[0], "No es igual que", lista_numeros[-1])

numeros_iguales()

"""Función Lambda"""

lista_numeros = [7,7,9,10,15,54,7]
numeros_iguales = lambda lista_numeros: print(f"{lista_numeros[0]} Es igual que {lista_numeros[-1]}") if(lista_numeros[0] == lista_numeros[-1]) else print(f"{lista_numeros[0]} No es igual que {lista_numeros[-1]}")
numeros_iguales(lista_numeros)