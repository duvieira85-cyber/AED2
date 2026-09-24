# Exercício 6 — Busca linear x busca binária
# A busca linear pode precisar percorrer toda a lista: O(n).
# A busca binária reduz o intervalo pela metade: O(log n).
# A busca binária exige que os dados estejam ordenados.


def busca_linear(lista, alvo):
    # Percorre os elementos um por um desde o início.
    for elemento in lista:
        # Compara o elemento atual com o valor procurado.
        if elemento == alvo:
            return True

    # O alvo não foi encontrado após percorrer a lista.
    return False


def busca_binaria(lista, alvo):
    # Define os limites do intervalo que ainda será pesquisado.
    esquerda = 0
    direita = len(lista) - 1

    # Continua enquanto existir uma faixa válida de pesquisa.
    while esquerda <= direita:
        # Verifica o elemento que está no meio do intervalo.
        meio = (esquerda + direita) // 2

        if lista[meio] == alvo:
            return True
        elif lista[meio] < alvo:
            # Descarta a metade esquerda.
            esquerda = meio + 1
        else:
            # Descarta a metade direita.
            direita = meio - 1

    # O valor não existe na lista.
    return False


if __name__ == "__main__":
    # A lista utilizada já está ordenada, permitindo as duas buscas.
    dados = [1, 4, 7, 12, 18]

    print("Busca linear:", busca_linear(dados, 12))
    print("Busca binária:", busca_binaria(dados, 12))
