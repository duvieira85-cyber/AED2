# Aula 12 — Grafos
# Reúne as soluções dos exercícios da aula:
# lista de adjacência, BFS, DFS e verificação de caminho.


from collections import deque


def adicionar_aresta(grafo, v1, v2):
    # Grafo não direcionado: vale nos dois sentidos.
    grafo.setdefault(v1, []).append(v2)
    grafo.setdefault(v2, []).append(v1)


def bfs(grafo, inicio):
    # Explora por níveis com uma fila.
    visitados = [inicio]
    fila = deque([inicio])
    ordem = []

    while fila:
        atual = fila.popleft()
        ordem.append(atual)

        for vizinho in grafo.get(atual, []):
            if vizinho not in visitados:
                visitados.append(vizinho)
                fila.append(vizinho)

    return ordem


def dfs(grafo, vertice, visitados):
    # Explora o mais fundo possível com recursão.
    visitados.append(vertice)

    for vizinho in grafo.get(vertice, []):
        if vizinho not in visitados:
            dfs(grafo, vizinho, visitados)

    return visitados


def existe_caminho(grafo, origem, destino):
    # BFS da origem: destino visitado significa caminho existente.
    visitados = [origem]
    fila = deque([origem])

    while fila:
        atual = fila.popleft()

        if atual == destino:
            return True

        for vizinho in grafo.get(atual, []):
            if vizinho not in visitados:
                visitados.append(vizinho)
                fila.append(vizinho)

    return False


if __name__ == "__main__":
    grafo = {}
    adicionar_aresta(grafo, "A", "B")
    adicionar_aresta(grafo, "A", "C")
    adicionar_aresta(grafo, "B", "D")
    adicionar_aresta(grafo, "C", "D")

    print(bfs(grafo, "A"))
    print(dfs(grafo, "A", []))
    print(existe_caminho(grafo, "A", "D"))
    print(existe_caminho(grafo, "A", "Z"))
