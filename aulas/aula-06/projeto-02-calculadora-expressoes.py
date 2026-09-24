import re


def avaliar_expressao(expressao):
    precedencia = {"+": 1, "-": 1, "*": 2, "/": 2}
    valores = []
    operadores = []

    tokens = re.findall(
        r"\d+(?:\.\d+)?|[()+\-*/]",
        expressao.replace(" ", ""),
    )

    def aplicar_operador():
        operador = operadores.pop()
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
            valores.append(float(token) if "." in token else int(token))

        elif token == "(":
            operadores.append(token)

        elif token == ")":
            while operadores and operadores[-1] != "(":
                aplicar_operador()

            if not operadores:
                raise ValueError("Parênteses desbalanceados")

            operadores.pop()

        else:
            while (
                operadores
                and operadores[-1] != "("
                and precedencia[operadores[-1]] >= precedencia[token]
            ):
                aplicar_operador()

            operadores.append(token)

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
