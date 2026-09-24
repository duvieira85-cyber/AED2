# Aula 06 — Exercícios e projetos resolvidos
# Reúne as soluções do Capítulo 6 em um único arquivo para facilitar os estudos.
# O foco da aula é o uso de pilhas e o princípio LIFO.


from exercicio_01_push_pop import acompanhar_pilha
from exercicio_02_peek_pop import executar as exercicio_2
from exercicio_03_propriedades_pilha import responder as exercicio_3
from exercicio_04_pop_pilha_vazia import contar_tentativas_invalidas
from exercicio_05_decimal_para_hexadecimal import decimal_para_hexa
from exercicio_06_balanceamento_delimitadores import balanceia_colchetes
from projeto_02_calculadora_expressoes import avaliar_expressao


if __name__ == "__main__":
    # Executa cada exercício individualmente para facilitar a revisão.
    print("Exercício 1:")
    acompanhar_pilha()

    print("\nExercício 2:")
    exercicio_2()

    print("\nExercício 3:")
    exercicio_3()

    print("\nExercício 4:")
    contar_tentativas_invalidas()

    # Testa a conversão de decimal para hexadecimal com valores diferentes.
    print("\nExercício 5:")
    print(decimal_para_hexa(26))
    print(decimal_para_hexa(255))
    print(decimal_para_hexa(0))
    print(decimal_para_hexa(4095))

    # Testa expressões com delimitadores balanceados e desbalanceados.
    print("\nExercício 6:")
    print(balanceia_colchetes("({[]})"))
    print(balanceia_colchetes("({[}])"))
    print(balanceia_colchetes("{(a+b)*[c-d]}"))
    print(balanceia_colchetes("((a+b)"))

    # Executa exemplos do Projeto 2, que utiliza pilhas
    # para controlar valores e operadores.
    print("\nProjeto 2:")
    print(avaliar_expressao("3 + 4 * (2 - 1)"))
    print(avaliar_expressao("10 / 2 + 6 * 3"))
