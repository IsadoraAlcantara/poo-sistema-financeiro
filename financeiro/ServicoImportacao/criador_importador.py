from enum import Enum
from financeiro.ServicoImportacao.importador_banco import (
    ImportadorBanco,
    ImportadorBancoInter,
    ImportadorBancoItau,
)


class OpcoesBanco(Enum):
    INTER = "inter"
    ITAU = "itau"


class CriadorImportador:

    def criar(self, banco: OpcoesBanco) -> ImportadorBanco:
        if banco == OpcoesBanco.INTER:
            return ImportadorBancoInter()
        if banco == OpcoesBanco.ITAU:
            return ImportadorBancoItau()
        raise ValueError(f"Banco desconhecido: {banco}")
