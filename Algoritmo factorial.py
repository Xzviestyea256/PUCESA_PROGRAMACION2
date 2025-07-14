izq=[]
der=[]
procesos = 0

palabra = "anita lava la tina"
palabra = palabra.lower().replace(" ", "")
mitad = len(palabra) // 2 +1
print(mitad)

for i in range(mitad):
    letra = palabra[i]
    izq.append(letra)
    procesos += 1

for j in range(mitad):
    letrr = palabra[-1 -j]
    der.append(letrr)
    procesos += 1

print(izq)
print(der)

if izq == der:
    print(f"La palabra {palabra} es un palindromo ")
else:
    print(f"La palabra {palabra} no es un palindromo ")
    
print(f"Procesos realizados: {procesos}")
