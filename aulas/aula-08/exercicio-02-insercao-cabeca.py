# Exercício 2 — Inserindo sempre na cabeça
# Cada novo nó passa a ser o primeiro elemento da lista.
# Por isso, a ordem final fica invertida em relação à ordem de inserção.


class Node:
    def __init__(self, data):
        # data guarda o valor armazenado neste nó.
        self.data = data

        # next aponta para o próximo nó da cadeia.
        self.next = None


class LinkedList:
    def __init__(self):
        # head aponta para o primeiro nó.
        # None representa uma lista vazia.
        self.head = None

    def add_head(self, data):
        # Criamos o novo nó que ficará no início.
        new_node = Node(data)

        # Antes de trocar a cabeça, ligamos o novo nó à antiga cabeça.
        new_node.next = self.head

        # Agora o novo nó passa a ser a nova cabeça.
        self.head = new_node

    def print_list(self):
        # Percorremos a cadeia a partir de head.
        values = []
        current = self.head

        while current:
            values.append(current.data)
            current = current.next

        return values


if __name__ == "__main__":
    lista = LinkedList()

    lista.add_head(1)
    lista.add_head(2)
    lista.add_head(3)

    print("Lista final:", lista.print_list())
    # Resultado esperado: [3, 2, 1]
