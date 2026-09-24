# Exercício 8 — Funcionários
# Demonstra herança e polimorfismo no cálculo de bônus por tipo de funcionário.

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_bonus(self):
        # Funcionário comum recebe 5% do salário como bônus.
        return self.salario * 0.05

    def __str__(self):
        return f"{self.nome} - Salário: R$ {self.salario:.2f}"


class Vendedor(Funcionario):
    def __init__(self, nome, salario, vendas):
        super().__init__(nome, salario)
        self.vendas = vendas

    def calcular_bonus(self):
        # O vendedor recebe o bônus base mais 2% sobre as vendas.
        return (self.salario * 0.05) + (self.vendas * 0.02)


class Gerente(Funcionario):
    def __init__(self, nome, salario, equipe):
        super().__init__(nome, salario)
        self.equipe = equipe

    def calcular_bonus(self):
        # O gerente recebe 10% do salário mais um valor por integrante da equipe.
        return (self.salario * 0.10) + (len(self.equipe) * 100)


# Cada objeto possui sua própria implementação de calcular_bonus().
funcionarios = [
    Funcionario("Ana", 3000),
    Vendedor("Carlos", 4000, 20000),
    Gerente("Mariana", 6000, ["João", "Pedro", "Lucas"])
]

for funcionario in funcionarios:
    print(
        f"Nome: {funcionario.nome} | "
        f"Tipo: {type(funcionario).__name__} | "
        f"Bônus: R$ {funcionario.calcular_bonus():.2f}"
    )
