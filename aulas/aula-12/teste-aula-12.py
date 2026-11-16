# Testes básicos da Aula 12
# Verifica lista de adjacência, arestas, vizinhos,
# BFS, DFS, caminho e os dois projetos da aula.
#
# Os nomes de arquivo da aula usam hifen, que não pode aparecer
# em um import normal — por isso os módulos são carregados
# pelo caminho com a biblioteca importlib.

import importlib.util
import os


def carregar(nome_arquivo):
    caminho = os.path.join(os.path.dirname(__file__), nome_arquivo)
    spec = importlib.util.spec_from_file_location(nome_arquivo[:-3].replace("-", "_"), caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


bfs = carregar("exercicio-04-busca-em-largura.py").bfs
dfs = carregar("exercicio-05-busca-em-profundidade.py").dfs
caminho = carregar("exercicio-06-caminho-existe.py").existe_caminho
rede = carregar("projeto-01-rede-social.py")
mapa = carregar("projeto-02-mapa-cidades.py")


def testar():
    grafo = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "D"],
        "D": ["B", "C"],
    }

    # BFS e DFS visitam todos os 4 vértices do grafo conectado.
    assert sorted(bfs(grafo, "A")) == ["A", "B", "C", "D"]
    assert sorted(dfs(grafo, "A", [])) == ["A", "B", "C", "D"]

    # Existe caminho dentro do componente e não existe para vértice isolado.
    assert caminho(grafo, "A", "D") is True
    grafo["E"] = []
    assert caminho(grafo, "A", "E") is False

    # Projeto 1: amizades e amigos em comum.
    rede.rede.clear()
    for nome in ["Ana", "Bruno", "Carla", "Diego"]:
        rede.adicionar_pessoa(nome)
    rede.criar_amizade("Ana", "Bruno")
    rede.criar_amizade("Ana", "Carla")
    rede.criar_amizade("Bruno", "Diego")
    rede.criar_amizade("Carla", "Diego")
    assert rede.amigos("Ana") == ["Bruno", "Carla"]
    assert rede.amigos_em_comum("Ana", "Diego") == ["Bruno", "Carla"]

    # Projeto 2: rota existe e rota impossível é detectada.
    mapa.mapa.clear()
    mapa.adicionar_estrada("Sorocaba", "Votorantim")
    mapa.adicionar_estrada("Sorocaba", "Itapetininga")
    mapa.adicionar_estrada("Itapetininga", "Campinas")
    assert "estrada(s)" in mapa.rota("Sorocaba", "Campinas")
    assert "Não existe rota" in mapa.rota("Votorantim", "Rio de Janeiro")

    print("Todos os testes da Aula 12 passaram.")


if __name__ == "__main__":
    testar()
