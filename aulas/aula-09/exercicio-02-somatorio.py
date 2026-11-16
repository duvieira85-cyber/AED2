# Exercício 2 — Somatório de 1 até n
# soma(n) = n + soma(n − 1), com caso base soma(1) = 1.


def somatorio(n):
    # Caso base: a soma de 1 até 1 é o próprio 1.
    if n <= 1:
        return 1

    # Caso recursivo: n mais a soma de tudo que veio antes.
    return n + somatorio(n - 1)


if __name__ == "__main__":
    # soma de 1 a 10 = 55.
    print(somatorio(10))
    print(somatorio(1))
