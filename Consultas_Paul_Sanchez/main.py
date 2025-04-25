from funciones import reg_paciente, reg_consulta, mostrar_paciente, mostrar_todo, mostrar_todo_cons

print("-------------")
print("Nombre: Paul Sanchez")
print("Fecha: 21 de abril, 2025")
print("Materia: Programación II")
print("Tema: Programación Orientada a Objetos en Phyton")
print("Modularizacion")
print("-------------")

def menu_main():
    while True:
        print("-------------SISTEMA DE REGISTRO DE PACIENTES-------------")
        print("1. Registrar Paciente")
        print("2. Registrar Consulta")
        print("3. Mostrar Paciente")    
        print("4. Mostrar todos los Pacientes")
        print("5. Mostrar todas las consultas")
        print("6. Salir")
        
        opcion_sis = int(input("Seleccione una opción: "))
        
        if opcion_sis == 1:
            reg_paciente()
        elif opcion_sis == 2:
            reg_consulta()
        elif opcion_sis == 3:
            mostrar_paciente()
        elif opcion_sis == 4:
            mostrar_todo()
        elif opcion_sis == 5:
            mostrar_todo_cons()
        elif opcion_sis == 6:
            print("Cerrando sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")
            
if __name__ == "__main__":
    menu_main()
