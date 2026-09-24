# Exercício 6 — Balanceamento de delimitadores
# Uma pilha permite conferir se cada fechamento corresponde à última abertura pendente.

def balanceia_colchetes(expressao):
    pares = {")": "(", "]": "[", "}": "{"}
    pilha = []

    for caractere in expressao:
        if caractere in "([{":
            # Guarda cada delimitador de abertura para conferência posterior.
            pilha.append(caractere)

        elif caractere in ")]}":
            # Um fechamento sem abertura correspondente torna a expressão inválida.
            if not pilha:
                return False

            abertura = pilha.pop()

            # O fechamento precisa corresponder exatamente à última abertura.
            if abertura != pares[caractere]:
                return False

    # Ao final, nenhuma abertura pode permanecer pendente.
    return not pilha


if __name__ == "__main__":
    print(balanceia_colchetes("({[]})"))
    print(balanceia_colchetes("({[}])"))
    print(balanceia_colchetes("{(a+b)*[c-d]}"))
    print(balanceia_colchetes("((a+b)"))
