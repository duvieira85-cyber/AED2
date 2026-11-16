# Exercício 6 — Contar nós e folhas
# Folha é o nó que não tem filhos.


class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


def contar_nos(raiz):
    # Árvore vazia tem zero nós.
    if raiz is None:
        return 0

    # A conta é 1 (a raiz) mais os nós das duas subárvores.
    return 1 + contar_nos(raiz.esquerda) + contar_nos(raiz.direita)


def contar_folhas(raiz):
    # Árvore vazia tem zero folhas.
    if raiz is None:
        return 0

    # Nó sem filhos é folha.
    if raiz.esquerda is None and raiz.direita is None:
        return 1

    # A conta soma as folhas das duas subárvores.
    return contar_folhas(raiz.esquerda) + contar_folhas(raiz.direita)


if __name__ == "__main__":
    raiz = No(10)
    raiz.esquerda = No(5)
    raiz.direita = No(20)
    raiz.esquerda.esquerda = No(3)

    print(contar_nos(raiz))
    print(contar_folhas(raiz))
