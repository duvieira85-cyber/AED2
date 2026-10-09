"""
PROVA1 — AED II
Sistema de controle de chamados de suporte.

Parte 1 — Pensamento computacional
- Fila de espera: deque, pois os chamados são atendidos na ordem de chegada (FIFO).
- Atendidos: lista usada como pilha, pois o último atendimento deve ser desfeito primeiro (LIFO).
- Simulação antes de programar:
    Inicial: fila [101, 102, 103, 104], atendidos []
    atender: fila [102, 103, 104], atendidos [101]
    atender: fila [103, 104], atendidos [101, 102]
    desfazer: fila [102, 103, 104], atendidos [101]
    atender: fila [103, 104], atendidos [101, 102]
- Complexidade de buscar_chamado: O(n) no pior caso, pois pode percorrer todos os n chamados da fila.

Prioridade é armazenada como dado do chamado, mas o enunciado determina atendimento por ordem de chegada (FIFO),
não por prioridade.
"""

from collections import deque


class CentralAtendimento:
    def __init__(self):
        self.fila_espera = deque()
        self.chamados_atendidos = []

    def adicionar_chamado(self, codigo, cliente, prioridade):
        """Adiciona o chamado ao final da fila de espera."""
        chamado = {
            "codigo": codigo,
            "cliente": cliente,
            "prioridade": prioridade,
        }
        self.fila_espera.append(chamado)
        return chamado

    def atender_proximo(self):
        """Atende o primeiro chamado da fila e registra na pilha de atendidos."""
        if not self.fila_espera:
            print("Não há chamados aguardando atendimento.")
            return None

        chamado = self.fila_espera.popleft()
        self.chamados_atendidos.append(chamado)
        print(f"Atendido: {chamado['codigo']} - {chamado['cliente']}")
        return chamado

    def desfazer_ultimo_atendimento(self):
        """Retira o atendimento mais recente e devolve o chamado ao início da fila."""
        if not self.chamados_atendidos:
            print("Não há atendimento para desfazer.")
            return None

        chamado = self.chamados_atendidos.pop()
        self.fila_espera.appendleft(chamado)
        print(f"Atendimento desfeito: {chamado['codigo']} - {chamado['cliente']}")
        return chamado

    def buscar_chamado(self, codigo):
        """Busca sequencialmente e retorna um chamado que ainda aguarda atendimento."""
        for chamado in self.fila_espera:
            if chamado["codigo"] == codigo:
                return chamado
        return None

    def exibir_situacao(self):
        """Exibe os códigos dos chamados aguardando e dos já atendidos."""
        aguardando = [chamado["codigo"] for chamado in self.fila_espera]
        atendidos = [chamado["codigo"] for chamado in self.chamados_atendidos]
        print(f"Chamados aguardando: {aguardando}")
        print(f"Chamados atendidos: {atendidos}")


if __name__ == "__main__":
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
    print("Busca do chamado 104:", central.buscar_chamado(104))
