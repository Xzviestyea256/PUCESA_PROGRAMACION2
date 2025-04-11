#La programacion orientada a objetos es un paradigma de programacion
#Consiste en partir el codigo para poderlo reutilizar e invocar esas funciones mas adelante
#En phyton las funciones son objetos como el resto dee tipos de datos, de manera que es posible asignar una funcion a una variable y 
#utilizar la variable para hacer la llamada a la funcion

#Funciones recursivas: Invoca la funcion detro de la funcion

#def cuenta_regresiva(numero):
#    numero -=1
#    if numero > 0:
#        print(numero)
#       cuenta_regresiva(numero)
#  else:
#        print("Explosion")
#    #print("Fin de la funcion", numero) 
#cuenta_regresiva(5)
#print("\n")

#Una clase en phyton es un pakno para crear objetos
"""class Persona:
    def __init__(self, nombre, edad, ocupacion): #init es un metodo, se centra en la creacion de clases y inilizacion de atributos
        #es como el formato de la funcion
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion
        #self es el lugar donde se guardan parametros
    
    def descripcion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, ocupacion: {self.ocupacion}"

#Crea objetos de tipo persona   
persona1 = Persona("Juan", 30, "Ingeniero")
persona2 = Persona("Maria", 25, "Doctora")

#Mostramos el contenido de cada uno de los objetos
print(persona1.descripcion())
print(persona2.descripcion())"""


class Persona:
    def __init__(self, nombre, edad, ocupacion): #init es un metodo, se centra en la creacion de clases y inilizacion de atributos
        #es como el formato de la funcion
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion
        #self es el lugar donde se guardan parametros
    
    def descripcion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, ocupacion: {self.ocupacion}"

def mostrar_menu():
    print("---Gestion de Personas---")
    print("1. Agregar Persona")
    print("2. Mostrar todas las personas")
    print("3. Buscar personas por nombre")
    print("4. Salir")
    
personas=[]
    
while True:
    mostrar_menu()
        
    opcion = input("Seleccione una opcion.  ")
        
    if opcion == "1":
        nombre = input("Ingrese el nombre de la perosna: ")
        edad = int(input("Ingrese la edad de la persona: "))
        ocupacion = input ("Ingrese la ocupacion de la persona: ")
        nueva_persona = Persona(nombre, edad, ocupacion)
        personas.append(nueva_persona)
        print(f"La persona {nombre}, ha sido agregada.")
            
    elif opcion == "2":
        if len(personas) > 0:
            print("\n--- Lista de Personas ---")
            for persona in personas:
                print(persona.descripcion())
            else:
                    print("No hay personas en la lista.")
        
    elif opcion == "3":
        if len(personas) > 0:
            nombre_buscar = input("Ingrese el nombre de la persona a buscar: ")
            encontrada = False
            for persona in personas:
                if persona.nombre.lower() == nombre_buscar.lower():
                    print("Persona encontrada: ")
                    print(persona.descripcion())
                    encontrada  = True
                    break
                if not encontrada:
                    print(f"No se encontro a {nombre_buscar} en la lista.")
            else: 
                print("No hay personas en la lista")
                
    elif opcion == "4":
        print("Hasta luego")
        break
    else:
        print("Opcion no valida, seleccione una opcion valida")