# Exercício 4 — Menores idades
# Comparamos duas abordagens para verificar se a menor idade aparece mais de uma vez.
# A primeira faz duas varreduras O(n); a segunda ordena a lista em O(n log n).


def contar_menor_repetido(idades):
    # Primeira passagem: procura a menor idade da lista.
    menor = 200

    for idade in idades:
        if idade < menor:
            # Atualiza a menor idade quando encontra um valor inferior.
            menor = idade

    # Segunda passagem: conta quantas vezes a menor idade aparece.
    cont = 0

    for idade in idades:
        if idade == menor:
            cont += 1

    # Retorna True quando a menor idade aparece mais de uma vez.
    return cont > 1


def menor_repetido_ordenando(idades):
    # A ordenação coloca as menores idades nas primeiras posições.
    idades.sort()

    # Se os dois primeiros valores forem iguais,
    # a menor idade aparece pelo menos duas vezes.
    return idades[0] == idades[1]


if __name__ == "__main__":
    # Usa uma cópia na segunda abordagem para preservar os dados originais.
    dados = [18, 22, 18, 30]

    print("Duas passagens:", contar_menor_repetido(dados))
    print("Ordenando:", menor_repetido_ordenando(dados.copy()))
