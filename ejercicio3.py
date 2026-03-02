# Ejercicio 3: Función recursiva para el n-ésimo número de Fibonacci

def fibonacci(n):
    if n < 0:
        raise ValueError("Fibonacci no está definido para números negativos")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print("=== Ejercicio 3: fibonacci(n) ===")
for i in range(10):
    print(f"fibonacci({i}) = {fibonacci(i)}")
