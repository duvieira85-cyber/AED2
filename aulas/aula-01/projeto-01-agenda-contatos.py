# Projeto 1 — A Agenda de Contatos
# Utiliza um dicionário para armazenar, buscar e listar contatos.
# O nome funciona como chave e os dados do contato ficam associados a ele.


# Dicionário principal que armazena todos os contatos cadastrados.
contatos = {}


def adicionar_contato(nome, telefone, email):
    # Cria ou atualiza o contato usando o nome como chave.
    contatos[nome] = {
        "telefone": telefone,
        "email": email
    }

    print(f"Contato {nome} adicionado com sucesso!")


def buscar_contato(nome):
    # Verifica se o nome existe antes de acessar seus dados.
    if nome in contatos:
        print(f"Informações de {nome}:")
        print(f" Telefone: {contatos[nome]['telefone']}")
        print(f" E-mail: {contatos[nome]['email']}")
    else:
        # Informa quando o contato pesquisado não está cadastrado.
        print(f"Contato {nome} não encontrado.")


def listar_contatos():
    # Percorre todos os contatos armazenados no dicionário.
    print("\nLista de contatos:")

    for nome, info in contatos.items():
        print(
            f"Nome: {nome}, "
            f"Telefone: {info['telefone']}, "
            f"E-mail: {info['email']}"
        )


# Exemplo de uso das operações da agenda.
adicionar_contato("Ana", "1234-5678", "ana@email.com")
adicionar_contato("Bruno", "9876-5432", "bruno@email.com")
buscar_contato("Ana")
listar_contatos()
