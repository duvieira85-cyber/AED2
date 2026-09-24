# Exercício 3 — Busca binária
# A busca binária reduz o intervalo pela metade a cada comparação: O(log n).
# A lista precisa estar ordenada para que a estratégia funcione.

def busca_binaria(lista, alvo):
    esquerda = 0
    direita = len(lista) - 1

    # Enquanto existir um intervalo válido para pesquisa.
    while esquerda <= direita:
        meio = (esquerda + direita) // 2

        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return -1


if __name__ == "__main__":
    print(busca_binaria([2, 5, 8, 12, 16, 21, 27], 21))
