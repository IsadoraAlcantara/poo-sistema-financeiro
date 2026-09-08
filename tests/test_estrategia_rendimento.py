from datetime import date
from financeiro.estrategia_rendimento import CDB


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

    def test_instancia_com_data_final(self) -> None:
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