from financeiro.lancamento import Lancamento


class Receita(Lancamento):

    def __init__(self, categoria, valor, date):
        super().__init__(categoria, valor, date)