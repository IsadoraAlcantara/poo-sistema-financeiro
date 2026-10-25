from enum import Enum
from financeiro.ServicoImportacao.importador_banco import (
    ImportadorBanco,
    ImportadorBancoInter,
    ImportadorBancoItau,
)
from financeiro.ServicoImportacao.leitor import Leitor


class OpcoesBanco(Enum):
    INTER = "inter"
    ITAU = "itau"


class CriadorImportador:

    def __init__(self, leitor: Leitor) -> None:
        self._leitor = leitor

    def criar(self, banco: OpcoesBanco) -> ImportadorBanco:
        if banco == OpcoesBanco.INTER:
            return ImportadorBancoInter(leitor=self._leitor)
        if banco == OpcoesBanco.ITAU:
            return ImportadorBancoItau(leitor=self._leitor)
        raise ValueError(f"Banco desconhecido: {banco}")
