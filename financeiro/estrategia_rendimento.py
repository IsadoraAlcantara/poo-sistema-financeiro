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


class JurosCompostos(EstrategiaRendimento):

    def __init__(self, taxa_juros_mensal: float):
        if taxa_juros_mensal <= 0:
            raise ValueError("A taxa de juro deve ser maior do que zero")
        self.taxa_juros_mensal = taxa_juros_mensal

    def meses_decorridos(self, inicio: date, fim: date) -> float:
        meses = (fim.year - inicio.year) * 12 + (fim.month - inicio.month)

        if fim.day < inicio.day:
            meses -= 1

        return meses

    def calcular(self, valor: float, inicio: date, fim: date) -> float:
        meses = self.meses_decorridos(inicio=inicio, fim=fim)
        montante = valor * (1 + (self.taxa_juros_mensal / 100)) ** meses
        return montante


class JurosSimples(EstrategiaRendimento):

    def __init__(self, taxa_juros_mensal: float):
        if taxa_juros_mensal <= 0:
            raise ValueError("A taxa de juro deve ser maior do que zero")
        self.taxa_juros_mensal = taxa_juros_mensal

    def meses_decorridos(self, inicio: date, fim: date) -> float:
        meses = (fim.year - inicio.year) * 12 + (fim.month - inicio.month)

        if fim.day < inicio.day:
            meses -= 1

        return meses

    def calcular(self, valor: float, inicio: date, fim: date) -> float:
        meses = self.meses_decorridos(inicio=inicio, fim=fim)
        montante = valor * (1 + (self.taxa_juros_mensal / 100) * meses)
        return montante


class IPCA(EstrategiaRendimento):

    def __init__(self, taxa_fixa_anual: float, ipca_anual):
        if taxa_fixa_anual <= 0:
            raise ValueError("A taxa fixa anual deve ser maior do que zero")
        self.taxa_fixa_anual = taxa_fixa_anual
        if ipca_anual <= 0:
            raise ValueError("O ipca anual deve ser maior do que zero")
        self.ipca_anual = ipca_anual

    def contar_dias_uteis(self, inicio: date, fim: date) -> int:
        dias = 0
        atual = inicio
        while atual < fim:
            if atual.weekday() < 5:
                dias += 1
            atual += timedelta(days=1)
        return dias

    def calcular(self, valor: float, inicio: date, fim: date) -> float:
        dias_uteis = self.contar_dias_uteis(inicio=inicio, fim=fim)
        fator_ipca_dia = (1 + self.ipca_anual / 100) ** (1 / 252)
        fator_juro_dia = (1 + self.taxa_fixa_anual / 100) ** (1 / 252)
        fator_diario = fator_ipca_dia * fator_juro_dia
        valor_final = valor * fator_diario ** dias_uteis
        return valor_final


if __name__ == "__main__":
    from financeiro.estrategia_rendimento import EstrategiaRendimento

    carteira = CDB(
        percentual=100,
        cdi_ano=11.777,
    )

    poupanca = Poupanca(
        selic_anual=7.5,
    )

    juros_compostos = JurosCompostos(taxa_juros_mensal=1)
    juros_simples = JurosSimples(taxa_juros_mensal=2)

    ipca = IPCA(taxa_fixa_anual=6, ipca_anual=4)

    print(
        f"Valor corrigido: {round(carteira.calcular(1000, inicio=date(2023, 10, 8), fim=date(2024, 10, 8)), 2)}"
    )
    print(f"Valor poupança: {poupanca.calcular(1000, inicio=date(2019, 10, 8),
        fim=date(2024, 10, 8))}")
    print(
        f"Valor juros compostos: {juros_compostos.calcular(30000, inicio=date(2019, 8, 8),
        fim=date(2019, 11, 8))}"
    )
    print(f"Valor juros simples: {juros_simples.calcular(1200, inicio=date(2019, 8, 8),
        fim=date(2020, 11, 8))}")
    print(
        juros_compostos.meses_decorridos(inicio=date(2019, 8, 8), fim=date(2020, 11, 8))
    )
    print(
        f"Valor ipca: {round(ipca.calcular(1000, inicio=date(2023, 1, 2), fim=date(2023, 12, 20)), 2)}"
    )
