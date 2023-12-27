#el programa lee un arreglo de numeros y se detiene la cantidad de segundos que indica el numero leido
import time

for i in [5,1,4,6,3,2,1]:
    print(f'Habra un retrazo de {i} segundos')
    time.sleep(i)
    