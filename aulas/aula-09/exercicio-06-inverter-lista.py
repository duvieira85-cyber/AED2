# Exercício 6 — Inverter uma lista (recursivo)
# A lista invertida é o último elemento seguido da inversão do resto.


def inverter(lista):
    # Caso base: lista vazia ou com um elemento é a própria lista.
    if len(lista) <= 1:
        return lista

    # Último elemento na frente da inversão do resto.
    return [lista[-1]] + inverter(lista[:-1])


if __name__ == "__main__":
    print(inverter([1, 2, 3, 4, 5]))
    print(inverter(["a", "b", "c"]))
