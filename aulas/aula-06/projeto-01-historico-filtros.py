# Projeto 1 — Histórico de filtros
# A pilha guarda cópias dos estados anteriores de um DataFrame.
# Isso permite implementar a operação de desfazer seguindo LIFO.


import pandas as pd


class HistoricoOperacoes:
    def __init__(self, dataframe):
        # Mantém uma cópia do estado inicial para não alterar
        # diretamente o DataFrame recebido pelo programa.
        self.estado_atual = dataframe.copy()

        # Cada item da pilha representa um estado anterior.
        self.pilha_estados = []

    def aplicar_filtro(self, condicao):
        # Salva o estado atual antes de aplicar uma nova alteração.
        # Assim, esse estado poderá ser recuperado pelo desfazer.
        self.pilha_estados.append(self.estado_atual.copy())

        # Cria o novo estado contendo somente as linhas que atendem à condição.
        self.estado_atual = self.estado_atual.loc[condicao].copy()

    def desfazer(self):
        # Sem estados anteriores, não existe operação para desfazer.
        if not self.pilha_estados:
            print("Nenhum estado anterior para desfazer.")
            return False

        # Recupera o estado mais recente salvo.
        # O último estado salvo é o primeiro a ser recuperado: LIFO.
        self.estado_atual = self.pilha_estados.pop()
        return True

    def mostrar(self):
        # Exibe o DataFrame atualmente ativo sem mostrar o índice.
        print(self.estado_atual.to_string(index=False))


if __name__ == "__main__":
    # Cria os dados utilizados no exemplo.
    df = pd.DataFrame({
        "produto": ["Notebook", "Mouse", "Monitor", "Teclado"],
        "vendas": [3200, 800, 2100, 1200],
    })

    # Cria o gerenciador responsável por manter o histórico.
    historico = HistoricoOperacoes(df)

    # Aplica um filtro e salva automaticamente o estado anterior.
    historico.aplicar_filtro(historico.estado_atual["vendas"] >= 1000)

    print("Após o filtro:")
    historico.mostrar()

    # Desfaz o último filtro recuperando o estado salvo na pilha.
    historico.desfazer()

    print("\nApós desfazer:")
    historico.mostrar()
