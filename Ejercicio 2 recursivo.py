def recursivo(n):
    """
    Función para calcular el factorial de un numero entero positivo mediante el bucle recursivo 

       parametros:
       n: numero entero positivo 

       salida:
        Devuelve el factorial del numero """ 
    if n < 0:
        return "El número debe ser entero positivo"
    if n == 0 or n == 1:
        return 1
    else:
        return n * recursivo(n - 1)


print(recursivo(6))