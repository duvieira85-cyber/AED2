# Aula 01 — Exercícios resolvidos
# Estrutura de Dados com Python — Capítulo 1
# Prof. Dr. Dilermando Piva Jr.

# ============================================================
# Exercício 1 — Lista de frutas
# Objetivo: criar uma lista, adicionar um elemento ao final
# e imprimir o resultado.
# ============================================================

frutas = ["maçã", "banana", "laranja"]
frutas.append("morango")
print(frutas)


# Saída esperada:
# ['maçã', 'banana', 'laranja', 'morango']


# ============================================================
# Exercício 2 — Pilha de livros
# Objetivo: simular uma pilha e compreender LIFO
# (Last In, First Out).
# ============================================================

livros = []
livros.append("O Pequeno Príncipe")
livros.append("Dom Quixote")
livros.append("1984")
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
clientes.append("Ana")
clientes.append("Bruno")
clientes.append("Carla")
clientes.append("Daniel")
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

contatos["Carlos"] = "1122-3344"

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

contatos = {}


def adicionar_contato(nome, telefone, email):
    contatos[nome] = {
        "telefone": telefone,
        "email": email
    }
    print(f"Contato {nome} adicionado com sucesso!")


def buscar_contato(nome):
    if nome in contatos:
        print(f"Informações de {nome}:")
        print(f" Telefone: {contatos[nome]['telefone']}")
        print(f" E-mail: {contatos[nome]['email']}")
    else:
        print(f"Contato {nome} não encontrado.")


def listar_contatos():
    print("\nLista de contatos:")
    for nome, info in contatos.items():
        print(
            f"Nome: {nome}, "
            f"Telefone: {info['telefone']}, "
            f"E-mail: {info['email']}"
        )


# Exemplo de uso
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
    tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada.")


def marcar_concluida(tarefa):
    if tarefa in tarefas:
        tarefas.remove(tarefa)
        print(f"Tarefa '{tarefa}' marcada como concluída.")
    else:
        print(f"Tarefa '{tarefa}' não encontrada na lista.")


def visualizar_tarefas():
    print("\nLista de tarefas pendentes:")
    for tarefa in tarefas:
        print(f"- {tarefa}")


# Exemplo de uso
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
