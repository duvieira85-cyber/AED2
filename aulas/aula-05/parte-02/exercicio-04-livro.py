# Exercício 4 — Classe Livro
# Demonstra uma classe simples com atributos e método para exibir os dados do livro.

class Livro:
    def __init__(self, titulo, autor):
        # Armazena as informações recebidas no objeto.
        self.titulo = titulo
        self.autor = autor

    def exibir(self):
        # Retorna os dados do livro em formato legível.
        return f"Título: {self.titulo} | Autor: {self.autor}"


if __name__ == "__main__":
    livro = Livro("Python para Análise de Dados", "Wes McKinney")
    print(livro.exibir())
