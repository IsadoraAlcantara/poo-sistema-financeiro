from abc import ABC, abstractmethod
from datetime import date, timedelta


class EstrategiaRendimento(ABC):

    @abstractmethod
    def calcular(self, valor: float, data_inicial: date, data_final: date) -> float:
        return valor


class CDB(EstrategiaRendimento):

    def __init__(self, percentual: float, cdi_ano: float) -> None:
        if percentual <= 0:
            raise ValueError("Percentual deve ser maior do que 0")
        self._percentual = percentual
        self.cdi_ano = cdi_ano

    def contar_dias_uteis(self, data_inicial: date, data_final: date) -> int:
        dias = 0
        atual = data_inicial
        while atual < data_final:
            if atual.weekday() < 5:
                dias += 1
            atual += timedelta(days=1)
        return dias

    def calcular(self, valor: float, inicio: date, fim: date) -> float:
        dias_uteis = self.contar_dias_uteis(data_inicial=inicio, data_final=fim)

        cdi_dia = (1 + self.cdi_ano / 100) ** (1 / 252) - 1
        taxa_CDB_dia = cdi_dia * (self._percentual / 100)
        valor_bruto = valor * (1 + taxa_CDB_dia) ** dias_uteis
        return valor_bruto


class Poupanca(EstrategiaRendimento):

    def __init__(self, selic_anual: float) -> None:
        if selic_anual <= 0:
            raise ValueError("O selic anual deve ser maior do que 0")
        self.selic_anual = selic_anual

    def meses_decorridos(self, inicio: date, fim: date) -> float:
        meses = (fim.year - inicio.year) * 12 + (fim.month - inicio.month)

        if fim.day < inicio.day:
            meses -= 1

        return meses

    def calcular(self, valor: float, inicio: date, fim: date) -> float:
        meses_decorridos = self.meses_decorridos(inicio=inicio, fim=fim)

        selic_porcentagem = self.selic_anual / 100
        if (selic_porcentagem) > 0.085:
            taxa_mes = 0.005
        else:
            taxa_mes = (1 + 0.7 * selic_porcentagem) ** (1 / 12) - 1

        valor_final = valor * (1 + taxa_mes) ** meses_decorridos
        return valor_final


if __name__ == "__main__":
    from financeiro.estrategia_rendimento import EstrategiaRendimento

    carteira = CDB(
        percentual=100,
        data_inicial=date(2023, 10, 8),
        data_final=date(2024, 10, 8),
        cdi_ano=11.777,
    )

    poupanca = Poupanca(
        selic_anual=7.5,
        data_inicial=date(2019, 10, 8),
        data_final=date(2024, 10, 8),
    )
    print(carteira.contar_dias_uteis())
    print(f"Valor corrigido: {round(carteira.calcular(1000), 2)}")
    print(f"Valor poupança: {poupanca.calcular(1000)}")
