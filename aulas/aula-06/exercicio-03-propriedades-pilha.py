# Exercício 3 — Propriedades fundamentais de uma pilha
# A pilha restringe as operações ao seu topo e segue o princípio LIFO.


def responder():
    # I: uma pilha vazia não possui elemento que possa ser removido.
    print("I — Verdadeira")

    # II: a inserção ocorre no topo, não em qualquer posição da pilha.
    print("II — Falsa")

    # III: o topo é o ponto de acesso das operações da pilha.
    print("III — Verdadeira")

    # IV: push() representa inserção no topo de uma pilha,
    # não uma operação característica de uma fila.
    print("IV — Falsa")

    # Reúne o resultado das quatro afirmações.
    print("Resposta: I e III apenas (Alternativa A)")


if __name__ == "__main__":
    # Executa a resposta do exercício.
    responder()
