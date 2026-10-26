from financeiro.ServicoImportacao.importador_banco import ImportadorBanco, ImportadorBancoItau
from financeiro.ServicoImportacao.formato_extrato import ExtratoBrutoDTO
from financeiro.ServicoImportacao.leitor import Leitor
from financeiro.extrato import Extrato


class TestImportadorBanco:

    def setup_method(self):
        self.leitor = Leitor()
        self.importador_itau = ImportadorBancoItau(leitor=self.leitor)

    def test_importador_itau_importa_dto(self):
        dto = self.importador_itau.importar_dto(caminho_arquivo="arquivo")
        assert isinstance(dto, ExtratoBrutoDTO)
        assert dto.transacoes[0].categoria == "PIX Recebido"
        assert dto.transacoes[0].data == "2026-10-01"
        assert dto.transacoes[0].valor == 5000.00


    def test_importador_itau_importar(self):
        extrato = self.importador_itau.importar(caminho_arquivo="arquivo")
        assert isinstance(extrato, Extrato)
        assert extrato.data_inicio == "2026-10-01"
        assert extrato.data_fim == "2026-10-31"
        assert len(extrato.fechamentos_filtrados) == 1