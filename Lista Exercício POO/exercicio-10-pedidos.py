# Exercício 10 — Mini sistema de pedidos de e-commerce
# Este exercício reúne classes, encapsulamento, herança,
# atributo de classe e polimorfismo.


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

    def calcular_frete(self):
        # Produto comum não possui frete.
        return 0

    def __str__(self):
        return f"{self.__id} - {self.__nome} - R$ {self.__preco:.2f}"


class ProdutoFisico(Produto):
    def __init__(self, nome, preco, peso):
        super().__init__(nome, preco)
        self.peso = peso

    def calcular_frete(self):
        # R$ 5,00 + R$ 2,00 para cada kg.
        return 5 + (2 * self.peso)


class ProdutoDigital(Produto):
    def __init__(self, nome, preco, tamanho_mb):
        super().__init__(nome, preco)
        self.tamanho_mb = tamanho_mb

    # Produto digital usa calcular_frete() da classe Produto,
    # que retorna zero.


class Cliente:
    def __init__(self, nome, email):
        self.__nome = nome
        self.__email = email

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def __str__(self):
        return f"{self.__nome} - {self.__email}"


class Pedido:
    contador = 0

    def __init__(self, cliente):
        Pedido.contador += 1

        self.__numero = Pedido.contador
        self.__cliente = cliente
        self.__produtos = []
        self.__status = "Aberto"

    def adicionar_produto(self, produto):
        # Depois de fechado, o pedido não aceita novos produtos.
        if self.__status == "Aberto":
            self.__produtos.append(produto)
            return True

        return False

    def calcular_total(self):
        total = 0

        for produto in self.__produtos:
            total += produto.get_preco()

        return total

    def calcular_frete_total(self):
        total = 0

        # Chamamos o mesmo método para todos os produtos.
        # Não precisamos testar se o produto é físico ou digital.
        for produto in self.__produtos:
            total += produto.calcular_frete()

        return total

    def fechar_pedido(self):
        self.__status = "Fechado"

    def __str__(self):
        return (
            f"Pedido: {self.__numero}\n"
            f"Cliente: {self.__cliente}\n"
            f"Status: {self.__status}\n"
            f"Total: R$ {self.calcular_total():.2f}\n"
            f"Frete: R$ {self.calcular_frete_total():.2f}"
        )


if __name__ == "__main__":
    cliente = Cliente("Eduardo", "eduardo@email.com")

    produto1 = ProdutoFisico("Teclado", 100, 2)
    produto2 = ProdutoFisico("Livro", 50, 1)
    produto3 = ProdutoDigital("Curso Python", 200, 500)

    pedido = Pedido(cliente)

    pedido.adicionar_produto(produto1)
    pedido.adicionar_produto(produto2)
    pedido.adicionar_produto(produto3)

    print(pedido)

    pedido.fechar_pedido()

    # Agora o pedido está fechado.
    produto4 = ProdutoDigital("Curso SQL", 150, 300)

    if pedido.adicionar_produto(produto4):
        print("Produto adicionado.")
    else:
        print("Não foi possível adicionar: pedido fechado.")

    print("\nResumo final:")
    print(pedido)
