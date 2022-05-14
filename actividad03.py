#Hecho por Allam
# Ejercicio 5.1:Defina una función en python que acepte el radio y devuelva el valor del area de un círculo de esas dimensiones
import math
def areaDeCirculo(radio):
    A = math.pi*radio**2
    return A


respuesta=areaDeCirculo(10)

print ("El area del circulo:  ",respuesta)

#5.2 Defina una función en python que acepte 3 valores y devuelva solo el maximo de los tres.
def elMaximoDe3Valores(num1,num2,num3):
    if (num1>num2) :
        mayor1y2=num1
    else :
        mayor1y2=num2

    if (mayor1y2>num3) :
        mayorEs=mayor1y2
    else :
        mayorEs=num3

    return mayorEs


respuesta=elMaximoDe3Valores(50,200,30)

print ("El mayor de los tres es:  ",respuesta)


#5.3 Dado una lista de enteros, defina una función en python que devuelva la suma de solo los valores impares de dicha lista

lista = [5,7,8,24,30,46,57]


def sumaDeSoloLosValoresImpares(laLista):
    suma = 0
    for x in laLista:
        residuo=x % 2
       
        if (residuo != 0):
            # el numero es impar
            suma = suma + x
    return suma

respuesta=sumaDeSoloLosValoresImpares(lista)

print ("La suma de los valores impares es:  ",respuesta)

# 5.4 Desarrolle una función en python que acepte una variable string como primer parámetro y la cantidad de caracteres de
#  como segundo parámetro. La función debe retornar un nuevo string que consista en el string original y el número correcto 
# de caracteres necesarios para que el string se salga centrado. No agregue caracteres al final del string.



def centrandoUnString(texto,totalEspacio):
    #esto era para probar
    #espacios=""
    #for i in range(totalEspacio):
     #   espacios += "-"
    #print(espacios)
    longDeTexto=len(texto)
    resta=totalEspacio-longDeTexto
    cantidadEspacioAlaIzquierda=round(resta/2)
    espacios=""
    for i in range(cantidadEspacioAlaIzquierda):
        espacios += " "
    return espacios+texto

respuesta=centrandoUnString("Hola",20)

print (respuesta)