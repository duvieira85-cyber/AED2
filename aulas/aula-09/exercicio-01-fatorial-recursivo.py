# Exercício 1 — Fatorial recursivo
# n! = n × (n − 1)!
# Caso base: 0! = 1. Sem caso base, a função chama a si mesma para sempre.


def fatorial(n):
    # Caso base: o fatorial de 0 e de 1 é 1.
    if n <= 1:
        return 1

    # Caso recursivo: n! = n × (n − 1)!
    return n * fatorial(n - 1)


if __name__ == "__main__":
    print(fatorial(5))
    print(fatorial(0))
