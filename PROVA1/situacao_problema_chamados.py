# Sistema de controle de chamados de suporte
# PROVA1 - AED II
#
# Enunciado inicial:
# Uma empresa deseja controlar chamadas de suporte recebidas ao longo do dia.
# Os chamados devem ser atendidos na ordem em que chegam. Se um atendimento
# tiver sido realizado por engano, deve ser possível desfazê-lo, devolvendo
# o chamado para o início da fila.
#
# Chamados iniciais, na ordem de chegada:
# 101 - Ana    - média
# 102 - Bruno  - alta
# 103 - Carla  - baixa
# 104 - Daniel - alta
#
# Aguardando as próximas instruções do enunciado para implementar o comportamento.

from collections import deque


chamados = deque([
    {"codigo": 101, "cliente": "Ana", "prioridade": "média"},
    {"codigo": 102, "cliente": "Bruno", "prioridade": "alta"},
    {"codigo": 103, "cliente": "Carla", "prioridade": "baixa"},
    {"codigo": 104, "cliente": "Daniel", "prioridade": "alta"},
])


if __name__ == "__main__":
    print("Chamados recebidos (ordem de chegada):")
    for chamado in chamados:
        print(
            f"{chamado['codigo']} - {chamado['cliente']} - "
            f"prioridade {chamado['prioridade']}"
        )
