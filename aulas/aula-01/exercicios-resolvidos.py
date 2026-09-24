# Aula 01 — Exercícios resolvidos
# Estrutura de Dados com Python — Capítulo 1
# Prof. Dr. Dilermando Piva Jr.
#
# Esta aula apresenta estruturas básicas do Python:
# listas, pilhas, filas e dicionários.


# ============================================================
# Exercício 1 — Lista de frutas
# Objetivo: criar uma lista, adicionar um elemento ao final
# e imprimir o resultado.
# ============================================================

frutas = ["maçã", "banana", "laranja"]

# append() adiciona o novo elemento ao final da lista.
frutas.append("morango")

# Exibe a lista depois da inclusão.
print(frutas)


# Saída esperada:
# ['maçã', 'banana', 'laranja', 'morango']


# ============================================================
# Exercício 2 — Pilha de livros
# Objetivo: simular uma pilha e compreender LIFO
# (Last In, First Out).
# ============================================================

livros = []

# Os livros são inseridos um após o outro.
livros.append("O Pequeno Príncipe")
livros.append("Dom Quixote")
livros.append("1984")

# pop() remove o último livro inserido, seguindo LIFO.
livro_removido = livros.pop()

print(f"Livro removido: {livro_removido}")
print(f"Pilha restante: {livros}")


# Saída esperada:
# Livro removido: 1984
# Pilha restante: ['O Pequeno Príncipe', 'Dom Quixote']


# ============================================================
# Exercício 3 — Fila de clientes
# Objetivo: simular uma fila e compreender FIFO
# (First In, First Out).
# ============================================================

clientes = []

# Os clientes entram na fila na ordem em que chegam.
clientes.append("Ana")
clientes.append("Bruno")
clientes.append("Carla")
clientes.append("Daniel")

# pop(0) remove o primeiro cliente, simulando o atendimento.
cliente_saiu = clientes.pop(0)

print(f"Cliente que saiu: {cliente_saiu}")
print(f"Fila restante: {clientes}")


# Saída esperada:
# Cliente que saiu: Ana
# Fila restante: ['Bruno', 'Carla', 'Daniel']


# ============================================================
# Exercício 4 — Dicionário de contatos
# Objetivo: armazenar e recuperar dados por meio de
# pares chave-valor.
# ============================================================

contatos = {
    "Ana": "1234-5678",
    "Bruno": "9876-5432"
}

# Adiciona um novo contato utilizando o nome como chave.
contatos["Carlos"] = "1122-3344"

# Acessa o telefone de Ana pela chave correspondente.
print("Telefone da Ana:")
print(contatos["Ana"])


# Saída esperada:
# Telefone da Ana:
# 1234-5678


# ============================================================
# Projeto 1 — A Agenda de Contatos
# Objetivo: usar um dicionário para armazenar, buscar e
# listar dados de contatos.
# ============================================================

# Dicionário que mantém todos os contatos cadastrados.
contatos = {}


def adicionar_contato(nome, telefone, email):
    # Cada nome funciona como chave e seus dados ficam agrupados
    # em outro dicionário com telefone e e-mail.
    contatos[nome] = {
        "telefone": telefone,
        "email": email
    }

    print(f"Contato {nome} adicionado com sucesso!")


def buscar_contato(nome):
    # Verifica primeiro se o nome existe para evitar acesso
    # a uma chave que não foi cadastrada.
    if nome in contatos:
        print(f"Informações de {nome}:")
        print(f" Telefone: {contatos[nome]['telefone']}")
        print(f" E-mail: {contatos[nome]['email']}")
    else:
        # Informa quando não existe contato com o nome pesquisado.
        print(f"Contato {nome} não encontrado.")


def listar_contatos():
    # Percorre todos os pares nome/dados armazenados no dicionário.
    print("\nLista de contatos:")

    for nome, info in contatos.items():
        print(
            f"Nome: {nome}, "
            f"Telefone: {info['telefone']}, "
            f"E-mail: {info['email']}"
        )


# Exemplo de uso das funções da agenda.
adicionar_contato("Ana", "1234-5678", "ana@email.com")
adicionar_contato("Bruno", "9876-5432", "bruno@email.com")
buscar_contato("Ana")
listar_contatos()


# Saída esperada:
# Contato Ana adicionado com sucesso!
# Contato Bruno adicionado com sucesso!
# Informações de Ana:
#  Telefone: 1234-5678
#  E-mail: ana@email.com
#
# Lista de contatos:
# Nome: Ana, Telefone: 1234-5678, E-mail: ana@email.com
# Nome: Bruno, Telefone: 9876-5432, E-mail: bruno@email.com


# ============================================================
# Projeto 2 — A Lista de Tarefas
# Objetivo: usar uma lista para adicionar tarefas, concluir
# itens e visualizar as tarefas pendentes.
# ============================================================

tarefas = [
    "Lavar a louça",
    "Estudar para a prova",
    "Fazer compras"
]


def adicionar_tarefa(tarefa):
    # Adiciona uma nova tarefa ao final da lista de pendências.
    tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada.")


def marcar_concluida(tarefa):
    # Verifica se a tarefa existe antes de tentar removê-la.
    if tarefa in tarefas:
        # A remoção representa a conclusão da tarefa.
        tarefas.remove(tarefa)
        print(f"Tarefa '{tarefa}' marcada como concluída.")
    else:
        # Informa quando a tarefa não está entre as pendências.
        print(f"Tarefa '{tarefa}' não encontrada na lista.")


def visualizar_tarefas():
    # Percorre somente as tarefas que ainda estão pendentes.
    print("\nLista de tarefas pendentes:")

    for tarefa in tarefas:
        print(f"- {tarefa}")


# Exemplo de uso da lista de tarefas.
adicionar_tarefa("Pagar as contas")
marcar_concluida("Lavar a louça")
visualizar_tarefas()


# Saída esperada:
# Tarefa 'Pagar as contas' adicionada.
# Tarefa 'Lavar a louça' marcada como concluída.
#
# Lista de tarefas pendentes:
# - Estudar para a prova
# - Fazer compras
# - Pagar as contas
