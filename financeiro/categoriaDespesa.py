from xmlrpc.client import Boolean
from financeiro.categoria import Categoria


class NomeCategoriaDespesa:
    ALIMENTACAO = "alimentacao"
    TRANSPORTE = "transporte"
    LAZER = "lazer"
    AGUA = "agua"
    LUZ = "luz"
    INTERNET = "internet"
    ALUGUEL = "aluguel"


class CategoriaDespesa(Categoria):

    def __init__(self, nome: NomeCategoriaDespesa, gasto_max: int):
        super().__init__(nome)
        if gasto_max <= 0:
            raise ValueError("O gasto máximo de uma categoria deve ser maior que zero")
        self.gasto_max = gasto_max
