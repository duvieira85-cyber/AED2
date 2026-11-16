# Testes básicos da Aula 10
# Todos os métodos devem produzir o mesmo resultado ordenado,
# inclusive com vetores repetidos, já ordenado e vazio.
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


bubble = carregar("exercicio-01-bubble-sort.py").bubble_sort
insertion = carregar("exercicio-02-insertion-sort.py").insertion_sort
selection = carregar("exercicio-03-selection-sort.py").selection_sort
merge = carregar("exercicio-04-merge-sort.py").merge_sort
quick = carregar("exercicio-05-quick-sort.py").quick_sort
projeto = carregar("projeto-01-catalogo-ordenado.py")


def testar():
    metodos = [bubble, insertion, selection, merge, quick]
    caso = [8, 3, 5, 1, 9, 2, 7, 1]

    # Todos os métodos ordenam o mesmo vetor da mesma forma.
    for metodo in metodos:
        assert metodo(caso[:]) == [1, 1, 2, 3, 5, 7, 8, 9]

    # Vetor já ordenado continua ordenado.
    for metodo in metodos:
        assert metodo([1, 2, 3, 4]) == [1, 2, 3, 4]

    # Vetor vazio permanece vazio.
    for metodo in metodos:
        assert metodo([]) == []

    # Projeto: catálogo por título e por nota.
    catalogo = [
        {"titulo": "B", "nota": 7.0},
        {"titulo": "A", "nota": 9.0},
    ]
    por_titulo = projeto.merge_por_chave(catalogo, lambda f: f["titulo"])
    assert [f["titulo"] for f in por_titulo] == ["A", "B"]
    por_nota = projeto.merge_por_chave(catalogo, lambda f: f["nota"], True)
    assert por_nota[0]["nota"] == 9.0

    print("Todos os testes da Aula 10 passaram.")


if __name__ == "__main__":
    testar()
