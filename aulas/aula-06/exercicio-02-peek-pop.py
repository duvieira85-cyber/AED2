# Exercício 2 — peek() consulta e pop() remove
# O acesso ao último item representa o topo da pilha usada neste exercício.

def executar():
    pilha = []

    pilha.append("a")
    pilha.append("b")

    # peek: consulta o topo sem removê-lo.
    x = pilha[-1]

    # pop: remove o elemento que estava no topo.
    pilha.pop()

    # Após remover "b", "a" passa a ser o novo topo.
    y = pilha[-1]

    print("x =", x)
    print("y =", y)


if __name__ == "__main__":
    executar()
