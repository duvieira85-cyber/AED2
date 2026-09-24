# Projeto 1 — Histórico de filtros
# A pilha guarda cópias dos estados anteriores para permitir a operação de desfazer.

import pandas as pd


class HistoricoOperacoes:
    def __init__(self, dataframe):
        # Mantém uma cópia para que o DataFrame original não seja alterado diretamente.
        self.estado_atual = dataframe.copy()

        # Cada item da pilha representa um estado anterior do DataFrame.
        self.pilha_estados = []

    def aplicar_filtro(self, condicao):
        # Salva o estado atual antes de aplicar uma nova alteração.
        self.pilha_estados.append(self.estado_atual.copy())

        # Cria o novo estado somente com as linhas que atendem à condição.
        self.estado_atual = self.estado_atual.loc[condicao].copy()

    def desfazer(self):
        if not self.pilha_estados:
            print("Nenhum estado anterior para desfazer.")
            return False

        # Recupera o último estado salvo, seguindo o princípio LIFO.
        self.estado_atual = self.pilha_estados.pop()
        return True

    def mostrar(self):
        # Exibe o estado atual do DataFrame.
        print(self.estado_atual.to_string(index=False))


if __name__ == "__main__":
    df = pd.DataFrame({
        "produto": ["Notebook", "Mouse", "Monitor", "Teclado"],
        "vendas": [3200, 800, 2100, 1200],
    })

    historico = HistoricoOperacoes(df)

    # Aplica um filtro e guarda automaticamente o estado anterior.
    historico.aplicar_filtro(historico.estado_atual["vendas"] >= 1000)

    print("Após o filtro:")
    historico.mostrar()

    # Desfaz o último filtro recuperando o estado salvo na pilha.
    historico.desfazer()

    print("\nApós desfazer:")
    historico.mostrar()
