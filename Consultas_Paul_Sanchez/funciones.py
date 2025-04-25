print("-------------")
print("Nombre: Paul Sanchez")
print("Fecha: 21 de abril, 2025")
print("Materia: Programación II")
print("Tema: Programación Orientada a Objetos en Phyton")
print("Modularizacion")
print("-------------")

from paciente import Paciente

pacientes = []
consultas = {}

def reg_paciente():
    nombre = input("Ingrese el nombre del paciente: ")
    cedula = input("Ingrese la cédula del paciente: ")
    edad = input("Ingrese la edad del paciente: ")
    tip_blod = input("Ingrese el tipo de sangre del paciente: ")
    paciente = Paciente(nombre, cedula, edad, tip_blod)
    pacientes.append(paciente)
    
def buscar_paciente(cedula):
    for pac in pacientes:
        if pac.cedula == cedula:
            return pac
    return None     

def agregar_consulta(cedula, fecha, diagnostico, tratamiento):
    crea_consulta = {
        "cedula": cedula,
        "fecha": fecha,
        "diagnostico": diagnostico,
        "tratamiento": tratamiento
    }
    if cedula not in consultas:
        consultas[cedula] = []

    consultas[cedula].append(crea_consulta)
    
def reg_consulta():
    cedula = input("Ingrese la cédula del paciente: ")
    fecha = input("Ingrese la fecha de la consulta: ")
    diagnostico = input("Ingrese el diagnostico: ")
    tratamiento = input("Ingrese el tratamiento: ")
    
    agregar_consulta(cedula, fecha, diagnostico, tratamiento)
    print("Consulta registrada con exito.")

def mostrar_paciente():
    cedula = input("Ingrese la cédula del paciente: ")
    paciente = buscar_paciente(cedula)
    if paciente:
        paciente.mostrar_datos()
    else:
        print("Paciente no encontrado.")
    

def mostrar_todo():
    if not pacientes:
        print("No hay pacientes registrados.")
    for pac in pacientes:
        pac.mostrar_datos() 
        
def mostrar_todo_cons():
    if not consultas:
        print("No hay consultas registradas.")
        return
    
    print("\n")
    for cedula, i in consultas.items():
        print(f"\nPaciente con cédula: {cedula}")
        for j in range(len(i)):
            consulta = i[j]
            print(f"Consulta #{j + 1}")
            print(f"Fecha: {consulta['fecha']}")
            print(f"Diagnóstico: {consulta['diagnostico']}")
            print(f"Tratamiento: {consulta['tratamiento']}")