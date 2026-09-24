# Exercício 2 — Busca por nome
# Como Mariana não está na lista, a busca percorre todos os elementos: pior caso O(n).

def busca_mariana(lista):
    for i in range(len(lista)):
        # Compara cada nome com o valor procurado.
        if lista[i] == "Mariana":
            return i

    return -1


if __name__ == "__main__":
    nomes = ["Ana", "Bruno", "Carlos"]
    print(busca_mariana(nomes))
