# Projeto 1 — Rede social: amigos e amigos em comum
# Cada pessoa é um vértice; amizade é uma aresta não direcionada.
# Amigos em comum = interseção das duas listas de vizinhos.


rede = {}

def adicionar_pessoa(nome):
    # Cria a pessoa na rede se ela ainda não existe.
    rede.setdefault(nome, [])

def criar_amizade(p1, p2):
    # Amizade vale nos dois sentidos.
    rede.setdefault(p1, []).append(p2)
    rede.setdefault(p2, []).append(p1)

def amigos(nome):
    return rede.get(nome, [])

def amigos_em_comum(p1, p2):
    # Amigo em comum é quem aparece nas duas listas.
    return [a for a in rede.get(p1, []) if a in rede.get(p2, [])]


if __name__ == "__main__":
    for nome in ["Ana", "Bruno", "Carla", "Diego"]:
        adicionar_pessoa(nome)

    criar_amizade("Ana", "Bruno")
    criar_amizade("Ana", "Carla")
    criar_amizade("Bruno", "Diego")
    criar_amizade("Carla", "Diego")

    print("Amigos de Ana:", amigos("Ana"))
    print("Amigos em comum entre Ana e Diego:", amigos_em_comum("Ana", "Diego"))
