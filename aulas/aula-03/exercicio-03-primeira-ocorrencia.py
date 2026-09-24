# Exercício 3 — Primeira ocorrência
# A busca sequencial termina assim que encontra a primeira ocorrência.
# Em uma lista com valores repetidos, somente o primeiro índice é retornado.


def primeira_ocorrencia(lista, valor):
    # Percorre a lista desde o primeiro elemento.
    for i in range(len(lista)):
        # Quando encontra o valor, retorna imediatamente seu índice.
        if lista[i] == valor:
            return i

    # O valor não apareceu na lista.
    return -1


if __name__ == "__main__":
    # O valor 12 aparece duas vezes, mas o primeiro índice é retornado.
    print(primeira_ocorrencia([7, 12, 5, 12, 8], 12))
