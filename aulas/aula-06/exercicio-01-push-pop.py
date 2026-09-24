# Exercício 1 — Acompanhando push e pop
# A pilha segue LIFO: o último elemento inserido é o primeiro a ser removido.

def acompanhar_pilha():
    pilha = []

    # Empilha os valores na ordem indicada pelo enunciado.
    pilha.append(5)
    pilha.append(10)

    # Remove o elemento que está no topo: 10.
    pilha.pop()

    pilha.append(7)
    pilha.append(3)

    # O último pop remove o 3.
    removido = pilha.pop()

    print("Último pop:", removido)
    print("Pilha final:", pilha)


if __name__ == "__main__":
    acompanhar_pilha()
