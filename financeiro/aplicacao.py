from datetime import date
from financeiro.estrategia_rendimento import EstrategiaRendimento


class Aplicacao:

    def __init__(
        self,
        valor: float,
        data_inicial: date,
        data_final: date,
        estrategia: EstrategiaRendimento,
    ) -> None:
        if valor <= 0:
            raise ValueError("O valor investido deve ser maior do que 0")
        self.valor = valor
        if data_inicial > data_final:
            raise ValueError(
                "A data inicial não pode ser posterior do que a data final"
            )
        self.data_inicial = data_inicial
        self.data_final = data_final
        self.estrategia = estrategia

    def calcular_valor_total(self) -> float:
        return self.estrategia.calcular(
            valor=self.valor, inicio=self.data_inicial, fim=self.data_final
        )

    def calcular_lucro(self) -> float:
        return self.calcular_valor_total() - self.valor


if __name__ == "__main__":
    from financeiro.estrategia_rendimento import CDB, Poupanca

    cdb = CDB(
        percentual=100,
        cdi_ano=11.777,
    )

    poupanca = Poupanca(
        selic_anual=7.5,
    )

    aplicacao1 = Aplicacao(
        data_inicial=date(2023, 10, 8),
        data_final=date(2024, 10, 8),
        valor=1000,
        estrategia=cdb,
    )

    aplicacao2 = Aplicacao(
        data_inicial=date(2023, 10, 8),
        data_final=date(2024, 10, 8),
        valor=1000,
        estrategia=poupanca,
    )

    print(f"Aplicação 1 total: {round(aplicacao1.calcular_valor_total(), 2)}")
    print(f"Aplicação 1 lucro: {round(aplicacao1.calcular_lucro(), 2)}")
    print(f"Aplicação 1 total: {round(aplicacao2.calcular_valor_total(), 2)}")
    print(f"Aplicação 1 lucro: {round(aplicacao2.calcular_lucro(), 2)}")
