# Exercício 3 — Aplicação de fila
# Uma fila é adequada quando as tarefas precisam ser processadas
# na mesma ordem em que foram recebidas.


def responder():
    # O princípio FIFO garante que a primeira tarefa recebida
    # seja também a primeira tarefa processada.
    print("Resposta: Alternativa C")
    print("Usar fila para tarefas que devem sair na mesma ordem em que chegam.")


if __name__ == "__main__":
    # Executa a resposta somente quando este arquivo é executado diretamente.
    responder()
