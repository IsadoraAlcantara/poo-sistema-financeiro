from abc import ABC, abstractmethod
from financeiro.extrato import Extrato
from financeiro.ServicoImportacao.documento import Documento, DocumentoPDF, DocumentoCSV, DocumentoHTML


class ExportadorExtrato(ABC):

    def exportar(self, extrato: Extrato, nome_arquivo: str) -> None:
        documento = self.criar_documento()

        titulo = f"EXTRATO CONSOLIDADO ({extrato.data_inicio} até {extrato.data_fim})"
        documento.adicionar_cabecalho(titulo)

        lancamentos = [
            f"Fechamentos inclusos : {len(extrato.fechamentos_filtrados)}",
            f"Total de lançamentos : {extrato.total_lancamentos}",
            f"Total de Créditos     : R$ {extrato.total_receitas:.2f}",
            f"Total de Débitos      : R$ {extrato.total_despesas:.2f}",
        ]
        documento.adicionar_corpo(lancamentos)

        rodape = (
            f"Saldo Consolidado: R$ {extrato.saldo_final:.2f} | "
            f"Conciliação Pendente: {'Sim' if extrato.possui_conciliacao_pendente() else 'Não'}"
        )
        documento.adicionar_rodape(rodape)
        documento.salvar(nome_arquivo)

    def criar_documento(self) -> Documento:
        pass


class ExportadorPDF(ExportadorExtrato):

    def criar_documento(self) -> Documento:
        return DocumentoPDF()


class ExportadorCSV(ExportadorExtrato):

    def criar_documento(self) -> Documento:
        return DocumentoCSV()


class ExportadorHTML(ExportadorExtrato):

    def criar_documento(self) -> Documento:
        return DocumentoHTML()


if __name__ == "__main__":
    from financeiro.receita import Receita
    from financeiro.despesa import Despesa
    from financeiro.conta import Conta
    from financeiro.categoria_despesa import CategoriaDespesa
    from financeiro.categoria_receita import CategoriaReceita
    from financeiro.conciliacao import Conciliacao
    from financeiro.extrato import Extrato

    cat_salario = CategoriaReceita(nome="SALARIO")
    cat_alimentacao = CategoriaDespesa(nome="ALIMENTACAO", gasto_max=1000)

    d2 = Despesa(cat_alimentacao, 600, "2026-11-20")
    r2 = Receita(cat_salario, 1200, "2026-11-21")
    conta = Conta()

    conta.adicionar_lancamento(d2)
    conta.adicionar_lancamento(r2)

    fechamento_novembro = conta.fechar_periodo("2026-11-30")
    todos_fechamentos = [fechamento_novembro]

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

    exportadores: list[ExportadorExtrato] = [
        ExportadorPDF(),
        ExportadorCSV(),
        ExportadorHTML(),
    ]

    for exportador in exportadores:
        exportador.exportar(extrato_novembro, "extrato_novembro_2026")
