# Ejercicio 4: Operaciones con la lista [1..10] usando map, filter y reduce

from functools import reduce

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"=== Ejercicio 4: Operaciones con {lista} ===\n")

# 4a) Cuadrados usando map
cuadrados = list(map(lambda x: x ** 2, lista))
print(f"Cuadrados (map):  {cuadrados}")

# 4b) Números pares usando filter
pares = list(filter(lambda x: x % 2 == 0, lista))
print(f"Pares (filter):   {pares}")

# 4c) Suma de [1..10] usando reduce
suma_total = reduce(lambda acc, x: acc + x, lista)
print(f"Suma [1..10] (reduce):    {suma_total}")

# 4d) Producto de [1..5] usando reduce
producto = reduce(lambda acc, x: acc * x, lista[:5])
print(f"Producto [1..5] (reduce): {producto}")
