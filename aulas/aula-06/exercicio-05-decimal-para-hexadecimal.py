def decimal_para_hexa(n):
    if n < 0:
        raise ValueError("n deve ser não-negativo")

    if n == 0:
        return "0"

    digitos = "0123456789ABCDEF"
    pilha = []

    while n > 0:
        resto = n % 16
        pilha.append(digitos[resto])
        n //= 16

    hexa = ""
    while pilha:
        hexa += pilha.pop()

    return hexa


if __name__ == "__main__":
    print(decimal_para_hexa(26))
    print(decimal_para_hexa(255))
    print(decimal_para_hexa(0))
    print(decimal_para_hexa(4095))
