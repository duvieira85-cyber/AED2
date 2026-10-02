# Exercício 2 — Herança e polimorfismo
# Resposta: alternativa C — Herança e polimorfismo.
#
# Vendedor e Gerente herdam de Funcionario.
# Cada classe pode ter sua própria versão de calcular_bonus().


class Funcionario:
    def calcular_bonus(self):
        return 0


class Vendedor(Funcionario):
    def calcular_bonus(self):
        return 100


class Gerente(Funcionario):
    def calcular_bonus(self):
        return 200


if __name__ == "__main__":
    funcionarios = [
        Vendedor(),
        Gerente()
    ]

    # Chamamos o mesmo método nos dois objetos.
    # Cada objeto executa sua própria versão do método.
    for funcionario in funcionarios:
        print("Bônus:", funcionario.calcular_bonus())
