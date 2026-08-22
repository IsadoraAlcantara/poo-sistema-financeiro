from financeiro.categoria import Categoria


class NomeCategoriaReceita:
    SALARIO = "salario"
    ALUGUEL_SALA = "aluguel_sala"


class CategoriaReceita(Categoria):

    def __init__(self, nome: NomeCategoriaReceita):
        super().__init__(nome)

    def possui_limite(self) -> bool:
        return True
