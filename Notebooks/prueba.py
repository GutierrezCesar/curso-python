#Insertar una cantidad en soles y mostrara un menu de opciones
#para convertir a dolaores o soles mexicanos
pesos = int(input('Ingrese la cantidad en pesos Mexicanos: '))
opcion = int(input('\nA cual moneda deseas convertir: '
                   '\n1. Dolares $17'
                   '\n2. Soles Peruanos $4\n'))

mensaje = 'La cantidad convertida en Dolares es: '
mensaje2 = 'La cantidad convertida en Soles Peruanos es: '
ancho = 80
if(opcion==1):
    total=pesos/17
    mensaje=mensaje.center(ancho)
    print(mensaje, round(total,2))
elif(opcion==2):
    total=pesos/4
    mensaje2=mensaje2.center(ancho)
    print(mensaje2, round(total,2))
else:
    print('Escogiste la opcion incorrecta')