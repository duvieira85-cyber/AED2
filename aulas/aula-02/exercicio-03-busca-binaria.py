def busca_binaria(lista, alvo):
    esquerda = 0
    direita = len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2

        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return -1


lista = [2, 5, 8, 12, 16, 21, 27, 31, 40]
print("Posição de 21:", busca_binaria(lista, 21))
print("Posição de 10:", busca_binaria(lista, 10))

# Complexidade: O(log n).
# A lista precisa estar ordenada.