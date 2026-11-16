# Aula 13 — Tabelas Hash
# Reúne as soluções dos exercícios da aula:
# função hash, inserção, busca, colisão por encadeamento e remoção.


TAMANHO = 10
tabela = [[] for _ in range(TAMANHO)]


def funcao_hash(chave):
    # Resto da divisão da chave pelo tamanho da tabela.
    return chave % TAMANHO


def inserir(chave, valor):
    # Guarda o par na lista encadeada da posição.
    tabela[funcao_hash(chave)].append((chave, valor))


def buscar(chave):
    # Procura a chave exata dentro da posição calculada.
    for chave_salva, valor in tabela[funcao_hash(chave)]:
        if chave_salva == chave:
            return valor

    return None


def remover(chave):
    # Remove o par com a chave exata da posição calculada.
    posicao = funcao_hash(chave)

    for i, (chave_salva, valor) in enumerate(tabela[posicao]):
        if chave_salva == chave:
            del tabela[posicao][i]
            return True

    return False


if __name__ == "__main__":
    inserir(12, "caneta")
    inserir(22, "caderno")

    print(buscar(12))
    print(buscar(22))
    print(buscar(99))

    remover(12)
    print(buscar(12))
    print(remover(12))
