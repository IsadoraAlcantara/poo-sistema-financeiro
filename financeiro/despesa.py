from financeiro.lancamento import Lancamento


class Despesa(Lancamento):

    def __init__(self, categoria: CategoriaDespesa, valor, date) -> None:
        super().__init__(categoria, valor, date)

    def alterar_valor(self, novo_valor) -> None:
        if novo_valor <= 0:
            raise ValueError("O valor de um lançamento não pode ser zero ou negativo")
        self._valor = novo_valor

    def alterar_categoria(self, nova_categoria: CategoriaDespesa) -> None:
        self.categoria = nova_categoria