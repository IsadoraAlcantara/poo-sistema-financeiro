from financeiro.categoria import Categoria
from financeiro.categoria_despesa import CategoriaDespesa, NomeCategoriaDespesa
from financeiro.categoria_receita import CategoriaReceita, NomeCategoriaReceita


class TestCategoria:

    def setup_method(self) -> None:
        self.cat_alimentacao = CategoriaDespesa(
            NomeCategoriaDespesa.ALIMENTACAO, gasto_max=500
        )
        self.cat_salario = CategoriaReceita(NomeCategoriaReceita.SALARIO)

    def test_categoria_abstrata_e_heranca(self):
        assert isinstance(self.cat_alimentacao, Categoria)
        assert isinstance(self.cat_salario, Categoria)

        assert self.cat_alimentacao.nome == NomeCategoriaDespesa.ALIMENTACAO
        assert self.cat_alimentacao.gasto_max == 500
        assert self.cat_salario.nome == NomeCategoriaReceita.SALARIO

    def test_verifica_se_possui_limite(self):
        assert self.cat_alimentacao.possui_limite()
        assert self.cat_salario.possui_limite() == False
