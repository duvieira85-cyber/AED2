# Exercício 2 — Limites esquerda e direita
# As duas variáveis que controlam a busca binária: onde o intervalo começa e onde termina.
# O intervalo para quando 'inicio' passa de 'fim' — sinal de que o valor não existe.


def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == alvo:
            return inicio, fim, meio

        if lista[meio] < alvo:
            # Descarta o meio e tudo que está à esquerda.
            inicio = meio + 1
        else:
            # Descarta o meio e tudo que está à direita.
            fim = meio - 1

    return -1, -1, -1


if __name__ == "__main__":
    # Mostra como os limites se movem a cada busca.
    print(busca_binaria([4, 9, 15, 21, 28, 33], 21))
    print(busca_binaria([4, 9, 15, 21, 28, 33], 99))
