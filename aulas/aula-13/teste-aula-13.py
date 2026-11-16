# Testes básicos da Aula 13
# Verifica função hash, inserção, busca, colisão,
# remoção e os dois projetos da aula.
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


colisao = carregar("exercicio-03-tratar-colisoes.py")
remover = carregar("exercicio-04-remover-chave.py")
estoque = carregar("projeto-01-estoque-produtos.py")
cache = carregar("projeto-02-cache-simples.py")


def testar():
    # Colisão: chaves 12, 22 e 32 caem na mesma posição e convivem.
    colisao.inserir(12, "primeiro")
    colisao.inserir(22, "segundo")
    colisao.inserir(32, "terceiro")
    assert colisao.tabela[2] == [(12, "primeiro"), (22, "segundo"), (32, "terceiro")]

    # Remoção encontra e remove a chave exata; repetida falha.
    remover.inserir(12, "caneta")
    remover.inserir(22, "caderno")
    assert remover.remover(12) is True
    assert remover.remover(12) is False

    # Projeto 1: estoque soma quantidades do mesmo código.
    estoque.adicionar(101, 30)
    estoque.adicionar(101, 5)
    assert estoque.consultar(101) == 35
    assert estoque.consultar(999) == 0

    # Projeto 2: cache devolve o valor sem recalcular.
    valor1, calculado1 = cache.consultar(4)
    valor2, calculado2 = cache.consultar(4)
    assert valor1 == valor2 == 16
    assert calculado1 is True and calculado2 is False

    print("Todos os testes da Aula 13 passaram.")


if __name__ == "__main__":
    testar()
