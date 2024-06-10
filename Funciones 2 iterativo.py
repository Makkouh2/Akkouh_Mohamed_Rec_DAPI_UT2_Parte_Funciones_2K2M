def iterativo (n):
    """la funcion es para iterativa para calcular el factorial de un numero entero positivo

       parametros:
       n: variable del numero para crear su factorial 

       salida:
       la funcion devuelve el factrial del numero """
    if n < 0:
        return "El numero tiene que ser entero y positivo"
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


print(iterativo(9))