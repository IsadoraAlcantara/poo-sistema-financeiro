from financeiro.formato_extrato import (
    FormatoCSV,
    FormatoJSON,
    FormatoOFX,
)
from financeiro.opcoes_formato_extrato import OpcoesFormatoExtrato


class Leitor:
    def ler(self, caminho_arquivo: str, formato: OpcoesFormatoExtrato, **dados) -> None:
        if formato == OpcoesFormatoExtrato.OFX:
            return FormatoOFX(
                caminho_arquivo,
                fitid_validacao=dados.get("fitid_validacao", "20260928001234598"),
            )
        if formato == OpcoesFormatoExtrato.CSV:
            return FormatoCSV(
                caminho_arquivo,
                delimitador=dados.get("delimitador", ";"),
                coluna_data=dados.get("coluna_data", "data"),
                coluna_valor=dados.get("coluna_valor", "montante"),
            )
        if formato == OpcoesFormatoExtrato.JSON:
            return FormatoJSON(
                caminho_arquivo, chave_raiz=dados.get("chave_raiz", "results")
            )
        raise ValueError(f"Forma de pagamento desconhecida: {formato}")
