# Exercício 6 — Remoção da primeira ocorrência
# Primeiro localizamos a primeira ocorrência do valor.
# Depois deslocamos os elementos seguintes uma posição para a esquerda
# para preencher o espaço que ficou vazio.


def remover_primeira_ocorrencia(lista, valor):
    # Não existe elemento para remover quando a lista está vazia.
    if not lista:
        return None

    # -1 representa que o valor ainda não foi encontrado.
    indice = -1

    # Procura somente até encontrar a primeira ocorrência.
    for i in range(len(lista)):
        if lista[i] == valor:
            indice = i
            break

    # Se o valor não foi encontrado, nenhuma alteração é feita.
    if indice == -1:
        return None

    # Guarda o elemento antes de alterar a estrutura da lista.
    elemento_removido = lista[indice]

    # Desloca os elementos posteriores uma posição para a esquerda.
    for j in range(indice, len(lista) - 1):
        lista[j] = lista[j + 1]

    # Remove a última posição, que ficou duplicada após o deslocamento.
    lista.pop()

    return elemento_removido


if __name__ == "__main__":
    dados = [10, 3, 7, 34, 23, 2, 21]

    print("Antes:", dados)
    print("Removido:", remover_primeira_ocorrencia(dados, 23))
    print("Depois:", dados)
