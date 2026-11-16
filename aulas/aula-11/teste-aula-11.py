# Testes básicos da Aula 11
# Verifica inserção, busca, percurso em ordem, extremos,
# contagens e os dois projetos da aula.
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


buscar = carregar("exercicio-02-bst-inserir-buscar.py")
em_ordem_mod = carregar("exercicio-03-percurso-em-ordem.py")
extremos = carregar("exercicio-05-menor-maior-valor.py")
contagens = carregar("exercicio-06-contar-nos-folhas.py")
dicionario = carregar("projeto-01-dicionario-bst.py")
indice = carregar("projeto-02-indice-palavras.py")


def montar_arvore():
    # Árvore de teste: 10 raiz, filhos 5 e 20, netos 3 e 25.
    raiz = buscar.No(10)
    raiz.esquerda = buscar.No(5)
    raiz.direita = buscar.No(20)
    raiz.esquerda.esquerda = buscar.No(3)
    raiz.direita.direita = buscar.No(25)
    return raiz


def testar():
    raiz = None
    for v in [10, 5, 20, 3, 7, 25]:
        raiz = buscar.inserir(raiz, v)

    # Busca encontra o que existe e não encontra o que não existe.
    assert buscar.buscar(raiz, 7) is True
    assert buscar.buscar(raiz, 99) is False

    # Percurso em ordem lista a BST em ordem crescente.
    assert em_ordem_mod.em_ordem(raiz, []) == [3, 5, 7, 10, 20, 25]

    # Menor e maior valor.
    assert extremos.menor_valor(raiz) == 3
    assert extremos.maior_valor(raiz) == 25

    # Contagens.
    assert contagens.contar_nos(raiz) == 6
    assert contagens.contar_folhas(raiz) == 3

    # Projeto 1: dicionário ordenado e busca de palavra.
    raiz_d = None
    for palavra, sigla in [("cachorro", "animal"), ("abelha", "inseto")]:
        raiz_d = dicionario.inserir(raiz_d, palavra, sigla)
    assert dicionario.buscar(raiz_d, "abelha") == "inseto"
    assert dicionario.listar(raiz_d, []) == ["abelha", "cachorro"]

    # Projeto 2: índice alfabético sem repetição.
    raiz_i = None
    for palavra in "dados e estrutura de dados".split():
        raiz_i = indice.inserir(raiz_i, palavra)
    assert indice.em_ordem(raiz_i, []) == ["dados", "de", "e", "estrutura"]

    print("Todos os testes da Aula 11 passaram.")


if __name__ == "__main__":
    testar()
