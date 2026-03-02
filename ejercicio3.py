"""
Ejercicio 3:
Escribe una función recursiva que calcule el n-ésimo número de Fibonacci.

¿Qué es la secuencia de Fibonacci?
La secuencia de Fibonacci es una serie de números donde cada número es la suma de los dos anteriores. Comienza con 0 y 1, y continúa indefinidamente. La secuencia se define de la siguiente manera:
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2) para n > 1
"""

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
