class Lampada:
    def __init__(self):
        self.__estado = False

    def ligar(self):
        self.__estado = True

    def desligar(self):
        self.__estado = False

    def is_acesa(self):
        return self.__estado


lampada = Lampada()
print(lampada.is_acesa())
lampada.ligar()
print(lampada.is_acesa())
lampada.desligar()
print(lampada.is_acesa())
