def busca_sequencial(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1


def verificar_convidado(lista_convidados, nome):
    if busca_sequencial(lista_convidados, nome) != -1:
        return f"O convidado '{nome}' está na lista."
    else:
        return f"O convidado '{nome}' não está na lista."


convidados = [
    "Ana",
    "Bruno",
    "Carla",
    "Daniel",
    "Elisa",
]

print(verificar_convidado(convidados, "Carla"))
print(verificar_convidado(convidados, "Fernando"))

# Melhor caso: O(1). Pior caso: O(n). Espaço adicional: O(1).
# Importante: índice 0 é válido; ausência é representada por -1.