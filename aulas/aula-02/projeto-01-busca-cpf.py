def buscar_aluno_linear(lista_alunos, cpf):
    for aluno in lista_alunos:
        if aluno["cpf"] == cpf:
            return aluno
    return None


def buscar_aluno_eficiente(dicionario_alunos, cpf):
    if cpf in dicionario_alunos:
        return dicionario_alunos[cpf]
    return None


lista_de_alunos = [
    {"nome": "Ana Souza", "cpf": "111.111.111-11", "curso": "CDN"},
    {"nome": "Bruno Lima", "cpf": "222.222.222-22", "curso": "ADS"},
    {"nome": "Carla Mendes", "cpf": "333.333.333-33", "curso": "CDN"},
]

dicionario_de_alunos = {
    aluno["cpf"]: aluno for aluno in lista_de_alunos
}

cpf_buscado = "222.222.222-22"

print(buscar_aluno_linear(lista_de_alunos, cpf_buscado))
print(buscar_aluno_eficiente(dicionario_de_alunos, cpf_buscado))

# Busca linear: O(n) no pior caso.
# Construção do índice: O(n).
# Consulta no dicionário: O(1) em média.