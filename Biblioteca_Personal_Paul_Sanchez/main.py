from funciones_libros import reg_libro, reg_prestamo, most_libro, all_libros
def separador():
    print("\n---------------------------------------------")
    
def libros_main():
    while True:
        print("----------Sistema de Biblioteca----------")
        print("1. Registrar nuevo libro")
        print("2. Registrar un préstamo")
        print("3. Mostrar información de un libro")
        print("4. Mostrar todos los libros")
        print("5. Salir del sistema")
        
        try:
            ops = int(input("Ingrese una opcion para continuar: "))
        except ValueError:
            print("Un error ha ocurrido, porfavor ingrese los datos correctamente")
            ops = int(input("Ingrese una opcion para continuar: "))
            
        separador()
        
        if ops == 1:
            reg_libro()
            separador()
        elif ops == 2:
            reg_prestamo()
            separador()
        elif ops == 3:
            most_libro()
            separador()
        elif ops == 4:
            all_libros()
            separador()
        elif ops == 5:
            print("Saliendo del sistema...")
            break
        
if __name__ == "__main__":
    libros_main()