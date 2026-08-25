from financeiro.categoria_receita import CategoriaReceita, NomeCategoriaReceita
from financeiro.categoria import Categoria


class TestCategoriaReceita:

    def test_criar_categoria_receita_com_sucesso(self) -> None:
        cat = CategoriaReceita(NomeCategoriaReceita.SALARIO)
        assert cat.nome == NomeCategoriaReceita.SALARIO

    def test_categoria_receita_herda_de_categoria(self) -> None:
        cat = CategoriaReceita(NomeCategoriaReceita.INVESTIMENTOS)
        assert isinstance(cat, Categoria)
