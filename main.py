import funciones
print("----------*Enoc Carrera*---------")
menu = """
Por favor escoja la opcion que desea realizar
1.Convertir Galones a litros
2.Convertir Libras a kilogramos
3.Convertir Celcius a farenheit
4.Convertir Litros a galones
5.Convertir Kilogramos a libras 
6.Salir del sistema 
Opcion: 
"""
conditional = True;
while conditional == True:
    op = int(input(menu))
    if op == 1:
#Aqui Llamamos la funcion que tenemos en nuestro otro archivo
        funciones.Galones_Litros()
    elif op == 2:
        print("Hola")

    elif op == 3:
        print("Mi nombre es: Carlos")
    elif op == 6:
        print("Hasta Luego. Gracias por usar nuestro software")
        break
    else:
        print("Estas funciones aun estan en desarrollo")