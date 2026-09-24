# Exercício 5 — Contagem de ocorrências
# Para contar todas as ocorrências, é necessário verificar todos os elementos.
# Por isso, a operação possui complexidade O(n).


def contar_ocorrencias(valor, lista):
    # Inicia a contagem em zero.
    contador = 0

    # Percorre toda a lista, pois o valor pode aparecer várias vezes.
    for elemento in lista:
        if elemento == valor:
            # Cada correspondência encontrada aumenta o contador.
            contador += 1

    # Retorna a quantidade total de ocorrências encontradas.
    return contador


if __name__ == "__main__":
    print(contar_ocorrencias(3, [1, 3, 5, 3, 7]))
    print(contar_ocorrencias("a", ["a", "b", "c", "a"]))
    print(contar_ocorrencias(10, [11, 12, 13]))
