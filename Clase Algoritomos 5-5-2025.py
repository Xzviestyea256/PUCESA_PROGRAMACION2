#Fecha: 5/5/2025
#Nombre: Paul Sanchez
#Tema: Algoritmos de busqueda 

#Un algoritomo de busqueda es un algoritomo usado para encontrar un elemento en una estructura de datos
#Tipos mas comunes de busqueda: 
#Lineal: Busca un elemento en una lista o arreglo de forma secuencial, revisando cada elemento uno por uno
#No requiere ordenamiento
#Binaria: Divide el arreglo ordenado en mitades para reucir el tiempo de busqueda
#Requiere ordenamiento

#Busqueda Lineal
#Consiste en buscar elementos de una lista o arreglo de inicio a fin.
#En cada paso, compara el elemento actual con el valor que se busca (llamado objetivo o traget)

def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i  # Devuelve el índice del elemento encontrado
    return -1  # Devuelve -1 si no se encuentra el elemento

datos = [12, 5, 8, 21, 9]
print(busqueda_lineal(datos, 21))  # Salida: 3 (índice del elemento encontrado) 

#Busqueda Binaria
##Solo funciona en listas ordenadas
#Toma el elemento del medio de la lista, si es menor que el objetivo, busca en la mitad derecha 
#de la lista, si es mayor, busca en la mitad izquierda

lista = [5,3,8,6,2,7,4,1] 
for i in range(len(lista)-1):
    for j in range(len(lista)-1-i):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]
            print(lista[j], lista[j+1], end=" ")
            
print(lista)
        

lista = [1,2,3,4,5]

def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio  # Devuelve el índice del elemento encontrado
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1

    return -1  # Devuelve -1 si no se encuentra el elemento

datos_ordenados = [1, 2, 3, 4, 5]
print(busqueda_binaria(datos_ordenados, 3))  # Salida: 2 (índice del elemento encontrado)


