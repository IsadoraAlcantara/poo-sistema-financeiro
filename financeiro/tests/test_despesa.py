from financeiro.despesa import Despesa
from financeiro.categoria_despesa import CategoriaDespesa, NomeCategoriaDespesa
from financeiro.categoria_receita import CategoriaReceita, NomeCategoriaReceita

class TestDespesa:


    def setup_method(self) -> None:
        self.cat_alimentacao = CategoriaDespesa(nome=NomeCategoriaDespesa.ALIMENTACAO, gasto_max=500)
        self.cat_transporte = CategoriaDespesa(nome=NomeCategoriaDespesa.TRANSPORTE, gasto_max=500)
        self.cat_salario = CategoriaReceita(nome=NomeCategoriaReceita.SALARIO)

    def test_cria_despesa(self):
        d1 = Despesa(self.cat_alimentacao, 300, "2026-08-20")
        assert d1.categoria == self.cat_alimentacao
        assert d1.valor == 300
        assert d1.data == "2026-08-20"

    def test_impacto_no_saldo(self):
        d1 = Despesa(self.cat_alimentacao, 300, "2026-08-20")
        assert d1.impacto_no_saldo() == -300

    def test_despesa_com_valor_nulo(self):
        try:
            Despesa(self.cat_alimentacao, 0, "2026-08-20")
            assert False, "Deveria ter lançado exceção"
        except ValueError:
            pass

    def test_despesa_com_valor_ivalido_negativo(self):
        try:
            Despesa(self.cat_alimentacao, -200, "2026-08-20")
            assert False, "Deveria ter lançado exceção"
        except ValueError:
            pass

    def test_categoria_invalida(self):
        try: 
            Despesa(self.cat_salario, 300, "2026-08-20")
            assert False, "Deveria ter lançado exceção"
        except TypeError:
            pass