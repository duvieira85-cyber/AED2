# Exercício 6 — Comparar o tempo dos métodos
# Roda os cinco métodos no mesmo vetor aleatório de 2000 elementos
# e mostra o tempo de cada um. O(n log n) vence com folga.


import random
import time

from exercicio_01_bubble_sort import bubble_sort
from exercicio_02_insertion_sort import insertion_sort
from exercicio_03_selection_sort import selection_sort
from exercicio_04_merge_sort import merge_sort
from exercicio_05_quick_sort import quick_sort


def medir(metodo, dados):
    # Cronometra uma cópia do vetor para não ordenar o original.
    copia = dados[:]
    inicio = time.perf_counter()
    metodo(copia)
    return time.perf_counter() - inicio


if __name__ == "__main__":
    dados = [random.randint(1, 10000) for _ in range(2000)]

    print("bubble   :", round(medir(bubble_sort, dados), 4), "s")
    print("insertion:", round(medir(insertion_sort, dados), 4), "s")
    print("selection:", round(medir(selection_sort, dados), 4), "s")
    print("merge    :", round(medir(merge_sort, dados), 4), "s")
    print("quick    :", round(medir(quick_sort, dados), 4), "s")
