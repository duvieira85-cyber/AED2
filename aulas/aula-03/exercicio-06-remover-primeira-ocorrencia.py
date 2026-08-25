def remove_elemento(lista, valor):
    if len(lista) == 0:
        return None

    indice = -1

    for i in range(len(lista)):
        if lista[i] == valor:
            indice = i
            break

    if indice == -1:
        return None

    elemento_removido = lista[indice]

    for j in range(indice, len(lista) - 1):
        lista[j] = lista[j + 1]

    lista.pop()
    return elemento_removido


dados = [10, 3, 7, 34, 23, 2, 21]
print("Lista original:", dados)

removido = remove_elemento(dados, 23)

if removido is not None:
    print(f"Valor {removido} removido.")
else:
    print("Valor não encontrado ou lista vazia.")

print("Lista após remoção:", dados)

# Complexidade total: O(n). Espaço adicional: O(1).