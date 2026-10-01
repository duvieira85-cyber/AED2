# Testes básicos da Aula 08
# O objetivo é verificar os principais casos do capítulo:
# lista vazia, inserção, remoção, busca do meio, reversão
# e navegação dos projetos duplamente encadeados.

from exercicio_02_insercao_cabeca import LinkedList as ListaCabeca
from exercicio_03_remocao_valor import LinkedList as ListaRemocao
from exercicio_05_comprimento_lista import LinkedList as ListaComprimento, get_length
from exercicio_06_elemento_meio import LinkedList as ListaMeio, find_middle_element
from exercicio_07_reversao_lista import LinkedList as ListaReversao, reverse_linked_list
from projeto_01_playlist import Music, MusicPlaylist
from projeto_02_historico_browser import BrowserHistory


def testar():
    # Inserção na cabeça: a última inserção deve aparecer primeiro.
    lista = ListaCabeca()
    lista.add_head(1)
    lista.add_head(2)
    lista.add_head(3)
    assert lista.print_list() == [3, 2, 1]

    # Remoção no meio: 9 deve desaparecer sem quebrar a cadeia.
    lista = ListaRemocao()
    for valor in [5, 7, 9, 11]:
        lista.append(valor)
    assert lista.remove(9) is True
    assert lista.print_list() == [5, 7, 11]
    assert lista.remove(99) is False

    # Lista vazia deve ter comprimento zero.
    lista = ListaComprimento()
    assert get_length(lista) == 0

    # Contagem de nós.
    for valor in [1, 2, 3]:
        lista.append(valor)
    assert get_length(lista) == 3

    # Ponteiros lento/rápido.
    lista = ListaMeio()
    for valor in [1, 2, 3, 4, 5]:
        lista.append(valor)
    assert find_middle_element(lista) == 3

    lista = ListaMeio()
    for valor in [1, 2, 3, 4]:
        lista.append(valor)
    assert find_middle_element(lista) == 3

    # Reversão.
    lista = ListaReversao()
    for valor in [1, 2, 3]:
        lista.append(valor)
    reverse_linked_list(lista)
    assert str(lista) == "3 -> 2 -> 1"

    # Playlist: avançar e voltar.
    playlist = MusicPlaylist()
    playlist.add_song(Music("A", "Artista 1"))
    playlist.add_song(Music("B", "Artista 2"))
    playlist.add_song(Music("C", "Artista 3"))
    assert playlist.play_next().title == "B"
    assert playlist.play_previous().title == "A"
    assert playlist.play_previous().title == "C"

    # Histórico: depois de voltar e visitar uma nova página,
    # o histórico futuro deve desaparecer.
    history = BrowserHistory()
    history.visit_page("A")
    history.visit_page("B")
    history.visit_page("C")
    assert history.go_back() == "B"
    history.visit_page("D")
    assert history.go_forward() is None


if __name__ == "__main__":
    testar()
    print("Todos os testes da Aula 08 passaram.")
