nombre=(input("Escriba su nombre"))
def saludo(nombre):
 
    """Función que saluda al nombre que ponga el usuario.
   Parámetros:
   -nombre:variable para escribir el nombre.
   Salida:
   -print:devuelve por pantalla Hola y el nombre que hayas puesto"""


   
    print('¡Hola', nombre + '!')
    return


saludo(nombre)