# Exercício 5 — Quick Sort
# Escolhe um pivô, cria a partição (menores à esquerda, maiores à direita)
# e repete o processo nas duas partes. O(n log n) no caso médio.


def quick_sort(lista):
    # Lista vazia ou unitária já está ordenada.
    if len(lista) <= 1:
        return lista

    # Usa o primeiro elemento como pivô.
    pivo = lista[0]
    menores = [x for x in lista[1:] if x <= pivo]
    maiores = [x for x in lista[1:] if x > pivo]

    # Ordena as duas partes e junta com o pivô no meio.
    return quick_sort(menores) + [pivo] + quick_sort(maiores)


if __name__ == "__main__":
    print(quick_sort([6, 2, 9, 1, 7, 3]))
