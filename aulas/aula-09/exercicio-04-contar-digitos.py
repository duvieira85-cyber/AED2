# Exercício 4 — Contar os dígitos de um número
# Enquanto o número tem mais de um dígito, divida por 10 e conte 1 + resto.


def contar_digitos(n):
    # Números menores que 10 têm apenas um dígito.
    if n < 10:
        return 1

    # Remove o último dígito e soma 1 à contagem do resto.
    return 1 + contar_digitos(n // 10)


if __name__ == "__main__":
    print(contar_digitos(12345))
    print(contar_digitos(7))
