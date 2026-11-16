# Exercício 4 — Merge Sort
# Divide para conquistar: divide o vetor ao meio, ordena cada metade
# e intercala as duas metades ordenadas. Complexidade O(n log n).


def merge_sort(lista):
    # Vetor de zero ou um elemento já está ordenado.
    if len(lista) <= 1:
        return lista

    # Divide o vetor ao meio.
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])

    # Intercala as duas metades ordenadas.
    return intercalar(esquerda, direita)


def intercalar(esquerda, direita):
    resultado = []
    i = j = 0

    # Compara os primeiros elementos das duas metades.
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    # Sobrou elemento em uma das metades: copia direto.
    resultado += esquerda[i:]
    resultado += direita[j:]
    return resultado


if __name__ == "__main__":
    print(merge_sort([8, 3, 5, 1, 9, 2]))
