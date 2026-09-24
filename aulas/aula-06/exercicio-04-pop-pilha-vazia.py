# Exercício 4 — Tentativa de pop em pilha vazia
# A sequência possui quatro pop(), todos válidos; portanto, o total de tentativas inválidas é zero.

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
            # Adiciona o valor no topo da pilha.
            pilha.append(valor)
        elif operacao == "pop":
            # Só existe tentativa inválida quando a pilha já está vazia.
            if pilha:
                pilha.pop()
            else:
                tentativas_invalidas += 1

    print("Tentativas de pop em pilha vazia:", tentativas_invalidas)


if __name__ == "__main__":
    contar_tentativas_invalidas()
