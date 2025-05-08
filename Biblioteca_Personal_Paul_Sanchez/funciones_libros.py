from libro import Libro

libros = []
lst_prest = {}

def reg_libro():
    try:
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        ISBN = int(input("Ingrese el ISBN del libro (13 dígitos): "))
        genero = input("Ingrese el género del libro: ")
    except ValueError: 
        print ("Un error ha ocurrido, porfavor ingrese los datos correctamente")
        return
    else:
        for comp in range (len(libros)):
            if libros[comp].ISBN == ISBN:
                print("El libro ya esta registrado")
                break
        libro = Libro(titulo, autor, ISBN, genero)
        libros.append(libro)

def buscar_libro(ISBN):
    for inf in libros:
        if inf.ISBN == ISBN:
            return inf
    return None

def agregar_prestamo(ISBN, nombre, fe1, fe2):
    prest = {
    "ISBN": ISBN,
    "Nombre": nombre,
    "Fecha inicial": fe1,
    "Fecha limite": fe2
        }
    if ISBN not in lst_prest:
        lst_prest[ISBN] = []
        
    lst_prest[ISBN].append(prest)


def reg_prestamo():
    try:
        ISBN = int(input("Ingrese el ISBN del libro: "))
        nombre = input("Ingrese el nombre del prestario: ")
        fe1 = input("Ingrese la fecha de inicio del prestamos (día/mes/año): ")
        fe2 = input("Ingrese la fecha de fin del prestamos (día/mes/año): ")
    except ValueError:
        print("Un error ha ocurrido, porfavor ingrese los datos correctamente")
        return
    else:
        agregar_prestamo(ISBN, nombre, fe1, fe2)
        print("Prestamo registrado")
    
def most_libro():
    ISBN = int(input("Ingrese el ISBN del libro: "))
    libro = buscar_libro(ISBN)
    if libro:
        libro.info_libros()
    else:
        print("El libro no se encuentra registrado en el sistema")
    try:
        print(f"Prestamos del libro: {lst_prest[ISBN]}\n")
    except KeyError:
        print("No hay prestamos registrados para este libro")

def all_libros():
    if not libros:
        print("No hay libros registrados en el sisrema")
        return
    for inf in libros:
        inf.info_libros()