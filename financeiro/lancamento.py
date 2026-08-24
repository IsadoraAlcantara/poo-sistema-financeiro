from abc import ABC, abstractmethod
from financeiro.categoria import Categoria

class Lancamento(ABC):

    def __init__(self, categoria: Categoria, valor: int, data: str) -> None:
        self.categoria = categoria
        self.valor = valor
        self.data = data

    @abstractmethod
    def impacto_no_saldo(self) -> None:
        pass

    def alterar_valor(self, novo_valor) -> None:
        if novo_valor <= 0:
            raise ValueError("O valor de um lançamento não pode ser zero ou negativo")
        self.valor = novo_valor

    def alterar_categoria(self, nova_categoria: Categoria) -> None:
        self.categoria = nova_categoria