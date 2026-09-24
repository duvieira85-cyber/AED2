# Exercício 3 — Busca binária
# A busca binária reduz o intervalo de pesquisa pela metade
# a cada comparação, resultando em complexidade O(log n).
# A lista precisa estar ordenada para que a estratégia funcione.


def busca_binaria(lista, alvo):
    # Define os limites inicial e final do intervalo de pesquisa.
    esquerda = 0
    direita = len(lista) - 1

    # Enquanto existir um intervalo válido para pesquisa.
    while esquerda <= direita:
        # Calcula o índice do elemento central do intervalo.
        meio = (esquerda + direita) // 2

        if lista[meio] == alvo:
            # O elemento central é o valor procurado.
            return meio
        elif lista[meio] < alvo:
            # Como a lista está ordenada, descarta a metade esquerda.
            esquerda = meio + 1
        else:
            # O alvo é menor que o elemento central,
            # então descarta a metade direita.
            direita = meio - 1

    # O intervalo terminou sem encontrar o elemento.
    return -1


if __name__ == "__main__":
    # Exemplo com uma lista ordenada e o valor 21 como alvo.
    print(busca_binaria([2, 5, 8, 12, 16, 21, 27], 21))
