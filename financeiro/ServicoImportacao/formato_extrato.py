from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class TransacaoDTO:
    categoria: str
    data: str
    valor: float


@dataclass
class ExtratoBrutoDTO:
    data_inicio: str
    data_fim: str
    transacoes: list[TransacaoDTO]


class FormatoExtrato(ABC):

    def __init__(
        self,
        caminho_arquivo: str,
    ) -> None:
        self._caminho_arquivo = caminho_arquivo

    @abstractmethod
    def ler_extrato(self) -> ExtratoBrutoDTO:
        pass


class FormatoOFX(FormatoExtrato):

    def __init__(self, caminho_arquivo: str, fitid_validacao: bool = True) -> None:
        super().__init__(caminho_arquivo)
        self._fitid_validacao = fitid_validacao

    def ler_extrato(self) -> ExtratoBrutoDTO:
        print(
            f"Lendo e parseando tags OFX de: {self._caminho_arquivo}, {'com' if self._fitid_validacao else 'sem'} validação de FITID"
        )

        return ExtratoBrutoDTO(
            data_inicio="2026-10-01",
            data_fim="2026-10-31",
            transacoes=[
                TransacaoDTO(
                    categoria="PIX Recebido", data="2026-10-01", valor=5000.00
                ),
                TransacaoDTO(
                    categoria="Supermercado", data="2026-10-05", valor=-450.00
                ),
            ],
        )


class FormatoCSV(FormatoExtrato):

    def __init__(
        self,
        caminho_arquivo: str,
        delimitador: str = ";",
        coluna_data: str = "Data",
        coluna_valor: str = "Valor",
    ) -> None:
        super().__init__(caminho_arquivo)
        self._delimitador = delimitador
        self._coluna_data = coluna_data
        self._coluna_valor = coluna_valor

    def ler_extrato(self) -> ExtratoBrutoDTO:
        print(
            f"Lendo CSV '{self._caminho_arquivo}' usando delimitador '{self._delimitador}' "
            f"e colunas [{self._coluna_data}, {self._coluna_valor}]"
        )
        return ExtratoBrutoDTO(
            data_inicio="2026-10-01",
            data_fim="2026-10-31",
            transacoes=[
                TransacaoDTO(
                    categoria="PIX Recebido", data="2026-10-01", valor=5000.00
                ),
                TransacaoDTO(
                    categoria="Supermercado", data="2026-10-05", valor=-450.00
                ),
            ],
        )


class FormatoJSON(FormatoExtrato):

    def __init__(self, caminho_arquivo: str, chave_raiz: str = "transacoes") -> None:
        super().__init__(caminho_arquivo)
        self._chave_raiz = chave_raiz

    def ler_extrato(self) -> ExtratoBrutoDTO:
        print(
            f"Lendo JSON '{self._caminho_arquivo}' acessando a chave '{self._chave_raiz}'"
        )
        return ExtratoBrutoDTO(
            data_inicio="2026-10-01",
            data_fim="2026-10-31",
            transacoes=[
                TransacaoDTO(
                    categoria="PIX Recebido", data="2026-10-01", valor=5000.00
                ),
                TransacaoDTO(
                    categoria="Supermercado", data="2026-10-05", valor=-450.00
                ),
            ],
        )
