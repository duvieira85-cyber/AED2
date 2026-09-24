# Exercício 2 — Pilha de livros
# A pilha segue o princípio LIFO: o último livro inserido é o primeiro a sair.

pilha = ["Python", "Java", "C++"]

# Adiciona um novo livro no topo da pilha.
pilha.append("JavaScript")

# Remove o livro que está no topo.
removido = pilha.pop()

print("Livro removido:", removido)
print("Pilha:", pilha)
