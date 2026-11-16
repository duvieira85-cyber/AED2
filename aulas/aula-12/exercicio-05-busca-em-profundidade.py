# Exercício 5 — Busca em profundidade (DFS)
# Explora o grafo indo o mais fundo possível antes de voltar,
# usando recursão e um conjunto de visitados.


def dfs(grafo, vertice, visitados):
    # Marca o vértice atual como visitado.
    visitados.append(vertice)

    # Visita cada vizinho que ainda não foi visitado.
    for vizinho in grafo.get(vertice, []):
        if vizinho not in visitados:
            dfs(grafo, vizinho, visitados)

    return visitados


if __name__ == "__main__":
    grafo = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "D"],
        "D": ["B", "C"],
    }

    print(dfs(grafo, "A", []))
