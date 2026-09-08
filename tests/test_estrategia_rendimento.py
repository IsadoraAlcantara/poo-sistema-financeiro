from datetime import date
from financeiro.estrategia_rendimento import EstrategiaRendimento, CDB


class TestRendimento:

    def test_calcula_cdb(self):
        carteira = CDB(
            percentual=100, data_inicial=date(2019, 10, 8), data_final=date(2024, 10, 8), cdi_ano=100
        )
        carteira.calcular(10000)
