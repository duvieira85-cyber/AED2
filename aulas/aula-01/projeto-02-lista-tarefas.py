# Projeto 2 — A Lista de Tarefas
# Usar uma lista para adicionar tarefas, concluir itens
# e visualizar as tarefas pendentes.

tarefas = [
    "Lavar a louça",
    "Estudar para a prova",
    "Fazer compras"
]


def adicionar_tarefa(tarefa):
    tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada.")


def marcar_concluida(tarefa):
    if tarefa in tarefas:
        tarefas.remove(tarefa)
        print(f"Tarefa '{tarefa}' marcada como concluída.")
    else:
        print(f"Tarefa '{tarefa}' não encontrada na lista.")


def visualizar_tarefas():
    print("\nLista de tarefas pendentes:")
    for tarefa in tarefas:
        print(f"- {tarefa}")


# Exemplo de uso
adicionar_tarefa("Pagar as contas")
marcar_concluida("Lavar a louça")
visualizar_tarefas()
