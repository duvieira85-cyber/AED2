# Exercício 4 — Classe Livro
# Cria uma classe simples para representar um livro.


class Livro:
    def __init__(self, titulo, autor, paginas):
        # Atributos do livro.
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def descricao(self):
        # Retorna a descrição solicitada no exercício.
        return f"{self.titulo} — {self.autor} ({self.paginas} páginas)"


if __name__ == "__main__":
    livro1 = Livro("Dom Casmurro", "Machado de Assis", 256)
    livro2 = Livro("O Hobbit", "J. R. R. Tolkien", 310)

    print(livro1.descricao())
    print(livro2.descricao())
