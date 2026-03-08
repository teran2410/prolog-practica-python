# """
# Ejercicio 3:
# Escribe una función recursiva que calcule el n-ésimo número de Fibonacci.

# ¿Qué es la secuencia de Fibonacci?
# La secuencia de Fibonacci es una serie de números donde cada número es la suma de los dos anteriores. Comienza con 0 y 1, y continúa indefinidamente. La secuencia se define de la siguiente manera:
# F(0) = 0
# F(1) = 1
# F(n) = F(n-1) + F(n-2) para n > 1
# """

n = 10
a, b = 0, 1

fibonacci_numbers = []

for _ in range(n):  
    fibonacci_numbers.append(str(a)) 
    a, b = b, a + b

for num in range(n):
    print(f"fibonacci({num}) = {fibonacci_numbers[num]}")