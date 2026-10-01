# Projeto 1 — Gerenciador de Playlist de Música
# Lista duplamente encadeada: cada nó conhece o anterior (prev)
# e o próximo (next), permitindo navegação nos dois sentidos.


class Music:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def __str__(self):
        return f"{self.title} - {self.artist}"


class DoublyNode:
    def __init__(self, data):
        self.data = data

        # next aponta para a próxima música.
        self.next = None

        # prev aponta para a música anterior.
        self.prev = None


class MusicPlaylist:
    def __init__(self):
        # head = primeira música da playlist.
        self.head = None

        # tail = última música.
        # Ter tail permite inserir no final em O(1).
        self.tail = None

        # current_song_node = música atualmente em reprodução.
        self.current_song_node = None

    def add_song(self, music):
        # Transformamos a música em um nó da lista.
        new_node = DoublyNode(music)

        if not self.head:
            # Primeira música: ela é head, tail e atual.
            self.head = new_node
            self.tail = new_node
            self.current_song_node = new_node
            return

        # O novo nó entra depois do tail atual.
        new_node.prev = self.tail
        self.tail.next = new_node

        # Atualizamos tail para o novo último nó.
        self.tail = new_node

    def remove_song(self, title):
        # Procuramos a música pelo título.
        current = self.head

        while current:
            if current.data.title == title:
                # Liga o predecessor ao sucessor.
                if current.prev:
                    current.prev.next = current.next
                else:
                    # Sem predecessor significa remoção da head.
                    self.head = current.next

                # Liga o sucessor ao predecessor.
                if current.next:
                    current.next.prev = current.prev
                else:
                    # Sem sucessor significa remoção da tail.
                    self.tail = current.prev

                # Se removemos a música atual, seguimos a lógica do material
                # e apontamos current para a head.
                if self.current_song_node == current:
                    self.current_song_node = self.head

                # Desconectar o nó removido evita referências residuais.
                current.next = None
                current.prev = None

                return True

            current = current.next

        return False

    def play_next(self):
        if not self.current_song_node:
            return None

        # Avança para a próxima música.
        self.current_song_node = self.current_song_node.next

        if not self.current_song_node:
            # No fim, a navegação volta para a primeira música.
            self.current_song_node = self.head

        return self.current_song_node.data if self.current_song_node else None

    def play_previous(self):
        if not self.current_song_node:
            return None

        # Volta para a música anterior.
        self.current_song_node = self.current_song_node.prev

        if not self.current_song_node:
            # Antes da primeira, voltamos para a última.
            self.current_song_node = self.tail

        return self.current_song_node.data if self.current_song_node else None

    def display_playlist(self):
        songs = []
        current = self.head

        # Percorremos a playlist do início até o fim.
        while current:
            songs.append(str(current.data))
            current = current.next

        print("Playlist:")
        for song in songs:
            print(f"- {song}")


if __name__ == "__main__":
    playlist = MusicPlaylist()

    playlist.add_song(Music("Bohemian Rhapsody", "Queen"))
    playlist.add_song(Music("Stairway to Heaven", "Led Zeppelin"))
    playlist.add_song(Music("Hotel California", "Eagles"))

    playlist.display_playlist()

    print("Tocando agora:", playlist.current_song_node.data)
    print("Próxima música:", playlist.play_next())
    print("Música anterior:", playlist.play_previous())

    playlist.remove_song("Stairway to Heaven")
    playlist.display_playlist()

# Complexidade:
# add_song() -> O(1)
# play_next() -> O(1)
# play_previous() -> O(1)
# remove_song() -> O(n) no pior caso
# display_playlist() -> O(n)
