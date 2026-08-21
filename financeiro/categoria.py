from abc import ABC, abstractmethod


class Categoria(ABC):

    def __init__(self, nome: str):
        self.nome = nome

    def alterar_gasto_max(self, novo_gasto_max: int) -> None:
        if novo_gasto_max <= 0:
            raise ValueError("O gasto máximo de uma categoria não pode ser negativo ou zero")
        self.gasto_max = novo_gasto_max