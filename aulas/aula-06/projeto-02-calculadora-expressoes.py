# Projeto 2 — Calculadora de expressões
# Utiliza duas pilhas: uma para valores e outra para operadores.
# A precedência dos operadores determina a ordem das operações.


import re


def avaliar_expressao(expressao):
    # Define a prioridade: multiplicação/divisão têm precedência
    # sobre adição/subtração.
    precedencia = {"+": 1, "-": 1, "*": 2, "/": 2}

    # Pilha dos números e pilha dos operadores encontrados na expressão.
    valores = []
    operadores = []

    # Remove espaços e separa números, parênteses e operadores.
    tokens = re.findall(
        r"\d+(?:\.\d+)?|[()+\-*/]",
        expressao.replace(" ", ""),
    )

    def aplicar_operador():
        # Retira o operador do topo da pilha.
        operador = operadores.pop()

        # Retira os dois últimos valores, respeitando a ordem da operação.
        b = valores.pop()
        a = valores.pop()

        if operador == "+":
            valores.append(a + b)
        elif operador == "-":
            valores.append(a - b)
        elif operador == "*":
            valores.append(a * b)
        elif operador == "/":
            # Evita realizar uma divisão inválida.
            if b == 0:
                raise ZeroDivisionError("Divisão por zero")

            valores.append(a / b)

    # Processa os tokens da expressão da esquerda para a direita.
    for token in tokens:
        if token.replace(".", "", 1).isdigit():
            # Números entram na pilha de valores.
            valores.append(float(token) if "." in token else int(token))

        elif token == "(":
            # A abertura marca o início de uma subexpressão.
            operadores.append(token)

        elif token == ")":
            # Resolve operadores até encontrar a abertura correspondente.
            while operadores and operadores[-1] != "(":
                aplicar_operador()

            # Não encontrar "(" significa que os parênteses estão inválidos.
            if not operadores:
                raise ValueError("Parênteses desbalanceados")

            # Remove o "(" que serviu apenas como marcador.
            operadores.pop()

        else:
            # Antes de empilhar o novo operador, resolve os operadores
            # que possuem precedência maior ou igual à atual.
            while (
                operadores
                and operadores[-1] != "("
                and precedencia[operadores[-1]] >= precedencia[token]
            ):
                aplicar_operador()

            operadores.append(token)

    # Resolve os operadores restantes depois do fim da expressão.
    while operadores:
        if operadores[-1] == "(":
            raise ValueError("Parênteses desbalanceados")

        aplicar_operador()

    # Uma expressão válida deve terminar com exatamente um valor.
    if len(valores) != 1:
        raise ValueError("Expressão inválida")

    return valores[0]


if __name__ == "__main__":
    # Exemplos que demonstram precedência e uso de parênteses.
    print(avaliar_expressao("3 + 4 * (2 - 1)"))
    print(avaliar_expressao("10 / 2 + 6 * 3"))
