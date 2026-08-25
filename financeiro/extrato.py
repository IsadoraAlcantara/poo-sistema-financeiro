from financeiro.fechamento import Fechamento
from financeiro.conciliacao import Conciliacao


class Extrato:

    def __init__(
        self,
        data_inicio: str,
        data_fim: str,
        fechamentos_totais: list[Fechamento],
        conciliacoes: list[Conciliacao] | None = None,
    ) -> None:
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.fechamentos_filtrados = [
            i
            for i in fechamentos_totais
            if self.data_inicio <= i.data_fechamento <= self.data_fim
        ]
        self.conciliacoes = list(conciliacoes) if conciliacoes else []

    @property
    def total_lancamentos(self) -> int:
        return sum(len(f.lancamentos) for f in self.fechamentos_filtrados)

    @property
    def total_receitas(self) -> int:
        return sum(f.total_receitas for f in self.fechamentos_filtrados)

    @property
    def total_despesas(self) -> int:
        return sum(f.total_despesas for f in self.fechamentos_filtrados)

    @property
    def saldo_final(self) -> int:
        return self.total_receitas - self.total_despesas

    def possui_conciliacao_pendente(self) -> bool:
        if not self.conciliacoes:
            return True
        for c in self.conciliacoes:
            try:
                c.validar()
            except ValueError:
                return True
        return False


if __name__ == "__main__":
    from financeiro.receita import Receita
    from financeiro.despesa import Despesa
    from financeiro.conta import Conta
    from financeiro.categoria_despesa import CategoriaDespesa, NomeCategoriaDespesa
    from financeiro.categoria_receita import CategoriaReceita, NomeCategoriaReceita
    from financeiro.conciliacao import Conciliacao

    cat_salario = CategoriaReceita(NomeCategoriaReceita.SALARIO)
    cat_alimentacao = CategoriaDespesa(NomeCategoriaDespesa.ALIMENTACAO, 1000)

    # Agosto
    d1 = Despesa(cat_alimentacao, 300, "2026-08-20")
    r1 = Receita(cat_salario, 1200, "2026-08-21")
    conta = Conta()

    conta.adicionar_lancamento(d1)
    conta.adicionar_lancamento(r1)

    fechamento_agosto = conta.fechar_periodo("2026-08-01")

    # Novembro
    d2 = Despesa(cat_alimentacao, 600, "2026-11-20")
    r2 = Receita(cat_salario, 1200, "2026-11-21")
    conta = Conta()

    conta.adicionar_lancamento(d2)
    conta.adicionar_lancamento(r2)

    fechamento_novembro = conta.fechar_periodo("2026-11-30")

    todos_fechamentos = [fechamento_agosto, fechamento_novembro]

    gastos_banco = [
        Despesa(cat_alimentacao, 600, "2026-11-03"),
        Receita(cat_salario, 1200, "2026-11-04"),
    ]

    conciliacao_nov = Conciliacao(
        lancamentos_origem=fechamento_novembro.lancamentos,
        lancamentos_destino=gastos_banco,
    )

    extrato_novembro = Extrato(
        data_inicio="2026-11-01",
        data_fim="2026-11-31",
        fechamentos_totais=todos_fechamentos,
        conciliacoes=[conciliacao_nov],
    )

    print("=" * 45)
    print(
        f"       EXTRATO CONSOLIDADO ({extrato_novembro.data_inicio} até {extrato_novembro.data_fim})"
    )
    print("=" * 45)
    print(f"Fechamentos inclusos : {len(extrato_novembro.fechamentos_filtrados)}")
    print(f"Total de lançamentos : {extrato_novembro.total_lancamentos}")
    print(f"Total de Créditos    : R$ {extrato_novembro.total_receitas:.2f}")
    print(f"Total de Débitos     : R$ {extrato_novembro.total_despesas:.2f}")
    print("-" * 45)
    print(f"Saldo Consolidado    : R$ {extrato_novembro.saldo_final:.2f}")
    print(
        f"Conciliação Pendente : {'Sim' if extrato_novembro.possui_conciliacao_pendente() else 'Não'}"
    )
    print("=" * 45)
