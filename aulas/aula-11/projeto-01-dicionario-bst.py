# Projeto 1 — Dicionário ordenado com BST
# Guarda pares palavra → significado em uma BST.
# O percurso em ordem lista as palavras em ordem alfabética.


class No:
    def __init__(self, palavra, significado):
        self.palavra = palavra
        self.significado = significado
        self.esquerda = None
        self.direita = None


def inserir(raiz, palavra, significado):
    # Ordena pela palavra, não pelo significado.
    if raiz is None:
        return No(palavra, significado)

    if palavra < raiz.palavra:
        raiz.esquerda = inserir(raiz.esquerda, palavra, significado)
    else:
        raiz.direita = inserir(raiz.direita, palavra, significado)

    return raiz


def buscar(raiz, palavra):
    # Busca BST pela palavra.
    if raiz is None:
        return "Palavra não encontrada."

    if raiz.palavra == palavra:
        return raiz.significado

    if palavra < raiz.palavra:
        return buscar(raiz.esquerda, palavra)

    return buscar(raiz.direita, palavra)


def listar(raiz, palavras):
    # Em ordem = alfabética.
    if raiz is None:
        return palavras

    listar(raiz.esquerda, palavras)
    palavras.append(raiz.palavra)
    listar(raiz.direita, palavras)

    return palavras


raiz = None
for par in [("cachorro", "animal doméstico"), ("abelha", "inseto que faz mel"), ("gato", "felino doméstico")]:
    raiz = inserir(raiz, par[0], par[1])

print(buscar(raiz, "abelha"))
print(listar(raiz, []))
