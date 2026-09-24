# Exercício 4 — Polimorfismo
# A função faz a mesma chamada para objetos diferentes, cada um com seu comportamento.

class Cachorro:
    def emitir_som(self):
        return "O cachorro late."


class Gato:
    def emitir_som(self):
        return "O gato mia."


def fazer_animal_emitir_som(animal):
    # Não importa a classe concreta; basta que o objeto possua emitir_som().
    print(animal.emitir_som())


if __name__ == "__main__":
    fazer_animal_emitir_som(Cachorro())
    fazer_animal_emitir_som(Gato())
