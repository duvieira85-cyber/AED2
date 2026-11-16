# Projeto 1 — Catálogo ordenado por título e por nota
# Usa merge sort com chave para ordenar o catálogo
# alfabeticamente por título ou pela nota maior para menor.


def merge_por_chave(lista, chave, reverso=False):
    # Merge sort que compara pela função chave informada.
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = merge_por_chave(lista[:meio], chave, reverso)
    direita = merge_por_chave(lista[meio:], chave, reverso)

    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        a, b = chave(esquerda[i]), chave(direita[j])

        if (not reverso and a <= b) or (reverso and a >= b):
            resultado.append(esquerda[i]); i += 1
        else:
            resultado.append(direita[j]); j += 1

    resultado += esquerda[i:]
    resultado += direita[j:]
    return resultado


catalogo = [
    {"titulo": "Interestelar", "nota": 8.6},
    {"titulo": "Avatar", "nota": 7.9},
    {"titulo": "Bacurau", "nota": 8.1},
    {"titulo": "Matrix", "nota": 8.7},
]

print("Por título:")
for f in merge_por_chave(catalogo, lambda f: f["titulo"]):
    print(" -", f["titulo"])

print("Por nota (maior para menor):")
for f in merge_por_chave(catalogo, lambda f: f["nota"], True):
    print(" -", f["titulo"], "|", f["nota"])
