# Exercício 9 — Produtos e contador de objetos
# contador é compartilhado por todos os objetos Produto.
# Cada produto recebe um id sequencial.


class Produto:
    contador = 0

    def __init__(self, nome, preco):
        Produto.contador += 1

        # Os três atributos são privados.
        self.__id = Produto.contador
        self.__nome = nome
        self.__preco = preco

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    def set_preco(self, novo_preco):
        if novo_preco > 0:
            self.__preco = novo_preco

    def aplicar_desconto(self, percentual):
        if 0 <= percentual <= 100:
            desconto = self.__preco * percentual / 100
            self.__preco -= desconto

    def __str__(self):
        return (
            f"ID: {self.__id} | "
            f"{self.__nome} | "
            f"R$ {self.__preco:.2f}"
        )


if __name__ == "__main__":
    produto1 = Produto("Teclado", 100)
    produto2 = Produto("Mouse", 50)
    produto3 = Produto("Monitor", 800)

    produto2.aplicar_desconto(10)
    produto3.set_preco(750)

    print(produto1)
    print(produto2)
    print(produto3)

    print("Quantidade de produtos criados:", Produto.contador)
