# Aula 11 — Árvores e Árvores Binárias
# Reúne as soluções dos exercícios da aula:
# BST com inserção, busca, percursos, extremos e contagens.


class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


def inserir(raiz, valor):
    # Menores à esquerda, maiores à direita.
    if raiz is None:
        return No(valor)

    if valor < raiz.valor:
        raiz.esquerda = inserir(raiz.esquerda, valor)
    else:
        raiz.direita = inserir(raiz.direita, valor)

    return raiz


def buscar(raiz, valor):
    # Não encontrou no caminho percorrido.
    if raiz is None:
        return False

    if raiz.valor == valor:
        return True

    if valor < raiz.valor:
        return buscar(raiz.esquerda, valor)

    return buscar(raiz.direita, valor)


def em_ordem(raiz, lista):
    # Esquerda → raiz → direita (ordem crescente na BST).
    if raiz is None:
        return lista

    em_ordem(raiz.esquerda, lista)
    lista.append(raiz.valor)
    em_ordem(raiz.direita, lista)

    return lista


def menor_valor(raiz):
    # Desce sempre pela esquerda.
    while raiz.esquerda is not None:
        raiz = raiz.esquerda

    return raiz.valor


def maior_valor(raiz):
    # Desce sempre pela direita.
    while raiz.direita is not None:
        raiz = raiz.direita

    return raiz.valor


def contar_nos(raiz):
    # Um nó mais os das subárvores.
    if raiz is None:
        return 0

    return 1 + contar_nos(raiz.esquerda) + contar_nos(raiz.direita)


def contar_folhas(raiz):
    # Folha é o nó sem filhos.
    if raiz is None:
        return 0

    if raiz.esquerda is None and raiz.direita is None:
        return 1

    return contar_folhas(raiz.esquerda) + contar_folhas(raiz.direita)


if __name__ == "__main__":
    raiz = None
    for v in [10, 5, 20, 3, 7, 25]:
        raiz = inserir(raiz, v)

    print(em_ordem(raiz, []))
    print(buscar(raiz, 7))
    print(buscar(raiz, 99))
    print(menor_valor(raiz), maior_valor(raiz))
    print(contar_nos(raiz), contar_folhas(raiz))
