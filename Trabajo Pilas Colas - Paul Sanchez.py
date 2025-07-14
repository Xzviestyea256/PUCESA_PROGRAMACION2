print("-------------")
print("Nombre: Paul Sanchez")
print("Fecha: 16 de junio, 2025")
print("Materia: Programación II")
print("Tema: Listas, Pilas y Colas")
print("-------------")

#Ejercicio 1 Pilas:
#Creación de la clase de las Pilas
class PilaTareas:
    def __init__(self):
        self.items = []
        
    def agregar_tarea(self, tarea):
        #Agrega la tarea a la pila mediante un append
        self.items.append(tarea)
        
    def terminar_tarea(self):
        #Elimina la ultima tarea de la pila mediante un pop y la muestra
        completada = self.items.pop()
        print(f"Tarea completada: {completada}")
        
    def ver_ultima_tarea(self):
        #Muestra la tarea mas reciente agregada a la pila
        print(f"Última tarea agregada: {self.items[-1]}")
        
    def tamaño(self):
        #Muestra el tamaño de la pila (cantidad de tareas)
        print("Tamaño actual de la lsiat de tareas:", len(self.items))
        
    def lista(self):
        #Muestra la lista de tareas
        print("Lista de tareas actual:", self.items)
    
pila = PilaTareas()
#Tareas de ejemplo agregadas por defecto
#Para no andar ingreando manualmente 10 tareas
#Se llama a la función agregar_tarea para añadir las tareas a la pila
pila.agregar_tarea("Barrer")
pila.agregar_tarea("Trapear")
pila.agregar_tarea("Ordenar inventario")
pila.agregar_tarea("Colocar productos")
pila.agregar_tarea("Organizar cajas")
pila.agregar_tarea("Revisar inventario")
pila.agregar_tarea("Atender clientes")
pila.agregar_tarea("Regrezar carritos")
pila.agregar_tarea("Limpiar estantes")
pila.agregar_tarea("Mover cajas")

print("------Sistema de Tareas------")
#Menu de opciones para la lista de tareas
while True:
    print("-----Menu de Opciones-----")
    print("1. Agregar tarea")
    print("2. Completar tarea")
    print("3. Ver última tarea")
    print("4. Salir")
    #Capta la opcion elegida por el usuario
    opcion = input("Seleccione una opción (1-4): ")
    print("\n")
    
    if opcion == "1":
        #Si el usuario lo desea, puede ingresar más tareas de las que ya vienen incluidas
        tarea = input("Ingrese la tarea a agregar: ")
        #Agrega la tarea ingresadao por el usuario a la pila
        pila.agregar_tarea(tarea)
        #Muestra la lista de tareas y el tamaño de la misma
        pila.lista()
        pila.tamaño()
        print(f"Tarea {tarea} agregada.")
        print("\n")
        
    elif opcion == "2":
        #Comprueba si la pila esta vacía, si lo esta muestra un mensaje informando al usuario
        #y continua el bucle, con tal de evitar errores
        if len(pila.items) == 0:
            print("No hay tareas para completar.")
            continue
        else:
        #Si la lista tiene tareas llama la función terminar_tarea para elimiar la más reciente
        #y muestra como quedó la lista de tareas y su tamaño despues del proceso
            pila.terminar_tarea()
            pila.lista()
            pila.tamaño()
        print("\n")
        
    elif opcion == "3":
        #Muestra la última tarea agregada a la pila
        pila.ver_ultima_tarea()
        print("\n")
        
    elif opcion == "4":
        #Función para "cerrar" el sistema
        print("Saliendo del sistema...")
        break
    else:
        #Si la opcion ingresadao por el usuario en el menú no es valida, muestar un mensaje
        print("Opción no válida, intente de nuevo.")
print("\n")

#Ejercicio 2 Colas:

