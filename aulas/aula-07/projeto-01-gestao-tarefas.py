# Projeto 1 — Gestão de tarefas
# Cada ciclo conclui no máximo uma tarefa.
# Novas tarefas entram no final da fila e aguardam sua vez,
# mantendo a ordem de chegada entre as tarefas pendentes.


from collections import deque


def gestao_tarefas(tarefas_iniciais, ciclos, novas_por_ciclo=None):
    # Caso não existam novas tarefas programadas, utiliza um dicionário vazio.
    novas_por_ciclo = novas_por_ciclo or {}

    # Cria a fila inicial preservando a ordem das tarefas recebidas.
    fila = deque(tarefas_iniciais)

    # Executa a simulação durante a quantidade de ciclos informada.
    for ciclo in range(1, ciclos + 1):
        print(f"--- Ciclo {ciclo} ---")

        if fila:
            # Retira e conclui a tarefa mais antiga da fila.
            atual = fila.popleft()
            print(f"Tarefa concluída: {atual}")
        else:
            # Informa quando não existe tarefa pendente para este ciclo.
            print("Não há tarefa pendente para processar.")

        # Adiciona as novas tarefas ao final da fila.
        # Elas serão processadas somente quando chegar a sua vez.
        for nova in novas_por_ciclo.get(ciclo, []):
            fila.append(nova)
            print(f"Tarefa adicionada: {nova}")


if __name__ == "__main__":
    # Executa um exemplo com tarefas iniciais e novas tarefas
    # chegando durante a simulação.
    gestao_tarefas(
        ["Relatório", "E-mail", "Backup"],
        5,
        {1: ["Atualizar dashboard"], 3: ["Conferir estoque"]},
    )
