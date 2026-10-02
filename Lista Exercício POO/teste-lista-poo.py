# Testes simples da Lista de Exercícios POO.
# A ideia é verificar as principais regras do enunciado.


from exercicio_04_livro import Livro
from exercicio_05_conta import Conta
from exercicio_06_animais import Cachorro, Gato
from exercicio_07_veiculo import Veiculo
from exercicio_08_funcionarios import Vendedor, Gerente
from exercicio_09_produtos import Produto
from exercicio_10_pedidos import Cliente, ProdutoFisico, ProdutoDigital, Pedido


def testar():
    # Exercício 4
    livro = Livro("Livro", "Autor", 100)
    assert livro.descricao() == "Livro — Autor (100 páginas)"

    # Exercício 5
    conta = Conta("Teste")
    conta.depositar(100)
    conta.depositar(50)
    assert conta.consultar_saldo() == 150

    # Exercício 6
    assert Cachorro("Rex").emitir_som() == "au au"
    assert Gato("Mimi").emitir_som() == "miau"

    # Exercício 7
    veiculo = Veiculo("ABC-1234", 100)
    veiculo.acelerar(150)
    assert "100 km/h" in str(veiculo)
    veiculo.frear(30)
    assert "70 km/h" in str(veiculo)

    # Exercício 8
    vendedor = Vendedor("Vendedor", 4000, 10000)
    gerente = Gerente("Gerente", 6000, 5)
    assert vendedor.calcular_bonus() == 400
    assert gerente.calcular_bonus() == 1100

    # Exercício 9
    Produto.contador = 0
    produto = Produto("Produto", 100)
    produto.aplicar_desconto(10)
    assert produto.get_preco() == 90

    # Exercício 10
    cliente = Cliente("Cliente", "cliente@email.com")
    fisico = ProdutoFisico("Produto físico", 100, 2)
    digital = ProdutoDigital("Produto digital", 50, 100)

    pedido = Pedido(cliente)
    assert pedido.adicionar_produto(fisico) is True
    assert pedido.adicionar_produto(digital) is True

    assert pedido.calcular_total() == 150
    assert pedido.calcular_frete_total() == 9

    pedido.fechar_pedido()

    # Depois de fechado, não deve aceitar produto.
    assert pedido.adicionar_produto(ProdutoDigital("Outro", 20, 50)) is False


if __name__ == "__main__":
    testar()
    print("Todos os testes da Lista de Exercícios POO passaram.")
