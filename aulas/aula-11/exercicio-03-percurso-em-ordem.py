# Exercício 3 — Percurso em ordem
# Visita esquerda → raiz → direita.
# Em uma BST, esse percurso lista os valores em ordem crescente.


class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


def em_ordem(raiz, lista):
    # Árvore vazia não acrescenta nada.
    if raiz is None:
        return lista

    # Esquerda, depois raiz, depois direita.
    em_ordem(raiz.esquerda, lista)
    lista.append(raiz.valor)
    em_ordem(raiz.direita, lista)

    return lista


if __name__ == "__main__":
    raiz = No(10)
    raiz.esquerda = No(5)
    raiz.direita = No(20)
    raiz.esquerda.esquerda = No(3)
    raiz.direita.direita = No(25)

    print(em_ordem(raiz, []))
