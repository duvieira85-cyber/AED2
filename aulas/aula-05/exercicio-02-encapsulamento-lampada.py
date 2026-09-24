# Exercício 2 — Encapsulamento
# O estado da lâmpada é controlado por métodos.
# O atributo interno não é alterado diretamente pelo código externo.


class Lampada:
    def __init__(self):
        # __acesa representa o estado interno da lâmpada.
        # O prefixo __ indica um atributo com acesso restrito pela classe.
        self.__acesa = False

    def ligar(self):
        # O método altera o estado interno para "ligada".
        self.__acesa = True

    def desligar(self):
        # O método altera o estado interno para "desligada".
        self.__acesa = False

    def esta_acesa(self):
        # Retorna o estado atual sem expor diretamente o atributo interno.
        return self.__acesa


if __name__ == "__main__":
    # Cria uma nova lâmpada inicialmente desligada.
    lampada = Lampada()

    # Liga a lâmpada e consulta seu estado.
    lampada.ligar()
    print("Lâmpada acesa:", lampada.esta_acesa())

    # Desliga a lâmpada e consulta novamente seu estado.
    lampada.desligar()
    print("Lâmpada acesa:", lampada.esta_acesa())
