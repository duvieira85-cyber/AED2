# Exercício 6 — Encontrando o elemento do meio
# Usamos dois ponteiros:
# slow_ptr avança um nó por vez.
# fast_ptr avança dois nós por vez.
# Quando fast_ptr termina, slow_ptr está aproximadamente no meio.


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


def find_middle_element(linked_list):
    # Lista vazia não possui elemento do meio.
    if not linked_list.head:
        return None

    # Os dois ponteiros começam no mesmo lugar.
    slow_ptr = linked_list.head
    fast_ptr = linked_list.head

    while fast_ptr and fast_ptr.next:
        # O rápido anda duas posições.
        fast_ptr = fast_ptr.next.next

        # O lento anda uma posição.
        slow_ptr = slow_ptr.next

    # slow_ptr chegou ao elemento central segundo esta estratégia.
    return slow_ptr.data


if __name__ == "__main__":
    lista = LinkedList()

    for value in [1, 2, 3, 4, 5]:
        lista.append(value)

    print("Elemento do meio:", find_middle_element(lista))
    # Resultado esperado: 3

# Para [1, 2, 3, 4], o material apresenta 3: o segundo dos dois centrais.
# Complexidade: O(n) de tempo e O(1) de espaço adicional.
