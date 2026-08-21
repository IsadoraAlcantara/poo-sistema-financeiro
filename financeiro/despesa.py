from financeiro.lancamento import Lancamento
from financeiro.categoriaDespesa import CategoriaDespesa


class Despesa(Lancamento):

    def __init__(self, categoria: CategoriaDespesa, valor: int, date: str) -> None:
        super().__init__(categoria, valor, date)

    def impacto_no_saldo(self) -> int:
        return -self.valor

    def alterar_valor(self, novo_valor) -> None:
        if novo_valor <= 0:
            raise ValueError("O valor de um lançamento não pode ser zero ou negativo")
        self._valor = novo_valor

    def alterar_categoria(self, nova_categoria: CategoriaDespesa) -> None:
        self.categoria = nova_categoria