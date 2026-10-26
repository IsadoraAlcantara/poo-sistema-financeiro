import pytest
from financeiro.conta import Conta
from financeiro.ServicoImportacao.criador_importador import CriadorImportador
from financeiro.ServicoImportacao.leitor import Leitor
from financeiro.ServicoImportacao.servico_importacao import ServicoImportacao
from financeiro.ServicoImportacao.criador_importador import OpcoesBanco
from financeiro.extrato import Extrato
from financeiro.ServicoImportacao.exportador_extrato import ExportadorPDF


class TestServicoImportacao:

    def setup_method(self):
        self.conta = Conta()
        leitor = Leitor()
        criador_importador = CriadorImportador(leitor=leitor)
        self.servico_importacao = ServicoImportacao(
            criador_importador=criador_importador
        )

    def test_verifica_novos_lancamentos(self):
        self.servico_importacao.importar_para_conta(
            conta=self.conta,
            caminho_arquivo="extrato_outubro.csv",
            banco=OpcoesBanco.INTER,
        )
        assert self.conta.saldo == 4550.00
        assert len(self.conta.lancamentos) == 2

    def test_exporta_extrato(self, capsys):
        exportador = ExportadorPDF()
        extrato = Extrato(
            data_inicio="2026-10-01",
            data_fim="2026-10-31",
            fechamentos_totais=[]
        )
        nome_arquivo = "transacoes"
        self.servico_importacao.exportar_extrato(
            extrato=extrato,
            nome_arquivo=nome_arquivo,
            exportador=exportador
        )

        captured = capsys.readouterr()
        saida_console = captured.out

        assert f"[Gerando Arquivo: {nome_arquivo}.pdf]" in saida_console