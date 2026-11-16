# Projeto 2 — Mapa de cidades: rota por BFS
# Cidades são vértices e rodovias são arestas.
# A BFS encontra se existe rota e em quantas estradas de distância.


from collections import deque

mapa = {}

def adicionar_estrada(c1, c2):
    # Rodovia é mão dupla.
    mapa.setdefault(c1, []).append(c2)
    mapa.setdefault(c2, []).append(c1)

def rota(origem, destino):
    # BFS guarda a distância em estradas junto com a visita.
    visitados = [origem]
    fila = deque([(origem, 0)])

    while fila:
        cidade, distancia = fila.popleft()

        if cidade == destino:
            return "Rota existe com " + str(distancia) + " estrada(s)."

        for vizinha in mapa.get(cidade, []):
            if vizinha not in visitados:
                visitados.append(vizinha)
                fila.append((vizinha, distancia + 1))

    return "Não existe rota entre as cidades."


if __name__ == "__main__":
    adicionar_estrada("Sorocaba", "Votorantim")
    adicionar_estrada("Sorocaba", "Itapetininga")
    adicionar_estrada("Itapetininga", "Campinas")

    print(rota("Sorocaba", "Campinas"))
    print(rota("Votorantim", "Rio de Janeiro"))
