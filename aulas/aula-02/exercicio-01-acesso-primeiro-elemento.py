# Exercício 1 — Acesso direto
# O acesso pelo índice é executado diretamente e tem complexidade O(1).

def primeiro_elemento(lista):
    return lista[0]


if __name__ == "__main__":
    print(primeiro_elemento([10, 20, 30]))
