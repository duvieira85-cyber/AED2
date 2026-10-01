# Projeto 2 — Histórico de Navegação do Browser
# Uma lista duplamente encadeada representa as páginas visitadas.
# prev = página anterior | next = próxima página | current = página atual


class HistoryNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class BrowserHistory:
    def __init__(self):
        # head permite iniciar a travessia pelo primeiro endereço.
        self.head = None

        # current identifica a página atualmente visualizada.
        self.current = None

    def visit_page(self, url):
        # Criamos o novo nó antes de conectar o novo endereço.
        new_node = HistoryNode(url)

        if not self.head:
            # Primeira página do histórico.
            self.head = new_node
            self.current = new_node
            return

        # Se current.next existe, há histórico futuro.
        # Ao visitar uma nova página depois de voltar, esse trecho é descartado.
        if self.current.next:
            temp = self.current.next

            # Primeiro quebramos o vínculo entre current e o futuro.
            self.current.next = None

            # Limpamos as duas referências dos nós descartados.
            while temp:
                next_temp = temp.next
                temp.prev = None
                temp.next = None
                temp = next_temp

        # A nova página fica logo depois da página atual.
        self.current.next = new_node
        new_node.prev = self.current

        # E passa a ser a página atual.
        self.current = new_node

    def go_back(self):
        # Só podemos voltar se existir predecessor.
        if self.current and self.current.prev:
            self.current = self.current.prev
            return self.current.data
        return None

    def go_forward(self):
        # Só podemos avançar se existir sucessor.
        if self.current and self.current.next:
            self.current = self.current.next
            return self.current.data
        return None

    def display_history(self):
        history = []
        current = self.head

        # Percorremos somente o histórico ativo.
        while current:
            history.append(current.data)
            current = current.next

        print("Histórico de Navegação:")
        for url in history:
            marker = " <- atual" if url == self.current.data else ""
            print(f"- {url}{marker}")


if __name__ == "__main__":
    history = BrowserHistory()

    history.visit_page("www.fatecvotorantim.edu.br")
    history.visit_page("www.google.com")
    history.visit_page("www.youtube.com")

    print("Voltar:", history.go_back())
    print("Avançar:", history.go_forward())
    print("Voltar novamente:", history.go_back())

    # Estamos no Google.
    # Uma nova visita descarta o YouTube do futuro.
    history.visit_page("www.wikipedia.org")

    history.display_history()
    print("Tentar avançar:", history.go_forward())

# Complexidade:
# go_back() -> O(1)
# go_forward() -> O(1)
# visita normal no final -> O(1)
# descarte de histórico futuro -> O(k)
# display_history() -> O(n)
