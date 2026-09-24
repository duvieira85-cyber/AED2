# Exercício 3 — Fila de clientes
# A fila segue o princípio FIFO (First In, First Out):
# o primeiro cliente que entra é o primeiro a ser atendido.

fila = ["Ana", "Bruno", "Carlos"]

# Adiciona Daniel ao final da fila, preservando a ordem de chegada.
fila.append("Daniel")

# pop(0) remove o primeiro elemento da lista, simulando o atendimento.
atendido = fila.pop(0)

# Exibe o cliente atendido e os clientes que continuam aguardando.
print("Cliente atendido:", atendido)
print("Fila:", fila)
