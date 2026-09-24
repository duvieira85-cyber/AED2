# Exercício 5 — Contagem de ocorrências
# Percorre a lista inteira para contar todas as vezes que o valor aparece.

def contar_ocorrencias(valor, lista):
    contador = 0

    for elemento in lista:
        if elemento == valor:
            # Incrementa o contador quando encontra o valor procurado.
            contador += 1

    return contador


if __name__ == "__main__":
    print(contar_ocorrencias(3, [1, 3, 5, 3, 7]))
    print(contar_ocorrencias("a", ["a", "b", "c", "a"]))
    print(contar_ocorrencias(10, [11, 12, 13]))
