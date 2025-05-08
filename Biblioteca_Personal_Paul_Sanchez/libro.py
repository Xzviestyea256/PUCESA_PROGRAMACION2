class Libro:
    def __init__ (self, titulo, autor, ISBN, genero):
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        #ISBN: Codigo de 13 digitos
        self.genero = genero

    def info_libros(self):
        print(f"\nTítulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"ISBN: {self.ISBN}")
        print(f"Género: {self.genero}") 

        
