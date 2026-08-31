from financeiro.estrategia_rendimento import EstrategiaRendimento, CDB


class TestRendimento:

    def test_calcula_cdb(self):
        carteira = CDB(percentual=100, data_inicial="10/08/2019", data_final="02/04/2024")
        carteira.calcular(10000)

        # ALTERAR DATA DE STR PARA DATE