# Aula 01 — Introdução às Estruturas de Dados

**Fonte:** Prof. Dr. Dilermando Piva Jr. — *Estrutura de Dados com Python — Capítulo 1*.

> Material de estudo baseado no PDF fornecido para esta conversa. A fonte apresenta resoluções comentadas dos exercícios e projetos propostos do Capítulo 1.

## Visão geral

O capítulo trabalha as estruturas nativas do Python usadas nos primeiros exercícios: **listas** e **dicionários**. Pilhas e filas são simuladas com listas, enfatizando que a estrutura pode ser usada de formas diferentes conforme as operações realizadas.

### Atividades

| Atividade | Nível | Tema | Prática |
|---|---|---|---|
| 1 | Aquecimento | Lista Python | Criar lista, usar `append()` e exibir elementos |
| 2 | Aplicação | Pilha (LIFO) | `append()` e `pop()` |
| 3 | Aplicação | Fila (FIFO) | Inserção no final e `pop(0)` |
| 4 | Aplicação | Dicionário | Pares chave-valor |
| Projeto 1 | Projeto prático | Agenda de contatos | Dicionário aninhado, adicionar, buscar e listar |
| Projeto 2 | Projeto prático | Lista de tarefas | Adicionar, concluir e visualizar pendentes |

## Exercício 1 — Lista de frutas

Criar `frutas` com `maçã`, `banana` e `laranja`, adicionar `morango` ao final e imprimir a lista.

```python
frutas = ["maçã", "banana", "laranja"]
frutas.append("morango")
print(frutas)
```

**Saída esperada:**

```text
['maçã', 'banana', 'laranja', 'morango']
```

Ponto principal: `append()` acrescenta um elemento ao final da lista, preservando a sequência.

## Exercício 2 — Pilha de livros

A lista `livros` representa uma pilha. Os livros são adicionados nesta ordem: `O Pequeno Príncipe`, `Dom Quixote`, `1984`. O topo é o último elemento. `pop()` sem índice remove o último elemento, representando **LIFO — Last In, First Out**.

```python
livros = []
livros.append("O Pequeno Príncipe")
livros.append("Dom Quixote")
livros.append("1984")
livro_removido = livros.pop()
print(f"Livro removido: {livro_removido}")
print(f"Pilha restante: {livros}")
```

**Saída esperada:**

```text
Livro removido: 1984
Pilha restante: ['O Pequeno Príncipe', 'Dom Quixote']
```

## Exercício 3 — Fila de clientes

A lista `clientes` representa uma fila. São adicionados `Ana`, `Bruno`, `Carla` e depois `Daniel`. Para retirar o primeiro cliente, usa-se `pop(0)`, representando **FIFO — First In, First Out**.

```python
clientes = []
clientes.append("Ana")
clientes.append("Bruno")
clientes.append("Carla")
clientes.append("Daniel")
cliente_saiu = clientes.pop(0)
print(f"Cliente que saiu: {cliente_saiu}")
print(f"Fila restante: {clientes}")
```

**Saída esperada:**

```text
Cliente que saiu: Ana
Fila restante: ['Bruno', 'Carla', 'Daniel']
```

O capítulo destaca a diferença: `pop()` remove o último elemento quando a lista simula uma pilha; `pop(0)` remove o primeiro quando simula uma fila.

## Exercício 4 — Dicionário de contatos

Criar `contatos` com Ana e Bruno, adicionar Carlos e consultar o telefone de Ana. O nome é a chave e o telefone é o valor.

```python
contatos = {
    "Ana": "1234-5678",
    "Bruno": "9876-5432"
}
contatos["Carlos"] = "1122-3344"
print("Telefone da Ana:")
print(contatos["Ana"])
```

**Saída esperada:**

```text
Telefone da Ana:
1234-5678
```

O conceito central é a associação **chave-valor**, diferente da localização principalmente por posição usada nas listas.

## Projeto 1 — Agenda de contatos

Objetivo: armazenar, buscar e listar contatos contendo nome, telefone e e-mail.

A solução utiliza um dicionário externo cuja chave é o nome e cujo valor é outro dicionário com `telefone` e `email`.

```python
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

adicionar_contato("Ana", "1234-5678", "ana@email.com")
adicionar_contato("Bruno", "9876-5432", "bruno@email.com")
buscar_contato("Ana")
listar_contatos()
```

O projeto também introduz a ideia de **Tipo Abstrato de Dados**: quem utiliza a agenda se concentra nas operações disponíveis — adicionar, buscar e listar — enquanto os detalhes internos ficam na implementação.

## Projeto 2 — Lista de tarefas

Objetivo: adicionar tarefas, concluir itens e visualizar apenas as tarefas pendentes.

Nesta proposta, uma tarefa concluída é removida da lista de pendências.

```python
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

adicionar_tarefa("Pagar as contas")
marcar_concluida("Lavar a louça")
visualizar_tarefas()
```

**Saída esperada:**

```text
Tarefa 'Pagar as contas' adicionada.
Tarefa 'Lavar a louça' marcada como concluída.
Lista de tarefas pendentes:
- Estudar para a prova
- Fazer compras
- Pagar as contas
```

## Revisão

O capítulo forma uma sequência de aprendizagem:

1. Manipular uma lista diretamente.
2. Usar uma lista para simular uma pilha (LIFO).
3. Usar uma lista para simular uma fila (FIFO).
4. Trabalhar com pares chave-valor em dicionários.
5. Combinar estruturas e funções em uma agenda.
6. Adicionar e remover itens de uma sequência em uma lista de tarefas.

### Síntese

A ideia central é perceber que a forma de organizar os dados determina como eles podem ser acessados e manipulados. Listas, pilhas, filas e dicionários possuem comportamentos diferentes, e escolher a estrutura adequada faz parte do desenvolvimento de algoritmos eficientes.

## Fonte

Material fornecido para estudo: *Estrutura de Dados com Python — Capítulo 1 — Introdução às Estruturas de Dados*, Prof. Dr. Dilermando Piva Jr., 9 páginas.
