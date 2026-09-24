from collections import deque


def executar():
    fila = deque()

    fila.append(10)
    fila.append(20)
    fila.popleft()
    fila.append(30)

    print("peek =", fila[0])


if __name__ == "__main__":
    executar()
