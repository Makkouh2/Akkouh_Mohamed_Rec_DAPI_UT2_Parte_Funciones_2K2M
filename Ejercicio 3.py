import math

def areadelcirculo(radio):
    """ Esta función te calcula el área del círculo
        
        Parámetros:
        radio: radio del círculo

        Salida:
        Devuelve el área del círculo"""
    return math.pi * radio ** 2

def volumendelcilindro(radio, altura):
    """ Esta función calcula el volumen de un cilindro usando la primera función.

        Parámetros:
        radio : El radio del cilindro.
        altura: La altura del cilindro.

        Salida:
        Devuelve el volumen del cilindro."""
    area = areadelcirculo(radio)
    return area * altura

radio = float(input("Escribe el radio: "))
altura = float(input("Escribe la altura: "))
print(f"Área del círculo de radio {radio}: {areadelcirculo(radio)}")
print(f"Volumen del cilindro de radio {radio} y altura {altura}: {volumendelcilindro(radio, altura)}")
