# Aula 03 — Vetores Não-Ordenados — Busca Sequencial


def busca_sequencial(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1


def conta_ocorrencias(valor, lista):
    contador = 0
    for elemento in lista:
        if elemento == valor:
            contador += 1
    return contador


def remove_elemento(lista, valor):
    if len(lista) == 0:
        return None

    indice = -1
    for i in range(len(lista)):
        if lista[i] == valor:
            indice = i
            break

    if indice == -1:
        return None

    elemento_removido = lista[indice]

    for j in range(indice, len(lista) - 1):
        lista[j] = lista[j + 1]

    lista.pop()
    return elemento_removido


def buscar_cliente(nome, lista_clientes):
    return busca_sequencial(lista_clientes, nome)


def buscar_filme(catalogo, titulo):
    indice = busca_sequencial(catalogo, titulo)
    if indice != -1:
        return f"Filme '{titulo}' encontrado na posição {indice} do catálogo."
    return f"Filme '{titulo}' não encontrado no catálogo."


def verificar_convidado(lista_convidados, nome):
    if busca_sequencial(lista_convidados, nome) != -1:
        return f"O convidado '{nome}' está na lista."
    return f"O convidado '{nome}' não está na lista."


if __name__ == "__main__":
    lista = [7, 12, 5, 12, 8]

    print("Exercício 1 — melhor caso:", busca_sequencial(lista, 7))
    print("Exercício 1 — pior caso:", busca_sequencial(lista, 99))
    print("Exercício 2 — Mariana:", busca_sequencial(["Ana", "Bruno", "Carlos"], "Mariana"))
    print("Exercício 3 — primeira ocorrência de 12:", busca_sequencial(lista, 12))

    clientes = ["Ana", "Bruno", "Carlos", "Daniel", "Elisa"]
    print("Exercício 4:", buscar_cliente("Carlos", clientes))
    print("Exercício 4:", buscar_cliente("Fernanda", clientes))

    print("Exercício 5:", conta_ocorrencias(3, [1, 3, 5, 3, 7]))
    print("Exercício 5:", conta_ocorrencias("a", ["a", "b", "c", "a"]))
    print("Exercício 5:", conta_ocorrencias(10, [11, 12, 13]))

    dados = [10, 3, 7, 34, 23, 2, 21]
    print("Exercício 6 — antes:", dados)
    print("Exercício 6 — removido:", remove_elemento(dados, 23))
    print("Exercício 6 — depois:", dados)

    filmes = ["Avatar", "Matrix", "Interestelar", "Toy Story", "O Senhor dos Anéis"]
    print("Projeto 1:", buscar_filme(filmes, "Interestelar"))
    print("Projeto 1:", buscar_filme(filmes, "Titanic"))

    convidados = ["Ana", "Bruno", "Carla", "Daniel", "Elisa"]
    print("Projeto 2:", verificar_convidado(convidados, "Carla"))
    print("Projeto 2:", verificar_convidado(convidados, "Fernando"))
