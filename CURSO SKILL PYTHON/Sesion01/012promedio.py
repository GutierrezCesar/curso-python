#el programa calcula y muestra el promedio de un alumno

print('Este programa calcula el promedio de 3 calificaciones de un alumno'
      '\n')

nombre=input('Escribe tu nombre alumno: ')
mat=float(input('Escribe tu calif. de matemáticas: '))
fis=float(input('Escribe tu calif de física: '))
quim=float(input('Escribe tu calif. de química: '))

'''prioridad de los operadores
exponenciación y () están en primer lugar
* /                 están en segundo lugar
+ -                 están en tercer lugar
'''

prom=(mat+fis+quim)/3
if (prom<6):
    print(nombre,'Estas reprobado, tu promedio es: ',round(prom,2))
else:
    print(nombre,'Estas aprobado, tu promedio es: ',round(prom,2))




