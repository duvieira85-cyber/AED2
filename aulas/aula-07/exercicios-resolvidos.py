# Aula 07 — Exercícios e projetos resolvidos
# Reúne em um único arquivo as soluções dos exercícios e projetos
# trabalhados no conteúdo de filas (FIFO).


from collections import deque


def exercicio_1():
    # Em uma fila, o primeiro elemento inserido é o primeiro removido.
    # Portanto, a operação dequeue() retira o elemento mais antigo.
    print("Resposta: Alternativa D")


def exercicio_2():
    # Inicializa a fila com dois elementos, mantendo a ordem de chegada.
    fila = deque([10, 20])

    # Remove 10, que foi o primeiro elemento enfileirado.
    fila.popleft()

    # Insere 30 no final da fila, depois do 20.
    fila.append(30)

    # Consulta o primeiro elemento sem removê-lo da fila.
    print("peek =", fila[0])


def exercicio_3():
    # O uso de fila é indicado quando as tarefas precisam ser
    # processadas na mesma ordem em que chegaram.
    print("Resposta: Alternativa C")


def exercicio_4(documentos, chegadas_por_ciclo=None):
    # A fila de impressão utiliza deque para representar o comportamento FIFO.
    chegadas_por_ciclo = chegadas_por_ciclo or {}

    # Os documentos iniciais entram na fila na ordem recebida.
    fila = deque(documentos)

    # Conta quantos documentos foram impressos desde o último resfriamento.
    impressos_desde_pausa = 0

    # Controla se o próximo ciclo será utilizado para resfriamento.
    resfriando = False

    # Inicia a simulação no primeiro ciclo.
    ciclo = 1

    # Continua enquanto houver documentos, resfriamento pendente
    # ou novas chegadas previstas.
    while fila or resfriando or ciclo in chegadas_por_ciclo:
        # Novos documentos são adicionados ao final da fila
        # antes do processamento do ciclo.
        for documento in chegadas_por_ciclo.get(ciclo, []):
            fila.append(documento)

        if resfriando:
            # O ciclo de resfriamento não remove nenhum documento da fila.
            resfriando = False

        elif fila:
            # Remove o documento mais antigo e registra uma impressão.
            fila.popleft()
            impressos_desde_pausa += 1

            if impressos_desde_pausa == 3:
                # Depois de três impressões, o próximo ciclo será de resfriamento.
                resfriando = True

                # Reinicia a contagem para o próximo grupo de três impressões.
                impressos_desde_pausa = 0

        # Avança para o próximo ciclo da simulação.
        ciclo += 1


def exercicio_5(preferenciais, comuns):
    # Mantém duas filas independentes, cada uma seguindo FIFO.
    pref = deque(preferenciais)
    comum = deque(comuns)

    # Continua enquanto houver senha em pelo menos uma das filas.
    while pref or comum:
        if pref:
            # Atende primeiro a senha que está há mais tempo
            # aguardando na fila preferencial.
            print("Preferencial:", pref.popleft())

        if comum:
            # Depois atende a senha mais antiga da fila comum.
            print("Comum:", comum.popleft())


def projeto_1(tarefas_iniciais, ciclos, novas_por_ciclo=None):
    # Caso não existam novas tarefas programadas, utiliza um dicionário vazio.
    novas_por_ciclo = novas_por_ciclo or {}

    # Inicializa a fila com as tarefas na ordem em que foram recebidas.
    fila = deque(tarefas_iniciais)

    # Simula cada ciclo do processamento.
    for ciclo in range(1, ciclos + 1):
        if fila:
            # Conclui somente a tarefa mais antiga neste ciclo.
            print("Concluída:", fila.popleft())

        # Novas tarefas entram no final da fila e aguardam sua vez.
        for nova in novas_por_ciclo.get(ciclo, []):
            fila.append(nova)


def projeto_2(clientes_iniciais, total_atendimentos, atendimentos_por_sessao, chegadas_por_sessao=None):
    # Caso não existam novas chegadas, utiliza um dicionário vazio.
    chegadas_por_sessao = chegadas_por_sessao or {}

    # Inicializa a fila com os clientes na ordem de chegada.
    fila = deque(clientes_iniciais)

    # Conta quantos clientes já foram atendidos.
    atendidos = 0

    # Inicia a simulação na primeira sessão.
    sessao = 1

    # Continua até atingir o número total de atendimentos solicitado.
    while atendidos < total_atendimentos:
        # Novos clientes entram no final da fila antes dos atendimentos.
        for novo in chegadas_por_sessao.get(sessao, []):
            fila.append(novo)

        # Processa a quantidade máxima de atendimentos prevista para a sessão.
        for _ in range(atendimentos_por_sessao):
            if not fila or atendidos == total_atendimentos:
                break

            # Remove sempre o cliente que está há mais tempo aguardando.
            print("Atendido:", fila.popleft())
            atendidos += 1

        # Avança para a próxima sessão.
        sessao += 1


if __name__ == "__main__":
    # Executa exemplos de todos os exercícios e projetos.
    exercicio_1()
    exercicio_2()
    exercicio_3()
    exercicio_4(["Relatório.pdf", "Contrato.docx", "Imagem.png"])
    exercicio_5(["P01", "P02"], ["C01", "C02"])
    projeto_1(["Relatório", "E-mail", "Backup"], 5, {1: ["Atualizar dashboard"]})
    projeto_2(["Cliente A", "Cliente B", "Cliente C"], 5, 2, {2: ["Cliente D"]})
