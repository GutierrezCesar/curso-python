import time

contador = 10

print('Inicia el cuento respectivo')
while contador > 0:
    print(contador)
    time.sleep(1)
    contador-=1 #contador = contador  - 1 
print('El cohete ha despegado con exito')