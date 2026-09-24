# Exercício 5 — Classe Conta
# Encapsula o saldo e utiliza métodos para controlar depósito e saque.

class Conta:
    def __init__(self, titular, saldo=0):
        # Define o titular e o saldo inicial da conta.
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        # Adiciona o valor informado ao saldo.
        self.saldo += valor

    def sacar(self, valor):
        # Só permite o saque quando existe saldo suficiente.
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        return False


if __name__ == "__main__":
    conta = Conta("Eduardo", 1000)

    conta.depositar(500)
    print("Saldo após depósito:", conta.saldo)

    print("Saque realizado:", conta.sacar(300))
    print("Saldo final:", conta.saldo)
