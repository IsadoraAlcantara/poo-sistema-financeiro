from datetime import date
from financeiro.estrategia_rendimento import CDB, Poupanca


class TestCDB:

    def test_instancia_com_percentual_zerado(self) -> None:
        try:
            CDB(
                percentual=0,
                data_inicial=date(2019, 10, 8),
                data_final=date(2024, 10, 8),
                cdi_ano=100,
            )
            assert False, "Deveria ter lançado exceção"
        except ValueError:
            pass

    def test_instancia_com_data_final_anterior_a_data_inicial(self) -> None:
        try:
            CDB(
                percentual=100,
                data_inicial=date(2019, 10, 8),
                data_final=date(2018, 10, 8),
                cdi_ano=100,
            )
            assert False, "Deveria ter lançado exceção"
        except ValueError:
            pass

    def test_contar_dias_uteis(self) -> None:
        carteira = CDB(
            percentual=100,
            data_inicial=date(2025, 10, 8),
            data_final=date(2026, 10, 8),
            cdi_ano=11.777,
        )
        assert carteira.contar_dias_uteis() == 261

    def test_calcular(self) -> None:
        carteira = CDB(
            percentual=100,
            data_inicial=date(2024, 1, 1),
            data_final=date(2024, 2, 1),
            cdi_ano=12,
        )
        assert round(carteira.calcular(1000), 2) == 1010.4


class TestPoupanca:

    def test_selic_anual_zerado(self) -> None:
        try:
            Poupanca(
                selic_anual=0,
                data_inicial=date(2019, 10, 8),
                data_final=date(2024, 10, 8),
            )
            assert False, "Deveria ter lançado exceção"
        except ValueError:
            pass

    def test_instancia_com_data_final_anterior_a_data_inicial(self) -> None:
        try:
            Poupanca(
                selic_anual=7.6,
                data_inicial=date(2019, 10, 8),
                data_final=date(2018, 10, 8),
            )
            assert False, "Deveria ter lançado exceção"
        except ValueError:
            pass

    def test_meses_decorridos(self) -> None:
        poupanca = Poupanca(
            selic_anual=7.6,
            data_inicial=date(2019, 10, 8),
            data_final=date(2020, 10, 8),
        )
        assert (
            poupanca.meses_decorridos(inicio=date(2019, 10, 8), fim=date(2020, 10, 8))
            == 12
        )

    def test_calcular(self) -> None:
        poupanca_selic_alto = Poupanca(
            selic_anual=10.5,
            data_inicial=date(2024, 1, 10),
            data_final=date(2024, 7, 10),
        )
        poupanca_selic_baixo = Poupanca(
            selic_anual=8.0,
            data_inicial=date(2024, 1, 15),
            data_final=date(2025, 1, 15),
        )
        assert round(poupanca_selic_alto.calcular(1000), 2) == 1030.38
        assert round(poupanca_selic_baixo.calcular(1000), 2) == 1056.00
