# Projeto 2 — Consulta de produto por código
# O vetor de códigos está ordenado em ordem crescente,
# o que permite usar busca binária para achar o produto na hora.


def busca_binaria(codigos, alvo):
    inicio = 0
    fim = len(codigos) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if codigos[meio] == alvo:
            return meio

        if codigos[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1


def consultar_produto(codigos, produtos, codigo):
    indice = busca_binaria(codigos, codigo)

    if indice == -1:
        return "Código " + str(codigo) + ": produto não cadastrado."

    return "Código " + str(codigo) + ": " + produtos[indice]


codigos = [101, 205, 310, 415, 520, 630]
produtos = ["Cadeira", "Mesa", "Luminária", "Sofá", "Estante", "Poltrona"]

print(consultar_produto(codigos, produtos, 415))
print(consultar_produto(codigos, produtos, 999))
