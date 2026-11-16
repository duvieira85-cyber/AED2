# Aula 09 — Recursão
# Reúne as soluções dos exercícios e projetos da aula.
# Toda função recursiva precisa de um caso base e de um caso recursivo.


def fatorial(n):
    # Caso base: 0! e 1! valem 1.
    if n <= 1:
        return 1

    return n * fatorial(n - 1)


def somatorio(n):
    # Caso base: soma de 1 até 1 é 1.
    if n <= 1:
        return 1

    return n + somatorio(n - 1)


def potencia(base, exp):
    # Qualquer base elevada a zero é 1.
    if exp == 0:
        return 1

    return base * potencia(base, exp - 1)


def contar_digitos(n):
    # Números menores que 10 têm um único dígito.
    if n < 10:
        return 1

    return 1 + contar_digitos(n // 10)


def maior_elemento(lista):
    # Com um único elemento, ele é o maior.
    if len(lista) == 1:
        return lista[0]

    maior_do_resto = maior_elemento(lista[1:])

    if lista[0] > maior_do_resto:
        return lista[0]

    return maior_do_resto


def inverter(lista):
    # Lista vazia ou unitária já está invertida.
    if len(lista) <= 1:
        return lista

    return [lista[-1]] + inverter(lista[:-1])


if __name__ == "__main__":
    print(fatorial(5))
    print(somatorio(10))
    print(potencia(2, 10))
    print(contar_digitos(12345))
    print(maior_elemento([3, 17, 8, 25, 9]))
    print(inverter([1, 2, 3, 4, 5]))
