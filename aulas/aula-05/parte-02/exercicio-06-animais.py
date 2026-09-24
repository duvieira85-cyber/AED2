# Exercício 6 — Herança e polimorfismo
# Classes filhas reutilizam a estrutura de Animal e implementam sons específicos.

class Animal:
    def emitir_som(self):
        # Comportamento genérico que será sobrescrito pelas subclasses.
        return "Som de animal"


class Cachorro(Animal):
    def emitir_som(self):
        # Implementação específica para cachorro.
        return "Au au!"


class Gato(Animal):
    def emitir_som(self):
        # Implementação específica para gato.
        return "Miau!"


def mostrar_som(animal):
    # A mesma função funciona com qualquer objeto compatível com a interface esperada.
    print(animal.emitir_som())


if __name__ == "__main__":
    mostrar_som(Cachorro())
    mostrar_som(Gato())
