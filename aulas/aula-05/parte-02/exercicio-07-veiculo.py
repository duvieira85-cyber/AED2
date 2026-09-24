# Exercício 7 — Hierarquia de veículos
# Demonstra herança, atributos compartilhados e método sobrescrito.

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def apresentar(self):
        # Retorna a identificação básica do veículo.
        return f"{self.marca} {self.modelo}"


class Carro(Veiculo):
    def apresentar(self):
        # Adiciona a informação específica do tipo carro.
        return f"Carro: {super().apresentar()}"


class Moto(Veiculo):
    def apresentar(self):
        # Adiciona a informação específica do tipo moto.
        return f"Moto: {super().apresentar()}"


if __name__ == "__main__":
    print(Carro("Toyota", "Corolla").apresentar())
    print(Moto("Honda", "CB 500").apresentar())
