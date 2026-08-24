from financeiro.receita import Receita
from financeiro.categoria_receita import CategoriaReceita, NomeCategoriaReceita
from financeiro.categoria_despesa import CategoriaDespesa, NomeCategoriaDespesa

class TestReceita:


    def setup_method(self) -> None:
        self.cat_investimentos = CategoriaReceita(nome=NomeCategoriaReceita.INVESTIMENTOS)
        self.cat_transporte = CategoriaDespesa(nome=NomeCategoriaDespesa.TRANSPORTE, gasto_max=500)

    def test_cria_receita(self):
        r1 = Receita(self.cat_investimentos, 300, "2026-08-20")
        assert r1.categoria == self.cat_investimentos
        assert r1.valor == 300
        assert r1.data == "2026-08-20"

    def test_impacto_no_saldo(self):
        r1 = Receita(self.cat_investimentos, 300, "2026-08-20")
        assert r1.impacto_no_saldo() == 300

    def test_receita_com_valor_nulo(self):
        try:
            Receita(self.cat_investimentos, 0, "2026-08-20")
            assert False, "Deveria ter lançado exceção"
        except ValueError:
            pass

    def test_receita_com_valor_ivalido_negativo(self):
        try:
            Receita(self.cat_investimentos, -200, "2026-08-20")
            assert False, "Deveria ter lançado exceção"
        except ValueError:
            pass

    def test_categoria_invalida(self):
        try: 
            Receita(self.cat_transporte, 300, "2026-08-20")
            assert False, "Deveria ter lançado exceção"
        except TypeError:
            pass