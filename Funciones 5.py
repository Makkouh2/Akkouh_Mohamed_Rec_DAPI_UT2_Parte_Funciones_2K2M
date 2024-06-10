def numeros_cuadrado(lista):
    """
    Funcion calcula el cuadrado de los números de la lista.

    Parámetros:
        lista: la lista de números de la cual se calculará el cuadrado.

    Salida:
        list: lista con los valores al cuadrado."""
    
    return [x**2 for x in lista]


numeros = [30, 5, 18, 9, 10]
resultado = numeros_cuadrado(numeros)
print(resultado)