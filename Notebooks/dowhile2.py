#El programa pedira numeros mientras los ingresados esten entre el 0 y 99
edad = 0

while True:
    edad = int(input('Escriba su edad: '))
    if(edad>0)and(edad<99):
        break
    print('Edad no valida, intenta de nuevo por favor')

print('Tu edad es: ', edad)