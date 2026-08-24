from financeiro.conta import Conta
from financeiro.despesa import Despesa
from financeiro.categoria_despesa import CategoriaDespesa, NomeCategoriaDespesa
from financeiro.conciliacao import Conciliacao


class TestConciliacaoBancaria:

    def setup_method(self) -> None:
        self.cat_alimentacao = CategoriaDespesa(NomeCategoriaDespesa.ALIMENTACAO, 1000)
        self.cat_transporte = CategoriaDespesa(NomeCategoriaDespesa.TRANSPORTE, 500)

    def test_conciliacao_correta(self):
        aplicacao = Conta()
        aplicacao.adicionar_lancamento(Despesa(self.cat_alimentacao, 120, "2026-08-10"))
        aplicacao.adicionar_lancamento(Despesa(self.cat_alimentacao, 80, "2026-08-15"))

        extrato_banco = Conta()
        extrato_banco.adicionar_lancamento(
            Despesa(self.cat_alimentacao, 100, "2026-08-10")
        )
        extrato_banco.adicionar_lancamento(
            Despesa(self.cat_transporte, 100, "2026-08-15")
        )

        conciliador = Conciliacao(aplicacao.lancamentos, extrato_banco.lancamentos)

        assert conciliador.total_origem() == 200
        assert conciliador.total_destino() == 200
        assert conciliador.diferenca() == 0
        assert conciliador.validar() is True

    def test_conciliacao_falha(self):
        aplicacao = Conta()
        aplicacao.adicionar_lancamento(Despesa(self.cat_alimentacao, 100, "2026-08-10"))

        extrato_banco = Conta()
        extrato_banco.adicionar_lancamento(Despesa(self.cat_alimentacao, 140, "2026-08-10"))

        conciliador = Conciliacao(aplicacao.lancamentos, extrato_banco.lancamentos)

        try:
            conciliador.validar()
            assert False, "Deveria ter lançado ConciliacaoErro por divergência de valores"
        except ValueError:
            pass
