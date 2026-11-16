# Exercício 2 — Adicionar arestas
# Grafo não direcionado: a aresta A-B vale nos dois sentidos,
# então cada vértice entra na lista do outro.


grafo = {}

def adicionar_aresta(grafo, v1, v2):
    # Cria a lista do vértice se ele ainda não existe.
    if v1 not in grafo:
        grafo[v1] = []
    if v2 not in grafo:
        grafo[v2] = []

    # Grafo não direcionado: a ligação vale nos dois sentidos.
    grafo[v1].append(v2)
    grafo[v2].append(v1)


if __name__ == "__main__":
    adicionar_aresta(grafo, "A", "B")
    adicionar_aresta(grafo, "B", "C")

    print(grafo)
