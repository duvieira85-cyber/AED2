# Exercício 7 — Veículo com velocidade controlada
# A velocidade atual e a velocidade máxima são controladas
# pelos métodos da classe.


class Veiculo:
    def __init__(self, placa, velocidade_max):
        self.__placa = placa
        self.__velocidade_max = 0
        self.__velocidade_atual = 0

        # Usamos o setter para validar a velocidade máxima.
        self.set_velocidade_max(velocidade_max)

    def get_placa(self):
        return self.__placa

    def get_velocidade_max(self):
        return self.__velocidade_max

    def set_velocidade_max(self, velocidade_max):
        # A nova máxima deve ser positiva.
        # Ela também não pode ficar abaixo da velocidade atual.
        if velocidade_max > 0 and velocidade_max >= self.__velocidade_atual:
            self.__velocidade_max = velocidade_max

    def acelerar(self, incremento=10):
        if incremento > 0:
            self.__velocidade_atual += incremento

            # Não podemos ultrapassar a velocidade máxima.
            if self.__velocidade_atual > self.__velocidade_max:
                self.__velocidade_atual = self.__velocidade_max

    def frear(self, decremento=10):
        if decremento > 0:
            self.__velocidade_atual -= decremento

            # A velocidade nunca pode ficar negativa.
            if self.__velocidade_atual < 0:
                self.__velocidade_atual = 0

    def __str__(self):
        return (
            f"Placa: {self.__placa} | "
            f"Velocidade: {self.__velocidade_atual} km/h | "
            f"Máxima: {self.__velocidade_max} km/h"
        )


if __name__ == "__main__":
    veiculo = Veiculo("ABC-1234", 100)

    print(veiculo)

    veiculo.acelerar()
    veiculo.acelerar(30)
    print(veiculo)

    veiculo.frear(20)
    print(veiculo)

    veiculo.frear(50)
    print(veiculo)
