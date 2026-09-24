# Exercício 2 — enqueue, dequeue e peek
# Uma fila insere elementos no final e remove elementos do início.
# Essas operações preservam o comportamento FIFO.


from collections import deque


def executar():
    # Cria uma fila vazia utilizando deque, estrutura adequada
    # para inserções e remoções nas extremidades.
    fila = deque()

    # enqueue: adiciona o primeiro elemento ao final da fila.
    fila.append(10)

    # enqueue: adiciona o segundo elemento depois do 10.
    fila.append(20)

    # dequeue: remove o primeiro elemento que entrou na fila, o 10.
    fila.popleft()

    # Um novo elemento entra no final da fila, depois do 20.
    fila.append(30)

    # peek: consulta o primeiro elemento da fila sem removê-lo.
    print("peek =", fila[0])


if __name__ == "__main__":
    # Executa o exemplo somente quando o arquivo é executado diretamente.
    executar()
