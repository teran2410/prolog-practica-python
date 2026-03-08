"""
Ejercicio 4:
Dada la lista [1,2,3,4,5,6,7,8,9,10]:
    Genera una nueva lista con los cuadrados de cada número usando map.
    Filtra los números pares usando filter
    Usa reduce para calcular:
        La suma de [1..10]
        El producto [1..5]

"""

from functools import reduce

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"=== Ejercicio 4: Operaciones con lista ===\n")

"""
Según google...
lambda se usa para crear funciones anónimas en una sola línea, sin necesidad de definirlas con def.
Es ideal cuando necesitamos una función pequeña que solo se usa una vez, como argumento de map, filter o reduce.
"""

# Usando map
cuadrados = list(map(lambda x: x ** 2, lista))
print(f"Cuadrados (map):  {cuadrados}")

# Usando filter
pares = list(filter(lambda x: x % 2 == 0, lista))
print(f"Pares (filter):   {pares}")

"""
reduce toma una función y una secuencia, y aplica la función de manera acumulativa a los elementos de la secuencia, reduciéndola a un solo valor.
Es útil para operaciones como sumas o productos.
"""

# Usando reduce para sumar [1..10]
suma_total = reduce(lambda acc, x: acc + x, lista)
print(f"Suma [1..10] (reduce):    {suma_total}")

# Usando reduce para multiplicar [1..5]
producto = reduce(lambda acc, x: acc * x, lista[:5])
print(f"Producto [1..5] (reduce): {producto}")
