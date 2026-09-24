# Exercício 9 — Produto com contador
# O atributo de classe mantém a quantidade total de objetos Produto criados.

class Produto:
    total_produtos = 0

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

        # Incrementa o contador compartilhado entre todas as instâncias.
        Produto.total_produtos += 1

    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f}"


if __name__ == "__main__":
    produtos = [
        Produto("Notebook", 3500),
        Produto("Mouse", 120),
        Produto("Teclado", 250),
    ]

    for produto in produtos:
        print(produto)

    print("Total de produtos:", Produto.total_produtos)
