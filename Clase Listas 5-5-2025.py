#Fecha: 5 de mayo, 2025
#Nombre: Paul Sanhcez
#Tema: Listas y arreglos 

#Un arreglo es somilar a una lista, está más enfocado en valores del mismo tipo
#Es mas eficiente en el suo de memoria
#Para trabajar con arreglos se usa array de la libreria estandar o numppy.array para procesamiento numerico

n = [5, 8, 2 ,9 ,1]
for num in n:
    print(num)

#Esto mes un arreglo, son elementos de un mismo tipo y opero con ellos
suma = 0
for num in n:
    suma += num     
print("Suma total: ",suma)

#Busqueda de un numeros mayor en una lista (algoritmo lineal)
n2 = [12, 45, 3, 22, 89, 5]
mayor = n2[0]
for num in n2:
    if num > mayor:
        mayor = num
print(n2)
print("El mayor es: ", mayor)


n3 = [4, 7, 10, 3, 2, 9, 8]
pares = 0
for num in n3:
    if num % 2 == 0:
        pares += 1
print("Cantidad de pares: ", pares)


ncuadrados= []
for i in range(1, 6):
    ncuadrados.append(i**2)
print("Cuadrados: ", ncuadrados)

