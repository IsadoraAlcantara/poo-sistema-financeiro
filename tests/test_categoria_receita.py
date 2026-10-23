from financeiro.categoria_receita import CategoriaReceita
from financeiro.categoria import Categoria


class TestCategoriaReceita:

    def test_criar_categoria_receita_com_sucesso(self) -> None:
        cat = CategoriaReceita("SALARIO")
        assert cat.nome == "SALARIO"

    def test_categoria_receita_herda_de_categoria(self) -> None:
        cat = CategoriaReceita("INVESTIMENTOS")
        assert isinstance(cat, Categoria)
