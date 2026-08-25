def fibonacci_recursivo(n):
    if n < 2:
        return n
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


print("fibonacci_recursivo(10):", fibonacci_recursivo(10))

# Complexidade: O(2^n) — versão recursiva ingênua,
# com chamadas redundantes que crescem exponencialmente.