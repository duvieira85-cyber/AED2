# Exercício 5 — Gerenciador de senhas
# Existem duas filas independentes: uma preferencial e outra comum.
# Em cada ciclo, é atendida no máximo uma senha de cada fila:
# primeiro a preferencial e depois a comum.
# A ordem interna de cada fila continua seguindo o princípio FIFO.


from collections import deque


def gerenciador_senhas(preferenciais, comuns):
    # Cria as duas filas preservando a ordem em que as senhas chegaram.
    fila_pref = deque(preferenciais)
    fila_comum = deque(comuns)

    # Continua enquanto existir alguém aguardando em qualquer uma das filas.
    while fila_pref or fila_comum:
        if fila_pref:
            # Remove a senha mais antiga da fila preferencial.
            # A fila comum não é alterada neste momento.
            senha = fila_pref.popleft()
            print(f"Atendendo (preferencial): {senha}")

        if fila_comum:
            # Depois da preferencial, remove a senha mais antiga
            # da fila comum.
            senha = fila_comum.popleft()
            print(f"Atendendo (comum): {senha}")


if __name__ == "__main__":
    # Executa um exemplo com três senhas preferenciais
    # e quatro senhas comuns.
    gerenciador_senhas(
        ["P01", "P02", "P03"],
        ["C01", "C02", "C03", "C04"],
    )
