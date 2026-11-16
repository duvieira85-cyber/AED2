# Exercício 1 — Busca binária básica
# Em um vetor ORDENADO, compara o alvo com o elemento do meio:
# se o alvo é maior, descarta a metade da esquerda; se é menor, descarta a da direita.


def busca_binaria(lista, alvo):
    # Limites do intervalo ainda possível.
    inicio = 0
    fim = len(lista) - 1

    # Enquanto houver um intervalo válido, testa o meio.
    while inicio <= fim:
        meio = (inicio + fim) // 2

        # Encontrou o valor no meio.
        if lista[meio] == alvo:
            return meio

        # O alvo está na metade da direita.
        if lista[meio] < alvo:
            inicio = meio + 1
        # O alvo está na metade da esquerda.
        else:
            fim = meio - 1

    # O valor não existe no vetor.
    return -1


if __name__ == "__main__":
    # O vetor precisa estar ordenado para a busca binária funcionar.
    print(busca_binaria([2, 5, 8, 12, 16, 23, 38, 56], 23))
    print(busca_binaria([2, 5, 8, 12, 16, 23, 38, 56], 5))
