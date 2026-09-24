# Projeto 2 — Fila de cinema
# Simula clientes aguardando atendimento em sessões sucessivas.
# A fila segue o princípio FIFO: quem chegou primeiro é atendido primeiro.


from collections import deque


def fila_cinema(
    clientes_iniciais,
    total_atendimentos,
    atendimentos_por_sessao,
    chegadas_por_sessao=None,
):
    # Caso não existam novas chegadas programadas, utiliza um dicionário vazio.
    chegadas_por_sessao = chegadas_por_sessao or {}

    # Inicializa a fila mantendo a ordem de chegada dos clientes.
    fila = deque(clientes_iniciais)

    # Controla quantos clientes já foram atendidos.
    atendidos = 0

    # Inicia a simulação na primeira sessão.
    sessao = 1

    # Continua até atingir o total de atendimentos solicitado.
    while atendidos < total_atendimentos:
        print(f"--- Sessão {sessao} ---")

        # Clientes que chegaram nesta sessão entram no final da fila
        # antes do início dos atendimentos.
        for novo in chegadas_por_sessao.get(sessao, []):
            fila.append(novo)
            print(f"Chegou à fila: {novo}")

        if not fila:
            # Se não houver clientes aguardando, não há atendimento possível.
            print("Não há clientes aguardando.")
            break

        # Processa no máximo a quantidade de clientes definida por sessão.
        for _ in range(atendimentos_por_sessao):
            if not fila or atendidos == total_atendimentos:
                break

            # Retira o cliente que está há mais tempo aguardando na fila.
            cliente = fila.popleft()
            print(f"{cliente} comprou ingresso e entrou.")

            # Atualiza o total de clientes já atendidos.
            atendidos += 1

        # Avança para a próxima sessão.
        sessao += 1


if __name__ == "__main__":
    # Executa um exemplo com clientes iniciais e novas chegadas
    # ocorrendo em sessões específicas.
    fila_cinema(
        ["Cliente A", "Cliente B", "Cliente C"],
        total_atendimentos=5,
        atendimentos_por_sessao=2,
        chegadas_por_sessao={2: ["Cliente D", "Cliente E"], 3: ["Cliente F"]},
    )
