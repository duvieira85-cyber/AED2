# Exercício 2 — Inserção e busca em árvore binária de busca
# Regra da BST: valores menores vão para a esquerda,
# valores maiores vão para a direita. Isso acelera a busca.


class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


def inserir(raiz, valor):
    # Árvore vazia: o novo nó se torna a raiz.
    if raiz is None:
        return No(valor)

    # Menor desce para a esquerda.
    if valor < raiz.valor:
        raiz.esquerda = inserir(raiz.esquerda, valor)
    # Maior desce para a direita.
    else:
        raiz.direita = inserir(raiz.direita, valor)

    return raiz


def buscar(raiz, valor):
    # Árvore vazia ou chegou ao fim: não encontrou.
    if raiz is None:
        return False

    # Encontrou o valor na raiz do trecho.
    if raiz.valor == valor:
        return True

    # Escolhe o lado pela regra da BST.
    if valor < raiz.valor:
        return buscar(raiz.esquerda, valor)

    return buscar(raiz.direita, valor)


if __name__ == "__main__":
    raiz = None
    for v in [10, 5, 20, 3, 7]:
        raiz = inserir(raiz, v)

    print(buscar(raiz, 7))
    print(buscar(raiz, 99))
