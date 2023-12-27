#El programa pedira numeros para promediarlos
contador = 0
suma = 0
numero = 0
while True:
    numero = int(input('Ingrese un numero para sumarlos (Ingresa -1 para salir)'))
    if(numero==-1):
        break
    suma+=numero
    contador+=1

if(contador>0):
    promedio = suma/contador
    print('La sum de los numeros es: ', suma)
    print('EL total de numeros introducidos por el usuario son: ', contador)
    print('El promedio de los numeros ingresados es: ', promedio)
else:
    print('No se ingresaron numeros validos')