# Exercício 1 — Classe Pessoa
# Demonstra a criação de uma classe com atributos, construtor
# e método de instância.


class Pessoa:
    def __init__(self, nome, idade):
        # __init__ é executado quando um novo objeto Pessoa é criado.
        # Os valores recebidos são armazenados nos atributos do objeto.
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        # O método utiliza os atributos do próprio objeto para montar
        # uma mensagem de apresentação.
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."


if __name__ == "__main__":
    # Cria uma instância da classe Pessoa com os dados informados.
    pessoa = Pessoa("Eduardo", 40)

    # Chama o método do objeto e exibe o resultado.
    print(pessoa.apresentar())
