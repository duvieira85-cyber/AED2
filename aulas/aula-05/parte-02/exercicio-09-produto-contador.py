class Produto:
    contador = 0

    def __init__(self, nome, preco):
        Produto.contador += 1
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
            return True
        return False

    def aplicar_desconto(self, percentual):
        if 0 <= percentual <= 100:
            self.__preco *= 1 - (percentual / 100)
            return True
        return False

    def __str__(self):
        return f"#{self.__id} - {self.__nome} - R$ {self.__preco:.2f}"


produto1 = Produto("Notebook", 3500)
produto2 = Produto("Mouse", 150)
produto3 = Produto("Teclado", 300)

produto2.aplicar_desconto(10)

print(produto1)
print(produto2)
print(produto3)
print(f"Total de objetos criados: {Produto.contador}")
