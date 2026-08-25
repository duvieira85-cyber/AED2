def busca_sequencial(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1


def buscar_filme(catalogo, titulo):
    indice = busca_sequencial(catalogo, titulo)

    if indice != -1:
        return f"Filme '{titulo}' encontrado na posição {indice} do catálogo."
    else:
        return f"Filme '{titulo}' não encontrado no catálogo."


catalogo_filmes = [
    "Avatar",
    "Matrix",
    "Interestelar",
    "Toy Story",
    "O Senhor dos Anéis",
]

print(buscar_filme(catalogo_filmes, "Interestelar"))
print(buscar_filme(catalogo_filmes, "Titanic"))

# Melhor caso: O(1). Pior caso: O(n).