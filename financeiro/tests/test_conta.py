from financeiro.conta import Conta
from financeiro.categoria_despesa import CategoriaDespesa, NomeCategoriaDespesa
from financeiro.categoria_receita import CategoriaReceita, NomeCategoriaReceita
from financeiro.despesa import Despesa
from financeiro.receita import Receita


class TestConta:

    def setup_method(self) -> None:
        self.cat_alimentacao = CategoriaDespesa(
            nome=NomeCategoriaDespesa.ALIMENTACAO, gasto_max=500
        )
        self.cat_internet = CategoriaDespesa(
            nome=NomeCategoriaDespesa.INTERNET, gasto_max=500
        )
        self.cat_salario = CategoriaReceita(nome=NomeCategoriaReceita.SALARIO)
        self.conta = Conta()

    def test_conta_inicial_vazia(self) -> None:
        assert self.conta.calcular_total_lancamentos() == 0
        assert len(self.conta.lancamentos) == 0

    def test_adiciona_lancamento_a_listagem(self) -> None:
        d1 = Despesa(self.cat_alimentacao, 400, "2026-08-20")
        self.conta.adicionar_lancamento(d1)
        assert len(self.conta.lancamentos) == 1

    def test_calcula_saldo_total(self) -> None:
        d1 = Despesa(self.cat_alimentacao, 400, "2026-08-20")
        r1 = Receita(self.cat_salario, 1200, "2026-08-21")
        self.conta.adicionar_lancamento(d1)
        self.conta.adicionar_lancamento(r1)

        assert self.conta.calcular_total_lancamentos() == 800

    def test_total_por_categoria(self) -> None:
        d1 = Despesa(self.cat_alimentacao, 400, "2026-08-20")
        d2 = Despesa(self.cat_alimentacao, 200, "2026-08-20")
        self.conta.adicionar_lancamento(d1)
        self.conta.adicionar_lancamento(d2)

        assert (
            self.conta.calcular_total_lancamentos_por_categoria(self.cat_alimentacao)
            == -600
        )

    def test_listagem_por_categoria(self) -> None:
        d1 = Despesa(self.cat_alimentacao, 400, "2026-08-20")
        d2 = Despesa(self.cat_internet, 200, "2026-08-20")
        self.conta.adicionar_lancamento(d1)
        self.conta.adicionar_lancamento(d2)

        lancamentos_alimentacao = self.conta.listar_lancamento_por_categoria(
            self.cat_alimentacao
        )

        assert len(lancamentos_alimentacao) == 1
        assert d1 in lancamentos_alimentacao
        assert d2 not in lancamentos_alimentacao

    def test_categoria_vazia(self) -> None:
        assert self.conta.listar_lancamento_por_categoria(self.cat_internet) == []
        assert (
            self.conta.calcular_total_lancamentos_por_categoria(self.cat_internet) == 0
        )

    def test_excedeu_gasto_max(self) -> None:
        d1 = Despesa(self.cat_alimentacao, 300, "2026-08-21")
        self.conta.adicionar_lancamento(d1)
        assert self.conta.excedeu_gasto_max(self.cat_alimentacao) is False

        d2 = Despesa(self.cat_alimentacao, 250, "2026-08-21")
        self.conta.adicionar_lancamento(d2)
        assert self.conta.excedeu_gasto_max(self.cat_alimentacao) is True

    def test_excedeu_gasto_max_com_categoria_invalida(self) -> None:
        try:
            self.conta.excedeu_gasto_max(self.cat_salario)
            assert False, "Deveria ter lançado exceção"
        except ValueError:
            pass
