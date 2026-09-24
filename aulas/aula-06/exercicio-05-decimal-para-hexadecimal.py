# Exercício 5 — Conversão de decimal para hexadecimal
# A pilha é usada para inverter a ordem dos restos obtidos nas divisões por 16.

def decimal_para_hexa(n):
    if n < 0:
        raise ValueError("n deve ser não-negativo")

    if n == 0:
        return "0"

    digitos = "0123456789ABCDEF"
    pilha = []

    while n > 0:
        # Cada resto representa um dígito hexadecimal.
        resto = n % 16
        pilha.append(digitos[resto])

        # Divisão inteira prepara o próximo passo da conversão.
        n //= 16

    hexa = ""

    while pilha:
        # Retira os dígitos na ordem inversa em que foram empilhados.
        hexa += pilha.pop()

    return hexa


if __name__ == "__main__":
    print(decimal_para_hexa(26))
    print(decimal_para_hexa(255))
    print(decimal_para_hexa(0))
    print(decimal_para_hexa(4095))
