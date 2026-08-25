def buscar_cliente(nome, lista_clientes):
    for i in range(len(lista_clientes)):
        if lista_clientes[i] == nome:
            return i
    return -1


clientes = ["Ana", "Bruno", "Carlos", "Daniel", "Elisa"]

busca1 = "Carlos"
busca2 = "Fernanda"

pos1 = buscar_cliente(busca1, clientes)
if pos1 != -1:
    print(f"Cliente '{busca1}' encontrado na posição {pos1}.")
else:
    print(f"Cliente '{busca1}' não encontrado na lista.")

pos2 = buscar_cliente(busca2, clientes)
if pos2 != -1:
    print(f"Cliente '{busca2}' encontrado na posição {pos2}.")
else:
    print(f"Cliente '{busca2}' não encontrado na lista.")

# Melhor caso: O(1). Pior caso: O(n). Espaço adicional: O(1).