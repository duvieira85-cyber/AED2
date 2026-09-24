# Exercício 4 — Dicionário de contatos
# Um dicionário armazena dados no formato chave-valor.
# Neste exemplo, o nome do contato é a chave e o telefone é o valor.

contatos = {
    "Ana": "1199999-1111",
    "Bruno": "1199999-2222"
}

# Adiciona Carlos usando seu nome como nova chave.
contatos["Carlos"] = "1199999-3333"

# Acessa o telefone de Ana diretamente pela chave "Ana".
print("Telefone da Ana:", contatos["Ana"])

# Exibe todos os contatos armazenados.
print("Contatos:", contatos)
