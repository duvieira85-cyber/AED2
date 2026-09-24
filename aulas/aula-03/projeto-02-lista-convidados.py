# Projeto 2 — Lista de convidados
# Verifica se um nome está presente em uma lista usando busca sequencial.
# Melhor caso: O(1). Pior caso: O(n). Espaço adicional: O(1).


def busca_sequencial(lista, alvo):
    # Percorre os convidados desde a primeira posição.
    for i in range(len(lista)):
        if lista[i] == alvo:
            # Retorna o índice assim que encontra o nome.
            return i

    # O convidado não foi encontrado.
    return -1


def verificar_convidado(lista_convidados, nome):
    # A posição -1 representa ausência na lista.
    if busca_sequencial(lista_convidados, nome) != -1:
        return f"O convidado '{nome}' está na lista."
    else:
        return f"O convidado '{nome}' não está na lista."


# Lista de convidados utilizada no exemplo.
convidados = [
    "Ana",
    "Bruno",
    "Carla",
    "Daniel",
    "Elisa",
]

# Carla está cadastrada e deve ser encontrada.
print(verificar_convidado(convidados, "Carla"))

# Fernando não está cadastrado e deve resultar em uma mensagem de ausência.
print(verificar_convidado(convidados, "Fernando"))

# Melhor caso: O(1). Pior caso: O(n). Espaço adicional: O(1).
# Importante: índice 0 é válido; ausência é representada por -1.
