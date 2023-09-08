dias_semana = ['Lunes','Martes','Miércoles','Jueves','Viernes']

#imprimir
for dia in dias_semana:
    print(dia)

#esto es un diccionario de alumnos con sus calificacioens
calificaciones = {'Pepe':[2,4,5],'Juan':[3,4,4],'Moisés': [4,3,5]}
#imprimir las claves
print("Alumnos: ")
for c in calificaciones:
    print(c)

#lista de alumnos y sus calificaciones
#primer metodo 
print("Alumnos y sus calificaciones - Método 1")
for clave in calificaciones:
    print(clave,' : ',calificaciones[clave])

#procesamos con dos for
print("Alumnos y sus calificaciones - Método 2")
for clave in calificaciones:
    print(clave)
    for calif in calificaciones[clave]:
        print(calif)


#imprimir las claves y calcular el promedio
#de los valores de la lista
