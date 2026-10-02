# Exercício 5 — Conta simples com encapsulamento
# O saldo fica privado e só é alterado pelo método depositar().


class Conta:
    def __init__(self, titular):
        self.titular = titular

        # __saldo é privado.
        self.__saldo = 0

    def depositar(self, valor):
        # O exercício permite somente valores positivos.
        if valor > 0:
            self.__saldo += valor

    def consultar_saldo(self):
        return self.__saldo


if __name__ == "__main__":
    conta = Conta("Eduardo")

    conta.depositar(100)
    conta.depositar(50)

    print("Titular:", conta.titular)
    print("Saldo:", conta.consultar_saldo())
