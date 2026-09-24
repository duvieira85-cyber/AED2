# Exercício 4 — Menores idades
# Comparamos duas abordagens: duas varreduras O(n) e ordenação O(n log n).

def contar_menor_repetido(idades):
    # Primeira passagem: encontra a menor idade.
    menor = 200
    for idade in idades:
        if idade < menor:
            menor = idade

    # Segunda passagem: conta quantas vezes a menor idade aparece.
    cont = 0
    for idade in idades:
        if idade == menor:
            cont += 1

    return cont > 1


def menor_repetido_ordenando(idades):
    # A ordenação coloca as menores idades nas primeiras posições.
    idades.sort()
    return idades[0] == idades[1]


if __name__ == "__main__":
    dados = [18, 22, 18, 30]
    print("Duas passagens:", contar_menor_repetido(dados))
    print("Ordenando:", menor_repetido_ordenando(dados.copy()))
