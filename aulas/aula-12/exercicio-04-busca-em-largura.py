# Exercício 4 — Busca em largura (BFS)
# Explora o grafo por níveis usando uma fila.
# Visita o vértice, marca como visitado e enfileira os vizinhos.


from collections import deque


def bfs(grafo, inicio):
    visitados = [inicio]
    fila = deque([inicio])
    ordem = []

    while fila:
        # Retira o vértice da frente da fila.
        atual = fila.popleft()
        ordem.append(atual)

        # Enfileira os vizinhos ainda não visitados.
        for vizinho in grafo.get(atual, []):
            if vizinho not in visitados:
                visitados.append(vizinho)
                fila.append(vizinho)

    return ordem


if __name__ == "__main__":
    grafo = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "D"],
        "D": ["B", "C"],
    }

    print(bfs(grafo, "A"))
