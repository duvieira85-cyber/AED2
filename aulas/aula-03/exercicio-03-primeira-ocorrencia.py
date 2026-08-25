def busca_sequencial(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1


lista = [7, 12, 5, 12, 8]
resultado = busca_sequencial(lista, 12)

print("Índice da primeira ocorrência de 12:", resultado)
# Resultado esperado: 1.
# A segunda ocorrência está no índice 3, mas a busca já terminou no índice 1.