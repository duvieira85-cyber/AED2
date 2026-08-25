def conta_ocorrencias(valor, lista):
    contador = 0

    for elemento in lista:
        if elemento == valor:
            contador += 1

    return contador


print(conta_ocorrencias(3, [1, 3, 5, 3, 7]))
print(conta_ocorrencias("a", ["a", "b", "c", "a"]))
print(conta_ocorrencias(10, [11, 12, 13]))

# Saída esperada:
# 2
# 2
# 0
# Complexidade: O(n), pois toda a lista precisa ser percorrida.