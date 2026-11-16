# Projeto 2 — Busca binária recursiva
# A mesma busca binária da Aula 04, agora escrita de forma recursiva:
# em vez de atualizar inicio/fim, a função chama a si mesma com o novo intervalo.


def busca_binaria_recursiva(lista, alvo, inicio, fim):
    # Intervalo vazio: o valor não existe no vetor.
    if inicio > fim:
        return -1

    meio = (inicio + fim) // 2

    # Encontrou o valor no meio do intervalo atual.
    if lista[meio] == alvo:
        return meio

    # Busca apenas na metade da direita.
    if lista[meio] < alvo:
        return busca_binaria_recursiva(lista, alvo, meio + 1, fim)

    # Busca apenas na metade da esquerda.
    return busca_binaria_recursiva(lista, alvo, inicio, meio - 1)


if __name__ == "__main__":
    ordenado = [2, 5, 8, 12, 16, 23, 38, 56]

    print(busca_binaria_recursiva(ordenado, 23, 0, len(ordenado) - 1))
    print(busca_binaria_recursiva(ordenado, 5, 0, len(ordenado) - 1))
    print(busca_binaria_recursiva(ordenado, 99, 0, len(ordenado) - 1))
