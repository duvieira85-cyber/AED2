def encontrar_maximo(lista):
    valor_maximo = lista[0]
    for numero in lista:
        if numero > valor_maximo:
            valor_maximo = numero
    return valor_maximo


numeros = [12, 7, 25, 3, 19]
print("Maior valor:", encontrar_maximo(numeros))

# Complexidade: O(n).