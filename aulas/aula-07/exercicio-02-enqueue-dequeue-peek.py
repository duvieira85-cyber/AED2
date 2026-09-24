# Exercício 2 — enqueue, dequeue e peek
# A fila insere elementos no final e remove elementos do início.

from collections import deque


def executar():
    fila = deque()

    # Enfileira os dois primeiros elementos.
    fila.append(10)
    fila.append(20)

    # Remove o primeiro elemento que entrou.
    fila.popleft()

    # Novo elemento entra no final da fila.
    fila.append(30)

    # peek consulta a frente sem remover.
    print("peek =", fila[0])


if __name__ == "__main__":
    executar()
