import pytest
from financeiro.ServicoImportacao.formato_extrato import FormatoCSV, FormatoExtrato


class TestFormatoExtrato:

    def setup_method(self):
        pass

    def test_formato_abstrato(self):
        with pytest.raises(TypeError):
            FormatoExtrato(caminho_arquivo="arquivo")

    def test_ler_extrato(self):
        parser = FormatoCSV(caminho_arquivo="arquivo")
        assert parser.ler_extrato().data_inicio == "2026-10-01"
        assert parser.ler_extrato().data_fim == "2026-10-31"
        assert parser.ler_extrato().transacoes[0].categoria == "PIX Recebido"
        assert parser.ler_extrato().transacoes[0].data == "2026-10-01"
        assert parser.ler_extrato().transacoes[0].valor == 5000.00