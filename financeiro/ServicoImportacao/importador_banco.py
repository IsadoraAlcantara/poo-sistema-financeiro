from abc import ABC, abstractmethod

from financeiro.extrato import Extrato
from financeiro.ServicoImportacao.formato_extrato import ExtratoBrutoDTO
from financeiro.fechamento import Fechamento
from financeiro.ServicoImportacao.leitor import Leitor, OpcoesFormatoExtrato

class ImportadorBanco(ABC):

    def __init__(self, leitor: Leitor) -> None:
        self.leitor = leitor

    @abstractmethod
    def importar_dto(self, caminho_arquivo: str) -> ExtratoBrutoDTO:
        pass

    def importar(self, caminho_arquivo: str) -> Extrato:
        dto = self.importar_dto(caminho_arquivo)
        return self._converter_dto_para_extrato(dto=dto)

    def _converter_dto_para_extrato(self, dto: ExtratoBrutoDTO) -> Extrato:
        fechamento_inicial = Fechamento(lancamentos=dto.transacoes, data_fechamento=dto.data_fim)
        return Extrato(
            data_inicio=dto.data_inicio,
            data_fim=dto.data_fim,
            fechamentos_totais=[fechamento_inicial],
        )


class ImportadorBancoInter(ImportadorBanco):

    def importar_dto(self, caminho_arquivo: str) -> ExtratoBrutoDTO:
        return self.leitor.ler(
            caminho_arquivo,
            formato=OpcoesFormatoExtrato.CSV,
            delimitador=";",
            coluna_data="data",
            coluna_valor="montante",
        )


class ImportadorBancoItau(ImportadorBanco):

    def importar_dto(self, caminho_arquivo: str) -> ExtratoBrutoDTO:
        return self.leitor.ler(
            caminho_arquivo,
            formato=OpcoesFormatoExtrato.OFX,
            fitid_validacao=True,
        )