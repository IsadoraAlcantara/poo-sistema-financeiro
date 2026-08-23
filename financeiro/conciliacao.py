from financeiro.lancamento import Lancamento


class Conciliacao:
    def __init__(self, lancamentos_origem: list[Lancamento], lancamentos_destino: list[Lancamento]) -> None:
        self.lancamentos_origem = list(lancamentos_origem)
        self.lancamentos_destino = list(lancamentos_destino)

    def total_origem(self) -> int:
        return sum(l.valor for l in self.lancamentos_origem)

    def total_destino(self) -> int:
        return sum(l.valor for l in self.lancamentos_destino)

    def diferenca(self) -> int:
        return abs(self.total_origem() - self.total_destino())

    def validar(self) -> bool:
        total_orig = self.total_origem()
        total_dest = self.total_destino()

        if total_orig != total_dest:
            raise ValueError("Os valores não batem")
        return True