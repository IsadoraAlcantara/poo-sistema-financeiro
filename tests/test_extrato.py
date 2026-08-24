from financeiro.fechamento import Fechamento
from financeiro.extrato import Extrato
from financeiro.despesa import Despesa
from financeiro.receita import Receita
from financeiro.categoria_despesa import CategoriaDespesa, NomeCategoriaDespesa
from financeiro.categoria_receita import CategoriaReceita, NomeCategoriaReceita


class TestExtrato:

    def setup_method(self) -> None:
        self.cat_alimentacao = CategoriaDespesa(NomeCategoriaDespesa.ALIMENTACAO, 1000)
        self.cat_salario = CategoriaReceita(NomeCategoriaReceita.SALARIO)

        julho = [Despesa(self.cat_alimentacao, 200, "2026-07-01")]
        self.fechamento_julho = Fechamento("2026-07-31", julho)

        agosto = [Despesa(self.cat_alimentacao, 150, "2026-08-01")]
        self.fechamento_agosto = Fechamento("2026-08-31", agosto)

        self.todos_fechamentos = [
            self.fechamento_julho,
            self.fechamento_agosto,
        ]

    def test_filtra_fechamentos(self):
        extrato_agosto = Extrato(
            data_inicio="2026-08-01",
            data_fim="2026-08-31",
            fechamentos_totais=self.todos_fechamentos,
        )

        assert len(extrato_agosto.fechamentos_filtrados) == 1
        assert self.fechamento_agosto in extrato_agosto.fechamentos_filtrados
        assert self.fechamento_julho not in extrato_agosto.fechamentos_filtrados

        assert extrato_agosto.total_receitas == 0
        assert extrato_agosto.total_despesas == 150
        assert extrato_agosto.saldo_final == -150
        assert extrato_agosto.total_lancamentos == 1

    def test_periodo_sem_fechamentos_retorna_zero(self):
        extrato_vazio = Extrato(
            data_inicio="2026-10-01",
            data_fim="2026-10-31",
            fechamentos_totais=self.todos_fechamentos,
        )

        assert len(extrato_vazio.fechamentos_filtrados) == 0
        assert extrato_vazio.total_receitas == 0
        assert extrato_vazio.total_despesas == 0
        assert extrato_vazio.saldo_final == 0
        assert extrato_vazio.total_lancamentos == 0
