print("-------------")
print("Nombre: Paul Sanchez")
print("Fecha: 13 de junio, 2025")
print("Materia: Programación II")
print("Tema: Listas, Pilas y Colas")

print("-------------")

# Cola: Estructura de datos lineal que sigue el principio FIFO (First In, First Out) 
from collections import deque

#Operaciones Basicas de una cola
# Encolar: Agregar un elemento al final de la cola
    #enqueue(): Agrega un elemento al fianl de la cola
    #dequeue(): Elimina el elemento al frente de la cola
    #is_empty(): Verifica si la cola esta vacia
    #peek() o front(): Muestra el elemento al frente sin eliminarlo
    #ssize(): Retorna el tamaño de la cola
    
cola = deque() #La lista esta internamente, no hace falta declararla

#Agrega elementos
cola.append("A")
cola.append("B")
cola.append("C")
print(cola)

#Eliminar primer elemento
primero = cola.popleft() #o pop(0)
print("Elemento atendido:", primero)
print("Cola actual:", cola)