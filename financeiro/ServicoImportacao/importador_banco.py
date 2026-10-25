from abc import ABC, abstractmethod
from financeiro.extrato import Extrato
from financeiro.ServicoImportacao.formato_extrato import ExtratoBrutoDTO
from financeiro.ServicoImportacao.leitor import Leitor, OpcoesFormatoExtrato

class ImportadorBanco(ABC):

    def __init__(self, leitor: Leitor) -> None:
        self.leitor = leitor

    @abstractmethod
    def importar_dto(self, caminho_arquivo: str) -> ExtratoBrutoDTO:
        pass

    def importar(self, caminho_arquivo: str) -> Extrato:
        dto = self.importar_dto(caminho_arquivo)
        return self._converter_dto_para_extrato(dto)

    # VER SE NAO PODE SER UM MÉTODO CONCRETO - SE SIM, NAO HA NECESSIDADE DE IMPLEMENTAR NAS CLASSES FILHAS
    @abstractmethod
    def _converter_dto_para_extrato(self, dto: ExtratoBrutoDTO) -> Extrato:
        pass


class ImportadorBancoInter(ImportadorBanco):

    def importar_dto(self, caminho_arquivo: str) -> ExtratoBrutoDTO:
        return self.leitor.ler(
            caminho_arquivo,
            formato=OpcoesFormatoExtrato.CSV,
            delimitador=";",
            coluna_data="data",
            coluna_valor="montante",
        )

    def _converter_dto_para_extrato(self, dto: ExtratoBrutoDTO) -> Extrato:
        return Extrato(
            data_inicio=dto.data_inicio,
            data_fim=dto.data_fim,
            fechamentos_totais=[],
        )


class ImportadorBancoItau(ImportadorBanco):

    def importar_dto(self, caminho_arquivo: str) -> ExtratoBrutoDTO:
        return self.leitor.ler(
            caminho_arquivo,
            formato=OpcoesFormatoExtrato.OFX,
            fitid_validacao=True,
        )


    def _converter_dto_para_extrato(self, dto: ExtratoBrutoDTO) -> Extrato:
        return Extrato(
            data_inicio=dto.data_inicio,
            data_fim=dto.data_fim,
            fechamentos_totais=[],
        )