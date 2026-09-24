# Projeto 1 — Catálogo de filmes
# Utiliza busca sequencial para localizar um filme pelo título.
# Melhor caso: O(1). Pior caso: O(n).


def busca_sequencial(lista, alvo):
    # Percorre o catálogo desde a primeira posição.
    for i in range(len(lista)):
        if lista[i] == alvo:
            # Retorna imediatamente a posição encontrada.
            return i

    # Indica que o título não está no catálogo.
    return -1


def buscar_filme(catalogo, titulo):
    # Reaproveita a busca sequencial para encontrar o título.
    indice = busca_sequencial(catalogo, titulo)

    if indice != -1:
        # O título foi encontrado e sua posição é conhecida.
        return f"Filme '{titulo}' encontrado na posição {indice} do catálogo."
    else:
        # O título não foi localizado.
        return f"Filme '{titulo}' não encontrado no catálogo."


# Catálogo utilizado no exemplo.
catalogo_filmes = [
    "Avatar",
    "Matrix",
    "Interestelar",
    "Toy Story",
    "O Senhor dos Anéis",
]

print(buscar_filme(catalogo_filmes, "Interestelar"))
print(buscar_filme(catalogo_filmes, "Titanic"))

# Complexidade:
# Melhor caso: O(1), quando o filme está na primeira posição.
# Pior caso: O(n), quando está na última posição ou não existe.
