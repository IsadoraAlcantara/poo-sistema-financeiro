from xmlrpc.client import Boolean


class Categoria:

    def __init__(self, nome, gasto_max: int, total_gasto: int, recorrente: Boolean):
        self.nome = nome
        self.gasto_max = gasto_max
        self.total_gasto = total_gasto
        self.recorrente = recorrente

    def calcular_total_gasto(self):
        total = 

class TipoCategoria:
    SALARIO = "salario"
    ALIMENTACAO = "alimentacao"
    TRANSPORTE = "transporte"
    LAZER = "lazer"
    AGUA = "agua"
    LUZ = "luz"
    INTERENET = "internet"
    ALUGUEL = "aluguel"
