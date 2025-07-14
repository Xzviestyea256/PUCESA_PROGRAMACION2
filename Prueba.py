from itertools import permutations

def permutar(lista):
    """
    Función que genera todas las permutaciones de una lista.
    La complejidad temporal es O(n!).
    """
    return list(permutations(lista))


# Ejemplo de uso:
numeros = [1, 2, 3]
todas_las_permutaciones = permutar(numeros)

print("Todas las permutaciones de", numeros, "son:")
for perm in todas_las_permutaciones:
    print(perm)