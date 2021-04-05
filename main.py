import funciones
print("----------*Enoc Carrera ©2021*---------")
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
#op toma y transforma a entero el numero que el usuario ingresa en la consola
    op = int(input(menu))
    if op == 1:
#Aqui Llamamos la funcion que tenemos en nuestro otro archivo
        funciones.Galones_Litros()
    elif op == 2:
        funciones.Libras_Kilogramos()
    elif op == 3:
        funciones.C_F()
    elif op == 4:
        funciones.Litros_Galones()
    elif op == 5:
        funciones.Kilogramos_Libras()
    elif op == 6:
        print("Hasta Luego. Gracias por usar nuestro software")
#break rompe el ciclo while para evitar que el ciclo se repita infinitamente
        break
    else:
        print("Estas funciones aun estan en desarrollo")