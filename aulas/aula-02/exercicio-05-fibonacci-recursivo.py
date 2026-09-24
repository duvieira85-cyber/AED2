# Exercício 5 — Fibonacci recursivo
# A função chama a si mesma duas vezes em cada nível da árvore recursiva,
# fazendo o número de chamadas crescer rapidamente.


def fibonacci_recursivo(n):
    # Casos-base: os dois primeiros termos da sequência de Fibonacci
    # são 0 e 1, portanto não é necessário continuar a recursão.
    if n < 2:
        return n

    # Calcula os dois termos anteriores e soma seus resultados.
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


if __name__ == "__main__":
    # Calcula o décimo termo da sequência.
    print(fibonacci_recursivo(10))
