#CALCULAR EL PRECIO DE VENTA
print('PRECIO DE VENTA')
a=float(input('INGRESE VALOR DE VENTA DEL PRODUCTO: '))
#OPERACIONES
IGV = a*0.18
PV = a + IGV

#SALIDA DE DATOS
print('='*25)
print('-------FACTURA DE VENTA-------')
print('='*25)
print('IGV: ', IGV)
print('Precio de venta: ', PV)