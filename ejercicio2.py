def max(num1, num2):
    if num1 >= num2:
        print("El número mayor es: ", num1)
    else:
        print("El número mayor es: ", num2)

num1 = int(input("Ingresa un número: "))
num2 = int(input("Ingresa un segundo número: "))

max(num1, num2)

"""Función Lambda"""

num_1 = int(input("Ingresa el primer número: "))
num_2 = int(input("Ingresa el segundo número: "))
max = lambda num_1, num_2: print(f"El mayor es: {num_1}") if(num_1 > num_2) else print(f"El mayor es: {num_2}")
max(num_1, num_2)