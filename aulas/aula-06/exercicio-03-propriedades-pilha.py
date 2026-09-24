# Exercício 3 — Propriedades fundamentais de uma pilha
# A pilha restringe inserção, remoção e consulta ao topo.

def responder():
    # I: uma pilha vazia não possui elemento para o pop.
    print("I — Verdadeira")

    # II: a inserção ocorre apenas no topo, não em qualquer posição.
    print("II — Falsa")

    # III: o topo é o ponto de acesso operacional da pilha.
    print("III — Verdadeira")

    # IV: push() adiciona ao topo da pilha, não descreve uma fila.
    print("IV — Falsa")

    print("Resposta: I e III apenas (Alternativa A)")


if __name__ == "__main__":
    responder()
