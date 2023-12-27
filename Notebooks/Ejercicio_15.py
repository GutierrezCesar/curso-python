#Mayúsculas y Minúsculas
letra = input('Ingrese una letra: ')
if letra >= 'a' and letra <= 'z':
    print('La letra ingresada es minuscula')
elif letra >='A' and letra <='Z':
    print('La letra ingresada es mayusula')
else:
    print('El valor introducido no es el correcto')