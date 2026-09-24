# Exercício 3 — Primeira ocorrência
# A busca termina assim que encontra a primeira ocorrência do valor.

def primeira_ocorrencia(lista, valor):
    for i in range(len(lista)):
        # Retorna imediatamente o primeiro índice encontrado.
        if lista[i] == valor:
            return i

    return -1


if __name__ == "__main__":
    print(primeira_ocorrencia([7, 12, 5, 12, 8], 12))
