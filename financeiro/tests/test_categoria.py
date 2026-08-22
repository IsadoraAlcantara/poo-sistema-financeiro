from financeiro.categoria import Categoria
from financeiro.categoriaDespesa import CategoriaDespesa, NomeCategoriaDespesa
from financeiro.categoriaReceita import CategoriaReceita, NomeCategoriaReceita


class TestCategoria:

    def test_categoria_abstrata_e_heranca(self):
        cat_alimentacao = CategoriaDespesa(
            NomeCategoriaDespesa.ALIMENTACAO, gasto_max=500
        )
        cat_receita = CategoriaReceita(NomeCategoriaReceita.SALARIO)

        assert isinstance(cat_alimentacao, Categoria)
        assert isinstance(cat_receita, Categoria)

        assert cat_alimentacao.nome == NomeCategoriaDespesa.ALIMENTACAO
        assert cat_receita.nome == NomeCategoriaReceita.SALARIO
