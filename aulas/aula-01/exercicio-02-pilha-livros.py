# Exercício 2 — Pilha de livros
# A pilha segue o princípio LIFO (Last In, First Out):
# o último elemento inserido é o primeiro a ser removido.

pilha = ["Python", "Java", "C++"]

# Insere um novo livro no topo da pilha.
pilha.append("JavaScript")

# pop() remove e retorna o elemento que está no topo.
removido = pilha.pop()

# Mostra qual livro foi removido e o estado restante da pilha.
print("Livro removido:", removido)
print("Pilha:", pilha)
