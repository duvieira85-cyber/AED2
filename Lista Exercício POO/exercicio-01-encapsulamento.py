# Exercício 1 — Objetos, encapsulamento e interface
# Resposta: alternativa B.
#
# O encapsulamento permite esconder a forma como o saldo é armazenado
# e disponibilizar métodos para trabalhar com o objeto.


class ContaBancaria:
    def __init__(self):
        # __saldo é um atributo privado.
        self.__saldo = 0

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def consultar_saldo(self):
        return self.__saldo


if __name__ == "__main__":
    conta = ContaBancaria()

    conta.depositar(100)
    conta.sacar(30)

    print("Saldo:", conta.consultar_saldo())

    # O saldo é acessado pelo método consultar_saldo(),
    # e não diretamente pelo atributo privado.
