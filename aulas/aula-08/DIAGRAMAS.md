# Aula 08 — Guia visual das referências

## Lista simplesmente encadeada

`head` aponta para o primeiro nó:

`head -> [1] -> [2] -> [3] -> None`

Cada nó possui:
- `data`: valor armazenado.
- `next`: referência para o próximo nó.

## Inserção na cabeça

Antes:

`head -> [1] -> [2] -> None`

Depois de `add_head(3)`:

`head -> [3] -> [1] -> [2] -> None`

O ponto principal é executar primeiro:

`new_node.next = self.head`

e somente depois:

`self.head = new_node`

## Remoção no meio

Antes:

`[5] -> [7] -> [9] -> [11]`

Removendo 9:

`[5] -> [7] --------> [11]`

O 7 passa a apontar diretamente para 11.

## Reversão

Original:

`[1] -> [2] -> [3] -> None`

Invertida:

`[3] -> [2] -> [1] -> None`

Durante a reversão, `next_node` preserva o restante da cadeia antes de alterar `current.next`.

## Lista duplamente encadeada

Cada nó conhece os dois vizinhos:

`None <- [A] <-> [B] <-> [C] -> None`

- `next`: caminha para frente.
- `prev`: caminha para trás.
- `head`: primeiro nó.
- `tail`: último nó.
- Um ponteiro adicional como `current` identifica o elemento ativo.