#Creación de la clase de las Colas con Prioridad
class ColaPrioridadClientes:
    def __init__(self):
        self.items = []
        
    def agregar_cliente(self, nombre, prioridad):
        #Agrega el nombre del cliente y su prioridad de atención  a la cola
        self.items.append((nombre, prioridad))
        
    def atender_cliente(self):
        #Primero ordena la cola según el valor de prioridad ingresado anteriormente
        self.items.sort(key=lambda x: x[1])
        #Elimina al primer elemento de la cola según su orden de priotidad (1 siendo el mas prioritario)
        atendido = self.items.pop(0)
        #Muestra un mensaje indicando el nombre del cliente atendido
        print(f"Cliente atendido: {atendido[0]}.")
        return atendido
        
    def mostrar_pendientes(self):
        #Muestra la lista de clientes por atender, ordenados según su prioridad
        print(f"Clientes pendientes: {self.items}")
        
    def tamaño(self):
        #Muestra la cantidad de clientes que hay en la lista
        print(f"Clientes por atender: {len(self.items)}")

cola = ColaPrioridadClientes()

#Clientes de ejemplo, cada uno con nombre y prioridad
#Para no andar ingresando manualmente 8 clientes
#Se llama a la función agregar_ciente para añadir cada uno a la cola
cola.agregar_cliente("Juan Arcos", 2)
cola.agregar_cliente("Ana Torres", 1)
cola.agregar_cliente("Luis Pérez", 3)
cola.agregar_cliente("María López", 4)
cola.agregar_cliente("Carlos García", 2)
cola.agregar_cliente("Sofía Martínez", 1)
cola.agregar_cliente("Pedro Sánchez", 3)
cola.agregar_cliente("Laura Jiménez", 4)

#Menú de opciones para la cola
print("------Sistema de Atención a Clientes------")
while True:
    print("-----Menu de Opciones-----")
    print("1. Agregar cliente")
    print("2. Atender cliente")
    print("3. Mostrar clientes pendientes")
    print("4. Salir")
    #Capta la opción elegida por el usuario
    opcion = input("Seleccione una opción (1-4): ")
    
    if opcion == "1":
        #Permite al usuario ingresar un nuevo cliente y su prioridad
        nombre = input("Ingrese el nombre del cliente: ")
        prioridad = int(input("Ingrese la prioridad del cliente (1-4): "))
        #Despues se llama a la función agregar_cliente para añadirlo a la cola
        cola.agregar_cliente(nombre, prioridad)
        #Finalmente se muestra al cliente ingresado y la prioridad del mismo
        print(f"Ingresado: Cliente {nombre}, con prioridad {prioridad}.")
        print("\n")
        
    elif opcion == "2":
        #Igual que en el "Sistema" anteriror, se comprueba que la cola no este vacia,
        #y si lo esta muestra un mensaje indicando la situación y continua el bucle, con tal de evitar errores
        if len(cola.items) == 0:
            print("No hay clientes para atender.")
            continue
        else:        
            #Si la cola tiene elementos llama a la funcion de atender_cliente
            #y despues muestra la lista de clientes pendientes y el tamaño de la cola
            cola.atender_cliente()
            cola.mostrar_pendientes()
            cola.tamaño()
        print("\n")

    elif opcion == "3":
        #Muestra la lista de clientes pendientes y su tamaño
        cola.mostrar_pendientes()
        print("\n")
        
    elif opcion == "4":
        #Función para "cerrar" el sistema
        print("Saliendo del programa...")
        break
    else:
        #Si la opcion ingresadao por el usuario en el menú no es valida, muestar un mensaje
        print("Opción no válida, intente de nuevo.")
        
        
#Reflexión Final
#Diferencias entre el funcionamiento de Pilas y Cola con Prioridad
    #Las Pilas funcionan con LIFO (Last in First Out), lo que hace que el ultimo elemento
    #que ingresa a la misma sea el ultimo en salir, siendo poco conveniente para casos donde
    #se necesita quitar a un elemento en especifico, ya que primero se deben de eliminar los anteriores
    
    #Las Colas con Prioridad por otro lado, funcionan con FIFO (First in First Out), lo que nos permite
    #ir eliminando primero al elemento más antiguo sin necesidad de eliminar al resto /también dependerá
    #de como se llegue a ordenar la cola. 