# Exercício 4 — Fila de impressão
# Os documentos são processados em ordem FIFO: o primeiro documento
# recebido é o primeiro a ser impresso.
# Após três impressões, a impressora precisa ficar um ciclo em resfriamento.
# Durante o resfriamento, novos documentos ainda podem chegar à fila.


from collections import deque


def fila_impressao(documentos, chegadas_por_ciclo=None):
    # Caso não existam chegadas programadas, utiliza um dicionário vazio.
    chegadas_por_ciclo = chegadas_por_ciclo or {}

    # Inicializa a fila mantendo a ordem original dos documentos.
    fila = deque(documentos)

    # Controla quantos documentos foram impressos desde a última pausa.
    impressos_desde_pausa = 0

    # Indica se o ciclo atual deve ser utilizado para resfriamento.
    resfriando = False

    # Inicia a simulação no primeiro ciclo.
    ciclo = 1

    # A simulação continua enquanto houver documentos, um resfriamento
    # pendente ou novas chegadas programadas para algum ciclo.
    while fila or resfriando or ciclo in chegadas_por_ciclo:
        # Novos documentos são adicionados ao final da fila no início
        # de cada ciclo, inclusive quando a impressora está resfriando.
        for documento in chegadas_por_ciclo.get(ciclo, []):
            fila.append(documento)
            print(f"Novo documento recebido: {documento}")

        if resfriando:
            # Durante o resfriamento nenhum documento é retirado da fila.
            print("Pausa para resfriamento da impressora.")

            # O resfriamento dura exatamente um ciclo.
            resfriando = False

        elif fila:
            # Remove o documento mais antigo da fila para impressão.
            atual = fila.popleft()
            print(f"Imprimindo documento: {atual}")

            # Registra mais uma impressão desde a última pausa.
            impressos_desde_pausa += 1

            if impressos_desde_pausa == 3:
                # Depois de três impressões, o próximo ciclo será
                # reservado para o resfriamento da impressora.
                resfriando = True

                # Reinicia a contagem para o próximo grupo de impressões.
                impressos_desde_pausa = 0

        # Avança a simulação para o próximo ciclo.
        ciclo += 1


if __name__ == "__main__":
    # Executa a simulação com documentos iniciais e uma nova chegada
    # programada para o quarto ciclo.
    fila_impressao(
        ["Relatório.pdf", "Contrato.docx", "Imagem.png",
         "Resumo.txt", "Tabela.xlsx", "Mapa.jpg"],
        {4: ["Ata.docx"]},
    )
