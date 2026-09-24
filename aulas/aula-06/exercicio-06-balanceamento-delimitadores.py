# Exercício 6 — Balanceamento de delimitadores
# Uma pilha permite verificar se cada delimitador de fechamento
# corresponde à última abertura que ainda está pendente.


def balanceia_colchetes(expressao):
    # Mapeia cada fechamento para seu respectivo delimitador de abertura.
    pares = {")": "(", "]": "[", "}": "{"}

    # Guarda os delimitadores de abertura encontrados.
    pilha = []

    # Analisa a expressão caractere por caractere.
    for caractere in expressao:
        if caractere in "([{":
            # Empilha cada abertura para conferir posteriormente.
            pilha.append(caractere)

        elif caractere in ")]}":
            # Um fechamento sem abertura correspondente torna a expressão inválida.
            if not pilha:
                return False

            # Retira a última abertura pendente, seguindo LIFO.
            abertura = pilha.pop()

            # O tipo do fechamento precisa corresponder à abertura retirada.
            if abertura != pares[caractere]:
                return False

    # Se ainda existir abertura na pilha, algum delimitador não foi fechado.
    return not pilha


if __name__ == "__main__":
    # Expressão balanceada.
    print(balanceia_colchetes("({[]})"))

    # Fechamento incompatível com a abertura.
    print(balanceia_colchetes("({[}])"))

    # Expressão com diferentes tipos de delimitadores corretamente balanceados.
    print(balanceia_colchetes("{(a+b)*[c-d]}"))

    # Falta um fechamento para uma das aberturas.
    print(balanceia_colchetes("((a+b)"))
