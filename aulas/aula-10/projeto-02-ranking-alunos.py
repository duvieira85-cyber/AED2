# Projeto 2 — Ranking de alunos por média
# Gera um ranking ordenado do maior para o menor
# e mostra a posição de cada aluno no top 3.


def bubble_ranking(alunos):
    # Cada aluno é uma tupla (nome, media).
    dados = alunos[:]

    for i in range(len(dados) - 1):

        for j in range(len(dados) - 1 - i):
            if dados[j][1] < dados[j + 1][1]:
                dados[j], dados[j + 1] = dados[j + 1], dados[j]

    return dados


alunos = [
    ("Ana", 8.4),
    ("Bruno", 6.9),
    ("Carla", 9.2),
    ("Diego", 7.5),
    ("Elisa", 8.4),
]

ranking = bubble_ranking(alunos)

print("Ranking por média:")
for i, (nome, media) in enumerate(ranking):
    print(i + 1, "-", nome, "|", media)

print("Top 3:", [nome for nome, media in ranking[:3]])
