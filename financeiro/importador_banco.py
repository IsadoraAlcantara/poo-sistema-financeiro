from abc import ABC, abstractmethod
from financeiro.extrato import Extrato
from financeiro.formato_extrato import ExtratoBrutoDTO
from financeiro.leitor import Leitor
from financeiro.opcoes_formato_extrato import OpcoesFormatoExtrato

class ImportadorBanco(ABC):

    def __init__(self, leitor: Leitor | None = None) -> None:
        self.leitor = leitor or Leitor()

    @abstractmethod
    def importar(self, caminho_arquivo: str) -> Extrato:
        pass


class ImportadorBancoInter(ImportadorBanco):

    def importar(self, caminho_arquivo: str) -> Extrato:
        dto = self.leitor.ler(
            caminho_arquivo,
            formato=OpcoesFormatoExtrato.CSV,
            delimitador=";",
            coluna_data="data",
            coluna_valor="montante"
        )

        return self._converter_dto_para_extrato(dto)

    def _converter_dto_para_extrato(self, dto: ExtratoBrutoDTO) -> Extrato:
        return Extrato(
            data_inicio=dto.data_inicio,
            data_fim=dto.data_fim,
            fechamentos_totais=[],
        )


class ImportadorBancoItau(ImportadorBanco):
    
    def importar(self, caminho_arquivo: str) -> Extrato:
        dto = self.leitor.ler(
            caminho_arquivo,
            formato=OpcoesFormatoExtrato.OFX,
            fitid_validacao=True
        )
        return self._converter_dto_para_extrato(dto)

    def _converter_dto_para_extrato(self, dto: ExtratoBrutoDTO) -> Extrato:
        return Extrato(
            data_inicio=dto.data_inicio,
            data_fim=dto.data_fim,
            fechamentos_totais=[],
        )