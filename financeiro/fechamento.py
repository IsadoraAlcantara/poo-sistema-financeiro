from financeiro.categoria import Categoria
from financeiro.lancamento import Lancamento


class Fechamento:

    def __init__(self, data_fechamento: str, lancamentos: list[Lancamento]) -> None:
        self.data_fechamento = data_fechamento
        self.lancamentos = list(lancamentos)

    @property
    def saldo_final_consolidado(self) -> float:
        return sum(l.valor for l in self.lancamentos)

    @property
    def total_receitas(self) -> float:
        return sum(l.valor for l in self.lancamentos if l.valor > 0)

    @property
    def total_despesas(self) -> float:
        return sum(l.valor for l in self.lancamentos if l.valor < 0)

    def calcular_total_por_categoria(self, categoria_escolhida: Categoria) -> int:
        lancamentos_filtrados = [
            i for i in self.lancamentos if i.categoria == categoria_escolhida
        ]
        return sum(i.valor for i in lancamentos_filtrados)
