# Desarrollar un programa con una función de argumentos indeterminados que
# permita calcular la suma de 2 o más números.
def suma_numeros(*args):
    suma = 0
    for numero in args:
        suma += numero
    return suma
resultado = suma_numeros(1, 2, 3, 4, 5)
print("La suma es:", resultado)
