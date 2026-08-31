
from abc import ABC, abstractmethod
from datetime import date


class EstrategiaRendimento(ABC):

    @abstractmethod
    def calcular(self, valor: float) -> float:
        return valor

class CDB(EstrategiaRendimento):

    def __init__(self, percentual: float, data_inicial: date, data_final: date) -> None:
        if not 0 <= percentual <= 100:
            raise ValueError("Percentual deve estar entre 0 e 100")
        self._percentual = percentual
        self.data_inicial = data_inicial
        self.data_final = data_final

    def calcular(self, valor: float) -> float:
        valorBruto = valor * (1 + (self._percentual / 100))
        return valorBruto
        