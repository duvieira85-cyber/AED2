from collections import deque


def gestao_tarefas(tarefas_iniciais, ciclos, novas_por_ciclo=None):
    novas_por_ciclo = novas_por_ciclo or {}
    fila = deque(tarefas_iniciais)

    for ciclo in range(1, ciclos + 1):
        print(f"--- Ciclo {ciclo} ---")

        if fila:
            atual = fila.popleft()
            print(f"Tarefa concluída: {atual}")
        else:
            print("Não há tarefa pendente para processar.")

        for nova in novas_por_ciclo.get(ciclo, []):
            fila.append(nova)
            print(f"Tarefa adicionada: {nova}")


if __name__ == "__main__":
    gestao_tarefas(
        ["Relatório", "E-mail", "Backup"],
        5,
        {1: ["Atualizar dashboard"], 3: ["Conferir estoque"]},
    )
