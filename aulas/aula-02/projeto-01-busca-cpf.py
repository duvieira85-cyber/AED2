# Projeto 1 — Busca de aluno por CPF
# Compara uma busca linear em uma lista com uma consulta
# em um dicionário indexado pelo CPF.


def buscar_aluno_linear(lista_alunos, cpf):
    # Percorre os alunos até encontrar o CPF informado.
    for aluno in lista_alunos:
        if aluno["cpf"] == cpf:
            # Retorna o cadastro completo quando encontra o aluno.
            return aluno

    # Retorna None quando nenhum aluno possui o CPF pesquisado.
    return None


def buscar_aluno_eficiente(dicionario_alunos, cpf):
    # O CPF é usado diretamente como chave do dicionário,
    # permitindo uma consulta média de O(1).
    if cpf in dicionario_alunos:
        return dicionario_alunos[cpf]

    # CPF não cadastrado.
    return None


# Lista original com os cadastros dos alunos.
lista_de_alunos = [
    {"nome": "Ana Souza", "cpf": "111.111.111-11", "curso": "CDN"},
    {"nome": "Bruno Lima", "cpf": "222.222.222-22", "curso": "ADS"},
    {"nome": "Carla Mendes", "cpf": "333.333.333-33", "curso": "CDN"},
]

# Cria um índice usando o CPF como chave para agilizar consultas.
dicionario_de_alunos = {
    aluno["cpf"]: aluno for aluno in lista_de_alunos
}

# CPF que será utilizado nas duas formas de busca.
cpf_buscado = "222.222.222-22"

print(buscar_aluno_linear(lista_de_alunos, cpf_buscado))
print(buscar_aluno_eficiente(dicionario_de_alunos, cpf_buscado))

# Complexidade:
# Busca linear: O(n) no pior caso.
# Construção do índice: O(n).
# Consulta no dicionário: O(1) em média.
