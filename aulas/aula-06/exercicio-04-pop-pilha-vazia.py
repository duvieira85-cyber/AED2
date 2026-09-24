# Exercício 4 — Tentativa de pop em pilha vazia
# A sequência possui quatro operações pop válidas.
# Portanto, não ocorre nenhuma tentativa de remover elemento de uma pilha vazia.


def contar_tentativas_invalidas():
    # Pilha inicialmente vazia.
    pilha = []

    # Contador das operações pop realizadas quando não havia elementos.
    tentativas_invalidas = 0

    # Sequência de operações fornecida pelo exercício.
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

    # Executa as operações na ordem em que foram definidas.
    for operacao, valor in operacoes:
        if operacao == "push":
            # Adiciona o valor no topo da pilha.
            pilha.append(valor)

        elif operacao == "pop":
            # Só existe tentativa inválida quando a pilha está vazia.
            if pilha:
                pilha.pop()
            else:
                tentativas_invalidas += 1

    print("Tentativas de pop em pilha vazia:", tentativas_invalidas)


if __name__ == "__main__":
    # Executa a simulação da sequência de operações.
    contar_tentativas_invalidas()
