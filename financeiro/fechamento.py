from financeiro.lancamento import Lancamento
from financeiro.receita import Receita
from financeiro.despesa import Despesa
from financeiro.categoria import Categoria


class Fechamento:

    def __init__(self, data_fechamento: str, lancamentos: list[Lancamento]) -> None:
        self.data_fechamento = data_fechamento
        self.lancamentos = list(lancamentos)

        self.total_receitas = sum(
            l.valor for l in self.lancamentos if isinstance(l, Receita)
        )
        self.total_despesas = sum(
            l.valor for l in self.lancamentos if isinstance(l, Despesa)
        )
        self.saldo_final = self.total_receitas - self.total_despesas

    def calcular_saldo_consolidado(self) -> int:
        return sum(i.impacto_no_saldo() for i in self.lancamentos)

    def calcular_total_por_categoria(self, categoria_escolhida: Categoria) -> int:
        lancamentos_filtrados = [
            i for i in self.lancamentos if i.categoria == categoria_escolhida
        ]
        return sum(i.impacto_no_saldo() for i in lancamentos_filtrados)
