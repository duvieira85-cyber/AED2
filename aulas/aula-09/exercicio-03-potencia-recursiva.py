# Exercício 3 — Potência recursiva
# base^exp = base × base^(exp − 1), com caso base exp = 0 → 1.


def potencia(base, exp):
    # Todo número elevado a zero é 1.
    if exp == 0:
        return 1

    # Multiplica a base pela potência com expoente menor.
    return base * potencia(base, exp - 1)


if __name__ == "__main__":
    print(potencia(2, 10))
    print(potencia(5, 3))
