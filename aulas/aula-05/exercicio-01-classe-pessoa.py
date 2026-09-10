class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def faz_aniversario(self):
        self.idade += 1

    def __str__(self):
        return f"{self.nome}, {self.idade} anos"


p1 = Pessoa("Ana", 20)
p2 = Pessoa("Carlos", 30)

print("Antes:")
print(p1)
print(p2)

p1.faz_aniversario()
p2.faz_aniversario()

print("Depois:")
print(p1)
print(p2)
