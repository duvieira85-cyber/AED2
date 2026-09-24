# Projeto 2 — Calculadora de expressões
# Usa duas pilhas: uma para valores e outra para operadores.
# A precedência dos operadores determina quando uma operação deve ser executada.

import re


def avaliar_expressao(expressao):
    # Define a prioridade dos operadores matemáticos.
    precedencia = {"+": 1, "-": 1, "*": 2, "/": 2}

    valores = []
    operadores = []

    # Separa números, parênteses e operadores da expressão.
    tokens = re.findall(
        r"\d+(?:\.\d+)?|[()+\-*/]",
        expressao.replace(" ", ""),
    )

    def aplicar_operador():
        # Retira primeiro o operador que está no topo da pilha.
        operador = operadores.pop()

        # Os dois últimos valores correspondem aos operandos da operação.
        b = valores.pop()
        a = valores.pop()

        if operador == "+":
            valores.append(a + b)
        elif operador == "-":
            valores.append(a - b)
        elif operador == "*":
            valores.append(a * b)
        elif operador == "/":
            if b == 0:
                raise ZeroDivisionError("Divisão por zero")
            valores.append(a / b)

    for token in tokens:
        if token.replace(".", "", 1).isdigit():
            # Números são armazenados na pilha de valores.
            valores.append(float(token) if "." in token else int(token))

        elif token == "(":
            # O parêntese de abertura marca o início de uma subexpressão.
            operadores.append(token)

        elif token == ")":
            # Resolve os operadores até encontrar o parêntese correspondente.
            while operadores and operadores[-1] != "(":
                aplicar_operador()

            if not operadores:
                raise ValueError("Parênteses desbalanceados")

            operadores.pop()

        else:
            # Antes de inserir o novo operador, resolve os de maior ou igual precedência.
            while (
                operadores
                and operadores[-1] != "("
                and precedencia[operadores[-1]] >= precedencia[token]
            ):
                aplicar_operador()

            operadores.append(token)

    # Finaliza as operações que ainda ficaram pendentes.
    while operadores:
        if operadores[-1] == "(":
            raise ValueError("Parênteses desbalanceados")
        aplicar_operador()

    if len(valores) != 1:
        raise ValueError("Expressão inválida")

    return valores[0]


if __name__ == "__main__":
    print(avaliar_expressao("3 + 4 * (2 - 1)"))
    print(avaliar_expressao("10 / 2 + 6 * 3"))
