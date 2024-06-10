def calcular_media(lista):
    """
    Función que calcula la media de una lista de números.

    Parámetros:
    lista: la lista de números de la cual se calculara la media.

    Salida:
    Me devuelve la media de los numeros"""
    
    suma = sum(lista)
    mediadelalista = suma / len(lista)
    return mediadelalista

lista = [30, 5, 18, 9, 10]
resultado = calcular_media(lista)
print(resultado)