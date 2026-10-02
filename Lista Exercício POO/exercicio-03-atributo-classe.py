# Exercício 3 — Atributo de instância x atributo de classe
# Resposta: alternativa B.
#
# contador pertence à classe Produto.
# Por isso, seu valor é compartilhado pelos objetos.


class Produto:
    contador = 0

    def __init__(self, nome):
        Produto.contador += 1
        self.nome = nome


if __name__ == "__main__":
    produto1 = Produto("Arroz")
    produto2 = Produto("Feijão")
    produto3 = Produto("Macarrão")

    print("Produto 1:", produto1.nome)
    print("Produto 2:", produto2.nome)
    print("Produto 3:", produto3.nome)

    print("Quantidade de produtos criados:", Produto.contador)
