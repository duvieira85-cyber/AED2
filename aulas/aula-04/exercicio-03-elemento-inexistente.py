# Exercício 3 — Elemento inexistente
# Quando inicio ultrapassa fim, o intervalo ficou vazio: o valor não está no vetor.
# A busca binária então retorna -1, como na busca sequencial.


def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == alvo:
            return meio

        if lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1


if __name__ == "__main__":
    # O 7 não existe no vetor, mas a busca segue o mesmo caminho até concluir.
    print(busca_binaria([3, 6, 9, 12, 15], 7))
    print(busca_binaria([3, 6, 9, 12, 15], 12))
