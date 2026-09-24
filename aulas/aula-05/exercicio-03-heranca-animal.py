# Exercício 3 — Herança
# Cachorro herda características de Animal e sobrescreve o comportamento de emitir som.

class Animal:
    def emitir_som(self):
        # Método genérico da classe base.
        return "O animal emite um som."


class Cachorro(Animal):
    def emitir_som(self):
        # Sobrescreve o método da classe pai com um comportamento específico.
        return "O cachorro late."


if __name__ == "__main__":
    cachorro = Cachorro()
    print(cachorro.emitir_som())
