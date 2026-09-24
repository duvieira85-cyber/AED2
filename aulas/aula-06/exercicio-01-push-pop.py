# Exercício 1 — Acompanhando push e pop
# A pilha segue LIFO (Last In, First Out):
# o último elemento inserido é o primeiro a ser removido.


def acompanhar_pilha():
    # Cria uma pilha inicialmente vazia.
    pilha = []

    # push: adiciona os valores ao topo da pilha.
    pilha.append(5)
    pilha.append(10)

    # pop: remove o elemento que está no topo, neste caso 10.
    pilha.pop()

    # Adiciona novamente dois valores ao topo.
    pilha.append(7)
    pilha.append(3)

    # O último valor inserido, 3, é o primeiro a sair.
    removido = pilha.pop()

    print("Último pop:", removido)
    print("Pilha final:", pilha)


if __name__ == "__main__":
    # Executa a sequência de operações do exercício.
    acompanhar_pilha()
