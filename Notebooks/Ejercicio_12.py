persona1 = int(input('Persona "x" Ingrese su edad: '))
persona2 = int(input('Persona "y" Ingrese su edad: '))

if persona1 == persona2:
    print('Ambas personas tienen la misma edad')
elif persona1 > persona2:
    print('La primera persona es mayor')
else:
    print('La segunda persona es mayor')
