# Exercício 1 — Bubble Sort
# Compara vizinhos e troca quando estão fora de ordem.
# A cada passada, o maior elemento "borbulha" até o fim do vetor.


def bubble_sort(lista):
    # Percorre o vetor n − 1 vezes.
    for i in range(len(lista) - 1):

        # Após i passadas, os i últimos já estão no lugar.
        for j in range(len(lista) - 1 - i):

            # Vizinhos fora de ordem trocam de posição.
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


if __name__ == "__main__":
    print(bubble_sort([5, 3, 8, 1, 9, 2]))
