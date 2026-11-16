# Projeto 2 — Cache simples de consultas
# Guarda o resultado da última consulta de cada chave:
# na primeira vez calcula, nas demais devolve do cache na hora.


TAMANHO = 10
cache = [[] for _ in range(TAMANHO)]
consultas = 0


def funcao_hash(chave):
    return chave % TAMANHO


def consultar(chave):
    global consultas

    # Procura no cache antes de calcular.
    for chave_salva, valor in cache[funcao_hash(chave)]:
        if chave_salva == chave:
            return valor, False

    # Não está no cache: calcula e guarda.
    valor = chave * chave
    cache[funcao_hash(chave)].append((chave, valor))
    consultas += 1

    return valor, True


if __name__ == "__main__":
    print(consultar(4), "(calculado)")
    print(consultar(4), "(cache)")
    print(consultar(7), "(calculado)")
    print(consultar(4), "(cache)")
    print("cálculos realizados:", consultas)
