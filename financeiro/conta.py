from financeiro.lancamento import Lancamento
from financeiro.categoria_despesa import (
    CategoriaDespesa,
    NomeCategoriaDespesa,
    Categoria,
)
from financeiro.despesa import Despesa
from financeiro.fechamento import Fechamento


class Conta:
    def __init__(self) -> None:
        self.lancamentos: list[Lancamento] = []

    def adicionar_lancamento(self, novo_lancamento: Lancamento) -> None:
        self.lancamentos.append(novo_lancamento)

    def calcular_total_lancamentos(self) -> int:
        return sum(i.impacto_no_saldo() for i in self.lancamentos)

    def listar_lancamento_por_categoria(
        self, categoria_escolhida: Categoria
    ) -> list[Lancamento]:
        lancamentos_filtados = [
            i for i in self.lancamentos if i.categoria == categoria_escolhida
        ]
        return lancamentos_filtados

    def calcular_total_lancamentos_por_categoria(
        self, categoria_escolhida: Categoria
    ) -> int:
        lancamentos_filtados = self.listar_lancamento_por_categoria(categoria_escolhida)
        return sum(i.impacto_no_saldo() for i in lancamentos_filtados)

    def excedeu_gasto_max(self, categoria_escolhida) -> bool:
        if not isinstance(categoria_escolhida, CategoriaDespesa):
            raise ValueError("Essa categoria não possui gasto máximo")
        total_gasto = -self.calcular_total_lancamentos_por_categoria(
            categoria_escolhida
        )
        return categoria_escolhida.gasto_max < total_gasto

    def fechar_periodo(self, periodo: str) -> Fechamento:
        fechamento = Fechamento(data_fechamento=periodo, lancamentos=self.lancamentos)
        self.lancamentos = []
        return fechamento


if __name__ == "__main__":
    from financeiro.despesa import Despesa
    from financeiro.categoria_despesa import CategoriaDespesa, NomeCategoriaDespesa
    from financeiro.receita import Receita
    from financeiro.categoria_receita import CategoriaReceita, NomeCategoriaReceita

    cat_alimentacao = CategoriaDespesa(
        nome=NomeCategoriaDespesa.ALIMENTACAO, gasto_max=500
    )
    cat_salario = CategoriaReceita(nome=NomeCategoriaReceita.SALARIO)

    despesa1 = Despesa(cat_alimentacao, 300, "2026-08-20")
    despesa2 = Despesa(cat_alimentacao, 400, "2026-08-20")
    receita1 = Receita(cat_salario, 1200, "2026-08-21")
    conta = Conta()

    conta.adicionar_lancamento(despesa1)
    conta.adicionar_lancamento(despesa2)
    conta.adicionar_lancamento(receita1)

    listaLancamentos = conta.listar_lancamento_por_categoria(cat_alimentacao)

    for l in listaLancamentos:
        print(
            f"Categoria: {l.categoria.nome}, Valor: {l.impacto_no_saldo()}, Data: {l.data}"
        )

    print(f"Valor total conta: {conta.calcular_total_lancamentos()}")
    print(
        f"Valor total por categoria: {conta.calcular_total_lancamentos_por_categoria(cat_alimentacao)}"
    )
    print(f"Excedeu o gasto máximo? {conta.excedeu_gasto_max(cat_alimentacao)}")

    fechamento_agosto = conta.fechar_periodo("2026-08-01")

    print(f"Receitas: R$ {fechamento_agosto.total_receitas}")
    print(f"Despesas: R$ {fechamento_agosto.total_despesas}")
    print(f"Saldo Final: R$ {fechamento_agosto.saldo_final}")
