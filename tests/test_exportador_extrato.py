from financeiro.categoria_despesa import CategoriaDespesa
from financeiro.categoria_receita import CategoriaReceita
from financeiro.despesa import Despesa
from financeiro.extrato import Extrato
from financeiro.fechamento import Fechamento
from financeiro.receita import Receita
from financeiro.ServicoImportacao.documento import (
    DocumentoCSV,
    DocumentoHTML,
    DocumentoPDF,
)
from financeiro.ServicoImportacao.exportador_extrato import (  # ajuste a importação conforme a estrutura do seu projeto
    ExportadorCSV,
    ExportadorHTML,
    ExportadorPDF,
)


class TestExportadores:

    # def setup_method(self) -> None:
    #     self.cat_alimentacao = CategoriaDespesa("ALIMENTACAO", 1000)
    #     self.cat_salario = CategoriaReceita("SALARIO")

    #     lancamentos = [
    #         Despesa(self.cat_alimentacao, 200, "2026-07-05"),
    #         Receita(self.cat_salario, 1200, "2026-07-10"),
    #     ]
    #     self.fechamento_julho = Fechamento("2026-07-31", lancamentos)

    #     self.extrato = Extrato(
    #         data_inicio="2026-07-01",
    #         data_fim="2026-07-31",
    #         fechamentos_totais=[self.fechamento_julho],
    #     )

    def test_exportador_pdf_cria_documento_pdf(self) -> None:
        exportador = ExportadorPDF()
        documento = exportador.criar_documento()
        assert isinstance(documento, DocumentoPDF)

    def test_exportador_csv_cria_documento_csv(self) -> None:
        exportador = ExportadorCSV()
        documento = exportador.criar_documento()
        assert isinstance(documento, DocumentoCSV)

    def test_exportador_html_cria_documento_html(self) -> None:
        exportador = ExportadorHTML()
        documento = exportador.criar_documento()
        assert isinstance(documento, DocumentoHTML)
