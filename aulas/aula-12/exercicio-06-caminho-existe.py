# Exercício 6 — Existe caminho entre dois vértices?
# Usa BFS partindo da origem: se o destino aparecer
# na lista de visitados, existe caminho.


from collections import deque


def existe_caminho(grafo, origem, destino):
    visitados = [origem]
    fila = deque([origem])

    while fila:
        atual = fila.popleft()

        # Chegou no destino: existe caminho.
        if atual == destino:
            return True

        for vizinho in grafo.get(atual, []):
            if vizinho not in visitados:
                visitados.append(vizinho)
                fila.append(vizinho)

    return False


if __name__ == "__main__":
    grafo = {
        "A": ["B"],
        "B": ["A", "C"],
        "C": ["B", "D"],
        "D": ["C"],
        "E": [],
    }

    print(existe_caminho(grafo, "A", "D"))
    print(existe_caminho(grafo, "A", "E"))
