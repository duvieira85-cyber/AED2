class Veiculo:
    def __init__(self, placa, velocidade_max):
        self.__placa = placa
        self.__velocidade_max = velocidade_max
        self.__velocidade_atual = 0

    def get_placa(self):
        return self.__placa

    def get_velocidade_max(self):
        return self.__velocidade_max

    def set_velocidade_max(self, nova_maxima):
        if nova_maxima > 0 and nova_maxima >= self.__velocidade_atual:
            self.__velocidade_max = nova_maxima
            return True
        return False

    def acelerar(self, incremento=10):
        if incremento > 0:
            self.__velocidade_atual = min(
                self.__velocidade_atual + incremento,
                self.__velocidade_max
            )

    def frear(self, decremento=10):
        if decremento > 0:
            self.__velocidade_atual = max(
                self.__velocidade_atual - decremento,
                0
            )

    def __str__(self):
        return (
            f"Placa: {self.__placa} | "
            f"Velocidade: {self.__velocidade_atual} km/h | "
            f"Máxima: {self.__velocidade_max} km/h"
        )


veiculo = Veiculo("ABC1D23", 100)

print(veiculo)
veiculo.acelerar()
veiculo.acelerar(50)
print(veiculo)
veiculo.acelerar(100)
print(veiculo)
veiculo.frear(30)
veiculo.frear()
print(veiculo)
veiculo.set_velocidade_max(120)
print(veiculo)
