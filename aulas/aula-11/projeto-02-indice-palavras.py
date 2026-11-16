# Projeto 2 — Índice alfabético de palavras
# Insere as palavras de uma frase em uma BST
# e gera o índice alfabético sem repetição.


class No:
    def __init__(self, palavra):
        self.palavra = palavra
        self.esquerda = None
        self.direita = None


def inserir(raiz, palavra):
    # Palavra repetida é simplesmente ignorada.
    if raiz is None:
        return No(palavra)

    if palavra < raiz.palavra:
        raiz.esquerda = inserir(raiz.esquerda, palavra)
    elif palavra > raiz.palavra:
        raiz.direita = inserir(raiz.direita, palavra)

    return raiz


def em_ordem(raiz, palavras):
    # Percurso em ordem gera a lista alfabética.
    if raiz is None:
        return palavras

    em_ordem(raiz.esquerda, palavras)
    palavras.append(raiz.palavra)
    em_ordem(raiz.direita, palavras)

    return palavras


frase = "estrutura de dados e algoritmos com python na fatec"
raiz = None

for palavra in frase.split():
    raiz = inserir(raiz, palavra)

print("Frase:", frase)
print("Índice:", em_ordem(raiz, []))
