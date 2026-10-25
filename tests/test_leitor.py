import pytest
from financeiro.ServicoImportacao.leitor import Leitor
from financeiro.ServicoImportacao.importador_banco import (
    ImportadorBancoInter,
    OpcoesFormatoExtrato,
)
from financeiro.ServicoImportacao.formato_extrato import ExtratoBrutoDTO


class TestLeitor:

    def setup_method(self):
        leitor = Leitor()
        self.importador = ImportadorBancoInter(leitor)

    def test_le_extrato_ofx(self):
        extrato = self.importador.leitor.ler(
            caminho_arquivo="aquivo.ofx",
            formato=OpcoesFormatoExtrato.OFX,
            fitid_validacao=True,
        )
        assert isinstance(extrato, ExtratoBrutoDTO)

    def test_formato_desconhecido_lanca_erro(self):
        with pytest.raises(ValueError):
            self.importador.leitor.ler(
                caminho_arquivo="aquivo.ofx",
                formato="formato",
                fitid_validacao=True,
            )
