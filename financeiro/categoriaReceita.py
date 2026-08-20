from financeiro.categoria import Categoria


class CategoriaReceita(Categoria):

    def __init__(self, nome):
        super().__init__(nome)

class NomeCategoriaReceita:
    SALARIO = "salario" 
    ALUGUEL_SALA = "aluguel_sala"