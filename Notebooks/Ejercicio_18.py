n1 = int(input('Ingrese el primer numero: '))
n2 = int(input('Ingrese el segundo numero: '))
n3 = int(input('Ingrese el tercer numero: '))
n4 = int(input('Ingrese el cuarto numero: '))
n5 = int(input('Ingrese el quinto numero: '))

r1 = n1 - n2
r2 = n1 - n3
r3 = n1 - n4
r4 = n1 - n5

menor_numero = r1

if r2 < menor_numero and r2 >= 0:
    menor_numero = r2
else:
    if r2 > menor_numero and r2 <= 0:
        menor_numero = r2

if r3 < menor_numero and r2 >= 0:
    menor_numero = r3
else:
    if r3 > menor_numero and r3 <= 0:
        menor_numero = r3

if r4 < menor_numero and r4 >= 0:
    menor_numero = r4
else:
    if r4 > menor_numero and r4 <= 0:
        menor_numero = r4
 
numero_cercano = n1 - menor_numero
print(f'El numero mas cercano a {n1} es: ', numero_cercano)
