from collections import deque


def exercicio_1():
    print("Resposta: Alternativa D")


def exercicio_2():
    fila = deque([10, 20])
    fila.popleft()
    fila.append(30)
    print("peek =", fila[0])


def exercicio_3():
    print("Resposta: Alternativa C")


def exercicio_4(documentos, chegadas_por_ciclo=None):
    chegadas_por_ciclo = chegadas_por_ciclo or {}
    fila = deque(documentos)
    impressos_desde_pausa = 0
    resfriando = False
    ciclo = 1

    while fila or resfriando or ciclo in chegadas_por_ciclo:
        for documento in chegadas_por_ciclo.get(ciclo, []):
            fila.append(documento)

        if resfriando:
            resfriando = False
        elif fila:
            fila.popleft()
            impressos_desde_pausa += 1
            if impressos_desde_pausa == 3:
                resfriando = True
                impressos_desde_pausa = 0

        ciclo += 1


def exercicio_5(preferenciais, comuns):
    pref = deque(preferenciais)
    comum = deque(comuns)

    while pref or comum:
        if pref:
            print("Preferencial:", pref.popleft())
        if comum:
            print("Comum:", comum.popleft())


def projeto_1(tarefas_iniciais, ciclos, novas_por_ciclo=None):
    novas_por_ciclo = novas_por_ciclo or {}
    fila = deque(tarefas_iniciais)

    for ciclo in range(1, ciclos + 1):
        if fila:
            print("Concluída:", fila.popleft())
        for nova in novas_por_ciclo.get(ciclo, []):
            fila.append(nova)


def projeto_2(clientes_iniciais, total_atendimentos, atendimentos_por_sessao, chegadas_por_sessao=None):
    chegadas_por_sessao = chegadas_por_sessao or {}
    fila = deque(clientes_iniciais)
    atendidos = 0
    sessao = 1

    while atendidos < total_atendimentos:
        for novo in chegadas_por_sessao.get(sessao, []):
            fila.append(novo)

        for _ in range(atendimentos_por_sessao):
            if not fila or atendidos == total_atendimentos:
                break
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
