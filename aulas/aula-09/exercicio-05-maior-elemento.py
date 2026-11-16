# Exercício 5 — Maior elemento de um vetor (recursivo)
# Compara o primeiro elemento com o maior do resto do vetor.


def maior_elemento(lista):
    # Caso base: um vetor com um único elemento já é a resposta.
    if len(lista) == 1:
        return lista[0]

    # O maior do vetor é o maior entre o primeiro e o maior do resto.
    maior_do_resto = maior_elemento(lista[1:])

    if lista[0] > maior_do_resto:
        return lista[0]

    return maior_do_resto


if __name__ == "__main__":
    print(maior_elemento([3, 17, 8, 25, 9]))
    print(maior_elemento([42]))
