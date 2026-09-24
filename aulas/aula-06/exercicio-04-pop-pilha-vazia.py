def contar_tentativas_invalidas():
    pilha = []
    tentativas_invalidas = 0

    operacoes = [
        ("push", 1),
        ("push", 2),
        ("push", 3),
        ("pop", None),
        ("push", 4),
        ("pop", None),
        ("pop", None),
        ("pop", None),
    ]

    for operacao, valor in operacoes:
        if operacao == "push":
            pilha.append(valor)
        elif operacao == "pop":
            if pilha:
                pilha.pop()
            else:
                tentativas_invalidas += 1

    print("Tentativas de pop em pilha vazia:", tentativas_invalidas)


if __name__ == "__main__":
    contar_tentativas_invalidas()
