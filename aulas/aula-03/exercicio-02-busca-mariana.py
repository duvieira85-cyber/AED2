def busca_sequencial(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1


nomes = [
    "Ana", "Bruno", "Carlos", "Daniel", "Elisa",
    "Fabio", "Gabriela", "Helena", "Igor", "Julia"
]

# No pior caso, "Mariana" não está na lista e todos os elementos são comparados.
resultado = busca_sequencial(nomes, "Mariana")
print("Resultado:", resultado)
print("Pior caso: até n comparações, portanto O(n).")