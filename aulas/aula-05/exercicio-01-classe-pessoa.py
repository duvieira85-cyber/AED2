# Exercício 1 — Classe Pessoa
# Demonstra a criação de uma classe com atributos, construtor e método de instância.

class Pessoa:
    def __init__(self, nome, idade):
        # Inicializa os dados do objeto.
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        # Retorna uma apresentação simples da pessoa.
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."


if __name__ == "__main__":
    pessoa = Pessoa("Eduardo", 40)
    print(pessoa.apresentar())
