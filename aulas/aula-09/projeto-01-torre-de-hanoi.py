# Projeto 1 — Torre de Hanói
# O problema clássico da recursão: mover n discos da haste origem para a destino,
# usando a haste auxiliar, sem colocar disco maior sobre menor.
# Movimentos mínimos: 2^n − 1.


def hanoi(n, origem, destino, auxiliar, movimentos):
    # Com um único disco, movimenta direto para o destino.
    if n == 1:
        movimentos.append("mover disco 1 de " + origem + " para " + destino)
        return

    # Move n − 1 discos para a auxiliar para liberar o maior.
    hanoi(n - 1, origem, auxiliar, destino, movimentos)
    movimentos.append("mover disco " + str(n) + " de " + origem + " para " + destino)
    # Move os n − 1 discos que estavam na auxiliar sobre o maior.
    hanoi(n - 1, auxiliar, destino, origem, movimentos)


if __name__ == "__main__":
    movimentos = []
    hanoi(3, "A", "C", "B", movimentos)

    for passo in movimentos:
        print(passo)

    # 3 discos exigem exatamente 7 movimentos.
    print("total de movimentos:", len(movimentos))
