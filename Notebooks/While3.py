#El programa contiene un numero secreto que el usuario debe adivinar
#tendra 3 opciones
numero_secreto = 9
adivinado = False
intentos = 0
quedan = 3

print('Solo tienes 3 intentos para adivinar el numero')

while not(adivinado)and(intentos<3): #while (adivinado == false)
    dato = int(input('Adivina el numero(es menor que 10): '))
    if(dato == numero_secreto):
        print('Felicitaciones, lograste adivinar el numero')
        adivinado = True
    else:
        intentos+=1
        if (intentos==3):
            print('Juego terminado')
        else:
            print('Por favor intentalo de nuevo')
            quedan -=1
            print(f'Te quedan {quedan} intentos')