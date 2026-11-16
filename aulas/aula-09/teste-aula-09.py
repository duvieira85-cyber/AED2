# Testes basicos da Aula 09
# Verifica caso base e caso recursivo dos exercicios e os projetos:
# fatorial, somatorio, potencia, digitos, maior elemento, inversao,
# Torre de Hanoi e busca binaria recursiva.
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


fatorial_mod = carregar("exercicio-01-fatorial-recursivo.py")
somatorio_mod = carregar("exercicio-02-somatorio.py")
potencia_mod = carregar("exercicio-03-potencia-recursiva.py")
digitos_mod = carregar("exercicio-04-contar-digitos.py")
maior_mod = carregar("exercicio-05-maior-elemento.py")
inverter_mod = carregar("exercicio-06-inverter-lista.py")
hanoi_mod = carregar("projeto-01-torre-de-hanoi.py")
binaria_mod = carregar("projeto-02-busca-binaria-recursiva.py")


def testar():
    # Casos base.
    assert fatorial_mod.fatorial(0) == 1
    assert somatorio_mod.somatorio(1) == 1
    assert potencia_mod.potencia(7, 0) == 1
    assert digitos_mod.contar_digitos(5) == 1

    # Casos recursivos.
    assert fatorial_mod.fatorial(5) == 120
    assert somatorio_mod.somatorio(10) == 55
    assert potencia_mod.potencia(2, 10) == 1024
    assert digitos_mod.contar_digitos(12345) == 5
    assert maior_mod.maior_elemento([3, 17, 8, 25, 9]) == 25
    assert inverter_mod.inverter([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]

    # Torre de Hanoi com 3 discos: 7 movimentos minimos.
    movimentos = []
    hanoi_mod.hanoi(3, "A", "C", "B", movimentos)
    assert len(movimentos) == 7

    # Busca binaria recursiva em vetor ordenado.
    ordenado = [2, 5, 8, 12, 16, 23, 38, 56]
    assert binaria_mod.busca_binaria_recursiva(ordenado, 23, 0, 7) == 5
    assert binaria_mod.busca_binaria_recursiva(ordenado, 99, 0, 7) == -1

    print("Todos os testes da Aula 09 passaram.")


if __name__ == "__main__":
    testar()
