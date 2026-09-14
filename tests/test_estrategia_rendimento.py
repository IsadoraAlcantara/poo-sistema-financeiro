from datetime import date
from financeiro.estrategia_rendimento import (
    CDB,
    Poupanca,
    JurosCompostos,
    JurosSimples,
    IPCA,
)


class TestCDB:

    def test_instancia_com_percentual_zerado(self) -> None:
        try:
            CDB(
                percentual=0,
                cdi_ano=100,
            )
            assert False, "Deveria ter lançado exceção"
        except ValueError:
            pass

    def test_contar_dias_uteis(self) -> None:
        carteira = CDB(
            percentual=100,
            cdi_ano=11.777,
        )
        assert (
            carteira.contar_dias_uteis(
                data_inicial=date(2025, 10, 8),
                data_final=date(2026, 10, 8),
            )
            == 261
        )

    def test_calcular(self) -> None:
        carteira = CDB(
            percentual=100,
            cdi_ano=12,
        )
        assert (
            round(
                carteira.calcular(
                    1000,
                    inicio=date(2024, 1, 1),
                    fim=date(2024, 2, 1),
                ),
                2,
            )
            == 1010.4
        )


class TestPoupanca:

    def test_selic_anual_zerado(self) -> None:
        try:
            Poupanca(
                selic_anual=0,
            )
            assert False, "Deveria ter lançado exceção"
        except ValueError:
            pass

    def test_meses_decorridos(self) -> None:
        poupanca = Poupanca(
            selic_anual=7.6,
        )
        assert (
            poupanca.meses_decorridos(inicio=date(2019, 10, 8), fim=date(2020, 10, 8))
            == 12
        )

    def test_calcular(self) -> None:
        poupanca_selic_alto = Poupanca(
            selic_anual=10.5,
        )
        poupanca_selic_baixo = Poupanca(
            selic_anual=8.0,
        )
        assert (
            round(
                poupanca_selic_alto.calcular(
                    1000,
                    inicio=date(2024, 1, 10),
                    fim=date(2024, 7, 10),
                ),
                2,
            )
            == 1030.38
        )
        assert (
            round(
                poupanca_selic_baixo.calcular(
                    1000,
                    inicio=date(2024, 1, 15),
                    fim=date(2025, 1, 15),
                ),
                2,
            )
            == 1056.00
        )


class TestJurosCompostos:

    def test_instancia_com_percentual_zerado(self) -> None:
        try:
            JurosCompostos(
                taxa_juros_mensal=0,
            )
            assert False, "Deveria ter lançado exceção"
        except ValueError:
            pass

    def test_contar_meses_decorridos(self) -> None:
        carteira = JurosCompostos(
            taxa_juros_mensal=1,
        )
        assert (
            carteira.meses_decorridos(
                inicio=date(2025, 10, 8),
                fim=date(2026, 10, 8),
            )
            == 12
        )

    def test_calcular(self) -> None:
        carteira = JurosCompostos(
            taxa_juros_mensal=1,
        )
        assert (
            round(
                carteira.calcular(
                    30000, inicio=date(2019, 8, 8), fim=date(2019, 11, 8)
                ),
                2,
            )
            == 30909.03
        )


class TestJurosSimples:

    def test_instancia_com_percentual_zerado(self) -> None:
        try:
            JurosSimples(
                taxa_juros_mensal=0,
            )
            assert False, "Deveria ter lançado exceção"
        except ValueError:
            pass

    def test_contar_meses_decorridos(self) -> None:
        carteira = JurosSimples(
            taxa_juros_mensal=1,
        )
        assert (
            carteira.meses_decorridos(
                inicio=date(2025, 10, 8),
                fim=date(2026, 10, 8),
            )
            == 12
        )

    def test_calcular(self) -> None:
        carteira = JurosSimples(
            taxa_juros_mensal=2,
        )
        assert (
            round(
                carteira.calcular(1200, inicio=date(2019, 1, 1), fim=date(2020, 4, 1)),
                2,
            )
            == 1560
        )


class TestCDB:

    def test_instancia_com_taxa_fixa_anual_zerada(self) -> None:
        try:
            IPCA(taxa_fixa_anual=0, ipca_anual=4)
            assert False, "Deveria ter lançado exceção"
        except ValueError:
            pass

    def test_instancia_com_ipca_anual_zerado(self) -> None:
        try:
            IPCA(taxa_fixa_anual=6, ipca_anual=0)
            assert False, "Deveria ter lançado exceção"
        except ValueError:
            pass

    def test_contar_dias_uteis(self) -> None:
        ipca = IPCA(taxa_fixa_anual=6, ipca_anual=4)
        assert (
            ipca.contar_dias_uteis(
                inicio=date(2025, 10, 8),
                fim=date(2026, 10, 8),
            )
            == 261
        )

    def test_calcular(self) -> None:
        ipca = IPCA(taxa_fixa_anual=6, ipca_anual=4)
        assert (
            round(
                ipca.calcular(1000, inicio=date(2023, 1, 2), fim=date(2023, 12, 20)), 2
            )
            == 1102.4
        )
