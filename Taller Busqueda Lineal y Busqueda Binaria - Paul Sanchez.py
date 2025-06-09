print("----------")
print("Nombre: Paul Sanchez")
print("Fecha: 19 de mayo, 2025")
print("Tema: Algoritmos de busqueda")
print("Taller Busqueda Lineal y Busqueda Binaria")
print("----------\n")

#1. Explicación Teóroca
#¿Qué es la búsqueda lineal? ¿Cómo funciona?
    #Es un método de busqueda que busca un elemento (usualmente ingresado por el usuario)
    #dentro de una lista de elementos, comparando cada elemento de inicio a fin de la 
    #con el objetivo (o target)

#¿Qué es la búsqueda binaria? ¿Qué condicion especial debe cumplir la lista?
    #Es un método de busqueda que busca un elemento (usualmente un numero) dentro de una lista
    #de elementos, para buscar su objetivo se divide la lista en 2 y se toma el valor medio de 
    #la lista, si el valor medio es el objetivo la busqueda termina, si no se compara con los 
    #valores adyacentes, dependiendo de cual número se acerque más al objetivo (mayor o menor)
    #se tomará una mitad de la lista y se volverá a dividir para continuar con la busqueda 
    #hasta encontar el objetivo
    #La condicion que la lista debe cumplir para la búsqueda binaria es que este ordenada, si 
    #no esta ordenada la busqueda no sería efectiva, ya que no hay forma para el algoritomo de 
    #que sepa si el valor buscado está a la izquierda o derecha

#¿En que casos conviene cada una?
    #La busqueda lineal es más conveniente cuando se buscan un elemento en una lista pequeña
    #(Yo diría entre 2 a 15 elementos)
    #La búsqueda n¿binaria conviene más cuando se trabaja con listas de datos relativamente grandes
    #que con busqueda lineal tardaria más tiempo en encontrar un elemento

#2. Desarrollo práctico 

productos = [
    "Jabon", "Leche", "Arroz", "Sal", "Azucar", "Aceite", "Cereal", 
    "Galletas", "Desinfectante", "Deja", "Cebolla", "Acelga", "Queso",
    "Carne", "Pollo", "Pescado", "Verdura", "Fruta", "Pan", "Cafe"
]

busquedas = []

print("----------")
print("Sistema de Busqueda de Productos")
print("----------\n")


while True:
    opcion = input("Ingrese el nombre del producto que desea buscar: ").strip().lower()
    busquedas.append(opcion)
    
    print("\n")
    print("----------")
    print("Busqueda Lineal")
    print("----------\n")

    operaciones = 0
    fin_lineal = False

    for i, producto in enumerate(productos):
        operaciones += 1
        if producto.lower() == opcion:
            print(f"El producto {opcion} se encuentra en la posición {i+1}")
            fin_lineal = True
            break
        
    if not fin_lineal:
        print(f"Producto {opcion} no encontrado en la lista")
    print(f"Operaciones realizadas para la busqueda lineal: {operaciones}")
    operaciones = 0
    print(f"----------\n")
    
    
    print("----------")
    print("Busqueda Binaria")
    print("----------\n")

    productos_ordenados = sorted(productos, key=lambda x: x.lower())
    
    operaciones2 = 0
    inicio = 0
    fin_lista_bin = len(productos_ordenados) - 1
    fin_binario = False

    while inicio <= fin_lista_bin:
        operaciones2 += 1
        medio = (inicio + fin_lista_bin) // 2
        producto_medio = productos_ordenados[medio].lower()
        
        if producto_medio == opcion:
            print(f"El producto {opcion} se encuentra en la posición {medio}")
            fin_binario = True
            break
        elif producto_medio < opcion:
            inicio = medio + 1
        else:
            fin_lista_bin = medio - 1

    if not fin_binario:
        print(f"Producto {opcion} no encontrado en la lista")
        
    print(f"Operaciones realizadas para la busqueda binaria: {operaciones2}")
    operaciones2 = 0
    print(f"----------\n")

    continuar = input("¿Desea buscar otro producto? (si/no): ").strip().lower()
    if continuar != 'si':
        print("Resumen de productos buscados: ")
        for j in range(len(busquedas)):
            print(f"{busquedas[j]}")
            
        print("Cerrando programa...")
        break