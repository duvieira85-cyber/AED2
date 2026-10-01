# Aula 08 — Exercícios e projetos resolvidos
# Reúne em um único arquivo as soluções do Capítulo 8 para revisão.
# Os exemplos individuais ficam separados para manter o estudo organizado.

from exercicio_01_complexidade_lista import responder as exercicio_1
from exercicio_02_insercao_cabeca import LinkedList as LinkedListCabeca
from exercicio_03_remocao_valor import LinkedList as LinkedListRemocao
from exercicio_04_busca_complexidade import responder as exercicio_4
from exercicio_05_comprimento_lista import LinkedList as LinkedListComprimento
from exercicio_05_comprimento_lista import get_length
from exercicio_06_elemento_meio import LinkedList as LinkedListMeio
from exercicio_06_elemento_meio import find_middle_element
from exercicio_07_reversao_lista import LinkedList as LinkedListReversao
from exercicio_07_reversao_lista import reverse_linked_list
from projeto_01_playlist import Music, MusicPlaylist
from projeto_02_historico_browser import BrowserHistory


if __name__ == "__main__":
    print("=== Exercício 1 ===")
    exercicio_1()

    print("\n=== Exercício 2 ===")
    lista = LinkedListCabeca()
    lista.add_head(1)
    lista.add_head(2)
    lista.add_head(3)
    print("Lista:", lista.print_list())

    print("\n=== Exercício 3 ===")
    lista = LinkedListRemocao()
    for value in [5, 7, 9, 11]:
        lista.append(value)
    print("Antes:", lista.print_list())
    lista.remove(9)
    print("Depois:", lista.print_list())

    print("\n=== Exercício 4 ===")
    exercicio_4()

    print("\n=== Exercício 5 ===")
    lista = LinkedListComprimento()
    for value in [1, 2, 3]:
        lista.append(value)
    print("Comprimento:", get_length(lista))

    print("\n=== Exercício 6 ===")
    lista = LinkedListMeio()
    for value in [1, 2, 3, 4, 5]:
        lista.append(value)
    print("Meio:", find_middle_element(lista))

    print("\n=== Exercício 7 ===")
    lista = LinkedListReversao()
    for value in [1, 2, 3]:
        lista.append(value)
    print("Original:", lista)
    reverse_linked_list(lista)
    print("Invertida:", lista)

    print("\n=== Projeto 1 ===")
    playlist = MusicPlaylist()
    playlist.add_song(Music("Bohemian Rhapsody", "Queen"))
    playlist.add_song(Music("Stairway to Heaven", "Led Zeppelin"))
    playlist.add_song(Music("Hotel California", "Eagles"))
    playlist.display_playlist()
    print("Atual:", playlist.current_song_node.data)
    print("Próxima:", playlist.play_next())
    print("Anterior:", playlist.play_previous())

    print("\n=== Projeto 2 ===")
    history = BrowserHistory()
    history.visit_page("www.fatecvotorantim.edu.br")
    history.visit_page("www.google.com")
    history.visit_page("www.youtube.com")
    print("Voltar:", history.go_back())
    print("Avançar:", history.go_forward())
    print("Voltar novamente:", history.go_back())
    history.visit_page("www.wikipedia.org")
    history.display_history()
    print("Avançar após nova visita:", history.go_forward())
