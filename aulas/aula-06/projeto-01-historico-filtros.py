import pandas as pd


class HistoricoOperacoes:
    def __init__(self, dataframe):
        self.estado_atual = dataframe.copy()
        self.pilha_estados = []

    def aplicar_filtro(self, condicao):
        self.pilha_estados.append(self.estado_atual.copy())
        self.estado_atual = self.estado_atual.loc[condicao].copy()

    def desfazer(self):
        if not self.pilha_estados:
            print("Nenhum estado anterior para desfazer.")
            return False

        self.estado_atual = self.pilha_estados.pop()
        return True

    def mostrar(self):
        print(self.estado_atual.to_string(index=False))


if __name__ == "__main__":
    df = pd.DataFrame({
        "produto": ["Notebook", "Mouse", "Monitor", "Teclado"],
        "vendas": [3200, 800, 2100, 1200],
    })

    historico = HistoricoOperacoes(df)

    historico.aplicar_filtro(historico.estado_atual["vendas"] >= 1000)
    print("Após o filtro:")
    historico.mostrar()

    historico.desfazer()
    print("\nApós desfazer:")
    historico.mostrar()
