from financeiro.lancamento import Lancamento
from financeiro.categoria_receita import CategoriaReceita


class Receita(Lancamento):

    def __init__(self, categoria: CategoriaReceita, valor: int, data: str) -> None:
        super().__init__(categoria, valor, data)

    def impacto_no_saldo(self) -> int:
        return self.valor