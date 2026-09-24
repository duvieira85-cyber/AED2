# Exercício 6 — Remoção da primeira ocorrência
# Primeiro localizamos o elemento; depois deslocamos os demais uma posição para a esquerda.

def remover_primeira_ocorrencia(lista, valor):
    if not lista:
        return None

    indice = -1

    for i in range(len(lista)):
        # Para na primeira ocorrência encontrada.
        if lista[i] == valor:
            indice = i
            break

    if indice == -1:
        return None

    elemento_removido = lista[indice]

    # Desloca os elementos posteriores para preencher o espaço removido.
    for j in range(indice, len(lista) - 1):
        lista[j] = lista[j + 1]

    lista.pop()
    return elemento_removido


if __name__ == "__main__":
    dados = [10, 3, 7, 34, 23, 2, 21]

    print("Antes:", dados)
    print("Removido:", remover_primeira_ocorrencia(dados, 23))
    print("Depois:", dados)
