# Exercício 1 — Complexidade da busca sequencial
# Melhor caso: O(1), quando o alvo está logo no início.
# Pior caso: O(n), quando o alvo está no fim ou não existe.

def busca_sequencial(lista, alvo):
    for i in range(len(lista)):
        # Percorre os elementos desde o índice 0.
        if lista[i] == alvo:
            return i
    return -1


if __name__ == "__main__":
    lista = [7, 12, 5, 12, 8]

    print("Melhor caso:", busca_sequencial(lista, 7))
    print("Pior caso:", busca_sequencial(lista, 99))
