mi_dicccionario = {}
mi_dicccionario2 = dict()

mi_dicccionario = {}
mi_dicccionario['primer_elemento'] = 'hola'
mi_dicccionario['segundo_elemento'] = 'adios'

mi_dicccionario['primer_elemento']
mi_dicccionario['segundo_elemento']

------------------------

calificaciones = {}
calificaciones['algoritmos'] = 9
calificaciones['matematicas'] = 10
calificaciones['web'] = 8
calificaciones['bases_de_datos'] = 10

for key in calificaciones:
    print(key)




for value in calificaciones.values():
    print(value)


for key, value in calificaciones.iteritems():
    print(value, key)



suma_de_calificaciones = 0

for calificacion in calificaciones.values():
    suma_de_calificaciones += calificacion



promedio = suma_de_calificaciones / len(calificaciones.values())



