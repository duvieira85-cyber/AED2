class Animal:
    def fazer_som(self):
        print("Algum som")


class Cachorro(Animal):
    def fazer_som(self):
        print("Au Au")


class Gato(Animal):
    def fazer_som(self):
        print("Miau")


def animais_falam(lista_animais):
    for animal in lista_animais:
        animal.fazer_som()


lista_animais = [Cachorro(), Gato(), Cachorro()]
animais_falam(lista_animais)
