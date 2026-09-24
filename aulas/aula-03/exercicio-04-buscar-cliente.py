# Exercício 4 — Busca de cliente
# Utiliza busca sequencial para localizar o cliente e retornar sua posição.

def buscar_cliente(nome, lista_clientes):
    for i in range(len(lista_clientes)):
        # Verifica cada cliente na ordem em que aparece na lista.
        if lista_clientes[i] == nome:
            return i

    return -1


if __name__ == "__main__":
    clientes = ["Ana", "Bruno", "Carlos", "Daniel", "Elisa"]

    print("Carlos:", buscar_cliente("Carlos", clientes))
    print("Fernanda:", buscar_cliente("Fernanda", clientes))
