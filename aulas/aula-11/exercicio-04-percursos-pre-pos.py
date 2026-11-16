# Exercício 4 — Percursos pré-ordem e pós-ordem
# Pré-ordem: raiz → esquerda → direita.
# Pós-ordem: esquerda → direita → raiz.


class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


def pre_ordem(raiz, lista):
    # Árvore vazia não acrescenta nada.
    if raiz is None:
        return lista

    # Raiz primeiro, depois esquerda e direita.
    lista.append(raiz.valor)
    pre_ordem(raiz.esquerda, lista)
    pre_ordem(raiz.direita, lista)

    return lista


def pos_ordem(raiz, lista):
    # Árvore vazia não acrescenta nada.
    if raiz is None:
        return lista

    # Esquerda e direita primeiro, raiz por último.
    pos_ordem(raiz.esquerda, lista)
    pos_ordem(raiz.direita, lista)
    lista.append(raiz.valor)

    return lista


if __name__ == "__main__":
    raiz = No(10)
    raiz.esquerda = No(5)
    raiz.direita = No(20)
    raiz.esquerda.esquerda = No(3)

    print(pre_ordem(raiz, []))
    print(pos_ordem(raiz, []))
