# Projeto 1 — Estoque de produtos por código
# O código do produto é a chave da tabela hash
# e a quantidade em estoque é o valor.


TAMANHO = 10
estoque = [[] for _ in range(TAMANHO)]


def posicao(codigo):
    return codigo % TAMANHO


def adicionar(codigo, quantidade):
    # Produto novo entra com a quantidade; existente soma.
    for i, (codigo_salvo, _) in enumerate(estoque[posicao(codigo)]):
        if codigo_salvo == codigo:
            estoque[posicao(codigo)][i] = (codigo, estoque[posicao(codigo)][i][1] + quantidade)
            return

    estoque[posicao(codigo)].append((codigo, quantidade))


def consultar(codigo):
    # Retorna a quantidade em estoque do código consultado.
    for codigo_salvo, quantidade in estoque[posicao(codigo)]:
        if codigo_salvo == codigo:
            return quantidade

    return 0


if __name__ == "__main__":
    adicionar(101, 30)
    adicionar(111, 15)
    adicionar(101, 5)

    print("estoque do código 101:", consultar(101))
    print("estoque do código 111:", consultar(111))
    print("estoque do código 999:", consultar(999))
