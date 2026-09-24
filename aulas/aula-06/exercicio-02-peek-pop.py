# Exercício 2 — peek() consulta e pop() remove
# O último item da lista representa o topo da pilha usada no exercício.
# peek consulta esse elemento sem removê-lo; pop remove o elemento.


def executar():
    # Cria uma pilha vazia.
    pilha = []

    # Insere os elementos na ordem indicada.
    pilha.append("a")
    pilha.append("b")

    # peek: consulta o topo sem alterar a pilha.
    x = pilha[-1]

    # pop: remove o elemento que estava no topo, "b".
    pilha.pop()

    # Depois da remoção, "a" passa a ser o novo topo.
    y = pilha[-1]

    print("x =", x)
    print("y =", y)


if __name__ == "__main__":
    # Executa o exemplo de consulta e remoção do topo.
    executar()
