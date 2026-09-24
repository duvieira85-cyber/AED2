# Exercício 2 — Busca por nome
# Mariana não está na lista, então a busca precisa percorrer
# todos os elementos antes de concluir que o nome não existe.
# Esse cenário representa o pior caso O(n).


def busca_mariana(lista):
    # Percorre os nomes desde a primeira posição.
    for i in range(len(lista)):
        # Compara o nome atual com o nome procurado.
        if lista[i] == "Mariana":
            return i

    # Retorna -1 quando Mariana não foi encontrada.
    return -1


if __name__ == "__main__":
    nomes = ["Ana", "Bruno", "Carlos"]

    # Como Mariana não está na lista, o resultado será -1.
    print(busca_mariana(nomes))
