#Crea una clase que tenga los atributos: titulo, autor, anio. 
#Agrega un método que imprima un mensaje con los datos del libro.

titulo=["Libro 1", "Libro 2", "Libro 3", "Libro 4"]
autor=["Montalvo", "Sanchez", "Arcos", "Glumbunny"]
anio=["1900", "2006", "2005", "2021"]

class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        
    def mensaje(self):
        return f"Titulo del libro: {self.titulo}\nAutor del libro: {self.autor}\nAño de publicacion: {self.anio}\n"

for i in range(len(autor)):
    librox = Libro(titulo[i], autor[i], anio[i])
    print(librox.mensaje())