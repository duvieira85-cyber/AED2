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


animais = [
    Cachorro("Rex"),
    Gato("Mimi")
]

for animal in animais:
    print(f"{animal.nome}: {animal.emitir_som()}")
