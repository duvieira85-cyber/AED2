def acompanhar_pilha():
    pilha = []

    pilha.append(5)
    pilha.append(10)
    pilha.pop()
    pilha.append(7)
    pilha.append(3)

    removido = pilha.pop()

    print("Último pop:", removido)
    print("Pilha final:", pilha)


if __name__ == "__main__":
    acompanhar_pilha()
