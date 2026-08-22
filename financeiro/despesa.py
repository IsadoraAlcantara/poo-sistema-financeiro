from financeiro.lancamento import Lancamento
from financeiro.categoria_despesa import CategoriaDespesa


class Despesa(Lancamento):

    def __init__(self, categoria: CategoriaDespesa, valor: int, data: str) -> None:
        super().__init__(categoria, valor, data)
        if not isinstance(categoria, CategoriaDespesa):
            raise TypeError("Uma despesa precisa ter uma categoria de despesa")

        if valor <= 0:
            raise ValueError("O valor da despesa deve ser maior que zero")

    def impacto_no_saldo(self) -> int:
        return -self.valor