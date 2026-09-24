def balanceia_colchetes(expressao):
    pares = {")": "(", "]": "[", "}": "{"}
    pilha = []

    for caractere in expressao:
        if caractere in "([{":
            pilha.append(caractere)
        elif caractere in ")]}":
            if not pilha:
                return False

            abertura = pilha.pop()
            if abertura != pares[caractere]:
                return False

    return not pilha


if __name__ == "__main__":
    print(balanceia_colchetes("({[]})"))
    print(balanceia_colchetes("({[}])"))
    print(balanceia_colchetes("{(a+b)*[c-d]}"))
    print(balanceia_colchetes("((a+b)"))
