#Menu de Opciones
#Sumar
#Restar
#Multiplicar
#Dividir
#Select opciones
#Ingresar por teclado 2 numeros, verifique el tipo de dato
#Validar que el segundo numero no sea cero
#Realizar la operacion seleccionada
#Mostrar el resultado
#Validar que la opcion seleccionada sea correcta
#Mostrar un mensaje de error si la operacion no es correcta



#Menu    
if True:
    print("----Menu de Opciones----")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    op = int(input("Ingrese aqui su seleccion: "))
    if op < 1 or op > 4:
        print("Opcion invalida")
        op = int(input("Ingrese aqui su seleccion: "))
        
    
if op >= 1 and op <= 4:
    num1 = float(input("Ingrese el primer valor: "))
    num2 = float(input("Ingrese el segundo valor: "))
 
    if type(num1) != float and type(num2) != float:
        print("Error los tipos de los valores ingresaados no son correctos")
        
        
    if op == 1:
        print(f"La suma de {num1} y {num2} es {num1+num2}") 
    elif op == 2:
        print(f"La resta de {num1} y {num2} es {num1-num2}")
    elif op == 3:
        print(f"La multiplicacion de {num1} y {num2} es {num1*num2}")
    elif op == 4:
        if num2 == 0:
            print("Operacion no valida, no se puede dividir para cero")
        else:
            print(f"La division de {num1} y {num2} es {num1/num2}")
else:
    print("Error... Opcion no valida")    
    
input("Fin de la operacion, pulse enter para cerrar el programa")

