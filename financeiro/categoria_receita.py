from financeiro.categoria import Categoria


class NomeCategoriaReceita:
    SALARIO = "salario"
    INVESTIMENTOS = "investimentos"
    FREELANCER = "freelancer"


class CategoriaReceita(Categoria):

    def __init__(self, nome: NomeCategoriaReceita) -> None:
        super().__init__(nome)

    def possui_limite(self) -> bool:
        return False
