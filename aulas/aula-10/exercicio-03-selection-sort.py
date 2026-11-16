# Exercício 3 — Selection Sort
# A cada rodada, seleciona o menor elemento da parte não ordenada
# e troca com a primeira posição dessa parte.


def selection_sort(lista):
    for i in range(len(lista) - 1):
        # Considera o primeiro elemento da parte não ordenada como menor.
        menor = i

        # Procura um menor no resto do vetor.
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[menor]:
                menor = j

        # Traz o menor para o início da parte não ordenada.
        lista[i], lista[menor] = lista[menor], lista[i]

    return lista


if __name__ == "__main__":
    print(selection_sort([9, 3, 6, 1, 8]))
