class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def descricao(self):
        return f"{self.titulo} — {self.autor} ({self.paginas} páginas)"


livro1 = Livro("Dom Casmurro", "Machado de Assis", 256)
livro2 = Livro("1984", "George Orwell", 328)

print(livro1.descricao())
print(livro2.descricao())
