# Exercício 4 — Contar os passos da busca binária
# A cada iteração metade do intervalo é descartada: é isso que dá O(log n).
# Em um vetor de 1000 elementos, bastam cerca de 10 comparações.


def busca_binaria_com_passos(lista, alvo):
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


if __name__ == "__main__":
    # Um vetor grande mostra a força da busca binária.
    vetor_grande = list(range(1, 1001))

    indice, passos = busca_binaria_com_passos(vetor_grande, 998)
    print("índice:", indice, "| comparações:", passos)

    # A busca sequencial precisaria de 998 comparações para o mesmo caso.
