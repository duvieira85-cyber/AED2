# Projeto 1 — A Agenda de Contatos
# Usar um dicionário para armazenar, buscar e listar contatos.

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
