# Projeto 2 — Recomendação de disciplinas
# Compara o histórico do aluno principal com os históricos dos demais.
# Disciplinas em comum indicam interesse semelhante; outras disciplinas
# desses alunos podem ser adicionadas como recomendações.


def recomendar_disciplinas(historicos_alunos, historico_aluno_principal):
    # set evita recomendações duplicadas.
    recomendacoes = set()

    for historico_outro_aluno in historicos_alunos:
        # Ignora o próprio histórico do aluno principal.
        if historico_outro_aluno != historico_aluno_principal:
            # A interseção encontra as disciplinas cursadas em comum.
            intersecao = (
                set(historico_aluno_principal)
                & set(historico_outro_aluno)
            )

            if intersecao:
                # A diferença mantém apenas disciplinas que o aluno principal
                # ainda não possui em seu histórico.
                diferenca = (
                    set(historico_outro_aluno)
                    - set(historico_aluno_principal)
                )

                # Adiciona as novas recomendações ao conjunto.
                recomendacoes.update(diferenca)

    # Converte o conjunto para lista antes de retornar o resultado.
    return list(recomendacoes)


# Históricos usados como base para encontrar alunos com interesses semelhantes.
historicos = [
    ["CD101", "CD102", "CD103"],
    ["CD102", "CD104", "CD105"],
    ["CD103", "CD106"],
    ["CD107", "CD108"],
    ["CD101", "CD105", "CD109", "CD110"],
]

# Histórico do aluno para o qual serão geradas as recomendações.
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
