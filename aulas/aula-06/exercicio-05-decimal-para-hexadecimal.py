# Exercício 5 — Conversão de decimal para hexadecimal
# A pilha é usada para inverter a ordem dos restos obtidos
# nas divisões sucessivas por 16.


def decimal_para_hexa(n):
    # O algoritmo trabalha somente com números não negativos.
    if n < 0:
        raise ValueError("n deve ser não-negativo")

    # Caso especial: zero possui representação hexadecimal "0".
    if n == 0:
        return "0"

    # Índices de 0 a 15 correspondem aos dígitos hexadecimais.
    digitos = "0123456789ABCDEF"

    # Armazena os restos das divisões, que serão lidos posteriormente
    # em ordem inversa utilizando a lógica LIFO.
    pilha = []

    while n > 0:
        # O resto da divisão por 16 determina o próximo dígito hexadecimal.
        resto = n % 16
        pilha.append(digitos[resto])

        # A divisão inteira reduz o número para a próxima etapa.
        n //= 16

    hexa = ""

    # Os restos são retirados do topo para reconstruir a representação correta.
    while pilha:
        hexa += pilha.pop()

    return hexa


if __name__ == "__main__":
    # Testa diferentes valores, incluindo zero.
    print(decimal_para_hexa(26))
    print(decimal_para_hexa(255))
    print(decimal_para_hexa(0))
    print(decimal_para_hexa(4095))
