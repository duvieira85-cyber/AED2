# Exercício 8 — Funcionários e cálculo de bônus
# Vendedor e Gerente herdam de Funcionario.
# Cada classe possui uma regra diferente para calcular_bonus().


class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_bonus(self):
        return self.salario * 0.05

    def __str__(self):
        return f"{self.nome} - R$ {self.salario:.2f}"


class Vendedor(Funcionario):
    def __init__(self, nome, salario, vendas):
        super().__init__(nome, salario)
        self.vendas = vendas

    def calcular_bonus(self):
        return self.salario * 0.05 + self.vendas * 0.02


class Gerente(Funcionario):
    def __init__(self, nome, salario, equipe):
        super().__init__(nome, salario)
        self.equipe = equipe

    def calcular_bonus(self):
        return self.salario * 0.10 + self.equipe * 100


if __name__ == "__main__":
    funcionario = Funcionario("Carlos", 3000)
    vendedor = Vendedor("Ana", 4000, 10000)
    gerente = Gerente("Marcos", 6000, 5)

    funcionarios = [funcionario, vendedor, gerente]

    for funcionario in funcionarios:
        print(
            funcionario.nome,
            "-",
            type(funcionario).__name__,
            "- Bônus: R$",
            f"{funcionario.calcular_bonus():.2f}"
        )
