# Exercício 4 — Remover uma chave da tabela hash
# Localiza a posição pela função hash e procura o par
# dentro da lista encadeada daquela posição.


TAMANHO = 10
tabela = [[] for _ in range(TAMANHO)]


def funcao_hash(chave):
    return chave % TAMANHO


def inserir(chave, valor):
    tabela[funcao_hash(chave)].append((chave, valor))


def remover(chave):
    posicao = funcao_hash(chave)

    # Procura o par com a chave exata na lista da posição.
    for i, (chave_salva, valor) in enumerate(tabela[posicao]):
        if chave_salva == chave:
            del tabela[posicao][i]
            return True

    return False


if __name__ == "__main__":
    inserir(12, "caneta")
    inserir(22, "caderno")

    print(remover(12))
    print(remover(12))
