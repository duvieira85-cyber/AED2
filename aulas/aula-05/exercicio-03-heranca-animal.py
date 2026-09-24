# Exercício 3 — Herança
# Demonstra herança e sobrescrita de método.
# Cachorro herda de Animal e fornece uma implementação específica
# para o comportamento de emitir som.


class Animal:
    def emitir_som(self):
        # Método definido na classe base com um comportamento genérico.
        return "O animal emite um som."


class Cachorro(Animal):
    def emitir_som(self):
        # A classe filha sobrescreve o método herdado
        # para fornecer um comportamento específico.
        return "O cachorro late."


if __name__ == "__main__":
    # Cria um objeto Cachorro. Ele possui o comportamento definido
    # na própria classe para emitir som.
    cachorro = Cachorro()

    print(cachorro.emitir_som())
