class Conta:
    def __init__(self, titular):
        self.titular = titular
        self.__saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            return True
        return False

    def consultar_saldo(self):
        return self.__saldo


conta = Conta("Ana")

conta.depositar(500)
conta.depositar(250)

print(f"Titular: {conta.titular}")
print(f"Saldo: R$ {conta.consultar_saldo():.2f}")
