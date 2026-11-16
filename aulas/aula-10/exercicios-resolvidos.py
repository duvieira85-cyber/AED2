# Aula 10 — Métodos de Ordenação
# Reúne as soluções dos exercícios da aula:
# bubble, insertion, selection, merge e quick sort.


def bubble_sort(lista):
    # Compara vizinhos e troca quando estão fora de ordem.
    for i in range(len(lista) - 1):

        for j in range(len(lista) - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


def insertion_sort(lista):
    # Insere cada elemento na posição correta da parte ordenada.
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = chave

    return lista


def selection_sort(lista):
    # Seleciona o menor da parte não ordenada e troca com o início.
    for i in range(len(lista) - 1):
        menor = i

        for j in range(i + 1, len(lista)):
            if lista[j] < lista[menor]:
                menor = j

        lista[i], lista[menor] = lista[menor], lista[i]

    return lista


def merge_sort(lista):
    # Divide ao meio, ordena as metades e intercala.
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])

    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i]); i += 1
        else:
            resultado.append(direita[j]); j += 1

    resultado += esquerda[i:]
    resultado += direita[j:]
    return resultado


def quick_sort(lista):
    # Particiona pelo pivô e ordena as duas partes.
    if len(lista) <= 1:
        return lista

    pivo = lista[0]
    menores = [x for x in lista[1:] if x <= pivo]
    maiores = [x for x in lista[1:] if x > pivo]

    return quick_sort(menores) + [pivo] + quick_sort(maiores)


if __name__ == "__main__":
    vetor = [8, 3, 5, 1, 9, 2, 7]

    print(bubble_sort(vetor[:]))
    print(insertion_sort(vetor[:]))
    print(selection_sort(vetor[:]))
    print(merge_sort(vetor[:]))
    print(quick_sort(vetor[:]))
