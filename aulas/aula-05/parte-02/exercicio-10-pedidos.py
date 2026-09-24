# Exercício 10 — Sistema de pedidos
# Modela pedidos, produtos e cálculo do valor total utilizando orientação a objetos.

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class ItemPedido:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def subtotal(self):
        # Calcula o valor do item considerando sua quantidade.
        return self.produto.preco * self.quantidade


class Pedido:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, produto, quantidade):
        # Adiciona um novo item ao pedido.
        self.itens.append(ItemPedido(produto, quantidade))

    def calcular_total(self):
        # Soma os subtotais de todos os itens do pedido.
        return sum(item.subtotal() for item in self.itens)

    def listar_itens(self):
        # Exibe cada item e seu subtotal.
        for item in self.itens:
            print(
                f"{item.produto.nome} x{item.quantidade}: "
                f"R$ {item.subtotal():.2f}"
            )


if __name__ == "__main__":
    arroz = Produto("Arroz", 25.00)
    feijao = Produto("Feijão", 9.50)

    pedido = Pedido()

    # Monta o pedido com os produtos e suas respectivas quantidades.
    pedido.adicionar_item(arroz, 2)
    pedido.adicionar_item(feijao, 3)

    pedido.listar_itens()
    print(f"Total do pedido: R$ {pedido.calcular_total():.2f}")
