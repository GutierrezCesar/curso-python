n1 = int(input('Ingrese el primer numero: '))
n2 = int(input('Ingrese el primer numero: '))
n3 = int(input('Ingrese el primer numero: '))

if n1>n2 and n1>n3:
    print(f'El numero mayor de {n1}, {n2} y {n3} es: ' + str(n1))
elif n2>n1 and n2>n3:
    print(f'El numero mayor de {n1}, {n2} y {n3} es: ' + str(n2))
else:
    print(f'El numero mayor de {n1}, {n2} y {n3} es: ' + str(n3))