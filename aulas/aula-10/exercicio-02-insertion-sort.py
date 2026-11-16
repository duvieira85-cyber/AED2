# Exercício 2 — Insertion Sort
# Percorre o vetor inserindo cada elemento na posição correta
# da parte já ordenada, como quem organiza cartas na mão.


def insertion_sort(lista):
    # A partir do segundo elemento, cada um procura seu lugar.
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1

        # Desloca os maiores uma casa para a direita.
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1

        # Insere a chave na posição encontrada.
        lista[j + 1] = chave

    return lista


if __name__ == "__main__":
    print(insertion_sort([7, 2, 9, 4, 1]))
