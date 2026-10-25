import pytest
from financeiro.ServicoImportacao.criador_importador import CriadorImportador, OpcoesBanco
from financeiro.ServicoImportacao.importador_banco import ImportadorBancoInter, ImportadorBancoItau
from financeiro.ServicoImportacao.leitor import Leitor


class TestCriadorImportador:

    def setup_method(self) -> None:
        leitor = Leitor()
        self.criador_importador = CriadorImportador(leitor=leitor)

    def test_cria_importacao_banco_inter(self) -> None:
        importador = self.criador_importador.criar(banco=OpcoesBanco.INTER)
        assert isinstance(importador, ImportadorBancoInter)

    def test_banco_desconhecido_lanca_erro(self) -> None:
        with pytest.raises(ValueError):
            self.criador_importador.criar(banco="banco qualquer")
            