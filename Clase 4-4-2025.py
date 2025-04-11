#Tipos de datos
"""a=5
b=2.5
c="Hola"
d="Mundo"
e=True

print(a, "es de tipo", type(a))
print(b, "es de tipo", type(b))
print(c, "es de tipo", type(c))
print(d, "es de tipo", type(d))
print(e, "es de tipo", type(e))

#Input
nombre = input("¿Cuál es tu nombre ")
edad = int(input("¿Cuántos años tienes? "))
altura = float(input("¿Cuánto mides?" ))

print(f"Hola {nombre} tines {edad} años")
print(f"Mides", altura, "metros")

#Operaciones
num1=int(input("Introduce el primer número: "))
num2=int(input("Introduce el segundo número: "))

suma=num1+num2
resta=num1-num2
mult=num1*num2
div=num1/num2
potencia=num1**num2
divent=num1//num2
modulo=num1%num2

print("La suma es", suma)
print("La resta es", resta)
print("La multiplicación es", mult)
print("La división es", div)
print("La potencia es", potencia)
print("La division entera es", divent)
print("El módulo es", modulo)

#Condicional
a=10
b = 5

#if simpl,e
if a>b:
    print("a es mayor que b")
#if doble
if a>b:
    print(a, "es mayor que ", b)
else:
    print(b, " es mayor que ", a)

#elif
if a>b:
    print(a, "es mayor que ", b)
elif a==b:
    print(a, " es igual a", b)
else:
    print(b, " es mayor que ", a)

#if compuesto
a=10
b = 5
c=3

if a>b:
    print(a, "es mayor que ", b)
    if a>c:
            print(a, "es mayor que ", c)
    else:
            print(a, "no es mayor que ", c)
else:
    print(a, "no es mayor que ", b)
    if a>c:
         print(a, "es mayor que ", c)
    else:
        print(a, "no es mayor que ", b)"
        

#if operaciones
a=5
b=5

if b==0:
    print("Error: Division para cero")
else:
    print(a/b)

if b!=0:
    print(a/b)
else:
    print("Error: Division para cero")


#Ciclo For

for i in range(5):
    print(i)
    
for j in range(1,5+1):
    print(j)

for h in range(0,5+1):
    print(f"Tabla de {h}")
    for k in range(0,10+1):
        print(f"{h}*{k} = {k*h}")
        
for i in [0,1,2]:
    print("Mnesaje", i)
    
for i in [2,4,8]:
    print(f"El valor de {i} y su cuadrado es", i**2)
    
for i in ["Edison", 20, "Ecuador", True, 7.77]:
    print("El valor de i es", i)\
    
for i in [1,2,3,4,5]:
    for j in [1,2,3,4,5]:
        print(i, "*", j, "=", i*j)
    
for i in [1,2,3,4,5,6,7,8,9,10]:        
    resto = i%2
    print(f"El resto de {i} entre 2 es", resto)
    if resto ==0:
        print(f"El numero {i} es par")
    else:
        print(f"El numero {i} es impar")"""
        
for i in range(1,11):
    if i%2== 0:
        print(i, "es par")

for i in range(1,11):
    if i%2!= 0:
        print(i, "es impar")