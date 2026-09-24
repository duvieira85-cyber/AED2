# Projeto 2 — A Lista de Tarefas
# Utiliza uma lista para adicionar tarefas, concluir itens
# e visualizar somente as tarefas que continuam pendentes.


# Lista inicial de tarefas que ainda precisam ser realizadas.
tarefas = [
    "Lavar a louça",
    "Estudar para a prova",
    "Fazer compras"
]


def adicionar_tarefa(tarefa):
    # Adiciona a nova tarefa ao final da lista de pendências.
    tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada.")


def marcar_concluida(tarefa):
    # Primeiro verifica se a tarefa existe na lista.
    if tarefa in tarefas:
        # Remove a tarefa da lista para representar sua conclusão.
        tarefas.remove(tarefa)
        print(f"Tarefa '{tarefa}' marcada como concluída.")
    else:
        # Informa quando a tarefa não foi encontrada.
        print(f"Tarefa '{tarefa}' não encontrada na lista.")


def visualizar_tarefas():
    # Percorre a lista e mostra somente as tarefas ainda pendentes.
    print("\nLista de tarefas pendentes:")

    for tarefa in tarefas:
        print(f"- {tarefa}")


# Exemplo de uso das operações da lista de tarefas.
adicionar_tarefa("Pagar as contas")
marcar_concluida("Lavar a louça")
visualizar_tarefas()
