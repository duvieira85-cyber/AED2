# Exercício 3 — Fila de clientes
# Simular uma fila e compreender o princípio FIFO.

clientes = []
clientes.append("Ana")
clientes.append("Bruno")
clientes.append("Carla")
clientes.append("Daniel")
cliente_saiu = clientes.pop(0)

print(f"Cliente que saiu: {cliente_saiu}")
print(f"Fila restante: {clientes}")
