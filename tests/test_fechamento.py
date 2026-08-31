from financeiro.fechamento import Fechamento
from financeiro.despesa import Despesa
from financeiro.receita import Receita
from financeiro.categoria_despesa import CategoriaDespesa, NomeCategoriaDespesa
from financeiro.categoria_receita import CategoriaReceita, NomeCategoriaReceita
from financeiro.conta import Conta


class TestFechamento:

    def setup_method(self):
        self.cat_salario = CategoriaReceita(NomeCategoriaReceita.SALARIO)
        self.cat_transporte = CategoriaDespesa(NomeCategoriaDespesa.TRANSPORTE, 1000)
        self.cat_alimentacao = CategoriaDespesa(NomeCategoriaDespesa.ALIMENTACAO, 1000)

        self.d1 = Despesa(self.cat_alimentacao, 300, "2026-08-20")
        self.d2 = Despesa(self.cat_transporte, 700, "2026-08-20")
        self.r1 = Receita(self.cat_salario, 1200, "2026-08-21")

        self.fechamento = Fechamento(
            data_fechamento="2026-08-31", lancamentos=[self.d1, self.d2, self.r1]
        )

    def test_saldo_final_consolidado(self):
        assert self.fechamento.saldo_final_consolidado == 200

    def test_total_receita(self):
        assert self.fechamento.total_receitas == 1200

    def test_total_despesa(self):
        assert self.fechamento.total_despesas == -1000

    def test_total_por_categoria(self):
        assert self.fechamento.calcular_total_por_categoria(self.cat_alimentacao) == -300

    def test_fechamento_vazio(self):
        fechamento_vazio = Fechamento("2026-08-31", [])
        assert fechamento_vazio.saldo_final_consolidado == 0
        assert fechamento_vazio.total_receitas == 0
        assert fechamento_vazio.total_despesas == 0
