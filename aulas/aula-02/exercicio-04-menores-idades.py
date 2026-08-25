def existe_2_menores_v1(idades):
    tamanho = len(idades)
    menor = 200

    for i in range(tamanho):
        if idades[i] < menor:
            menor = idades[i]

    cont = 0
    for i in range(tamanho):
        if idades[i] == menor:
            cont += 1

    return cont > 1


def existe_2_menores_v2(idades):
    idades.sort()
    return idades[0] == idades[1]


idades1 = [18, 22, 18, 30, 25]
idades2 = [18, 22, 20, 30, 25]

print("v1:", existe_2_menores_v1(idades1))
print("v2:", existe_2_menores_v2(idades2))
print("Complexidade v1: O(n)")
print("Complexidade v2: O(n log n)")

# Dois laços consecutivos: O(n) + O(n) = O(n).
# sort() domina a segunda versão: O(n log n).