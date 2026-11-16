# Aula 04 — Vetores Ordenados — Busca Binária
# Reúne as soluções dos exercícios e projetos da aula.
# O foco é a busca binária sobre vetores ordenados e o ganho de O(log n).


def busca_binaria(lista, alvo):
    # Limites do intervalo ainda possível.
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        # Encontra o valor no meio do intervalo.
        if lista[meio] == alvo:
            return meio

        # Descarta a metade da esquerda.
        if lista[meio] < alvo:
            inicio = meio + 1
        # Descarta a metade da direita.
        else:
            fim = meio - 1

    # O valor não existe no vetor.
    return -1


def busca_binaria_com_passos(lista, alvo):
    # Mesma busca, mas também conta as comparações realizadas.
    inicio = 0
    fim = len(lista) - 1
    passos = 0

    while inicio <= fim:
        meio = (inicio + fim) // 2
        passos += 1

        if lista[meio] == alvo:
            return meio, passos

        if lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1, passos


def primeira_ocorrencia(lista, alvo):
    # Encontra uma ocorrência e caminha para a esquerda até a primeira.
    indice = busca_binaria(lista, alvo)

    if indice == -1:
        return -1

    while indice > 0 and lista[indice - 1] == alvo:
        indice -= 1

    return indice


if __name__ == "__main__":
    ordenado = [2, 5, 8, 12, 16, 23, 38, 56]

    print(busca_binaria(ordenado, 23))
    print(busca_binaria(ordenado, 5))
    print(busca_binaria(ordenado, 99))

    indice, passos = busca_binaria_com_passos(list(range(1, 1001)), 998)
    print("índice:", indice, "| comparações:", passos)

    print(primeira_ocorrencia([2, 8, 8, 8, 8, 15, 21], 8))
