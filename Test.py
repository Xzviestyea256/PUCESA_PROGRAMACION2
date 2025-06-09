catalogo = [
    "Cien años de soledad", "Don Quijote", "Rayuela", "El Principito", 
    "Fahrenheit 451", "Crimen y castigo", "1984", "Los miserables",
    "Orgullo y prejuicio", "La Odisea", "La Ilíada", "Moby Dick", 
    "Ulises", "En busca del tiempo perdido", "El gran Gatsby"
]

# Entrada del usuario
libro_buscado = input("Ingresa el título del libro que deseas buscar: ").strip().lower()

# BÚSQUEDA LINEAL
comparaciones_lineal = 0
encontrado_lineal = False

for i, titulo in enumerate(catalogo):
    comparaciones_lineal += 1
    if titulo.lower() == libro_buscado:
        print(f"[Búsqueda Lineal] Libro encontrado en la posición {i}.")
        encontrado_lineal = True
        break

if not encontrado_lineal:
    print("[Búsqueda Lineal] Libro no encontrado.")

print(f"Comparaciones realizadas (lineal): {comparaciones_lineal}")

# BÚSQUEDA BINARIA
catalogo_ordenado = sorted(catalogo, key=lambda x: x.lower())
comparaciones_binaria = 0
inicio = 0
fin = len(catalogo_ordenado) - 1
encontrado_binaria = False

while inicio <= fin:
    comparaciones_binaria += 1
    medio = (inicio + fin) // 2
    titulo_medio = catalogo_ordenado[medio].lower()
    
    if titulo_medio == libro_buscado:
        print(f"[Búsqueda Binaria] Libro encontrado en la posición {medio}.")
        encontrado_binaria = True
        break
    elif libro_buscado < titulo_medio:
        fin = medio - 1
    else:
        inicio = medio + 1

if not encontrado_binaria:
    print("[Búsqueda Binaria] Libro no encontrado.")

print(f"Comparaciones realizadas (binaria): {comparaciones_binaria}")
