def recomendar_disciplinas(historicos_alunos, historico_aluno_principal):
    recomendacoes = set()

    for historico_outro_aluno in historicos_alunos:
        if historico_outro_aluno != historico_aluno_principal:
            intersecao = (
                set(historico_aluno_principal)
                & set(historico_outro_aluno)
            )

            if intersecao:
                diferenca = (
                    set(historico_outro_aluno)
                    - set(historico_aluno_principal)
                )
                recomendacoes.update(diferenca)

    return list(recomendacoes)


historicos = [
    ["CD101", "CD102", "CD103"],
    ["CD102", "CD104", "CD105"],
    ["CD103", "CD106"],
    ["CD107", "CD108"],
    ["CD101", "CD105", "CD109", "CD110"],
]

historico_principal = ["CD101", "CD102"]
recomendadas = recomendar_disciplinas(
    historicos,
    historico_principal
)

print("Disciplinas recomendadas:", recomendadas)

# A interseção identifica interesses em comum.
# A diferença exclui disciplinas já cursadas pelo aluno principal.
# O set evita recomendações duplicadas.
# Complexidade analisada no capítulo: O(n * m), considerando alunos e disciplinas.