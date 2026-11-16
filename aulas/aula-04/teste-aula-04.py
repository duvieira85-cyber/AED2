# Testes basicos da Aula 04
# Verifica a busca binaria em casos de borda: primeira posicao,
# ultima posicao, valor inexistente, contagem de passos
# e primeira ocorrencia em vetor com repetidos.
#
# Os nomes de arquivo da aula usam hifen, que nao pode aparecer
# em um import normal — por isso os modulos sao carregados
# pelo caminho com a biblioteca importlib.

import importlib.util
import os


def carregar(nome_arquivo):
    caminho = os.path.join(os.path.dirname(__file__), nome_arquivo)
    spec = importlib.util.spec_from_file_location(nome_arquivo[:-3].replace("-", "_"), caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


basica_mod = carregar("exercicio-01-busca-binaria-basica.py")
inexistente_mod = carregar("exercicio-03-elemento-inexistente.py")
passos_mod = carregar("exercicio-04-contar-passos.py")
primeira_mod = carregar("exercicio-05-primeira-ocorrencia.py")


def testar():
    vetor = [2, 5, 8, 12, 16, 23, 38, 56]

    # Valores presentes em posicoes variadas.
    assert basica_mod.busca_binaria(vetor, 2) == 0
    assert basica_mod.busca_binaria(vetor, 56) == 7
    assert basica_mod.busca_binaria(vetor, 23) == 5

    # Valores inexistentes retornam -1.
    assert inexistente_mod.busca_binaria(vetor, 99) == -1
    assert inexistente_mod.busca_binaria([], 10) == -1

    # Vetor grande resolve em poucas comparacoes.
    indice, passos = passos_mod.busca_binaria_com_passos(list(range(1, 1001)), 998)
    assert indice == 997 and passos <= 10

    # Primeira ocorrencia em vetor com repetidos.
    assert primeira_mod.primeira_ocorrencia([2, 8, 8, 8, 8, 15, 21], 8) == 1
    assert primeira_mod.primeira_ocorrencia([2, 8, 8, 8, 8, 15, 21], 15) == 5

    print("Todos os testes da Aula 04 passaram.")


if __name__ == "__main__":
    testar()
