from datetime import date
from financeiro.aplicacao import Aplicacao
from financeiro.estrategia_rendimento import EstrategiaRendimento, CDB, Poupanca


class TestAplicacao:

    def setup_method(self) -> None:
        self.cdb = CDB(
            percentual=100,
            cdi_ano=12,
        )

        self.poupanca = Poupanca(
            selic_anual=7.5,
        )

    def test_valor_investido_nulo(self) -> None:
        try:
            Aplicacao(valor=0, data_inicial=date(2019, 8, 10), data_final=date(2020, 8, 10), estrategia=self.cdb)
            assert False, "Deveria ter lançado excessão"
        except ValueError:
            pass

    def test_instancia_com_data_inicio_posterior_a_data_fim(self) -> None:
        try:
            Aplicacao(valor=1000, data_inicial=date(2019, 8, 10), data_final=date(2018, 8, 10), estrategia=self.cdb)
            assert False, "Deveria ter lançado excessão"
        except ValueError:
            pass

    def test_calcular_valor_total(self) -> None:
        aplicacao = Aplicacao(valor=1000, data_inicial=date(2024, 1, 1), data_final=date(2024, 2, 1), estrategia=self.cdb)
        assert round(aplicacao.calcular_valor_total(), 2) == 1010.4

    def test_calcular_lucro(self) -> None:
        aplicacao = Aplicacao(valor=1000, data_inicial=date(2024, 1, 1), data_final=date(2024, 2, 1), estrategia=self.cdb)
        assert round(aplicacao.calcular_lucro(), 2) == 10.4