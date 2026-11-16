# Exercício 3 — Vizinhos de um vértice
# Os vizinhos são os vértices ligados diretamente por uma aresta.


grafo = {
    "A": ["B", "C"],
    "B": ["A", "C"],
    "C": ["A", "B"],
    "D": ["C"],
}


def vizinhos(grafo, vertice):
    # Usa get para não quebrar em vértice isolado.
    return grafo.get(vertice, [])


if __name__ == "__main__":
    print(vizinhos(grafo, "A"))
    print(vizinhos(grafo, "D"))
