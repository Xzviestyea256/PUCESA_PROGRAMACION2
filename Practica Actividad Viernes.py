print("-------------")
print("Nombre: Paul Sanchez")
print("Fecha: 14 de abril, 2025")
print("Materia: Programación II")
print("Tema: Programación Orientada a Objetos en Phyton")
#Estructura orientada a objetos
print("-------------\n")

#Crea una clase que tenga los atributos: titulo, autor, anio. 
#Agrega un método que imprima un mensaje con los datos del libro.
class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        
    def mensaje(self):
        return f"Titulo del libro: {self.titulo}\nAutor del libro: {self.autor}\nAño de publicacion: {self.anio}\n"
    
Libro1 = Libro("Fabulas", "Esopo", 1999)
print(Libro1.mensaje())

    
print("-----------------\n")

#Crea una clase con atributos nombre, carrera, y nota_final. 
#Agrega un método que diga si aprobó (nota ≥ 7).

class Estudiante:
    def __init__(self, nombre, carrera, nota_final):
        self.nombre = nombre
        self.carrera = carrera
        self.nota_final = nota_final
        
    def aprobacion(self):
        if self.nota_final >= 7:
            return f"{self.nombre}, de la carrera {self.carrera} ha aprobado la materia con un {self.nota_final}"
        else:
            return f"{self.nombre}, de la carrera {self.carrera} ha reprobado la materia con un {self.nota_final}"
        
estudiante1 = Estudiante("Arturo", "Marketing", 10)
estudiante2 = Estudiante("Pepe", "Sistemas", 3)
print(estudiante1.aprobacion())
print(estudiante2.aprobacion())
print("")

print("-----------------\n")

#Crea una clase base Vehiculo con el método moverse. 
#Crea una clase Auto que herede de Vehiculo y sobrescriba el método.

class Vehiculo:
    def moverse(self):
        print(f"Vehiculo en movimiento")
    
class Auto(Vehiculo):
    def moverse(self):
        print(f"El vehiculo se mueve")
        
Auto1 = Auto()
Auto1.moverse()
print("")

print("-----------------\n")

#Crea dos clases: Pajaro y Gato, cada una con el método sonido(). 
#Luego, usa una función que reciba un objeto y llame al método sonido().

class Pajaro:
    def sonido(self):
        print("Tweet")

class Gato:
    def sonido(self):
        print("Miau")
        
def funcion_sonido(animal):
    animal.sonido()

pajaro = Pajaro()
gato = Gato()

funcion_sonido(gato)
funcion_sonido(pajaro)