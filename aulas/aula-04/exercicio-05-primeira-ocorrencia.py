# Exercício 5 — Primeira ocorrência em vetor ordenado
# Em um vetor ordenado com valores repetidos, a busca binária acha "uma" ocorrência,
# não necessariamente a primeira. Depois de encontrar, caminha para a esquerda
# enquanto o elemento anterior também for igual ao alvo.


def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == alvo:
            return meio

        if lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1


def primeira_ocorrencia(lista, alvo):
    # Busca binária encontra uma das ocorrências.
    indice = busca_binaria(lista, alvo)

    if indice == -1:
        return -1

    # Caminha para a esquerda enquanto houver repetição do valor.
    while indice > 0 and lista[indice - 1] == alvo:
        indice -= 1

    return indice


if __name__ == "__main__":
    # O 8 aparece quatro vezes; a primeira está no índice 1.
    print(primeira_ocorrencia([2, 8, 8, 8, 8, 15, 21], 8))
    print(primeira_ocorrencia([2, 8, 8, 8, 8, 15, 21], 15))
