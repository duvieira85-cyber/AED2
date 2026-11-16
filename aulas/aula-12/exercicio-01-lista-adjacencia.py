# Exercício 1 — Lista de adjacência
# O grafo é representado por um dicionário: cada vértice
# aponta para a lista de seus vizinhos.


grafo = {
    "A": ["B", "C"],
    "B": ["A"],
    "C": ["A", "D"],
    "D": ["C"],
}

if __name__ == "__main__":
    # Mostra cada vértice e seus vizinhos.
    for vertice in grafo:
        print(vertice, "->", grafo[vertice])
