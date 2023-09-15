# Crear una funcion que permita calcular la raíz n de un número.
def raiz_n(numero, n):
    if n <= 0:
        return "El valor de n debe ser mayor que cero."
    resultado = numero ** (1/n)
    return resultado
numero = 16
n = 2
resultado = raiz_n(numero, n)
print(f"La raíz {n}-ésima de {numero} es: {resultado}")
