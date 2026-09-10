class Animal:
    def fazer_som(self):
        print("Algum som")


class Cachorro(Animal):
    def fazer_som(self):
        print("Au Au")


class Gato(Animal):
    def fazer_som(self):
        print("Miau")


a = Animal()
c = Cachorro()
g = Gato()

a.fazer_som()
c.fazer_som()
g.fazer_som()
