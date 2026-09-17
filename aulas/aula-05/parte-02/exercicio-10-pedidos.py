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

    def calcular_frete(self):
        return 0

    def __str__(self):
        return f"#{self.__id} - {self.__nome} - R$ {self.__preco:.2f}"


class ProdutoFisico(Produto):
    def __init__(self, nome, preco, peso):
        super().__init__(nome, preco)
        self.peso = peso

    def calcular_frete(self):
        return 5 + (2 * self.peso)


class ProdutoDigital(Produto):
    def __init__(self, nome, preco, tamanho_mb):
        super().__init__(nome, preco)
        self.tamanho_mb = tamanho_mb


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
        self.__status = "aberto"

    def adicionar_produto(self, produto):
        if self.__status == "fechado":
            print("Pedido fechado: não é possível adicionar produtos.")
            return False
        self.__produtos.append(produto)
        return True

    def calcular_total(self):
        return sum(produto.get_preco() for produto in self.__produtos)

    def calcular_frete_total(self):
        return sum(produto.calcular_frete() for produto in self.__produtos)

    def fechar_pedido(self):
        self.__status = "fechado"

    def __str__(self):
        linhas = [
            f"Pedido #{self.__numero}",
            f"Cliente: {self.__cliente}",
            f"Status: {self.__status}",
            "Produtos:"
        ]
        for produto in self.__produtos:
            linhas.append(f"  - {produto}")
        linhas.append(f"Total: R$ {self.calcular_total():.2f}")
        linhas.append(f"Frete: R$ {self.calcular_frete_total():.2f}")
        return "\n".join(linhas)


cliente = Cliente("Ana", "ana@email.com")

produtos = [
    ProdutoFisico("Livro", 80, 1.2),
    ProdutoDigital("Curso Python", 150, 850),
    ProdutoFisico("Caderno", 30, 0.5)
]

pedido = Pedido(cliente)

for produto in produtos:
    pedido.adicionar_produto(produto)

print(pedido)

pedido.fechar_pedido()

print("\nDepois de fechar:")
print(pedido)

print("\nTentativa de adicionar outro produto:")
pedido.adicionar_produto(ProdutoFisico("Caneta", 5, 0.1))
