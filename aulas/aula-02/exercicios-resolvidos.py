# Aula 02 — Complexidade de Algoritmos
# Exercícios e projetos resolvidos.


def exercicio_1(lista):
    print(lista[0])


def exercicio_2(lista):
    valor_maximo = lista[0]
    for numero in lista:
        if numero > valor_maximo:
            valor_maximo = numero
    return valor_maximo


def exercicio_3(lista, alvo):
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1


def exercicio_4_v1(idades):
    menor = 200
    for idade in idades:
        if idade < menor:
            menor = idade
    cont = 0
    for idade in idades:
        if idade == menor:
            cont += 1
    return cont > 1


def exercicio_4_v2(idades):
    idades.sort()
    return idades[0] == idades[1]


def fibonacci_recursivo(n):
    if n < 2:
        return n
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


def busca_linear(lista, alvo):
    for elemento in lista:
        if elemento == alvo:
            return True
    return False


def busca_binaria(lista, alvo):
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return True
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return False


def buscar_aluno_linear(lista_alunos, cpf):
    for aluno in lista_alunos:
        if aluno["cpf"] == cpf:
            return aluno
    return None


def buscar_aluno_eficiente(dicionario_alunos, cpf):
    return dicionario_alunos.get(cpf)


def recomendar_disciplinas(historicos_alunos, historico_aluno_principal):
    recomendacoes = set()
    principal = set(historico_aluno_principal)

    for historico in historicos_alunos:
        outro = set(historico)
        if outro != principal and principal & outro:
            recomendacoes.update(outro - principal)

    return list(recomendacoes)


if __name__ == "__main__":
    print("Exercício 1:")
    exercicio_1([10, 20, 30])
    print("Exercício 2:", exercicio_2([12, 7, 25, 3, 19]))
    print("Exercício 3:", exercicio_3([2, 5, 8, 12, 16, 21, 27], 21))
    print("Exercício 4 v1:", exercicio_4_v1([18, 22, 18, 30]))
    print("Exercício 4 v2:", exercicio_4_v2([18, 22, 18, 30]))
    print("Exercício 5:", fibonacci_recursivo(10))
    print("Exercício 6:", busca_linear([1, 4, 7, 12, 18], 12))

    alunos = [
        {"nome": "Ana Souza", "cpf": "111.111.111-11", "curso": "CDN"},
        {"nome": "Bruno Lima", "cpf": "222.222.222-22", "curso": "ADS"},
    ]
    indice = {aluno["cpf"]: aluno for aluno in alunos}
    print("Projeto 1:", buscar_aluno_linear(alunos, "222.222.222-22"))
    print("Projeto 1 otimizado:", buscar_aluno_eficiente(indice, "222.222.222-22"))

    historicos = [
        ["CD101", "CD102", "CD103"],
        ["CD102", "CD104", "CD105"],
        ["CD103", "CD106"],
        ["CD107", "CD108"],
    ]
    print("Projeto 2:", recomendar_disciplinas(historicos, ["CD101", "CD102"]))
