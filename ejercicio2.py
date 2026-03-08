"""
Ejercicio 2:
Implementa una función recursiva factorial(n) que calcule el factorial.
"""

def factorial(n):
        fact = 1
        for num in range(1, n + 1):
            fact *= num
        print(fact)

factorial(6)