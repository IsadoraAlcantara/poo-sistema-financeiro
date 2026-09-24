from abc import ABC, abstractmethod
from financeiro.extrato import Extrato


class LeitorExtrato(ABC):

    def __init__(
        self,
        caminho_arquivo: str,
    ) -> None:
        self._caminho_arquivo = caminho_arquivo

    def ler_extrato(self) -> list[Extrato]:
        pass


class LeitorOFX(LeitorExtrato):

    def __init__(self, caminho_arquivo: str, fitid_validacao: bool = True) -> None:
        super().__init__(caminho_arquivo)
        self._fitid_validacao = fitid_validacao

    def ler_extrato(self) -> list[Extrato]:
        print(f"Lendo e parseando tags OFX de: {self._caminho_arquivo}")
        # IMPLEMENTAR LER EXTRATO MAIS TARDE
        # return [
        #     Extrato(date.today(), "Supermercado (OFX)", -150.00),
        #     Extrato(date.today(), "Transferência Recebida (OFX)", 500.00),
        # ]


class LeitorCSV(LeitorExtrato):

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

    def ler_extrato(self) -> list[Extrato]:
        print(
            f"Lendo CSV '{self._caminho_arquivo}' usando delimitador '{self._delimitador}' "
            f"e colunas [{self._coluna_data}, {self._coluna_valor}]"
        )
        # IMPLEMENTAR LER EXTRATO MAIS TARDE
        # return [
        #     Extrato(date.today(), "Supermercado (CSV)", -150.00),
        #     Extrato(date.today(), "Transferência Recebida (CSV)", 500.00),
        # ]

class LeitorJSON(LeitorExtrato):

    def __init__(self, caminho_arquivo: str, chave_raiz: str = "transacoes") -> None:
        super().__init__(caminho_arquivo)
        self._chave_raiz = chave_raiz

    def ler_transacoes(self) -> list[Extrato]:
        print(f"Lendo JSON '{self._caminho_arquivo}' acessando a chave '{self._chave_raiz}'")
        # IMPLEMENTAR LER EXTRATO MAIS TARDE
        # return [
        #     Extrato(date.today(), "Academia (JSON)", -120.00),
        # ]