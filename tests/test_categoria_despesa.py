from financeiro.categoria_despesa import CategoriaDespesa, NomeCategoriaDespesa
from financeiro.categoria import Categoria


class TestCategoriaDespesa:

    def test_criar_categoria_despesa(self) -> None:
        cat_aluguel = CategoriaDespesa(NomeCategoriaDespesa.ALUGUEL, gasto_max=500)
        assert cat_aluguel.nome == NomeCategoriaDespesa.ALUGUEL
        assert cat_aluguel.gasto_max == 500
        assert isinstance(cat_aluguel, Categoria)

    def test_criar_categoria_com_valor_nulo(self) -> None:
        try:
            CategoriaDespesa(NomeCategoriaDespesa.TRANSPORTE, gasto_max=0)
            assert False, "Deveria ter lançado exceção"
        except ValueError:
            pass

    def test_alterar_gasto_max(self) -> None:
        cat = CategoriaDespesa(NomeCategoriaDespesa.LAZER, gasto_max=300)
        cat.alterar_gasto_max(450)
        assert cat.gasto_max == 450

    def test_alterar_gasto_max_com_valor_nulo(self) -> None:
        try:
            CategoriaDespesa(NomeCategoriaDespesa.LAZER, gasto_max=0)
            assert False, "Deveria ter lançado exceção"
        except ValueError:
            pass
