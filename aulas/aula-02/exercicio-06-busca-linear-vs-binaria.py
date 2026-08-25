def busca_linear(lista, alvo):
    for elemento in lista:
        if elemento == alvo:
            return True
    return False


def busca_binaria(lista, alvo):
    esquerda = 0
    direita = len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return True
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return False


lista = [1, 4, 7, 12, 18, 25, 31, 40]
alvo = 25

print("Busca linear:", busca_linear(lista, alvo))
print("Ordenar + busca binária:", busca_binaria(lista, alvo))
print("Uma busca: linear O(n) é melhor que ordenar + binária O(n log n).")
print("Muitas buscas: ordenar uma vez pode compensar o custo inicial.")

# Para m buscas:
# linear: O(m*n)
# ordenar uma vez + m buscas binárias: O(n log n + m log n)