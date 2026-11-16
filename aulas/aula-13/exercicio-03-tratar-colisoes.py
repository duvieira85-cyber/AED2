# Exercício 3 — Tratamento de colisão por encadeamento
# Colisão acontece quando duas chaves caem na mesma posição.
# A solução aqui é encadeamento: a posição guarda uma lista
# de pares, e a busca compara as chaves dentro dessa lista.


TAMANHO = 10
tabela = [[] for _ in range(TAMANHO)]


def funcao_hash(chave):
    return chave % TAMANHO


def inserir(chave, valor):
    posicao = funcao_hash(chave)
    tabela[posicao].append((chave, valor))


if __name__ == "__main__":
    # As chaves 12, 22 e 32 caem todas na posição 2: colisão.
    inserir(12, "primeiro")
    inserir(22, "segundo")
    inserir(32, "terceiro")

    for i, lista in enumerate(tabela):
        if lista:
            print("posição", i, "->", lista)
