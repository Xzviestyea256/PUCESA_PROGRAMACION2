print("----------")
print("Nombre: Paul Sanchez")
print("Fecha: 5 de mayo, 2025")
print("Tema: Algoritmos de busqueda")
print("----------")
input("Presione enter para continuar")
print("---------------------------------")

print("Actividad Práctica 1")
print("---------------------------------")

def busq_fruta(lista, objetivo):
    #Funcion que busca el valor str ingresado por el usuario (opcion = objetivo) 
    #en la lista de frutas (frutas = lista)
    operaciones = 0
    #Variable que resetea el numero de operaciones realizadas cada que se busca un elemento
    #en la lista, seria más util si el programa no terminara despues de mostra los valores
    #solicitados.
    for i in range(len(lista)):
        #Bucle for que recorre la lista de frutas
        operaciones += 1
        #Suma 1 a la variable operaciones cada vez que se repite el proceso
        if lista[i] == objetivo:
            return i, operaciones
        #Si el elemento en la lista es igual al str ingresado por el usuario,
        #retorna la posicion en la que se encuentra el elemento y el 
        #numero de operaciones realizadas
    return -1, operaciones
    #Si el elemento no se encuentra en la lista, retorna -1 
    #y el numero de operaciones realizadas

frutas = ["manzana", "banana", "naranja", "kiwi", "mango", "pera", "uva", "sandia", "piña", "cereza"]
#Lista de frutas
opcion = input("Ingrese una fruta: ") #Input que guarda el valor str ingresado por el usuario
opcion = opcion.lower() #Convierte el str ingresado por el usuario a minusculas

poscicion, operaciones = busq_fruta(frutas, opcion)
#Tupla que contiene la posición y el número de operaciones realizadas
#Permite almacenar los valores de la posición y el número de operaciones realizadas
#en dos variables distintas, pero que dependen de una sola funcion para obtener su valor.
#Se toma la lista de frutas y el str ingresado por el usuario como argumentos de la funcion
#para obtener la posición y el número de operaciones realizadas, gracias a la funcion.

if poscicion != -1:
    print(f"La fruta {opcion} se encuentra en la posición: {poscicion}")
    #Print que muestra la posicion en la que se encuentra la fruta ingresada por el usuario
    #si esta se encuentra en la lista de frutas, para eso la funcion no debe retornar
    #el valor -1
else:   
    print(f"La fruta {opcion} no se encuentra en la lista")
    #Print que muestra que la fruta ingresada por el usuario no se encuentra en la 
    #lista de frutas, solo se muestra si la funcion retorna el valor -1

print(f"Número de operaciones realizadas: {operaciones}")
#Print que muestra el número de operaciones realizadas para encontrar la fruta, si la fruta
#no se encuentra en la lista, el número de operaciones realizadas sera 10, el numero de 
#elementos de la lista.
print("---------------------------------")
input("Presione enter para continuar")
print("---------------------------------")

print("Actividad Practica 2")
print("---------------------------------")

def busq_binaria(lista, objetivo):
    #Funcion que se encarga de buscar el valor ingresado por el usuario dentro de 
    #la lista, que está ordenada de menor a mayor.
    inicio = 0
    #Variable que determina en donde inicia la "partición" de la lista, ira cambiando
    #de valor si no se encuentra el elemento que se busca en la lista.
    fin = len(lista) - 1
    #Variable que determina donde termina la "particion" de la lista, de igual manera
    #ira cambiando de valor si no se encuentra el elemento que se busca en la lista.
    contador = 0
    #Variable que lleva un registro del numero de veces que se realiza una
    #"particion" de la lista
    while inicio <= fin:
    #Bucle while quue se mantrendra activo miestras el valor de inicio sea menor
    #o igual al valor de fin.
        medio = (inicio + fin) // 2
        #Variable medio, su valor se basa en la suma de los valores de inicio y fin,
        #dividido entre 2, esto permite saber el punto medio de la "partición" de la lista
        #Ira variando cada vez que se realice una nueva "partición" y el valor de inicio
        #y fin cambie.
        contador += 1
        #Suma 1 al valor del contador ya que se ha realizado una nueva "partición"
        if lista[medio] == objetivo:
            #If que revisa si el valor del medio coincide con el elemento que se busca
            return medio, contador
        #return que devuelve el valor donde se encontró el elemento y el numero de veces 
        #que se realizó una "partición" de la lista
        elif lista[medio] < objetivo:
            #eif que actua si el valor del medio es menor al elemento que se busca
            inicio = medio + 1
            #Si el valor que se encuentra en la posicion determinada por el medio es menor 
            #al elemento que se busca, se modifica el valor de inicio sumandole 1 al valor
            #medio, asi se podra volver a realizar el calculo del valor medio y partir la
            #lista para encontrar el elemento buscado.
        else:
            fin = medio - 1
            #Si ninguno de los parámetros anteriores se cumple, se modifica el valor de fin
            #restandole 1 al valor medio, para que se pueda volver a realizar el calculo del
            #valor medio y partir la lista para encontrar el elemento buscado.
    return -1, contador
#Return que devuelve -1 como posicion del elemento si el mismo no se encuentra en la lista
#y el numero de veces que se realizó una "partición" de la lista.

numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#Lista que contiene valores del 10 al 100 en intrervalos de 10
buscar = int(input("Ingrese el número a buscar: "))
#Variable que almaecena un valor ingresado por el usuario, debe ser un valor numerico

poscicion2, contador = busq_binaria(numeros, buscar)
#Tupla que contiene la posición del elemento y el número de "particiones" de la lista

if poscicion2 != -1:
    #If que comprueba que el valor de la posicion del elemento no sea -1, si no lo es
    #muestra un mensaje indicando la posicion en la lista del mismo
    print(f"El número {buscar} se encuentra en la posición: {poscicion2}")
else:
    #else que actua si el valor ingresado no esta en la lista, muestra un mensaje
    #indicando que el elemento no se encuentra en la lista
    print(f"El número {buscar} no se encuentra en la lista")
    
print(f"La lista se partió: {contador} veces")
#print que muestra el numero de veces que se realizó una "partición" de la lista


#Con respecto a las tuplas:
#Mi idea original era que los contadores se ubicaran dentro de la funcion de busqueda de cada 
#actividad, cuando se imprimia el resultado de la busqueda de un elemento no presente en la lista,
#me tiraba el mensaje de exito, cosa que no queria. Tras darle unas vueltas y buscar en internet 
#di con la solución de las tuplas, cosa que por alguna razón no se me habia ocurrido.