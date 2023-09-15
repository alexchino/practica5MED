# Crear una función que permita realizar una división en el caso de que el
# denominador sea 0, mostrar al usuario el mensaje “La división entre cero no está
# definida” caso contrario mostrar el resultado de la división.

def division_personalizada(dividendo, divisor):
    if divisor == 0:
        return "La división entre cero no está definida"
    resultado = dividendo / divisor
    return resultado

dividendo = 10
divisor = 0

resultado = division_personalizada(dividendo, divisor)
if isinstance(resultado, str):
    print(resultado)
else:
    print(f"El resultado de la división es: {resultado}")
