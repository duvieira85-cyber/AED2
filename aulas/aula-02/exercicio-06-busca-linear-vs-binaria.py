# Exercício 6 — Busca linear x busca binária
# A busca linear pode percorrer toda a lista: O(n).
# A busca binária reduz o intervalo de pesquisa pela metade: O(log n).

def busca_linear(lista, alvo):
    for elemento in lista:
        # Compara cada elemento com o valor procurado.
        if elemento == alvo:
            return True
    return False


def busca_binaria(lista, alvo):
    esquerda = 0
    direita = len(lista) - 1

    # Funciona corretamente quando a lista está ordenada.
    while esquerda <= direita:
        meio = (esquerda + direita) // 2

        if lista[meio] == alvo:
            return True
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return False


if __name__ == "__main__":
    dados = [1, 4, 7, 12, 18]
    print("Busca linear:", busca_linear(dados, 12))
    print("Busca binária:", busca_binaria(dados, 12))
