# Exercício 1 — Nó de árvore binária
# Cada nó guarda um valor e as referências para os filhos
# da esquerda e da direita. Sem filhos, as referências são None.


class No:
    # Um nó guarda um valor e aponta para os dois filhos.
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


if __name__ == "__main__":
    # Monta uma árvore de três nós: 10 com filhos 5 e 20.
    raiz = No(10)
    raiz.esquerda = No(5)
    raiz.direita = No(20)

    print(raiz.valor, raiz.esquerda.valor, raiz.direita.valor)
