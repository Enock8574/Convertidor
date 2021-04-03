#Enoc Carrera ©2021
#Esta funcion es para convertir galones a litros
def Galones_Litros():
    print("Ingrese la cantidad de galones que desea convertir a litros \n")
    Galones = int(input("G: "))
    #Formula matematica
    Resultado = float((Galones*3.785)/1)
    print(f": {Resultado} L")
#Converir libras a kilogramos
def Libras_Kilogramos():
    print("Ingrese la cantidad de libras para ser convertidas a kilogramos \n")
    Libras = int(input("Lb: "))
    #Fomula
    Resultado = round(Libras/2.205, 5)
    print(f"{Resultado} Kg")
#Convertir Celcius a Fahrenheit
def C_F():
    print("Ingrese la cantidad de grados celcius para ser convertida a Fahrenheit \n")
    Celcius = int(input("°C: "))
    #Formula
    Resultado = round((Celcius*9/5)+32, 1)
    print(f"{Resultado} °F")