def ingresar_datos(n):
    datos = []
    for i in range(n):
        valor = float(input(f"Ingrese el dato {i + 1}: "))
        datos.append(valor)
    return datos

def ordenar_lista(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def calcular_sumatoria(lista):
    suma = 0
    for dato in lista:
        suma += dato
    return suma

def calcular_media(lista):
    suma = calcular_sumatoria(lista)
    n = len(lista)
    if n > 0:
        media = suma / n
        return media
    else:
        return None  
    
def calcular_mediana(lista):
    lista_ordenada = ordenar_lista(lista)
    n = len(lista_ordenada)
    if n % 2 == 0:
        mediana = (lista_ordenada[n // 2 - 1] + lista_ordenada[n // 2]) / 2
    else:
        mediana = lista_ordenada[n // 2]
    return mediana


def calcular_moda(lista):
    contador = {}
    for dato in lista:
        if dato in contador:
            contador[dato] += 1
        else:
            contador[dato] = 1

    moda = None
    max_frecuencia = 0
    for dato, frecuencia in contador.items():
        if frecuencia > max_frecuencia:
            moda = dato
            max_frecuencia = frecuencia

    return moda

def calcular_desviacion_estandar(lista):
    media = calcular_media(lista)
    n = len(lista)
    suma_cuadrados = 0
    for dato in lista:
        suma_cuadrados += (dato - media) ** 2

    if n > 0:
        desviacion_estandar = (suma_cuadrados / n) ** 0.5
        return desviacion_estandar
    else:
        return None  

n = int(input("Ingrese la cantidad de datos: "))
datos = ingresar_datos(n)

print("Lista de datos:", datos)
print("Lista ordenada:", ordenar_lista(datos))
print("Sumatoria:", calcular_sumatoria(datos))
print("Media:", calcular_media(datos))
print("Mediana:", calcular_mediana(datos))
print("Moda:", calcular_moda(datos))
print("Desviación estándar:", calcular_desviacion_estandar(datos))
