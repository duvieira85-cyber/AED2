# Exercício 5 — Contar a frequência de palavras
# Uso clássico de tabela hash: a palavra é a chave
# e o contador é o valor, atualizado a cada ocorrência.


frase = "estrutura de dados com python estrutura de dados"
contagem = {}


def funcao_hash(palavra):
    # Soma dos códigos das letras como posição da palavra.
    return sum(ord(letra) for letra in palavra)


if __name__ == "__main__":
    for palavra in frase.split():
        posicao = funcao_hash(palavra)

        # Palavra nova entra com 1; repetida soma 1 ao contador.
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1

    for palavra, quantidade in contagem.items():
        print(palavra, "->", quantidade)
