# Exercício 2 — Encontrar o maior valor
# É necessário percorrer a lista para comparar os elementos, resultando em O(n).

def encontrar_maximo(lista):
    valor_maximo = lista[0]

    # Compara cada elemento com o maior valor encontrado até o momento.
    for numero in lista:
        if numero > valor_maximo:
            valor_maximo = numero

    return valor_maximo


if __name__ == "__main__":
    print(encontrar_maximo([12, 7, 25, 3, 19]))
