from financeiro.ServicoImportacao.formato_extrato import (
    FormatoCSV,
    FormatoJSON,
    FormatoOFX,
)
from financeiro.ServicoImportacao.opcoes_formato_extrato import OpcoesFormatoExtrato
from financeiro.ServicoImportacao.formato_extrato import ExtratoBrutoDTO


class Leitor:
    def ler(self, caminho_arquivo: str, formato: OpcoesFormatoExtrato, **dados) -> ExtratoBrutoDTO:
        if formato == OpcoesFormatoExtrato.OFX:
            parser = FormatoOFX(
                caminho_arquivo,
                fitid_validacao=dados.get("fitid_validacao", "20260928001234598"),
            )
            return parser.ler_extrato()
        if formato == OpcoesFormatoExtrato.CSV:
            parser = FormatoCSV(
                caminho_arquivo,
                delimitador=dados.get("delimitador", ";"),
                coluna_data=dados.get("coluna_data", "data"),
                coluna_valor=dados.get("coluna_valor", "montante"),
            )
            return parser.ler_extrato()
        if formato == OpcoesFormatoExtrato.JSON:
            parser = FormatoJSON(
                caminho_arquivo, chave_raiz=dados.get("chave_raiz", "results")
            )
            return parser.ler_extrato()
        raise ValueError(f"Formato de arquivo desconhecido: {formato}")
