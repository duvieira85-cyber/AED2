# Exercício 5 — Menor e maior valor da BST
# Pela regra da BST, o menor valor está indo sempre à esquerda
# e o maior está indo sempre à direita.


class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


def menor_valor(raiz):
    # Desce sempre pela esquerda até o fim.
    while raiz.esquerda is not None:
        raiz = raiz.esquerda

    return raiz.valor


def maior_valor(raiz):
    # Desce sempre pela direita até o fim.
    while raiz.direita is not None:
        raiz = raiz.direita

    return raiz.valor


if __name__ == "__main__":
    raiz = No(10)
    raiz.esquerda = No(5)
    raiz.direita = No(20)
    raiz.esquerda.esquerda = No(3)

    print(menor_valor(raiz))
    print(maior_valor(raiz))
