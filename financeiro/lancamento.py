from abc import ABC, abstractmethod
from financeiro.categoria import Categoria

class Lancamento(ABC):

    def __init__(self, categoria: Categoria, valor: int, data: str):
        self.categoria = categoria
        self.valor = valor
        self.data = data

    @abstractmethod
    def impacto_no_saldo(self):
        pass

    def alterar_valor(self, novo_valor):
        if novo_valor <= 0:
            raise ValueError("O valor de um lançamento não pode ser zero ou negativo")
        self.valor = novo_valor

    def alterar_categoria(self, nova_categoria):
        if nova_categoria.strip() == "":
            raise ValueError("O valor de um lançamento não pode ser zero ou negativo")
        self.valor = nova_categoria
    # refazer como uma classe em categoria