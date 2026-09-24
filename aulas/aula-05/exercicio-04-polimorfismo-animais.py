# Exercício 4 — Polimorfismo
# A mesma função pode trabalhar com objetos de classes diferentes.
# Cada objeto responde à chamada emitir_som() de acordo com sua própria classe.


class Cachorro:
    def emitir_som(self):
        # Implementação específica para um cachorro.
        return "O cachorro late."


class Gato:
    def emitir_som(self):
        # Implementação específica para um gato.
        return "O gato mia."


def fazer_animal_emitir_som(animal):
    # A função não precisa saber qual é a classe concreta.
    # Basta que o objeto disponibilize o método emitir_som().
    print(animal.emitir_som())


if __name__ == "__main__":
    # A mesma função é utilizada com dois tipos de objeto.
    fazer_animal_emitir_som(Cachorro())
    fazer_animal_emitir_som(Gato())
