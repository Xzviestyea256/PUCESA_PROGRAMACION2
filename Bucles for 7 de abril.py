"""for i in range(0, 2+1):
    print("Tabla del", i)
    for j in range(0, 2+1):
        for k in range(0, 2+1):
            print(i, "*", j, "+", k,"=", (i*j)+k)
        
    
for t in [1,2,3]:
    print("Texto1 ", end="")
        
#
for r in [1,2,3]:
    print("El cuadrado de ", r**2)
print("\n")
    
#
for i in [1,2,3,4,5]:
    print("Tabla del", i)
    for j in [5,4,3,2,1]:
        print(i, "*", j, "=", i*j)"""

#
Num=[0,1,2,3,4,5,6,7,8,9,10]
for h in Num:
    resid = h%2
    if resid == 0:
        print(h, "es par")
for h in Num:
    resid = h%2
    if resid != 0:
        print(h, "es impar")