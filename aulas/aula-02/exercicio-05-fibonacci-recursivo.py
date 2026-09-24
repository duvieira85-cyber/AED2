# Exercício 5 — Fibonacci recursivo
# A função chama a si mesma duas vezes em cada nível, gerando crescimento exponencial.

def fibonacci_recursivo(n):
    # Casos-base: os dois primeiros termos da sequência.
    if n < 2:
        return n

    # Calcula os dois termos anteriores recursivamente.
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


if __name__ == "__main__":
    print(fibonacci_recursivo(10))
