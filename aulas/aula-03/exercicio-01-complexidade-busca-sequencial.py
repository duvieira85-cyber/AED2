# Exercício 1 — Complexidade da busca sequencial
# Melhor caso: O(1), quando o alvo está logo no início.
# Pior caso: O(n), quando o alvo está no fim ou não existe.


def busca_sequencial(lista, alvo):
    # Percorre os índices da lista começando pela posição 0.
    for i in range(len(lista)):
        # Compara o elemento atual com o valor procurado.
        if lista[i] == alvo:
            # A busca termina imediatamente quando encontra o alvo.
            return i

    # O valor não foi encontrado em nenhuma posição.
    return -1


if __name__ == "__main__":
    lista = [7, 12, 5, 12, 8]

    # 7 está na primeira posição: representa o melhor caso.
    print("Melhor caso:", busca_sequencial(lista, 7))

    # 99 não existe: é necessário percorrer toda a lista.
    print("Pior caso:", busca_sequencial(lista, 99))
