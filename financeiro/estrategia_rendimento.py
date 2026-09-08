from abc import ABC, abstractmethod
from datetime import date, timedelta


class EstrategiaRendimento(ABC):

    @abstractmethod
    def calcular(self, valor: float) -> float:
        return valor


class CDB(EstrategiaRendimento):

    def __init__(
        self, percentual: float, data_inicial: date, data_final: date, cdi_ano=float
    ) -> None:
        if not 0 <= percentual:
            raise ValueError("Percentual deve ser maior do que 100")
        self._percentual = percentual
        if data_inicial > data_final:
            raise ValueError("A data inicial não pode ser posterior do que a data final")
        self.data_inicial = data_inicial
        self.data_final = data_final
        self.cdi_ano = cdi_ano
        self.dias_uteis = self.contar_dias_uteis()

    def contar_dias_uteis(self) -> int:
        dias = 0
        atual = self.data_inicial
        while atual < self.data_final:
            if atual.weekday() < 5:
                dias += 1
            atual += timedelta(days=1)
        return dias

    def calcular(
        self,
        valor: float,
    ) -> float:
        cdi_dia = (1 + self.cdi_ano / 100) ** (1 / 252) - 1
        taxa_CDB_dia = cdi_dia * (self._percentual / 100)
        valor_bruto = valor * (1 + taxa_CDB_dia) ** self.dias_uteis
        return valor_bruto


class Poupanca(EstrategiaRendimento):

    def __init__(self, selic_anual: float, data_inicial: date, data_final: date):
        self.selic_anual = selic_anual
        if data_inicial > data_final:
            raise ValueError("A data inicial não pode ser posterior do que a data final")
        self.data_inicial = data_inicial
        self.data_final = data_final
        self._meses_decorridos = self.meses_decorridos(inicio=data_inicial, fim=data_final)

    def meses_decorridos(self, inicio: date, fim: date) -> float:
        meses = (fim.year - inicio.year) * 12 + (fim.month - inicio.month)

        if (fim.day < inicio.day):
            meses -= 1

        return meses


    def calcular(self, valor: float):
        selic_porcentagem = self.selic_anual / 100
        if ((selic_porcentagem) > 0.085):
            taxa_mes = 0.005
        else:
            taxa_mes = (1 + 0.7 * selic_porcentagem) ** (1 / 12) - 1
            
        valor_final = valor * (1 + taxa_mes) ** self._meses_decorridos
        return valor_final



if __name__ == "__main__":
    from financeiro.estrategia_rendimento import EstrategiaRendimento

    carteira = CDB(
        percentual=100,
        data_inicial=date(2023, 10, 8),
        data_final=date(2024, 10, 8),
        cdi_ano=100
    )

    poupanca = Poupanca(
            selic_anual=7.5,
            data_inicial=date(2019, 10, 8),
            data_final=date(2024, 10, 8),
        )
    print(carteira.contar_dias_uteis())
    print(f"Valor corrigido: {round(carteira.calcular(1000), 2)}")
    print(f"Valor poupança: {poupanca.calcular(1000)}")
