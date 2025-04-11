#funciones def
#Parametros y argumentos
"""def funcion(nombre):
    print("Texto", nombre)

funcion("txt2")
print("\n")

#Argumentos Posicionales y Nominales
#Posicionales: Asocian parametros de la funcion en el mismo orden que aparecen en la definicion de la funcion, van en orden
#Nominales: Se indica explicitamente el nombre del paramnetro al que se asocia un argumento de la forma parametro = argumento
#Estos dos se pueden mesclar, python toma el valor del primero que NO tenga definido un =

def datos(nombre, apellido):
    print("Texto 1", nombre, apellido)
datos("Paul", "Sanchez") #Argumentos posicionales
datos(nombre="Paul", apellido="Sanchez") #Argumentos nominales
print("\n")

#Retorno de una funcion
def area_tri(base, altura):
    calc=base*altura/2
    print(calc)
area_tri(2,3)
area_tri(4,5)
print("\n")"""

#Argumentos por defecto

def welcome(nombre, lenguaje = "Phyton"):
    print("Bienvenido a", lenguaje, nombre + "1") #Aqui va a dar error
welcome("Texto")
welcome("Texto", "PHP")
#Los parametros con arguemnto por defecto deben inidcarse dcespues despues de los parametros sin argumentos por defecro. De lo contrario se produce un error
print("\n")

# *parametro: Se antepone un asterisco al nombre del parametro y en la invocacion de la funcion se pasa el numero variable de argumentos separados por comas
def menu(*platos):
    print("Hoy tenemos: ", end="")
    for plato in platos:
        print(plato, end=", ")
menu("Pasta", "Pizza", "Ensalada") #Lista de parametros
print("\n")

# **parametro: Se anteponen Dos asteriscos al nombre delm aprametro y a la invocacion de la funcion variable de arguementos por pares nombre = valor, separados por comas
def contacto(**info):
    print("Datos del contacto")
    for clave, valor in info.items():
        print(clave, ":", valor)
contacto(nombre= "Paul", Email = "correo@gmail.com") #Se puede mandar infinidad parametros siempre y cuando se respeta el orden y contenido para estos valores
print("\n")
contacto(nombre = "Paul", Email = "correo@gmail.com", direccion = "Ambato")
print("\n")



