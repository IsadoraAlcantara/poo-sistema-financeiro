from financeiro.lancamento import Lancamento
from financeiro.despesa import Despesa
from financeiro.categoria_despesa import CategoriaDespesa, NomeCategoriaDespesa

class TestLancamento:

    def setup_method(self) -> None:
        self.cat_alimentacao = CategoriaDespesa(nome=NomeCategoriaDespesa.ALIMENTACAO, gasto_max=500)
        self.cat_transporte = CategoriaDespesa(nome=NomeCategoriaDespesa.TRANSPORTE, gasto_max=500)


    def test_cria_lancamento(self) -> None:
        d1 = Despesa(self.cat_alimentacao, 300, "2026-08-20")
        assert d1.categoria == self.cat_alimentacao
        assert d1.valor == 300
        assert d1.data == "2026-08-20"

    def test_altetar_valor(self) -> None:
        d1 = Despesa(self.cat_alimentacao, 300, "2026-08-20")
        d1.alterar_valor(400)
        assert d1.valor == 400

    def test_altetar_valor_invalido_nulo(self) -> None:
        d1 = Despesa(self.cat_alimentacao, 300, "2026-08-20")
        try: 
            d1.alterar_valor(0)
            assert False, "Deveria ter lançado exceção"
        except:
            pass

    def test_altetar_valor_invalido_negativo(self) -> None:
        d1 = Despesa(self.cat_alimentacao, 300, "2026-08-20")
        try: 
            d1.alterar_valor(-100)
            assert False, "Deveria ter lançado exceção"
        except:
            pass

    def test_altetar_categoria(self) -> None:
        d1 = Despesa(self.cat_alimentacao, 300, "2026-08-20")
        d1.alterar_categoria(self.cat_transporte)
        assert d1.categoria == self.cat_transporte