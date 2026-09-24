# Exercício 1 — Acesso direto
# O acesso pelo índice permite chegar diretamente ao elemento desejado.
# Por isso, acessar uma posição conhecida da lista tem complexidade O(1).


def primeiro_elemento(lista):
    # O índice 0 representa o primeiro elemento da lista.
    return lista[0]


if __name__ == "__main__":
    # Executa um exemplo simples de acesso ao primeiro elemento.
    print(primeiro_elemento([10, 20, 30]))
