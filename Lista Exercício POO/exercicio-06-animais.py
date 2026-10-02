# Exercício 6 — Animais: herança e polimorfismo
# Cachorro e Gato são animais.
# Os dois possuem o método emitir_som(), mas cada um faz uma coisa diferente.


class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        return ""


class Cachorro(Animal):
    def emitir_som(self):
        return "au au"


class Gato(Animal):
    def emitir_som(self):
        return "miau"


if __name__ == "__main__":
    cachorro = Cachorro("Rex")
    gato = Gato("Mimi")

    animais = [cachorro, gato]

    # Não precisamos testar se é cachorro ou gato.
    # Apenas chamamos o mesmo método.
    for animal in animais:
        print(animal.nome, ":", animal.emitir_som())
