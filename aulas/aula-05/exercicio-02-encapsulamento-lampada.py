# Exercício 2 — Encapsulamento
# O estado da lâmpada é controlado por métodos, evitando alteração direta do atributo interno.

class Lampada:
    def __init__(self):
        # Atributo privado: representa o estado interno da lâmpada.
        self.__acesa = False

    def ligar(self):
        # Altera o estado para ligada.
        self.__acesa = True

    def desligar(self):
        # Altera o estado para desligada.
        self.__acesa = False

    def esta_acesa(self):
        # Permite consultar o estado sem acessar o atributo privado diretamente.
        return self.__acesa


if __name__ == "__main__":
    lampada = Lampada()
    lampada.ligar()
    print("Lâmpada acesa:", lampada.esta_acesa())
    lampada.desligar()
    print("Lâmpada acesa:", lampada.esta_acesa())
