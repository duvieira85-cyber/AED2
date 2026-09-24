# Exercício 4 — Busca de cliente
# Utiliza busca sequencial para localizar um cliente e retornar
# sua posição na lista.


def buscar_cliente(nome, lista_clientes):
    # Percorre os clientes na ordem em que aparecem na lista.
    for i in range(len(lista_clientes)):
        # Compara o nome atual com o nome procurado.
        if lista_clientes[i] == nome:
            return i

    # Retorna -1 quando o cliente não está cadastrado.
    return -1


if __name__ == "__main__":
    clientes = ["Ana", "Bruno", "Carlos", "Daniel", "Elisa"]

    # Carlos existe na lista, então sua posição é localizada.
    print("Carlos:", buscar_cliente("Carlos", clientes))

    # Fernanda não existe, portanto o resultado será -1.
    print("Fernanda:", buscar_cliente("Fernanda", clientes))
