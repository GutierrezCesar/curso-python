#Ecuacion de primer grado
ANCHO = 40
Relleno1 = '-'
Relleno2 = ' '
Cadena_vacio = ''

################################################

Mensaje_inicial = 'Ecuacion de primer grado: ax + b = 0'

################################################

#Declarar variables
a, b, x = 0, 0, 0

#Formato de salida final en pantalla

formato_ecuacion = 'Ecuacion: {} x + {} = 0'

###############################################
#Encabezado del programa
print(Cadena_vacio.center(ANCHO,Relleno1))
print(Mensaje_inicial.center(ANCHO,Relleno2))
print(Cadena_vacio.center(ANCHO,Relleno1))

#Encabezado del programa
a = float(input('Ingrese el valor de a: '))
b = float(input('Ingrese el valor de b: '))

print(Cadena_vacio.center(ANCHO,Relleno1))
print(formato_ecuacion.format(a,b))
print(Cadena_vacio.center(ANCHO,Relleno1))

try:
    x = -b/a
    print('La solucion de la ecuacion es x = ', x)
except:
    if b!=0:
        print('La ecuacion no tiene solucion')
    else:
        print('La ecuacion tiene infinitas soluciones')