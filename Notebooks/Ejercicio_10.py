#CABEZAL
print('-' * 40)
print('CALCULADORA FREELANCER (USD)')
print('-' * 40)
#FIN DE CABEZADO

#CUERPO
HoraSemanal = 40
HoraMensual = 160
DolaresPorHora = int(input('Ingrese la cantidad de dolar: '))
Pago_semanal = (DolaresPorHora * HoraSemanal)
Pago_mensual = (DolaresPorHora * HoraMensual)

#SALIDA
print('Precio en dolares por hora: ', DolaresPorHora)
print('-' * 40)
print('PAGO SEMANAL: ', Pago_semanal)
print('PAGO MENSUAL: ', Pago_mensual)