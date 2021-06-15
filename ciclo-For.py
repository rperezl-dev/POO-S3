class For:
    def __init__(self):
        pass

    #ciclo repetitivo de los incrementos o decrementos se ejecuta mientras tenga valores
    def usoFor(self):
        nombre='Daniel'
        datos = ['Daniel', 50, True]
        numeros = (2, 5, 6, 4, 1)
        docente = {'nombre':'Daniel', 'edad':50, 'fac':'faci'}
        listaNotas = [(30,40), [20,40],(50,40)] #Elemento coleccion: coleccion de elementos de cualquier tipo
        listaAlumnos= [{'nombre':'Erick','final':70},{'nombre':'Yadi','final':60},{'nombre':'Danny','final':90}]
        #range([inicio=0],limite,[inc/dec=1]). Genera un rango de valores desde un valor inicial a un valor final
        #se ejecuta desde inicio hasta el limite
        #for i in range(5): #rango (0,1,2,3,4)
        #    print('i={}'.format(i))
        #for i in range(2,10): #rango (2,3,4,5,6,7,8,9)
        #    print('i={}'.format(i))
        #for i in range(4,10,2):  # rango (4,6,8)
        #    print('i={}'.format(i), end=' ') #end sale en forma horizontal
        #for i in range(12,3,-3):  # rango (4,6,8) #Cuando rango inicial es mayor; va de mayor a menor
        #    print('i={}'.format(i), end=' ')

        longitud = len(datos)
        #print(datos[0])# len trabaja en listas, tuplas y diccionarios
        #print(datos[1])
        #print(datos[2])
        #j=0
        #while j < longitud:
        #    print('while',datos[j])
        #    j+=1 #j=j+1

        #for i in range(longitud-1,-1,-1):
        #    print('for',datos[i])

        #for i,dato in enumerate(datos):#enumerate solo aplicable a las listas y tuplas
        #    print('for',i,dato)
        # dato toma cada elemento de la coleccion nuos(cadena,kista,tupla)

        #for dato in numeros:#enumerate solo aplicable a las listas y tuplas
        #    print(dato)

        #for dato in ['H','o','l','a','que','tal']:
        #    print(dato)

        print('\n Diccionario de notas')
        #for clave,valor in docente.items():
        #    print(clave,':',valor,end=' ')

        for alumnos in listaAlumnos:
            for clave, valor in alumnos.items():
                print(clave, ':', valor, end=' ')
            print()


#usar la clase es instanciar
bucle1=For()
bucle1.usoFor()