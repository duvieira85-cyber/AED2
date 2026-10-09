from collections import deque


class CentralAtendimento:
    def __init__(self):
        self.fila_espera = deque()
        self.chamados_atendidos = []

    def adicionar_chamado(self, codigo, cliente, prioridade):
        chamado = {
            "codigo": codigo,
            "cliente": cliente,
            "prioridade": prioridade
        }
        self.fila_espera.append(chamado)

    def atender_proximo(self):
        if not self.fila_espera:
            print("Não há chamados aguardando atendimento.")
            return

        chamado = self.fila_espera.popleft()
        self.chamados_atendidos.append(chamado)
        print(f"Atendido: {chamado['codigo']} - {chamado['cliente']}")

    def desfazer_ultimo_atendimento(self):
        if not self.chamados_atendidos:
            print("Não há atendimento para desfazer.")
            return

        chamado = self.chamados_atendidos.pop()
        self.fila_espera.appendleft(chamado)
        print(f"Atendimento desfeito: {chamado['codigo']} - {chamado['cliente']}")

    def buscar_chamado(self, codigo):
        for chamado in self.fila_espera:
            if chamado["codigo"] == codigo:
                return chamado
        return None

    def exibir_situacao(self):
        aguardando = [c["codigo"] for c in self.fila_espera]
        atendidos = [c["codigo"] for c in self.chamados_atendidos]
        print(f"Chamados aguardando: {aguardando}")
        print(f"Chamados atendidos: {atendidos}")


central = CentralAtendimento()

central.adicionar_chamado(101, "Ana", "Média")
central.adicionar_chamado(102, "Bruno", "Alta")
central.adicionar_chamado(103, "Carla", "Baixa")
central.adicionar_chamado(104, "Daniel", "Alta")

central.atender_proximo()
central.atender_proximo()
central.desfazer_ultimo_atendimento()
central.atender_proximo()

central.exibir_situacao()
print(central.buscar_chamado(104))
