print("-------------")
print("Nombre: Paul Sanchez")
print("Fecha: 9 de junio, 2025")
print("Materia: Programación II")
print("Tema: Listas, Pilas y Colas")
print("Historial de navegación con Pilas")
print("-------------")

#Objetivo: Simular el comportamiento de un  navegador web utilizando uan pila para registrar el historial

#Paso 1: Creación de la Pila
historial = []
print("Historial:", historial)

#Paso 2: Agregar páginas a la Pila
historial.append("www.google.com")
historial.append("www.python.org")
historial.append("www.stackoverflow.com")
print("Historial:", historial)

#Paso 3: Mostrar los elementos de la pila si la misma tiene elementos
if len(historial) >= 0:
    print("Pagina actual:", historial[-1])
else:
    print("No hay páginas en el historial")
    
#Paso 4: Preguntar al usuario si desea "Volver" a la págian anterior, si lo hace 
#Elimina la página mas reciente y vuelve a preguntar. El proceso para si ya no hay elementos en la Pila
while True:
    seleccion = int(input("Desea volver a la página anterior? 1 para volver, 2 para cancelar: "))

    if seleccion == 1:
        eliminada = historial.pop()
        print("Volvieste desde:", eliminada)
        if len(historial) == 0:
            break
        print("Página actual:", historial[-1])

    elif seleccion == 2:
        print("")
        break
    else:
        print("No es posible volver, el historial está vacio")
        break
        
#Paso 5: Si la Pila no tiene elementos para este punto muestra un mensaje con esa información,
#Si aun tiene elementos, los muestra
if len(historial) == 0:
    print("El historial está vacío")
else:
    print("Páginas restantes:", historial)