# Exercício 5 — Comprimento de uma lista encadeada
# O algoritmo visita cada nó e incrementa um contador.
# Quando current chega a None, sabemos quantos nós foram encontrados.


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


def get_length(linked_list):
    # Começamos com zero nós contados.
    count = 0

    # current começa na cabeça da lista.
    current = linked_list.head

    while current:
        # Cada passagem pelo while corresponde a um nó visitado.
        count += 1

        # Avançamos para o próximo nó.
        current = current.next

    return count


if __name__ == "__main__":
    lista = LinkedList()

    for value in [1, 2, 3]:
        lista.append(value)

    print(f"Comprimento da lista: {get_length(lista)}")
    # Resultado esperado: 3

# Complexidade: O(n) de tempo e O(1) de espaço adicional.
