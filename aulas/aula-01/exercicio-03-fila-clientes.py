# Exercício 3 — Fila de clientes
# A fila segue o princípio FIFO: o primeiro cliente que entra é o primeiro a sair.

fila = ["Ana", "Bruno", "Carlos"]

# Adiciona um novo cliente ao final da fila.
fila.append("Daniel")

# Remove o cliente que está no início da fila.
atendido = fila.pop(0)

print("Cliente atendido:", atendido)
print("Fila:", fila)
