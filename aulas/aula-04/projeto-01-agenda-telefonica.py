# Projeto 1 — Agenda telefônica ordenada
# Mantém os contatos em ordem alfabética e usa busca binária
# para localizar um nome e mostrar o telefone correspondente.


def busca_binaria(nomes, alvo):
    inicio = 0
    fim = len(nomes) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if nomes[meio] == alvo:
            return meio

        if nomes[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1


def consultar(agenda, nome):
    # A agenda guarda os nomes já em ordem alfabética.
    nomes = sorted(agenda.keys())
    indice = busca_binaria(nomes, nome)

    if indice == -1:
        return "'" + nome + "' não está na agenda."

    return nome + ": " + agenda[nomes[indice]]


agenda = {
    "Bruno": "(15) 99123-4567",
    "Ana": "(15) 99777-1122",
    "Carla": "(15) 99555-8080",
    "Diego": "(15) 99444-7070",
}

print(consultar(agenda, "Carla"))
print(consultar(agenda, "Zeca"))
