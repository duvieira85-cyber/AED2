# Exercício 1 — Função hash por resto da divisão
# A função hash transforma a chave em um índice da tabela.
# O resto da divisão da chave pelo tamanho da tabela
# sempre cai dentro dos limites: de 0 a tamanho − 1.


def funcao_hash(chave, tamanho):
    # Chave numérica: resto da divisão pelo tamanho da tabela.
    return chave % tamanho


if __name__ == "__main__":
    # Tabela com 10 posições.
    for chave in [12, 25, 37, 100]:
        print(chave, "->", funcao_hash(chave, 10))
