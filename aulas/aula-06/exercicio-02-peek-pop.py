def executar():
    pilha = []

    pilha.append("a")
    pilha.append("b")

    x = pilha[-1]
    pilha.pop()
    y = pilha[-1]

    print("x =", x)
    print("y =", y)


if __name__ == "__main__":
    executar()
