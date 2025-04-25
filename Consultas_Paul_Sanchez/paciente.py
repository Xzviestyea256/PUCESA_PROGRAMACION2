print("-------------")
print("Nombre: Paul Sanchez")
print("Fecha: 21 de abril, 2025")
print("Materia: Programación II")
print("Tema: Programación Orientada a Objetos en Phyton")
print("Modularizacion")
print("-------------")

class Paciente:
    def __init__(self, nombre, cedula, edad, tip_blod):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.tip_blod = tip_blod

    def mostrar_datos(self):
        print(f"\nNombre: {self.nombre}")
        print(f"Cédula: {self.cedula}")
        print(f"Edad: {self.edad}")
        print(f"Tipo de Sangre: {self.tip_blod}\n")
        


        