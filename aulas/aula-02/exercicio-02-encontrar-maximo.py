# Exercício 2 — Encontrar o maior valor
# É necessário percorrer a lista para comparar seus elementos.
# Por isso, a complexidade é O(n), pois cada elemento pode ser analisado.


def encontrar_maximo(lista):
    # Assume inicialmente que o primeiro elemento é o maior.
    valor_maximo = lista[0]

    # Compara cada elemento com o maior valor encontrado até o momento.
    for numero in lista:
        if numero > valor_maximo:
            # Atualiza o maior valor quando encontra um número maior.
            valor_maximo = numero

    # Ao final da varredura, contém o maior elemento da lista.
    return valor_maximo


if __name__ == "__main__":
    # Executa um exemplo com diferentes valores.
    print(encontrar_maximo([12, 7, 25, 3, 19]))
