# Aula 07 — Exercícios e projetos resolvidos
# Reúne as soluções do Capítulo 7 em um único arquivo.

from collections import deque


def exercicio_1():
    # A fila remove o elemento mais antigo primeiro.
    print("Resposta: Alternativa D")


def exercicio_2():
    fila = deque([10, 20])

    # Remove 10, que foi o primeiro elemento enfileirado.
    fila.popleft()

    # Novo elemento é inserido no final.
    fila.append(30)

    # peek consulta a frente sem removê-la.
    print("peek =", fila[0])


def exercicio_3():
    # Tarefas processadas na ordem de chegada são um caso típico de FIFO.
    print("Resposta: Alternativa C")


def exercicio_4(documentos, chegadas_por_ciclo=None):
    # Representa a fila de impressão usando deque para operações FIFO eficientes.
    chegadas_por_ciclo = chegadas_por_ciclo or {}
    fila = deque(documentos)

    impressos_desde_pausa = 0
    resfriando = False
    ciclo = 1

    while fila or resfriando or ciclo in chegadas_por_ciclo:
        # Novos documentos são adicionados ao final antes do processamento.
        for documento in chegadas_por_ciclo.get(ciclo, []):
            fila.append(documento)

        if resfriando:
            # Consome exatamente um ciclo com a impressora em resfriamento.
            resfriando = False
        elif fila:
            # Remove o documento mais antigo da fila.
            fila.popleft()
            impressos_desde_pausa += 1

            if impressos_desde_pausa == 3:
                # Após três impressões, reserva o próximo ciclo para resfriamento.
                resfriando = True
                impressos_desde_pausa = 0

        ciclo += 1


def exercicio_5(preferenciais, comuns):
    pref = deque(preferenciais)
    comum = deque(comuns)

    while pref or comum:
        if pref:
            # Atende primeiro a frente da fila preferencial.
            print("Preferencial:", pref.popleft())

        if comum:
            # Em seguida atende a frente da fila comum.
            print("Comum:", comum.popleft())


def projeto_1(tarefas_iniciais, ciclos, novas_por_ciclo=None):
    novas_por_ciclo = novas_por_ciclo or {}
    fila = deque(tarefas_iniciais)

    for ciclo in range(1, ciclos + 1):
        if fila:
            # Conclui somente a tarefa mais antiga neste ciclo.
            print("Concluída:", fila.popleft())

        # Novas tarefas entram no final da fila.
        for nova in novas_por_ciclo.get(ciclo, []):
            fila.append(nova)


def projeto_2(clientes_iniciais, total_atendimentos, atendimentos_por_sessao, chegadas_por_sessao=None):
    chegadas_por_sessao = chegadas_por_sessao or {}
    fila = deque(clientes_iniciais)
    atendidos = 0
    sessao = 1

    while atendidos < total_atendimentos:
        # Novos clientes chegam ao final da fila antes dos atendimentos.
        for novo in chegadas_por_sessao.get(sessao, []):
            fila.append(novo)

        for _ in range(atendimentos_por_sessao):
            if not fila or atendidos == total_atendimentos:
                break

            # Retira sempre o cliente mais antigo.
            print("Atendido:", fila.popleft())
            atendidos += 1

        sessao += 1


if __name__ == "__main__":
    exercicio_1()
    exercicio_2()
    exercicio_3()
    exercicio_4(["Relatório.pdf", "Contrato.docx", "Imagem.png"])
    exercicio_5(["P01", "P02"], ["C01", "C02"])
    projeto_1(["Relatório", "E-mail", "Backup"], 5, {1: ["Atualizar dashboard"]})
    projeto_2(["Cliente A", "Cliente B", "Cliente C"], 5, 2, {2: ["Cliente D"]})
