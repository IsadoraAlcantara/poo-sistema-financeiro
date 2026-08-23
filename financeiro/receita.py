from financeiro.lancamento import Lancamento
from financeiro.categoria_receita import CategoriaReceita


class Receita(Lancamento):

    def __init__(self, categoria: CategoriaReceita, valor: int, data: str) -> None:
        super().__init__(categoria, valor, data)
        if not isinstance(categoria, CategoriaReceita):
            raise TypeError("Uma receita precisa ter uma categoria de receita")

        if valor <= 0:
            raise ValueError("O valor da receita deve ser maior que zero")


    def impacto_no_saldo(self) -> int:
        return self.valor