# Exercício 5 — Gerenciador de senhas
# Existem duas filas independentes: preferencial e comum.
# Em cada ciclo, atende-se primeiro uma preferencial e depois uma comum.

from collections import deque


def gerenciador_senhas(preferenciais, comuns):
    fila_pref = deque(preferenciais)
    fila_comum = deque(comuns)

    while fila_pref or fila_comum:
        if fila_pref:
            # Mantém FIFO dentro da fila preferencial.
            senha = fila_pref.popleft()
            print(f"Atendendo (preferencial): {senha}")

        if fila_comum:
            # Mantém FIFO dentro da fila comum.
            senha = fila_comum.popleft()
            print(f"Atendendo (comum): {senha}")


if __name__ == "__main__":
    gerenciador_senhas(
        ["P01", "P02", "P03"],
        ["C01", "C02", "C03", "C04"],
    )
