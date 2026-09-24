from collections import deque


def fila_cinema(
    clientes_iniciais,
    total_atendimentos,
    atendimentos_por_sessao,
    chegadas_por_sessao=None,
):
    chegadas_por_sessao = chegadas_por_sessao or {}
    fila = deque(clientes_iniciais)
    atendidos = 0
    sessao = 1

    while atendidos < total_atendimentos:
        print(f"--- Sessão {sessao} ---")

        for novo in chegadas_por_sessao.get(sessao, []):
            fila.append(novo)
            print(f"Chegou à fila: {novo}")

        if not fila:
            print("Não há clientes aguardando.")
            break

        for _ in range(atendimentos_por_sessao):
            if not fila or atendidos == total_atendimentos:
                break

            cliente = fila.popleft()
            print(f"{cliente} comprou ingresso e entrou.")
            atendidos += 1

        sessao += 1


if __name__ == "__main__":
    fila_cinema(
        ["Cliente A", "Cliente B", "Cliente C"],
        total_atendimentos=5,
        atendimentos_por_sessao=2,
        chegadas_por_sessao={2: ["Cliente D", "Cliente E"], 3: ["Cliente F"]},
    )
