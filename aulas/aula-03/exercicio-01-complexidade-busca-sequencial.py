def busca_sequencial(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1


# Melhor caso: alvo no índice 0 -> O(1).
# Pior caso: alvo no final ou ausente -> O(n).

lista = [10, 20, 30, 40, 50]
print("Melhor caso:", busca_sequencial(lista, 10))
print("Pior caso:", busca_sequencial(lista, 99))