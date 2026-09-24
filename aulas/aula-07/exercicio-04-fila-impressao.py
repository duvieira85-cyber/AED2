from collections import deque


def fila_impressao(documentos, chegadas_por_ciclo=None):
    chegadas_por_ciclo = chegadas_por_ciclo or {}
    fila = deque(documentos)
    impressos_desde_pausa = 0
    resfriando = False
    ciclo = 1

    while fila or resfriando or ciclo in chegadas_por_ciclo:
        for documento in chegadas_por_ciclo.get(ciclo, []):
            fila.append(documento)
            print(f"Novo documento recebido: {documento}")

        if resfriando:
            print("Pausa para resfriamento da impressora.")
            resfriando = False
        elif fila:
            atual = fila.popleft()
            print(f"Imprimindo documento: {atual}")
            impressos_desde_pausa += 1

            if impressos_desde_pausa == 3:
                resfriando = True
                impressos_desde_pausa = 0

        ciclo += 1


if __name__ == "__main__":
    fila_impressao(
        ["Relatório.pdf", "Contrato.docx", "Imagem.png",
         "Resumo.txt", "Tabela.xlsx", "Mapa.jpg"],
        {4: ["Ata.docx"]},
    )
