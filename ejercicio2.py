"""
Ejercicio 2:
Implementa una función recursiva factorial(n) que calcule el factorial.
"""

def factorial(n):
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    # El factorial de 0 y 1 es 1, por lo que se puede manejar con una sola condición y retornar 1 para ambos casos. Así evitamos error al calcular factorial(0) y factorial(1).
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("=== Ejercicio 2: factorial(n) ===")
for i in range(3):
    print(f"factorial({i}) = {factorial(i)}")
