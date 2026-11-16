# Exercício 2 — Tabela hash básica
# A tabela é uma lista de listas. Cada chave entra na posição
# calculada pela função hash, com acesso direto na busca.


TAMANHO = 10
tabela = [[] for _ in range(TAMANHO)]


def funcao_hash(chave):
    return chave % TAMANHO


def inserir(chave, valor):
    # Calcula a posição e guarda o par na lista interna.
    posicao = funcao_hash(chave)
    tabela[posicao].append((chave, valor))


def buscar(chave):
    # Procura o par dentro da lista da posição calculada.
    posicao = funcao_hash(chave)

    for chave_salva, valor in tabela[posicao]:
        if chave_salva == chave:
            return valor

    return None


if __name__ == "__main__":
    inserir(12, "caneta")
    inserir(25, "caderno")

    print(buscar(12))
    print(buscar(25))
