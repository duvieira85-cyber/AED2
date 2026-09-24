# Aula 02 — Complexidade de Algoritmos
# Reúne exercícios e projetos resolvidos sobre acesso, buscas,
# recursão, complexidade e uso de estruturas auxiliares.


def exercicio_1(lista):
    # O índice 0 permite acessar diretamente o primeiro elemento.
    # Esse acesso tem complexidade O(1).
    print(lista[0])


def exercicio_2(lista):
    # Assume o primeiro elemento como maior valor inicial.
    valor_maximo = lista[0]

    # Percorre a lista procurando valores maiores.
    for numero in lista:
        if numero > valor_maximo:
            valor_maximo = numero

    return valor_maximo


def exercicio_3(lista, alvo):
    # Define os limites do intervalo que será pesquisado.
    esquerda = 0
    direita = len(lista) - 1

    # A busca binária reduz o intervalo pela metade a cada passo.
    while esquerda <= direita:
        meio = (esquerda + direita) // 2

        if lista[meio] == alvo:
            # O elemento central é o alvo.
            return meio
        elif lista[meio] < alvo:
            # Descarta a metade esquerda.
            esquerda = meio + 1
        else:
            # Descarta a metade direita.
            direita = meio - 1

    # O alvo não foi encontrado.
    return -1


def exercicio_4_v1(idades):
    # Primeira passagem: encontra a menor idade.
    menor = 200

    for idade in idades:
        if idade < menor:
            menor = idade

    # Segunda passagem: conta quantas vezes a menor idade aparece.
    cont = 0

    for idade in idades:
        if idade == menor:
            cont += 1

    # Mais de uma ocorrência significa que a menor idade se repete.
    return cont > 1


def exercicio_4_v2(idades):
    # A ordenação coloca a menor idade nas primeiras posições.
    idades.sort()

    # Se as duas primeiras forem iguais, a menor está repetida.
    return idades[0] == idades[1]


def fibonacci_recursivo(n):
    # Casos-base da sequência: 0 e 1.
    if n < 2:
        return n

    # Soma os dois termos anteriores usando recursão.
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


def busca_linear(lista, alvo):
    # Verifica cada elemento sequencialmente.
    for elemento in lista:
        if elemento == alvo:
            return True

    # O alvo não apareceu na lista.
    return False


def busca_binaria(lista, alvo):
    # Define os limites da lista ordenada.
    esquerda = 0
    direita = len(lista) - 1

    while esquerda <= direita:
        # Examina o elemento central do intervalo atual.
        meio = (esquerda + direita) // 2

        if lista[meio] == alvo:
            return True
        elif lista[meio] < alvo:
            # O alvo só pode estar à direita.
            esquerda = meio + 1
        else:
            # O alvo só pode estar à esquerda.
            direita = meio - 1

    return False


def buscar_aluno_linear(lista_alunos, cpf):
    # Procura o CPF percorrendo os alunos um a um.
    for aluno in lista_alunos:
        if aluno["cpf"] == cpf:
            return aluno

    # CPF não encontrado.
    return None


def buscar_aluno_eficiente(dicionario_alunos, cpf):
    # O CPF é usado como chave do dicionário,
    # permitindo uma consulta média de O(1).
    return dicionario_alunos.get(cpf)


def recomendar_disciplinas(historicos_alunos, historico_aluno_principal):
    # set evita recomendações duplicadas.
    recomendacoes = set()

    # Converte o histórico principal para conjunto para facilitar
    # interseções e diferenças.
    principal = set(historico_aluno_principal)

    for historico in historicos_alunos:
        outro = set(historico)

        # Considera somente históricos diferentes do principal
        # que possuam alguma disciplina em comum.
        if outro != principal and principal & outro:
            # Adiciona disciplinas que o aluno principal ainda não cursou.
            recomendacoes.update(outro - principal)

    return list(recomendacoes)


if __name__ == "__main__":
    # Executa exemplos dos exercícios da aula.
    print("Exercício 1:")
    exercicio_1([10, 20, 30])

    print("Exercício 2:", exercicio_2([12, 7, 25, 3, 19]))
    print("Exercício 3:", exercicio_3([2, 5, 8, 12, 16, 21, 27], 21))
    print("Exercício 4 v1:", exercicio_4_v1([18, 22, 18, 30]))
    print("Exercício 4 v2:", exercicio_4_v2([18, 22, 18, 30]))
    print("Exercício 5:", fibonacci_recursivo(10))
    print("Exercício 6:", busca_linear([1, 4, 7, 12, 18], 12))

    # Dados usados no Projeto 1.
    alunos = [
        {"nome": "Ana Souza", "cpf": "111.111.111-11", "curso": "CDN"},
        {"nome": "Bruno Lima", "cpf": "222.222.222-22", "curso": "ADS"},
    ]

    # Cria um índice por CPF para tornar as consultas mais eficientes.
    indice = {aluno["cpf"]: aluno for aluno in alunos}

    print("Projeto 1:", buscar_aluno_linear(alunos, "222.222.222-22"))
    print("Projeto 1 otimizado:", buscar_aluno_eficiente(indice, "222.222.222-22"))

    # Históricos usados no Projeto 2 para gerar recomendações.
    historicos = [
        ["CD101", "CD102", "CD103"],
        ["CD102", "CD104", "CD105"],
        ["CD103", "CD106"],
        ["CD107", "CD108"],
    ]

    print("Projeto 2:", recomendar_disciplinas(historicos, ["CD101", "CD102"]))
