from financeiro.lancamento import Lancamento
from financeiro.categoria_despesa import CategoriaDespesa


class Despesa(Lancamento):

    def __init__(self, categoria: CategoriaDespesa, valor: int, data: str) -> None:
        super().__init__(categoria, valor, data)

    def impacto_no_saldo(self) -> int:
        return -self.valor