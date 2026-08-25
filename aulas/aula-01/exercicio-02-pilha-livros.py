# Exercício 2 — Pilha de livros
# Simular uma pilha e compreender o princípio LIFO.

livros = []
livros.append("O Pequeno Príncipe")
livros.append("Dom Quixote")
livros.append("1984")
livro_removido = livros.pop()

print(f"Livro removido: {livro_removido}")
print(f"Pilha restante: {livros}")
