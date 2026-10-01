# Exercício 3 — Remoção de um nó por valor
# Para remover um nó do meio, o ponto principal é reconectar o anterior ao sucessor.
# Exemplo: 5 -> 7 -> 9 -> 11 se torna 5 -> 7 -> 11.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        # Cria o novo nó que será acrescentado ao final.
        new_node = Node(data)

        if self.head is None:
            # Se a lista está vazia, o primeiro nó também é a cabeça.
            self.head = new_node
            return

        # Caminhamos até o último nó.
        current = self.head
        while current.next:
            current = current.next

        # O último nó passa a apontar para o novo nó.
        current.next = new_node

    def remove(self, value):
        # Lista vazia: nada para remover.
        if self.head is None:
            return False

        # Caso especial: o valor está justamente na cabeça.
        if self.head.data == value:
            self.head = self.head.next
            return True

        # Precisamos localizar o nó anterior ao alvo.
        current = self.head
        while current.next and current.next.data != value:
            current = current.next

        if current.next:
            # current.next é o nó que será removido.
            # Fazemos current apontar para o próximo do nó removido.
            # Assim a cadeia continua conectada.
            current.next = current.next.next
            return True

        # Percorremos tudo e o valor não foi encontrado.
        return False

    def print_list(self):
        values = []
        current = self.head
        while current:
            values.append(current.data)
            current = current.next
        return values


if __name__ == "__main__":
    lista = LinkedList()

    for value in [5, 7, 9, 11]:
        lista.append(value)

    print("Antes:", lista.print_list())
    lista.remove(9)
    print("Depois:", lista.print_list())
    # Resultado esperado: [5, 7, 11]
