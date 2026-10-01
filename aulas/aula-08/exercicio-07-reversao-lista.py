# Exercício 7 — Revertendo a lista encadeada
# Antes de inverter current.next, precisamos guardar o próximo nó.
# Caso contrário, perderíamos o caminho para o restante da lista.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def __str__(self):
        values = []
        current = self.head

        while current:
            values.append(str(current.data))
            current = current.next

        return " -> ".join(values)


def reverse_linked_list(linked_list):
    # prev representa o nó que ficará atrás do current.
    prev = None

    # Começamos na cabeça original.
    current = linked_list.head

    while current:
        # 1. Salvamos o próximo nó antes de mexer na ligação.
        next_node = current.next

        # 2. Invertimos a seta do nó atual.
        current.next = prev

        # 3. Avançamos as referências auxiliares.
        prev = current
        current = next_node

    # prev ficou no antigo último nó.
    # Ele passa a ser a nova cabeça.
    linked_list.head = prev


if __name__ == "__main__":
    lista = LinkedList()

    for value in [1, 2, 3]:
        lista.append(value)

    print("Lista original:", lista)
    reverse_linked_list(lista)
    print("Lista invertida:", lista)

# Resultado esperado:
# Lista original: 1 -> 2 -> 3
# Lista invertida: 3 -> 2 -> 1
# Complexidade: O(n) de tempo e O(1) de espaço adicional.
