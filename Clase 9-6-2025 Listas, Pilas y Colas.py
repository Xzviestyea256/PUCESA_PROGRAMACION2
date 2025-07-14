print("-------------")
print("Nombre: Paul Sanchez")
print("Fecha: 9 de junio, 2025")
print("Materia: Programación II")
print("Tema: Listas, Pilas y Colas")

print("-------------")

#Pila: Estructura de datos lineal, que sigue el principio LIFO (Last In, First Out)

#Metodo Push insertar un elemento en el tope de la lista
pila = [] #pila vacia
pila.append("Plato 1")
pila.append("Plato 2")
pila.append("Plato 3")

print(pila)

#Metodo pop(): Elimina el elemento en el topde de la lista
elemento=pila.pop()

print(pila)

#metodo peek: Ver tope de la pila sin eliminarlo
if pila:
    print("Elemento en el tope de la pila", pila[-1])

#Metodo isEmpty: verificar si la pila esta vacia
if len(pila) == 0:
    print("La pila esta vacia")
else:
    print("La pila no esta vacia")
    
    
pila2 = []
#Push
pila2.append("A")
pila2.append("B")
#Peek
print("Tope:", pila2[-1])
#Pop
print("Elemento retirado: ", pila2.pop())
#isEmpty
print("¿Pila vacía?", len(pila2) == 0)


#Ejercicios de practica
#1
pila3 = []
pila3.append("uno")
pila3.append("dos")
pila3.append("tres")
print("Contenido de la pila:", pila3)

ultimo=pila.pop()
print("pila sin el ultimo elemento: ", pila)
print("Elemento eliminado", ultimo)

print("Tope de la pila: ", pila3[-1])

print("¿Pila vacía?", len(pila3) == 0)

#Gestión de Tareas Pendientes con una Pila

tareas = []
completadas = []

#Agregar tareas a la Plia (push)
tareas.append("Estudiar pilas en Python")
tareas.append("Hacer ejercicios de estructuras de datos")
tareas.append("Leer documentación oficial de Python")
print("Tareas pendientes:", tareas)

#Ver la tarea más reciente soon eliminarla (peek)
if tareas:
    print("Tarea más reciente:", tareas[-1])
else:
    print("No hay tareas pendientes.")

#Marcar tarea como completada (pop), y agregandolas a la lista de completdas con (push)
while len(tareas) >= 0: 
    if tareas:
        completada = tareas.pop()
        print("Tarea completada:", completada)
        completadas.append(completada)
        print("Tareas pendientes:", tareas)
    else:
        print("No hay tareas para completar.")
        break

#Verificar si quedan tareas pendientes (isEmpty)
if len(tareas) == 0:
    print("Tareas completadas:", completadas)
    print("Todas las tareas han sido completadas.")
    
else:
    print("Tareas restantes:", tareas)